<!-- source: https://platform.claude.com/docs/en/api/csharp/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/csharp/beta -->

<!-- chunk-start -->

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

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

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

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

      - `long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

#### Example

```csharp
EventStreamParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

await foreach (var betaManagedAgentsStreamSessionEvents in client.Beta.Sessions.Events.StreamStreaming(parameters))
{
    Console.WriteLine(betaManagedAgentsStreamSessionEvents);
}
```

##### Response (200)

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

## Beta › Sessions › Resources

### Add Session Resource

`BetaManagedAgentsFileResource Beta.Sessions.Resources.Add(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `ResourceAddParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string fileID`

    Body param: ID of a previously uploaded file.

    minLength: 1, maxLength: 128

  - `required Type type`

    Body param

    - `File`

  - `string? mountPath`

    Body param: Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    minLength: 1, maxLength: 4096

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsFileResource:`

  - `required string ID`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string FileID`

  - `required string MountPath`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
ResourceAddParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    FileID = "file_011CNha8iCJcU1wXNR6q4V8w",
    Type = Type.File,
};

var betaManagedAgentsFileResource = await client.Beta.Sessions.Resources.Add(parameters);

Console.WriteLine(betaManagedAgentsFileResource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "created_at": "2026-03-15T10:00:00Z",
  "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "mount_path": "/uploads/receipt.pdf",
  "type": "file",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

### List Session Resources

`ResourceListPage Beta.Sessions.Resources.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `ResourceListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `int limit`

    Query param: Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

    format: int32

  - `string page`

    Query param: Opaque cursor from a previous response's next_page field.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsSessionResource: union`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceListParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7"
};

var page = await client.Beta.Sessions.Resources.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
      "created_at": "2026-03-15T10:00:00Z",
      "file_id": "file_011CNha8iCJcU1wXNR6q4V8w",
      "mount_path": "/uploads/receipt.pdf",
      "type": "file",
      "updated_at": "2026-03-15T10:00:00Z"
    },
    {
      "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
      "created_at": "2026-03-15T10:00:00Z",
      "mount_path": "/workspace/example-repo",
      "type": "github_repository",
      "updated_at": "2026-03-15T10:00:00Z",
      "url": "https://github.com/example-org/example-repo",
      "checkout": {
        "name": "main",
        "type": "branch"
      }
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

### Get Session Resource

`ResourceRetrieveResponse Beta.Sessions.Resources.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `ResourceRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class ResourceRetrieveResponse: union`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var resource = await client.Beta.Sessions.Resources.Retrieve(parameters);

Console.WriteLine(resource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Update Session Resource

`ResourceUpdateResponse Beta.Sessions.Resources.Update(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `ResourceUpdateParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `required string authorizationToken`

    Body param: New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class ResourceUpdateResponse: union`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Url`

    - `Checkout? Checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `required string Name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `required Type Type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `required string Sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `required Type Type`

  - `class BetaManagedAgentsFileResource:`

    - `required string ID`

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string FileID`

    - `required string MountPath`

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `required string MemoryStoreID`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `required Type Type`

    - `Access? Access`

      Access mode for an attached memory store.

      - `ReadWrite`

      - `ReadOnly`

    - `string Description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `string? Instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `string? MountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `string? Name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```csharp
ResourceUpdateParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
    AuthorizationToken = "ghp_exampletoken",
};

var resource = await client.Beta.Sessions.Resources.Update(parameters);

Console.WriteLine(resource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZCKr6eXyl0gWMOdQiu",
  "created_at": "2026-03-15T10:00:00Z",
  "mount_path": "/workspace/example-repo",
  "type": "github_repository",
  "updated_at": "2026-03-15T10:00:00Z",
  "url": "https://github.com/example-org/example-repo",
  "checkout": {
    "name": "main",
    "type": "branch"
  }
}
```

### Delete Session Resource

`BetaManagedAgentsDeleteSessionResource Beta.Sessions.Resources.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `ResourceDeleteParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string resourceID`

    Path param: Path parameter resource_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `required string ID`

  - `required Type Type`

#### Example

```csharp
ResourceDeleteParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ResourceID = "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
};

var betaManagedAgentsDeleteSessionResource = await client.Beta.Sessions.Resources.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeleteSessionResource);
```

##### Response (200)

```json
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

## Beta › Sessions › Threads

### List Session Threads

`ThreadListPage Beta.Sessions.Threads.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `ThreadListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `int limit`

    Query param: Maximum results per page. Defaults to 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous response's next_page. Forward-only.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

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

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

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

##### Response (200)

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
          "id": "claude-opus-5",
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
                },
                "type": "bash"
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

### Get Session Thread

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `ThreadRetrieveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

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

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```csharp
ThreadRetrieveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

##### Response (200)

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
      "id": "claude-opus-5",
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
            },
            "type": "bash"
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

### Archive Session Thread

`BetaManagedAgentsSessionThread Beta.Sessions.Threads.Archive(parameters, cancellationToken = default)`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `ThreadArchiveParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `required string ID`

    Unique identifier for this thread.

  - `required Agent Agent`

    The resolved agent a session thread runs: a saved-agent snapshot, the platform advisor entry, or an inline-defined (ephemeral) agent snapshot.

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

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

      - `required string Name`

      - `required IReadOnlyList<Skill> Skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `required string SkillID`

          - `required Type Type`

          - `required string Version`

      - `required string? System`

      - `required IReadOnlyList<Tool> Tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `required Type Type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `required Type Type`

              - `JsonElement Type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `int? MaxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `required bool Enabled`

              - `JsonElement Name constant`

              - `required PermissionPolicy PermissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonElement Type constant`

              - `IReadOnlyList<string> AllowedDomains`

              - `IReadOnlyList<string> BlockedDomains`

              - `BetaManagedAgentsUserLocation? UserLocation`

                Approximate user location for search result localization.

                - `JsonElement Type constant`

                  Location precision. Only "approximate" is supported.

                - `string? City`

                  City name.

                  minLength: 1, maxLength: 255

                - `string? Country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `string? Region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `string? Timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for agent tools.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required Type Type`

        - `class BetaManagedAgentsMcpToolset:`

          - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

            - `required bool Enabled`

            - `required string Name`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `required bool Enabled`

            - `required PermissionPolicy PermissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `required string McpServerName`

          - `required Type Type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `required string Description`

          - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonElement Type constant`

            - `IReadOnlyDictionary<string, JsonElement>? Properties`

            - `IReadOnlyList<string>? Required`

          - `required string Name`

          - `required Type Type`

      - `required Type Type`

      - `required int Version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `required string Model`

        The advisor model id.

      - `required Type Type`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? ParentThreadID`

    Parent thread that spawned this thread. Null for the primary thread.

  - `required string SessionID`

    The session this thread belongs to.

  - `required BetaManagedAgentsSessionThreadStats? Stats`

    Timing statistics for a session thread.

    - `double ActiveSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `double DurationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `double StartupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `required BetaManagedAgentsSessionThreadStatus Status`

    SessionThreadStatus enum

    - `Running`

    - `Idle`

    - `Rescheduling`

    - `Terminated`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaManagedAgentsSessionThreadUsage? Usage`

    Cumulative token usage for a session thread across all turns.

    - `double ActiveSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `BetaManagedAgentsCacheCreationUsage CacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `int Ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `int Ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `int InputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `BetaMonetaryAmount? ListCost`

      A monetary amount in a specific currency.

      - `required string Amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `required BetaCurrency Currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `int OutputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `BetaManagedAgentsServerToolUsage? ServerToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `int WebFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `int WebSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```csharp
ThreadArchiveParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    ThreadID = "sthr_011CZkZVWa6oIjw0rgXZpnBt",
};

var betaManagedAgentsSessionThread = await client.Beta.Sessions.Threads.Archive(parameters);

Console.WriteLine(betaManagedAgentsSessionThread);
```

##### Response (200)

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
      "id": "claude-opus-5",
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
            },
            "type": "bash"
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

## Beta › Sessions › Threads › Events

### List Session Thread Events

`EventListPage Beta.Sessions.Threads.Events.List(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `EventListParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

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

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

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

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

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

      format: date-time

    - `required Type Type`

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

    - `bool? IsError`

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

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

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

    - `bool? IsError`

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

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

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

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

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

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

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

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

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

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

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

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

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

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

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

##### Response (200)

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

### Stream Session Thread Events

`BetaManagedAgentsStreamSessionThreadEvents Beta.Sessions.Threads.Events.StreamStreaming(parameters, cancellationToken = default)`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `EventStreamParams parameters`

  - `required string sessionID`

    Path param: Path parameter session_id

  - `required string threadID`

    Path param: Path parameter thread_id

  - `IReadOnlyList<BetaManagedAgentsDeltaType> eventDeltas`

    Query param: When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `AgentMessage`

    - `AgentThinking`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

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

          minLength: 1

        - `required Type Type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `required Source Source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `required string Data`

              Base64-encoded image data.

              minLength: 1

            - `required string MediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `required Source Source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `required string Data`

              Base64-encoded document data.

              minLength: 1

            - `required string MediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `required Type Type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `required string Data`

              The plain text content.

              minLength: 1

            - `required MediaType MediaType`

              MIME type of the text content. Must be "text/plain".

            - `required Type Type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `required Type Type`

            - `required string Url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `required string FileID`

              ID of a previously uploaded file.

              minLength: 1

            - `required Type Type`

        - `required Type Type`

        - `string? Context`

          Additional context about the document for the model.

        - `string? Title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `required string ID`

      Unique identifier for this event.

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required Result Result`

      UserToolConfirmationResult enum

      - `Allow`

      - `Deny`

    - `required string ToolUseID`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

    - `string? DenyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? SessionThreadID`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required string CustomToolUseID`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

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

          - `required bool Enabled`

            Whether citations are enabled for this search result.

        - `required IReadOnlyList<BetaManagedAgentsSearchResultContent> Content`

          Array of text content blocks from the search result.

          - `required string Text`

            The text content.

            minLength: 1

          - `required Type Type`

        - `required string Source`

          The URL source of the search result.

          minLength: 1

        - `required string Title`

          The title of the search result.

          minLength: 1

        - `required Type Type`

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

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

      format: date-time

    - `required Type Type`

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

    - `bool? IsError`

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

      format: date-time

    - `required Type Type`

    - `EvaluatedPermission EvaluatedPermission`

      AgentEvaluatedPermission enum

      - `Allow`

      - `Ask`

      - `Deny`

    - `string? SessionThreadID`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to.

    - `required Type Type`

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

    - `bool? IsError`

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

      format: date-time

    - `required Type Type`

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

      format: date-time

    - `required string ToSessionThreadID`

      Public `sthr_` ID of the thread the message was sent to.

    - `required Type Type`

    - `string? ToAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

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

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `required Type Type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `required Type Type`

        - `required Type Type`

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

        - `required string VaultID`

          ID of the vault containing the affected credential.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required StopReason StopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `required IReadOnlyList<string> EventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `required Type Type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `required Type Type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the callable agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public `sthr_` ID of the newly created thread.

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `required string ID`

      Unique identifier for this event.

    - `required string Explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeEvaluationStartID`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string Result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `required Type Type`

    - `required BetaManagedAgentsSpanModelUsage Usage`

      Token usage for a single model request.

      - `required int CacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `required int CacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `required int InputTokens`

        Input tokens consumed by this request.

        format: int32

      - `required int OutputTokens`

        Output tokens generated by this request.

        format: int32

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `required string ID`

      Unique identifier for this event.

    - `required bool? IsError`

      Whether the model request resulted in an error.

    - `required string ModelRequestStartID`

      The id of the corresponding `span.model_request_start` event.

    - `required BetaManagedAgentsSpanModelUsage ModelUsage`

      Token usage for a single model request.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `required string ID`

      Unique identifier for this event.

    - `required int Iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `required string OutcomeID`

      The `outc_` ID of the outcome being evaluated.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `required string ID`

      Unique identifier for this event.

    - `required string Description`

      What the agent should produce. Copied from the input event.

    - `required int? MaxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `required string OutcomeID`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Rubric Rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `required string FileID`

          ID of the rubric file.

        - `required Type Type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `required string Content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that started running.

    - `required Type Type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `required string ID`

      Unique identifier for this event.

    - `required string AgentName`

      Name of the agent the thread runs.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that terminated.

    - `required Type Type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `required string ID`

      Unique identifier for this event.

    - `required string ToolUseID`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `required Type Type`

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

    - `bool? IsError`

      Whether the tool execution resulted in an error.

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

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

      format: date-time

    - `required string SessionThreadID`

      Public sthr_ ID of the thread that is retrying.

    - `required Type Type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `BetaManagedAgentsSessionAgent? Agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `required string ID`

      - `required string? Description`

      - `required IReadOnlyList<BetaManagedAgentsMcpServerUrlDefinition> McpServers`

        - `required string Name`

        - `required Type Type`

        - `required string Url`

      - `required BetaManagedAgentsModelConfig Model`

        Model identifier and configuration.

        - `required BetaManagedAgentsModel ID`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `ClaudeSonnet5`

            High-performance model for coding and agents

          - `ClaudeFable5`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `ClaudeOpus5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_8`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_7`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_6`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_6`

            Best combination of speed and intelligence

          - `ClaudeHaiku4_5`

            Fastest model with near-frontier intelligence

          - `ClaudeHaiku4_5_20251001`

            Fastest model with near-frontier intelligence

          - `ClaudeOpus4_5`

            Powerful intelligence for long-running agents and coding

          - `ClaudeOpus4_5_20251101`

            Powerful intelligence for long-running agents and coding

          - `ClaudeSonnet4_5`

            High-performance model for agents and coding

          - `ClaudeSonnet4_5_20250929`

            High-performance model for agents and coding

        - `Effort Effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `required Type Type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `required Type Type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `required Type Type`

        - `string InferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Speed Speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `Standard`

          - `Fast`

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

                - `required string Version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `required string SkillID`

                - `required Type Type`

                - `required string Version`

            - `required string? System`

            - `required IReadOnlyList<Tool> Tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `required IReadOnlyList<BetaManagedAgentsAgentToolConfig> Configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `required Type Type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `required Type Type`

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `int? MaxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `required bool Enabled`

                    - `JsonElement Name constant`

                    - `required PermissionPolicy PermissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonElement Type constant`

                    - `IReadOnlyList<string> AllowedDomains`

                    - `IReadOnlyList<string> BlockedDomains`

                    - `BetaManagedAgentsUserLocation? UserLocation`

                      Approximate user location for search result localization.

                      - `JsonElement Type constant`

                        Location precision. Only "approximate" is supported.

                      - `string? City`

                        City name.

                        minLength: 1, maxLength: 255

                      - `string? Country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `string? Region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `string? Timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `required BetaManagedAgentsAgentToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for agent tools.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required Type Type`

              - `class BetaManagedAgentsMcpToolset:`

                - `required IReadOnlyList<BetaManagedAgentsMcpToolConfig> Configs`

                  - `required bool Enabled`

                  - `required string Name`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required BetaManagedAgentsMcpToolsetDefaultConfig DefaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `required bool Enabled`

                  - `required PermissionPolicy PermissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `required string McpServerName`

                - `required Type Type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `required string Description`

                - `required BetaManagedAgentsCustomToolInputSchema InputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonElement Type constant`

                  - `IReadOnlyDictionary<string, JsonElement>? Properties`

                  - `IReadOnlyList<string>? Required`

                - `required string Name`

                - `required Type Type`

            - `required Type Type`

            - `required int Version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `required string Model`

              The advisor model id.

            - `required Type Type`

        - `required Type Type`

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

      - `required int Version`

        format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `required BetaMonetaryAmount MaxListCost`

        A monetary amount in a specific currency.

        - `required string Amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `required BetaCurrency Currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `required Type Type`

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

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `required string ID`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `required Type Type`

    - `required Type Type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `required BetaManagedAgentsDeltaContent Delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `required BetaManagedAgentsTextBlock Content`

        Regular text content.

      - `required Type Type`

      - `long Index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `required string EventID`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `required Type Type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `required string ID`

      Unique identifier for this event.

    - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

      System content blocks. Text-only.

      - `required string Text`

        The text content.

        minLength: 1

      - `required Type Type`

    - `required Type Type`

    - `DateTimeOffset? ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `required string ID`

      Unique identifier for this event.

    - `required DateTimeOffset ProcessedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required Type Type`

    - `required BetaManagedAgentsSessionUsageSnapshot Usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `double ActiveSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `BetaManagedAgentsCacheCreationUsage CacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `int Ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `int Ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `int CacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `int InputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `BetaMonetaryAmount ListCost`

        A monetary amount in a specific currency.

      - `int OutputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `BetaManagedAgentsServerToolUsage ServerToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `int WebFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `int WebSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `BetaManagedAgentsBudgetLimit? Budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

  Server-sent event in a single thread's stream.

#### Example

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

##### Response (200)

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

## Beta › Deployments

### Create Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Create(parameters, cancellationToken = default)`

**POST** `/v1/deployments`

Create Deployment

#### Parameters

- `DeploymentCreateParams parameters`

  - `required Agent agent`

    Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `string`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `required string ID`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `required string environmentID`

    Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

    minLength: 1, maxLength: 128

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required string name`

    Body param: Human-readable name for the deployment.

    minLength: 1, maxLength: 256

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? description`

    Body param: Description of what the deployment does.

    maxLength: 2048

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<Resource> resources`

    Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string> vaultIds`

    Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

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

##### Response (200)

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

### List Deployments

`DeploymentListPage Beta.Deployments.List(parameters, cancellationToken = default)`

**GET** `/v1/deployments`

List Deployments

#### Parameters

- `DeploymentListParams parameters`

  - `string agentID`

    Query param: Filter by agent ID.

  - `DateTimeOffset createdAtGte`

    Query param: Return deployments created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return deployments created at or before this time (inclusive).

    format: date-time

  - `bool includeArchived`

    Query param: When true, includes archived deployments. Default: false (exclude archived).

  - `int limit`

    Query param: Maximum results per page. Default 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor.

  - `BetaManagedAgentsDeploymentStatus status`

    Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentListParams parameters = new();

var page = await client.Beta.Deployments.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Get Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

#### Parameters

- `DeploymentRetrieveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentRetrieveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

##### Response (200)

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

### Update Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Update(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

#### Parameters

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

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `int Version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `BetaManagedAgentsBudgetLimit? budget`

    Body param: A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `string? description`

    Body param: Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `string environmentID`

    Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

    maxLength: 128

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string name`

    Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `IReadOnlyList<Resource>? resources`

    Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `required string AuthorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `required string FileID`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `BetaManagedAgentsScheduleParams? schedule`

    Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `IReadOnlyList<string>? vaultIds`

    Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentUpdateParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Update(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

##### Response (200)

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

### Archive Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Archive(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

#### Parameters

- `DeploymentArchiveParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentArchiveParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Archive(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

##### Response (200)

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

### Run Deployment Now

`BetaManagedAgentsDeploymentRun Beta.Deployments.Run(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

#### Parameters

- `DeploymentRunParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

  - `required Type Type`

#### Example

```csharp
DeploymentRunParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeploymentRun = await client.Beta.Deployments.Run(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
```

##### Response (200)

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

### Pause Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Pause(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

#### Parameters

- `DeploymentPauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentPauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Pause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

##### Response (200)

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

### Unpause Deployment

`BetaManagedAgentsDeployment Beta.Deployments.Unpause(parameters, cancellationToken = default)`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

#### Parameters

- `DeploymentUnpauseParams parameters`

  - `required string deploymentID`

    Path parameter deployment_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `required string ID`

    Unique identifier for this deployment.

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

            minLength: 1

          - `required Type Type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `required Source Source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `required string Data`

                Base64-encoded image data.

                minLength: 1

              - `required string MediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `required Source Source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `required string Data`

                Base64-encoded document data.

                minLength: 1

              - `required string MediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `required Type Type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `required string Data`

                The plain text content.

                minLength: 1

              - `required MediaType MediaType`

                MIME type of the text content. Must be "text/plain".

              - `required Type Type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `required Type Type`

              - `required string Url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `required string FileID`

                ID of a previously uploaded file.

                minLength: 1

              - `required Type Type`

          - `required Type Type`

          - `string? Context`

            Additional context about the document for the model.

          - `string? Title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `required Type Type`

      - `required Type Type`

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

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `required string Content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `required Type Type`

      - `required Type Type`

      - `int? MaxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `required IReadOnlyList<BetaManagedAgentsSystemContentBlock> Content`

        System content blocks to append. Text-only.

        - `required string Text`

          The text content.

          minLength: 1

        - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `required string Name`

    Human-readable name.

  - `required BetaManagedAgentsDeploymentPausedReason? PausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `required Type Type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `required BetaManagedAgentsDeploymentPausedReasonError Error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `required Type Type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `required Type Type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `required Type Type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `required Type Type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `required Type Type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `required Type Type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `required Type Type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `required Type Type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `required Type Type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `required Type Type`

      - `required Type Type`

  - `required IReadOnlyList<BetaManagedAgentsSessionResourceConfig> Resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `required Type Type`

      - `required string Url`

        Github URL of the repository

      - `Checkout? Checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `required string Name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `required Type Type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `required string Sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `required string FileID`

        ID of a previously uploaded file.

      - `required Type Type`

      - `string? MountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `required string MemoryStoreID`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `required Type Type`

      - `Access? Access`

        Access mode for an attached memory store.

        - `ReadWrite`

        - `ReadOnly`

      - `string? Instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `required BetaManagedAgentsSchedule? Schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `required string Expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `required string Timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `required Type Type`

    - `DateTimeOffset? LastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `IReadOnlyList<DateTimeOffset> UpcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `required BetaManagedAgentsDeploymentStatus Status`

    Lifecycle status of a deployment.

    - `Active`

    - `Paused`

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

    - `required Type Type`

#### Example

```csharp
DeploymentUnpauseParams parameters = new()
{
    DeploymentID = "depl_011CZkZcDH3vPqd7xnEfwTai"
};

var betaManagedAgentsDeployment = await client.Beta.Deployments.Unpause(parameters);

Console.WriteLine(betaManagedAgentsDeployment);
```

##### Response (200)

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

## Beta › Deployment Runs

### List Deployment Runs

`DeploymentRunListPage Beta.DeploymentRuns.List(parameters, cancellationToken = default)`

**GET** `/v1/deployment_runs`

List Deployment Runs

#### Parameters

- `DeploymentRunListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return runs created strictly after this time (exclusive).

    format: date-time

  - `DateTimeOffset createdAtGte`

    Query param: Return runs created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLt`

    Query param: Return runs created strictly before this time (exclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return runs created at or before this time (inclusive).

    format: date-time

  - `string deploymentID`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `bool hasError`

    Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `int limit`

    Query param: Maximum results per page. Default 20, maximum 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `BetaManagedAgentsTriggerType triggerType`

    Query param: Filter runs by what triggered them. Omit to return all runs.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

  - `required Type Type`

#### Example

```csharp
DeploymentRunListParams parameters = new();

var page = await client.Beta.DeploymentRuns.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Get Deployment Run

`BetaManagedAgentsDeploymentRun Beta.DeploymentRuns.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

#### Parameters

- `DeploymentRunRetrieveParams parameters`

  - `required string deploymentRunID`

    Path parameter deployment_run_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `required string ID`

    Unique identifier for this run (`drun_...`).

  - `required BetaManagedAgentsAgentReference Agent`

    A resolved agent reference with a concrete version.

    - `required string ID`

    - `required Type Type`

    - `required int Version`

      format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DeploymentID`

    ID of the deployment that produced this run.

  - `required Error? Error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `required string Message`

        Human-readable error description.

      - `required Type Type`

  - `required string? SessionID`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `required BetaManagedAgentsTriggerContext TriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `required DateTimeOffset ScheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `required Type Type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `required Type Type`

  - `required Type Type`

#### Example

```csharp
DeploymentRunRetrieveParams parameters = new()
{
    DeploymentRunID = "deployment_run_id"
};

var betaManagedAgentsDeploymentRun = await client.Beta.DeploymentRuns.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsDeploymentRun);
```

##### Response (200)

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

## Beta › Vaults

### Create Vault

`BetaManagedAgentsVault Beta.Vaults.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults`

Create Vault

#### Parameters

- `VaultCreateParams parameters`

  - `required string displayName`

    Body param: Human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
VaultCreateParams parameters = new() { DisplayName = "Example vault" };

var betaManagedAgentsVault = await client.Beta.Vaults.Create(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

##### Response (200)

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

### List Vaults

`VaultListPage Beta.Vaults.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults`

List Vaults

#### Parameters

- `VaultListParams parameters`

  - `bool includeArchived`

    Query param: Whether to include archived vaults in the results.

  - `int limit`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination token from a previous `list_vaults` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
VaultListParams parameters = new();

var page = await client.Beta.Vaults.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Get Vault

`BetaManagedAgentsVault Beta.Vaults.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}`

Get Vault

#### Parameters

- `VaultRetrieveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
VaultRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

##### Response (200)

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

### Update Vault

`BetaManagedAgentsVault Beta.Vaults.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}`

Update Vault

#### Parameters

- `VaultUpdateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `string? displayName`

    Body param: Updated human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
VaultUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Update(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

##### Response (200)

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

### Delete Vault

`BetaManagedAgentsDeletedVault Beta.Vaults.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

#### Parameters

- `VaultDeleteParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `required string ID`

    Unique identifier of the deleted vault.

  - `required Type Type`

#### Example

```csharp
VaultDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsDeletedVault = await client.Beta.Vaults.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedVault);
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

### Archive Vault

`BetaManagedAgentsVault Beta.Vaults.Archive(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/archive`

Archive Vault

#### Parameters

- `VaultArchiveParams parameters`

  - `required string vaultID`

    Path parameter vault_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `required string ID`

    Unique identifier for the vault.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string DisplayName`

    Human-readable name for the vault.

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the vault.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```csharp
VaultArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv"
};

var betaManagedAgentsVault = await client.Beta.Vaults.Archive(parameters);

Console.WriteLine(betaManagedAgentsVault);
```

##### Response (200)

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

## Beta › Vaults › Credentials

### Create Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Create(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

#### Parameters

- `CredentialCreateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required Auth auth`

    Body param: Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `required string AccessToken`

        OAuth access token.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshParams? Refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `required string ClientID`

          OAuth client ID.

          minLength: 1, maxLength: 1024

        - `required string RefreshToken`

          OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `required string TokenEndpoint`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `required TokenEndpointAuth TokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `required string ClientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `string? Scope`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `required string Token`

        Static bearer token value.

        minLength: 1, maxLength: 8192

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableCreateParams:`

      Parameters for creating an environment variable credential.

      - `required BetaManagedAgentsCredentialNetworkingParams Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `required string SecretValue`

        Secret value. Write-only; never returned in responses.

        minLength: 1, maxLength: 4096

      - `required Type Type`

      - `BetaManagedAgentsInjectionLocationParams InjectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

  - `string? displayName`

    Body param: Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

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

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

#### Example

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

##### Response (200)

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

### List Credentials

`CredentialListPage Beta.Vaults.Credentials.List(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `CredentialListParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `bool includeArchived`

    Query param: Whether to include archived credentials in the results.

  - `int limit`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `string page`

    Query param: Opaque pagination token from a previous `list_credentials` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

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

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

#### Example

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

##### Response (200)

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

### Get Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `CredentialRetrieveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

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

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

#### Example

```csharp
CredentialRetrieveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Update Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Update(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

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

      - `string? AccessToken`

        Updated OAuth access token.

        minLength: 1, maxLength: 8192

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `BetaManagedAgentsMcpOAuthRefreshUpdateParams? Refresh`

        Parameters for updating OAuth refresh token configuration.

        - `string? RefreshToken`

          Updated OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `string? Scope`

          Updated OAuth scope for the refresh request.

          maxLength: 8192

        - `TokenEndpointAuth TokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `required Type Type`

            - `string? ClientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `required Type Type`

            - `string? ClientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `required Type Type`

      - `string? Token`

        Updated static bearer token value.

        minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `required Type Type`

      - `BetaManagedAgentsInjectionLocationUpdateParams InjectionLocation`

        Updated injection location.

        - `bool Body`

          Substitute when the placeholder appears in the request body.

        - `bool Header`

          Substitute when the placeholder appears in a request header value.

      - `BetaManagedAgentsCredentialNetworkingParams? Networking`

        Updated networking scope. Full replacement.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `required Type Type`

      - `string? SecretValue`

        Updated secret value.

        minLength: 1, maxLength: 4096

  - `string? displayName`

    Body param: Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

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

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

#### Example

```csharp
CredentialUpdateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Update(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Delete Credential

`BetaManagedAgentsDeletedCredential Beta.Vaults.Credentials.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `CredentialDeleteParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `required string ID`

    Unique identifier of the deleted credential.

  - `required Type Type`

#### Example

```csharp
CredentialDeleteParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsDeletedCredential = await client.Beta.Vaults.Credentials.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedCredential);
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`BetaManagedAgentsCredential Beta.Vaults.Credentials.Archive(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `CredentialArchiveParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `required string ID`

    Unique identifier for the credential.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Auth Auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

      - `DateTimeOffset? ExpiresAt`

        A timestamp in RFC 3339 format

        format: date-time

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

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `required Type Type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `required Type Type`

        - `string? Resource`

          OAuth resource indicator.

        - `string? Scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `required string McpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `required Type Type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `required BetaManagedAgentsInjectionLocationResponse InjectionLocation`

        Where in the outbound request the secret value is substituted.

        - `required bool Body`

          Whether the placeholder is substituted in the request body.

        - `required bool Header`

          Whether the placeholder is substituted in request header values.

      - `required Networking Networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `required Type Type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `required IReadOnlyList<string> AllowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `required Type Type`

      - `required string SecretName`

        Name of the environment variable.

      - `required Type Type`

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata attached to the credential.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault this credential belongs to.

  - `string? DisplayName`

    Human-readable name for the credential.

#### Example

```csharp
CredentialArchiveParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredential = await client.Beta.Vaults.Credentials.Archive(parameters);

Console.WriteLine(betaManagedAgentsCredential);
```

##### Response (200)

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

### Validate Credential

`BetaManagedAgentsCredentialValidation Beta.Vaults.Credentials.McpOAuthValidate(parameters, cancellationToken = default)`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `CredentialMcpOAuthValidateParams parameters`

  - `required string vaultID`

    Path param: Path parameter vault_id

  - `required string credentialID`

    Path param: Path parameter credential_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `required string CredentialID`

    Unique identifier of the credential that was validated.

  - `required bool HasRefreshToken`

    Whether the credential has a refresh token configured.

  - `required BetaManagedAgentsMcpProbe? McpProbe`

    The failing step of an MCP validation probe.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

      - `required string Body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `required bool BodyTruncated`

        Whether `body` was truncated.

      - `required string ContentType`

        Value of the `Content-Type` response header.

      - `required int StatusCode`

        HTTP status code.

        format: int32

    - `required string Method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `required BetaManagedAgentsRefreshObject? Refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `required BetaManagedAgentsRefreshHttpResponse? HttpResponse`

      An HTTP response captured during a credential validation probe.

    - `required Status Status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `Succeeded`

      - `Failed`

      - `ConnectError`

      - `NoRefreshToken`

  - `required BetaManagedAgentsCredentialValidationStatus Status`

    Overall verdict of a credential validation probe.

    - `Valid`

    - `Invalid`

    - `Unknown`

  - `required Type Type`

  - `required DateTimeOffset ValidatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string VaultID`

    Identifier of the vault containing the credential.

#### Example

```csharp
CredentialMcpOAuthValidateParams parameters = new()
{
    VaultID = "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    CredentialID = "vcrd_011CZkZEMt8gZan2iYOQfSkw",
};

var betaManagedAgentsCredentialValidation = await client.Beta.Vaults.Credentials.McpOAuthValidate(parameters);

Console.WriteLine(betaManagedAgentsCredentialValidation);
```

##### Response (200)

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

## Beta › Memory Stores

### Create a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Create(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores`

Create a memory store

#### Parameters

- `MemoryStoreCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

    minLength: 1, maxLength: 255

  - `string description`

    Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

    maxLength: 1024

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```csharp
MemoryStoreCreateParams parameters = new() { Name = "x" };

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Create(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

##### Response (200)

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

### List memory stores

`MemoryStoreListPage Beta.MemoryStores.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores`

List memory stores

#### Parameters

- `MemoryStoreListParams parameters`

  - `DateTimeOffset createdAtGte`

    Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

    format: date-time

  - `bool includeArchived`

    Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `int limit`

    Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```csharp
MemoryStoreListParams parameters = new();

var page = await client.Beta.MemoryStores.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Retrieve a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

#### Parameters

- `MemoryStoreRetrieveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```csharp
MemoryStoreRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

##### Response (200)

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

### Update a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Update(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a memory store

#### Parameters

- `MemoryStoreUpdateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string? description`

    Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

    maxLength: 1024

  - `IReadOnlyDictionary<string, string>? metadata`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `string? name`

    Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

    minLength: 1, maxLength: 255

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```csharp
MemoryStoreUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Update(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

##### Response (200)

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

### Delete a memory store

`BetaManagedAgentsDeletedMemoryStore Beta.MemoryStores.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

#### Parameters

- `MemoryStoreDeleteParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `required string ID`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `required Type Type`

#### Example

```csharp
MemoryStoreDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsDeletedMemoryStore = await client.Beta.MemoryStores.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemoryStore);
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

### Archive a memory store

`BetaManagedAgentsMemoryStore Beta.MemoryStores.Archive(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

#### Parameters

- `MemoryStoreArchiveParams parameters`

  - `required string memoryStoreID`

    Path parameter memory_store_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `required string ID`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string Description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```csharp
MemoryStoreArchiveParams parameters = new()
{
    MemoryStoreID = "memory_store_id"
};

var betaManagedAgentsMemoryStore = await client.Beta.MemoryStores.Archive(parameters);

Console.WriteLine(betaManagedAgentsMemoryStore);
```

##### Response (200)

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

## Beta › Memory Stores › Memories

### Create a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Create(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

#### Parameters

- `MemoryCreateParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string? content`

    Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `required string path`

    Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

    minLength: 2, maxLength: 1024

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

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

##### Response (200)

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

### List memories

`MemoryListPage Beta.MemoryStores.Memories.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

#### Parameters

- `MemoryListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `int depth`

    Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

    format: int32

  - `int limit`

    Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `string pathPrefix`

    Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `BetaManagedAgentsMemoryView view`

    Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryListItem: union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `required string ID`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `required string ContentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `required int ContentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      format: int32

    - `required DateTimeOffset CreatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `required string MemoryStoreID`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `required string MemoryVersionID`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `required string Path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `required Type Type`

    - `required DateTimeOffset UpdatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `string? Content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `required string Path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `required Type Type`

#### Example

```csharp
MemoryListParams parameters = new() { MemoryStoreID = "memory_store_id" };

var page = await client.Beta.MemoryStores.Memories.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Retrieve a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

#### Parameters

- `MemoryRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```csharp
MemoryRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

##### Response (200)

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

### Update a memory

`BetaManagedAgentsMemory Beta.MemoryStores.Memories.Update(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

#### Parameters

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

    minLength: 2, maxLength: 1024

  - `BetaManagedAgentsPrecondition precondition`

    Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `required string ID`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `required string ContentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `required int ContentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryStoreID`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `required string MemoryVersionID`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `required string Path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `required Type Type`

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `string? Content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```csharp
MemoryUpdateParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsMemory = await client.Beta.MemoryStores.Memories.Update(parameters);

Console.WriteLine(betaManagedAgentsMemory);
```

##### Response (200)

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

### Delete a memory

`BetaManagedAgentsDeletedMemory Beta.MemoryStores.Memories.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

#### Parameters

- `MemoryDeleteParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryID`

    Path param: Path parameter memory_id

  - `string expectedContentSha256`

    Query param: Query parameter for expected_content_sha256

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). Deleting a memory does not erase its version history: its versions remain listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) while they are retained (each version is kept for at least the version retention period after it was written, unless the store itself is deleted).

  - `required string ID`

    ID of the deleted memory (a `mem_...` value).

  - `required Type Type`

#### Example

```csharp
MemoryDeleteParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryID = "memory_id",
};

var betaManagedAgentsDeletedMemory = await client.Beta.MemoryStores.Memories.Delete(parameters);

Console.WriteLine(betaManagedAgentsDeletedMemory);
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_deleted"
}
```

## Beta › Memory Stores › Memory Versions

### List memory versions

`MemoryVersionListPage Beta.MemoryStores.MemoryVersions.List(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

#### Parameters

- `MemoryVersionListParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `string apiKeyID`

    Query param: Query parameter for api_key_id

  - `DateTimeOffset createdAtGte`

    Query param: Return versions created at or after this time (inclusive).

    format: date-time

  - `DateTimeOffset createdAtLte`

    Query param: Return versions created at or before this time (inclusive).

    format: date-time

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string memoryID`

    Query param: Query parameter for memory_id

  - `BetaManagedAgentsMemoryVersionOperation operation`

    Query param: Query parameter for operation

  - `string page`

    Query param: Query parameter for page

  - `string serviceAccountID`

    Query param: Query parameter for service_account_id

  - `string sessionID`

    Query param: Query parameter for session_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `Created`

    - `Modified`

    - `Deleted`

  - `required Type Type`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonElement Type constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

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

##### Response (200)

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

### Retrieve a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `MemoryVersionRetrieveParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `BetaManagedAgentsMemoryView view`

    Query param: Query parameter for view

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `Created`

    - `Modified`

    - `Deleted`

  - `required Type Type`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonElement Type constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```csharp
MemoryVersionRetrieveParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Retrieve(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

##### Response (200)

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

### Redact a memory version

`BetaManagedAgentsMemoryVersion Beta.MemoryStores.MemoryVersions.Redact(parameters, cancellationToken = default)`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `MemoryVersionRedactParams parameters`

  - `required string memoryStoreID`

    Path param: Path parameter memory_store_id

  - `required string memoryVersionID`

    Path param: Path parameter memory_version_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and are not deleted with the memory; each version is retained for at least the version retention period after it was written, unless the store itself is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `required string ID`

    Unique identifier for this version (a `memver_...` value).

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string MemoryID`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the memory's retained versions, including the `deleted` row while the lineage is retained.

  - `required string MemoryStoreID`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `required BetaManagedAgentsMemoryVersionOperation Operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `Created`

    - `Modified`

    - `Deleted`

  - `required Type Type`

  - `string? Content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `string? ContentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `int? ContentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `BetaManagedAgentsActor CreatedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `required string SessionID`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `required string ApiKeyID`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `required Type Type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `required Type Type`

      - `required string UserID`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `required string ServiceAccountID`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonElement Type constant`

  - `string? Path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `DateTimeOffset? RedactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `BetaManagedAgentsActor RedactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```csharp
MemoryVersionRedactParams parameters = new()
{
    MemoryStoreID = "memory_store_id",
    MemoryVersionID = "memory_version_id",
};

var betaManagedAgentsMemoryVersion = await client.Beta.MemoryStores.MemoryVersions.Redact(parameters);

Console.WriteLine(betaManagedAgentsMemoryVersion);
```

##### Response (200)

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

## Beta › Files

### Upload File

`BetaFileMetadata Beta.Files.Upload(parameters, cancellationToken = default)`

**POST** `/v1/files`

Upload File

#### Parameters

- `FileUploadParams parameters`

  - `required string file`

    Body param: The file to upload

    format: binary

  - `long expiresInSeconds`

    Body param: Seconds from upload until the file expires and its bytes become permanently unavailable. Must be between 3600 (one hour) and 7776000 (ninety days).

    minimum: 3600, maximum: 7776000

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

#### Example

```csharp
FileUploadParams parameters = new()
{
    File = Encoding.UTF8.GetBytes("Example data")
};

var betaFileMetadata = await client.Beta.Files.Upload(parameters);

Console.WriteLine(betaFileMetadata);
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z",
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### List Files

`FileListPage Beta.Files.List(parameters, cancellationToken = default)`

**GET** `/v1/files`

List Files

#### Parameters

- `FileListParams parameters`

  - `IReadOnlyList<string>? ids`

    Query param: Restrict the result set to Files whose `id` is in this list. At most 100 entries (after de-duplication). Mutually exclusive with `page` and `limit`. When supplied, the response is always a single page (`next_page` is null). IDs that do not resolve to a visible File — including deleted Files — are silently omitted.

  - `long limit`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `string? page`

    Query param: Opaque page cursor returned in a prior list response's `next_page`. Prefixed `page_`.

  - `string scopeID`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

#### Example

```csharp
FileListParams parameters = new();

var page = await client.Beta.Files.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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
      "expires_at": "2025-05-15T18:37:24.100435Z",
      "scope": {
        "id": "id",
        "type": "session"
      }
    }
  ],
  "next_page": "next_page"
}
```

### Download File

`HttpResponse Beta.Files.Download(parameters, cancellationToken = default)`

**GET** `/v1/files/{file_id}/content`

Download File

#### Parameters

- `FileDownloadParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Example

```csharp
FileDownloadParams parameters = new() { FileID = "file_id" };

var response = await client.Beta.Files.Download(parameters);

Console.WriteLine(response);
```

### Get File Metadata

`BetaFileMetadata Beta.Files.RetrieveMetadata(parameters, cancellationToken = default)`

**GET** `/v1/files/{file_id}`

Get File Metadata

#### Parameters

- `FileRetrieveMetadataParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFileMetadata:`

  - `required string ID`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `required string Filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `required string MimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `required long SizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonElement Type constant`

    Object type.

    For files, this is always `"file"`.

  - `bool Downloadable`

    Whether the file can be downloaded.

  - `DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string representing when the file will expire and become unavailable for download. Null if the file does not expire. For files uploaded with `expires_in_seconds`, this is the upload time plus that value.

    format: date-time

  - `BetaFileScope? Scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `required string ID`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonElement Type constant`

      The type of scope (e.g., `"session"`).

#### Example

```csharp
FileRetrieveMetadataParams parameters = new() { FileID = "file_id" };

var betaFileMetadata = await client.Beta.Files.RetrieveMetadata(parameters);

Console.WriteLine(betaFileMetadata);
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "created_at": "2025-04-15T18:37:24.100435Z",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 102400,
  "type": "file",
  "downloadable": false,
  "expires_at": "2025-05-15T18:37:24.100435Z",
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### Delete File

`BetaDeletedFile Beta.Files.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/files/{file_id}`

Delete File

#### Parameters

- `FileDeleteParams parameters`

  - `required string fileID`

    ID of the File.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDeletedFile:`

  - `required string ID`

    ID of the deleted file.

  - `Type Type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

#### Example

```csharp
FileDeleteParams parameters = new() { FileID = "file_id" };

var betaDeletedFile = await client.Beta.Files.Delete(parameters);

Console.WriteLine(betaDeletedFile);
```

##### Response (200)

```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file_deleted"
}
```

## Beta › Skills

### Create Skill

`BetaSkill Beta.Skills.Create(parameters, cancellationToken = default)`

**POST** `/v1/skills`

Create Skill

#### Parameters

- `SkillCreateParams parameters`

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `string? displayName`

    Body param: Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkill:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string DisplayName`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `required string LatestVersionID`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `required BetaSkillSource Source`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `required Type Type`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `Custom`

      - `Anthropic`

      - `AnthropicExample`

      - `Plugin`

  - `JsonElement Type constant`

    Object type.

    For Skills, this is always `"skill"`.

  - `required DateTimeOffset UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```csharp
SkillCreateParams parameters = new()
{
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var betaSkill = await client.Beta.Skills.Create(parameters);

Console.WriteLine(betaSkill);
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List Skills

`SkillListPage Beta.Skills.List(parameters, cancellationToken = default)`

**GET** `/v1/skills`

List Skills

#### Parameters

- `SkillListParams parameters`

  - `long limit`

    Query param: Number of results to return per page.

    Ranges from `1` to `1000`. Defaults to `20`.

    minimum: 1, maximum: 1000

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

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkill:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string DisplayName`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `required string LatestVersionID`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `required BetaSkillSource Source`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `required Type Type`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `Custom`

      - `Anthropic`

      - `AnthropicExample`

      - `Plugin`

  - `JsonElement Type constant`

    Object type.

    For Skills, this is always `"skill"`.

  - `required DateTimeOffset UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```csharp
SkillListParams parameters = new();

var page = await client.Beta.Skills.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "display_name",
      "latest_version_id": "latest_version_id",
      "source": {
        "type": "custom"
      },
      "type": "skill",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

### Get Skill

`BetaSkill Beta.Skills.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}`

Get Skill

#### Parameters

- `SkillRetrieveParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkill:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string DisplayName`

    Human-readable, single-line label for the Skill. Maximum 255 characters.
    Always set: derived from the SKILL.md frontmatter `name` when omitted at
    creation. Not unique.

  - `required string LatestVersionID`

    ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.

  - `required BetaSkillSource Source`

    Where the Skill comes from.

    Possible values:

    * `"custom"`: authored by the platform user; private to their workspace
    * `"anthropic"`: published by Anthropic; shared and read-only
    * `"anthropic_example"`: Anthropic-published sample Skill
    * `"plugin"`: resolved from an installed plugin

    - `required Type Type`

      Where the Skill comes from.

      Possible values:

      * `"custom"`: authored by the platform user; private to their workspace
      * `"anthropic"`: published by Anthropic; shared and read-only
      * `"anthropic_example"`: Anthropic-published sample Skill
      * `"plugin"`: resolved from an installed plugin

      - `Custom`

      - `Anthropic`

      - `AnthropicExample`

      - `Plugin`

  - `JsonElement Type constant`

    Object type.

    For Skills, this is always `"skill"`.

  - `required DateTimeOffset UpdatedAt`

    ISO 8601 timestamp of when the skill was last updated.

    format: date-time

#### Example

```csharp
SkillRetrieveParams parameters = new() { SkillID = "skill_id" };

var betaSkill = await client.Beta.Skills.Retrieve(parameters);

Console.WriteLine(betaSkill);
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete Skill

`BetaDeletedSkill Beta.Skills.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

#### Parameters

- `SkillDeleteParams parameters`

  - `required string skillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDeletedSkill:`

  - `required string ID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `JsonElement Type constant`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

#### Example

```csharp
SkillDeleteParams parameters = new() { SkillID = "skill_id" };

var betaDeletedSkill = await client.Beta.Skills.Delete(parameters);

Console.WriteLine(betaDeletedSkill);
```

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```

## Beta › Skills › Versions

### Create Skill Version

`BetaSkillVersion Beta.Skills.Versions.Create(parameters, cancellationToken = default)`

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

#### Parameters

- `VersionCreateParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required IReadOnlyList<string> files`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkillVersion:`

  - `required string ID`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Name`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `required string SkillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `JsonElement Type constant`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

#### Example

```csharp
VersionCreateParams parameters = new()
{
    SkillID = "skill_id",
    Files =
    [
        Encoding.UTF8.GetBytes("Example data")
    ],
};

var betaSkillVersion = await client.Beta.Skills.Versions.Create(parameters);

Console.WriteLine(betaSkillVersion);
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### List Skill Versions

`VersionListPage Beta.Skills.Versions.List(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

#### Parameters

- `VersionListParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `long? limit`

    Query param: Number of results to return per page.

    Ranges from `1` to `1000`. Defaults to `20`.

    minimum: 1, maximum: 1000

  - `string? page`

    Query param: Optionally set to the `next_page` token from the previous response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkillVersion:`

  - `required string ID`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Name`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `required string SkillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `JsonElement Type constant`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

#### Example

```csharp
VersionListParams parameters = new() { SkillID = "skill_id" };

var page = await client.Beta.Skills.Versions.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

### Download Skill Version Content

`HttpResponse Beta.Skills.Versions.Download(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

#### Parameters

- `VersionDownloadParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Identifies the skill version by its version ID.

    Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Example

```csharp
VersionDownloadParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var response = await client.Beta.Skills.Versions.Download(parameters);

Console.WriteLine(response);
```

### Get Skill Version

`BetaSkillVersion Beta.Skills.Versions.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

#### Parameters

- `VersionRetrieveParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Identifies the skill version: a version ID, or the literal `latest` for the skill's most recent version.

    Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaSkillVersion:`

  - `required string ID`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `required DateTimeOffset CreatedAt`

    ISO 8601 timestamp of when the skill was created.

    format: date-time

  - `required string Description`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `required string Name`

    The Skill's immutable kebab-case slug, set at creation from the first
    upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
    later upload must resolve to the same value. Also the top-level directory
    of the Skill's mounted files and the base name of a downloaded archive.

  - `required string SkillID`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `JsonElement Type constant`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

#### Example

```csharp
VersionRetrieveParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var betaSkillVersion = await client.Beta.Skills.Versions.Retrieve(parameters);

Console.WriteLine(betaSkillVersion);
```

##### Response (200)

```json
{
  "id": "id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "description": "description",
  "name": "name",
  "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_version"
}
```

### Delete Skill Version

`BetaDeletedSkillVersion Beta.Skills.Versions.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

#### Parameters

- `VersionDeleteParams parameters`

  - `required string skillID`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `required string version`

    Path param: Identifies the skill version by its version ID.

    Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDeletedSkillVersion:`

  - `required string ID`

    Unique identifier for this Skill Version. The id addresses the version in
    paths and pins it in references.

  - `JsonElement Type constant`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

#### Example

```csharp
VersionDeleteParams parameters = new()
{
    SkillID = "skill_id",
    Version = "version",
};

var betaDeletedSkillVersion = await client.Beta.Skills.Versions.Delete(parameters);

Console.WriteLine(betaDeletedSkillVersion);
```

##### Response (200)

```json
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

## Beta › User Profiles

### Create User Profile

`BetaUserProfile Beta.UserProfiles.Create(parameters, cancellationToken = default)`

**POST** `/v1/user_profiles`

Create User Profile

#### Parameters

- `UserProfileCreateParams parameters`

  - `AccessType accessType`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? externalID`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `string? name`

    Body param: Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `Relationship relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `Active`

      - `Pending`

      - `Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

#### Example

```csharp
UserProfileCreateParams parameters = new();

var betaUserProfile = await client.Beta.UserProfiles.Create(parameters);

Console.WriteLine(betaUserProfile);
```

##### Response (200)

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

### List User Profiles

`UserProfileListPage Beta.UserProfiles.List(parameters, cancellationToken = default)`

**GET** `/v1/user_profiles`

List User Profiles

#### Parameters

- `UserProfileListParams parameters`

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `Order order`

    Query param: Query parameter for order

    - `Asc`

    - `Desc`

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `Active`

      - `Pending`

      - `Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

#### Example

```csharp
UserProfileListParams parameters = new();

var page = await client.Beta.UserProfiles.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Get User Profile

`BetaUserProfile Beta.UserProfiles.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

#### Parameters

- `UserProfileRetrieveParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `Active`

      - `Pending`

      - `Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

#### Example

```csharp
UserProfileRetrieveParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Retrieve(parameters);

Console.WriteLine(betaUserProfile);
```

##### Response (200)

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

### Update User Profile

`BetaUserProfile Beta.UserProfiles.Update(parameters, cancellationToken = default)`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

#### Parameters

- `UserProfileUpdateParams parameters`

  - `required string userProfileID`

    Path param: Path parameter user_profile_id

  - `AccessType? accessType`

    Body param: How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? externalID`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `string? name`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `Relationship? relationship`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaUserProfile:`

  - `required string ID`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required IReadOnlyDictionary<string, string> Metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `required IReadOnlyDictionary<string, BetaUserProfileTrustGrant> TrustGrants`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `required Status Status`

      Status of the trust grant.

      - `Active`

      - `Pending`

      - `Rejected`

  - `required Type Type`

    Object type. Always `user_profile`.

  - `required DateTimeOffset UpdatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `AccessType AccessType`

    How the platform uses the API on behalf of the entity this profile represents. `application`: the platform sells a product that uses the API behind the scenes, and the profile represents an individual end-user of that product. `passthrough`: the platform resells raw inference, and the profile identifies the resold-to company.

    - `Application`

    - `Passthrough`

  - `string? ExternalID`

    Platform's own identifier for this user. Not enforced unique.

  - `string? Name`

    Real-world name of the entity this profile represents (company or individual). For a resold-to company (`access_type` `passthrough`, or `relationship` `resold` under the `user-profiles-2026-03-24` header) this is that company's name.

  - `Relationship Relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `External`

    - `Resold`

    - `Internal`

#### Example

```csharp
UserProfileUpdateParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfile = await client.Beta.UserProfiles.Update(parameters);

Console.WriteLine(betaUserProfile);
```

##### Response (200)

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

### Create Enrollment URL

`BetaUserProfileEnrollmentUrl Beta.UserProfiles.CreateEnrollmentUrl(parameters, cancellationToken = default)`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

#### Parameters

- `UserProfileCreateEnrollmentUrlParams parameters`

  - `required string userProfileID`

    Path parameter user_profile_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `required DateTimeOffset ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required Type Type`

    Object type. Always `enrollment_url`.

  - `required string Url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

#### Example

```csharp
UserProfileCreateEnrollmentUrlParams parameters = new()
{
    UserProfileID = "uprof_011CZkZCu8hGbp5mYRQgUmz9"
};

var betaUserProfileEnrollmentUrl = await client.Beta.UserProfiles.CreateEnrollmentUrl(parameters);

Console.WriteLine(betaUserProfileEnrollmentUrl);
```

##### Response (200)

```json
{
  "expires_at": "2026-03-15T10:15:00Z",
  "type": "enrollment_url",
  "url": "https://platform.claude.com/user-profiles/enrollment/M3J0bGJxZ2ppMnptbnB1"
}
```

## Beta › Dreams

### Create a Dream

`BetaDream Beta.Dreams.Create(parameters, cancellationToken = default)`

**POST** `/v1/dreams`

Create a Dream

#### Parameters

- `DreamCreateParams parameters`

  - `required IReadOnlyList<BetaDreamInput> inputs`

    Body param

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required Model model`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `required string ID`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

        minLength: 1, maxLength: 256

      - `Speed? Speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `Standard`

        - `Fast`

  - `string? instructions`

    Body param

    minLength: 1, maxLength: 4096

  - `BetaOutputBehavior outputBehavior`

    Body param: The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `required Type Type`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `required int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `required int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `required int OutputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

##### Response (200)

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

### List Dreams

`DreamListPage Beta.Dreams.List(parameters, cancellationToken = default)`

**GET** `/v1/dreams`

List Dreams

#### Parameters

- `DreamListParams parameters`

  - `DateTimeOffset createdAtGt`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

    format: date-time

  - `DateTimeOffset createdAtLt`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

    format: date-time

  - `bool includeArchived`

    Query param: Query parameter for include_archived

  - `int limit`

    Query param: Query parameter for limit

    format: int32

  - `string page`

    Query param: Query parameter for page

  - `IReadOnlyList<BetaDreamStatus> statuses`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `required Type Type`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `required int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `required int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `required int OutputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```csharp
DreamListParams parameters = new();

var page = await client.Beta.Dreams.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Get a Dream

`BetaDream Beta.Dreams.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/dreams/{dream_id}`

Get a Dream

#### Parameters

- `DreamRetrieveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `required Type Type`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `required int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `required int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `required int OutputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```csharp
DreamRetrieveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Retrieve(parameters);

Console.WriteLine(betaDream);
```

##### Response (200)

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

### Cancel a Dream

`BetaDream Beta.Dreams.Cancel(parameters, cancellationToken = default)`

**POST** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

#### Parameters

- `DreamCancelParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `required Type Type`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `required int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `required int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `required int OutputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```csharp
DreamCancelParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Cancel(parameters);

Console.WriteLine(betaDream);
```

##### Response (200)

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

### Archive a Dream

`BetaDream Beta.Dreams.Archive(parameters, cancellationToken = default)`

**POST** `/v1/dreams/{dream_id}/archive`

Archive a Dream

#### Parameters

- `DreamArchiveParams parameters`

  - `required string dreamID`

    Path parameter dream_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `required string ID`

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? EndedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required BetaDreamError? Error`

    Failure detail for a Dream whose `status` is `failed`.

    - `required string Message`

    - `required string Type`

  - `required IReadOnlyList<BetaDreamInput> Inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `required IReadOnlyList<string> SessionIds`

      - `required Type Type`

  - `required string? Instructions`

  - `required BetaDreamModelConfig Model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `required string ID`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Speed Speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `Standard`

      - `Fast`

  - `required BetaOutputBehavior OutputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `required Type Type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `required string MemoryStoreID`

        minLength: 1

      - `required Type Type`

  - `required IReadOnlyList<BetaDreamOutput> Outputs`

    - `required string MemoryStoreID`

    - `required Type Type`

  - `required string? SessionID`

  - `required BetaDreamStatus Status`

    Lifecycle status of a Dream.

    - `Pending`

    - `Running`

    - `Completed`

    - `Failed`

    - `Canceled`

  - `required Type Type`

  - `required BetaDreamUsage Usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `required int CacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `required int CacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `required int InputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `required int OutputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

```csharp
DreamArchiveParams parameters = new() { DreamID = "dream_id" };

var betaDream = await client.Beta.Dreams.Archive(parameters);

Console.WriteLine(betaDream);
```

##### Response (200)

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

## Beta › Tunnels

### Create Tunnel

`BetaTunnel Beta.Tunnels.Create(parameters, cancellationToken = default)`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

#### Parameters

- `TunnelCreateParams parameters`

  - `string? displayName`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

    minLength: 1, maxLength: 255

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelCreateParams parameters = new();

var betaTunnel = await client.Beta.Tunnels.Create(parameters);

Console.WriteLine(betaTunnel);
```

##### Response (200)

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

### Get Tunnel

`BetaTunnel Beta.Tunnels.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

#### Parameters

- `TunnelRetrieveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelRetrieveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Retrieve(parameters);

Console.WriteLine(betaTunnel);
```

##### Response (200)

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

### List Tunnels

`TunnelListPage Beta.Tunnels.List(parameters, cancellationToken = default)`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

#### Parameters

- `TunnelListParams parameters`

  - `bool includeArchived`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `int limit`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelListParams parameters = new();

var page = await client.Beta.Tunnels.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Archive Tunnel

`BetaTunnel Beta.Tunnels.Archive(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

#### Parameters

- `TunnelArchiveParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `required string ID`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string? DisplayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `required string Domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelArchiveParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnel = await client.Beta.Tunnels.Archive(parameters);

Console.WriteLine(betaTunnel);
```

##### Response (200)

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

### Reveal Tunnel Token

`BetaTunnelToken Beta.Tunnels.RevealToken(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

#### Parameters

- `TunnelRevealTokenParams parameters`

  - `required string tunnelID`

    Path parameter tunnel_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelRevealTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RevealToken(parameters);

Console.WriteLine(betaTunnelToken);
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Rotate Tunnel Token

`BetaTunnelToken Beta.Tunnels.RotateToken(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

#### Parameters

- `TunnelRotateTokenParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `string? reason`

    Body param: Optional free-text reason for the rotation, recorded for audit.

    maxLength: 1024

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `required string ID`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `required string TunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonElement Type constant`

#### Example

```csharp
TunnelRotateTokenParams parameters = new() { TunnelID = "tunnel_id" };

var betaTunnelToken = await client.Beta.Tunnels.RotateToken(parameters);

Console.WriteLine(betaTunnelToken);
```

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

## Beta › Tunnels › Certificates

### Create Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Create(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

- `CertificateCreateParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string caCertificatePem`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

    maxLength: 8192

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type constant`

#### Example

```csharp
CertificateCreateParams parameters = new()
{
    TunnelID = "tunnel_id",
    CACertificatePem = "ca_certificate_pem",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Create(parameters);

Console.WriteLine(betaTunnelCertificate);
```

##### Response (200)

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

### Get Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

- `CertificateRetrieveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type constant`

#### Example

```csharp
CertificateRetrieveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Retrieve(parameters);

Console.WriteLine(betaTunnelCertificate);
```

##### Response (200)

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

### List Tunnel Certificates

`CertificateListPage Beta.Tunnels.Certificates.List(parameters, cancellationToken = default)`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `CertificateListParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `bool includeArchived`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `int limit`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

    format: int32

  - `string page`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type constant`

#### Example

```csharp
CertificateListParams parameters = new() { TunnelID = "tunnel_id" };

var page = await client.Beta.Tunnels.Certificates.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

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

### Archive Tunnel Certificate

`BetaTunnelCertificate Beta.Tunnels.Certificates.Archive(parameters, cancellationToken = default)`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

- `CertificateArchiveParams parameters`

  - `required string tunnelID`

    Path param: Path parameter tunnel_id

  - `required string certificateID`

    Path param: Path parameter certificate_id

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `required string ID`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `required DateTimeOffset? ArchivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset CreatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required DateTimeOffset? ExpiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `required string Fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `required string TunnelID`

    ID of the tunnel the certificate is registered against.

  - `JsonElement Type constant`

#### Example

```csharp
CertificateArchiveParams parameters = new()
{
    TunnelID = "tunnel_id",
    CertificateID = "certificate_id",
};

var betaTunnelCertificate = await client.Beta.Tunnels.Certificates.Archive(parameters);

Console.WriteLine(betaTunnelCertificate);
```

##### Response (200)

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

## Beta › Organization

### Get Current Organization

`BetaOrganization Beta.Organization.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/me`

Retrieve information about the organization associated with the authenticated API key.

#### Parameters

- `OrganizationRetrieveParams parameters`

#### Returns

- `class BetaOrganization:`

  - `required string ID`

    ID of the Organization.

    format: uuid

  - `required string Name`

    Name of the Organization.

  - `JsonElement Type constant`

    Object type.

    For Organizations, this is always `"organization"`.

#### Example

```csharp
OrganizationRetrieveParams parameters = new();

var betaOrganization = await client.Beta.Organization.Retrieve(parameters);

Console.WriteLine(betaOrganization);
```

##### Response (200)

```json
{
  "id": "12345678-1234-5678-1234-567812345678",
  "name": "Organization Name",
  "type": "organization"
}
```

## Beta › Organization › API Keys

### List API Keys

`ApiKeyListPage Beta.Organization.ApiKeys.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/api_keys`

List API Keys

#### Parameters

- `ApiKeyListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string? createdByUserID`

    Filter by the ID of the User who created the object.

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Status? status`

    Filter by API key status.

    - `Active`

    - `Archived`

    - `Expired`

    - `Inactive`

  - `string? workspaceID`

    Filter by Workspace ID.

#### Returns

- `class BetaApiKey:`

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required string ID`

      ID of the actor that created the object.

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount`

      - `User`

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type constant`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

      - `JsonElement Type constant`

        Principal type. Always `"service_account_actor"` for a Service Account.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type constant`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type constant`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active`

    - `Archived`

    - `Expired`

    - `Inactive`

  - `JsonElement Type constant`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyListParams parameters = new();

var page = await client.Beta.Organization.ApiKeys.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by": {
        "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
        "type": "user"
      },
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "name": "Developer Key",
      "partial_key_hint": "sk-ant-api03-R2D...igAA",
      "principal": {
        "type": "user_actor",
        "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
      },
      "scope": {
        "type": "workspace",
        "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
      },
      "status": "active",
      "type": "api_key",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get API Key

`BetaApiKey Beta.Organization.ApiKeys.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/api_keys/{api_key_id}`

Get API Key

#### Parameters

- `ApiKeyRetrieveParams parameters`

  - `required string apiKeyID`

    ID of the API key.

#### Returns

- `class BetaApiKey:`

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required string ID`

      ID of the actor that created the object.

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount`

      - `User`

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type constant`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

      - `JsonElement Type constant`

        Principal type. Always `"service_account_actor"` for a Service Account.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type constant`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type constant`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active`

    - `Archived`

    - `Expired`

    - `Inactive`

  - `JsonElement Type constant`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyRetrieveParams parameters = new() { ApiKeyID = "api_key_id" };

var betaApiKey = await client.Beta.Organization.ApiKeys.Retrieve(parameters);

Console.WriteLine(betaApiKey);
```

##### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

### Update API Key

`BetaApiKey Beta.Organization.ApiKeys.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/api_keys/{api_key_id}`

Update API Key

#### Parameters

- `ApiKeyUpdateParams parameters`

  - `required string apiKeyID`

    ID of the API key.

  - `string? name`

    Name of the API key.

    maxLength: 500, minLength: 1

  - `Status? status`

    Status of the API key.

    - `Active`

    - `Archived`

    - `Inactive`

#### Returns

- `class BetaApiKey:`

  - `required string ID`

    ID of the API key.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the API Key was created.

    format: date-time

  - `required BetaApiKeyCreatedBy? CreatedBy`

    The ID and type of the actor that created the API key, or `null` when the
    creator is not recorded (legacy, workload-identity-federated, or
    system-created keys).

    - `required string ID`

      ID of the actor that created the object.

    - `required Type Type`

      Type of the actor that created the object.

      - `ServiceAccount`

      - `User`

  - `required DateTimeOffset? ExpiresAt`

    RFC 3339 datetime string indicating when the API Key expires, or `null` if it never expires.

    format: date-time

  - `required string Name`

    Name of the API key.

  - `required string? PartialKeyHint`

    Partially redacted hint for the API key.

  - `required Principal? Principal`

    The principal the API key acts as (a User or a Service Account), or `null` if the API key is not bound to a principal.

    - `class BetaApiKeyUserActor:`

      - `JsonElement Type constant`

        Principal type. Always `"user_actor"` for a User.

      - `required string UserID`

        ID of the User the API key acts as.

    - `class BetaApiKeyServiceAccountActor:`

      - `required string ServiceAccountID`

        ID of the Service Account the API key acts as.

      - `JsonElement Type constant`

        Principal type. Always `"service_account_actor"` for a Service Account.

  - `required Scope Scope`

    Where the API key belongs: its Workspace (`{"type": "workspace", "workspace_id": "wrkspc_..."}`, with the Workspace's real ID even when it is the organization's default Workspace), or the organization (`{"type": "organization"}`) for a principal-bound API key that has no Workspace.

    - `class BetaApiKeyOrganizationScope:`

      - `JsonElement Type constant`

        Scope type. Always `"organization"`: the API key has no Workspace. Only a principal-bound API key can have this scope.

    - `class BetaApiKeyWorkspaceScope:`

      - `JsonElement Type constant`

        Scope type. Always `"workspace"`: the API key belongs to one Workspace.

      - `required string WorkspaceID`

        ID of the Workspace the API key belongs to. Unlike the deprecated top-level `workspace_id`, this is the Workspace's real ID even for the organization's default Workspace.

  - `required Status Status`

    Status of the API key.

    - `Active`

    - `Archived`

    - `Expired`

    - `Inactive`

  - `JsonElement Type constant`

    Object type.

    For API Keys, this is always `"api_key"`.

  - `required string? WorkspaceID`

    **Deprecated**: Use `scope` instead. `workspace_id` is `null` both for an API key in the default Workspace and for a principal-bound API key that has no Workspace.

    Deprecated: use `scope` instead. ID of the Workspace associated with the API key, or `null` if the API key belongs to the default Workspace. Also `null` for a principal-bound API key that has no Workspace; `scope` tells the two apart.

#### Example

```csharp
ApiKeyUpdateParams parameters = new() { ApiKeyID = "api_key_id" };

var betaApiKey = await client.Beta.Organization.ApiKeys.Update(parameters);

Console.WriteLine(betaApiKey);
```

##### Response (200)

```json
{
  "id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by": {
    "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
    "type": "user"
  },
  "expires_at": "2024-10-30T23:58:27.427722Z",
  "name": "Developer Key",
  "partial_key_hint": "sk-ant-api03-R2D...igAA",
  "principal": {
    "type": "user_actor",
    "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q"
  },
  "scope": {
    "type": "workspace",
    "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
  },
  "status": "active",
  "type": "api_key",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Beta › Organization › External Keys

### Create External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys`

Create an external key config owned by the caller's organization.

#### Parameters

- `ExternalKeyCreateParams parameters`

  - `required ProviderConfig providerConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfigParam:`

      Azure Key Vault provider configuration.

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `string? displayName`

    Human-friendly display name.

    maxLength: 255, minLength: 1

  - `Geo geo`

    Data residency geo. Only `us` is supported.

    - `Us`

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type constant`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type constant`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfig:`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyCreateParams parameters = new()
{
    ProviderConfig = new BetaAwsExternalKeyConfig()
    {
        KmsArn = "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        Region = "us-east-1",
        RoleArn = "arn:aws:iam::111122223333:role/anthropic-cmek",
    },
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Create(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### List External Keys

`ExternalKeyListPage Beta.Organization.ExternalKeys.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/external_keys`

List external key configs in the caller's organization.

Results are ordered by creation time (newest first). Use the
`next_page` cursor from the response to fetch subsequent pages.

#### Parameters

- `ExternalKeyListParams parameters`

  - `long limit`

    Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type constant`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type constant`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfig:`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyListParams parameters = new();

var page = await client.Beta.Organization.ExternalKeys.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "attachment": {
        "type": "attached"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "prod-us-key",
      "geo": "us",
      "provider_config": {
        "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
        "type": "aws",
        "region": "us-east-1",
        "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
      },
      "type": "external_key",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "next_page": "next_page"
}
```

### Get External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/external_keys/{external_key_id}`

Retrieve a single external key config in the caller's organization by ID.

#### Parameters

- `ExternalKeyRetrieveParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type constant`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type constant`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfig:`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyRetrieveParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Retrieve(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Update External Key

`BetaExternalKey Beta.Organization.ExternalKeys.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys/{external_key_id}`

Partially update an external key config. Omitted fields are left unchanged.

`display_name` is always editable. `geo` and `provider_config` cannot
be changed once any workspace references this config, because previously
encrypted data requires the original key identity to decrypt.

#### Parameters

- `ExternalKeyUpdateParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

  - `string? displayName`

    Human-friendly display name.

    maxLength: 255, minLength: 1

  - `Geo? geo`

    Data residency geo. Only `us` is supported.

    - `Us`

  - `ProviderConfig? providerConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfigParam:`

      Azure Key Vault provider configuration.

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

#### Returns

- `class BetaExternalKey:`

  CMEK external key config belonging to the caller's organization.

  Configs are organization-scoped. Workspaces attach to a config; once any
  workspace references it, the provider fields become effectively immutable
  (existing encrypted data needs the config for decrypt).

  - `required string ID`

    Identifier of the external key config. A tagged ID prefixed `ekey_`, or — for organizations on the Claude Platform on AWS — the AWS KMS key ARN.

  - `required Attachment Attachment`

    Whether any workspace uses this config to encrypt its data — counting live and archived workspaces (an archived workspace's data remains encrypted under the config), excluding deleted ones. Only an attached config is used by the encryption path; an `unattached` config is inert and can be deleted.

    - `class BetaExternalKeyAttachedAttachment:`

      - `JsonElement Type constant`

    - `class BetaExternalKeyUnattachedAttachment:`

      - `JsonElement Type constant`

  - `required DateTimeOffset CreatedAt`

    format: date-time

  - `required string? DisplayName`

    Human-friendly display name. Null if none was set.

  - `required string Geo`

    Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.

  - `required ProviderConfig ProviderConfig`

    KMS provider identity and auth coordinates.

    - `class BetaAwsExternalKeyConfig:`

      - `required string KmsArn`

        Full ARN of the AWS KMS key.

        maxLength: 2048

      - `JsonElement Type constant`

      - `string? Region`

        AWS region. Derived from `kms_arn` if omitted.

      - `string? RoleArn`

        **Deprecated**

        IAM role ARN. Deprecated — Anthropic reaches the KMS key via a managed intermediate role; this field is ignored.

    - `class BetaGcpExternalKeyConfig:`

      - `required string KeyName`

        Full resource name of the Cloud KMS key.

      - `JsonElement Type constant`

    - `class BetaAzureExternalKeyConfig:`

      - `required string KeyName`

        Name of the key within the vault.

      - `required string TenantID`

        Azure AD tenant ID.

      - `JsonElement Type constant`

      - `required string VaultUri`

        Key Vault data-plane URI — `https://{vault-name}.vault.azure.net` or `https://{hsm-name}.managedhsm.azure.net`.

      - `string? ClientID`

        Azure AD application (client) ID. Omit to use Anthropic's multitenant app. Provide only if using a single-tenant app registration in the customer's directory.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    format: date-time

#### Example

```csharp
ExternalKeyUpdateParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var betaExternalKey = await client.Beta.Organization.ExternalKeys.Update(parameters);

Console.WriteLine(betaExternalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "attachment": {
    "type": "attached"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "prod-us-key",
  "geo": "us",
  "provider_config": {
    "kms_arn": "arn:aws:kms:us-east-1:111122223333:key/abcd1234-5678-90ab-cdef-000011112222",
    "type": "aws",
    "region": "us-east-1",
    "role_arn": "arn:aws:iam::111122223333:role/anthropic-cmek"
  },
  "type": "external_key",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

### Delete External Key

`ExternalKeyDeleteResponse Beta.Organization.ExternalKeys.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/external_keys/{external_key_id}`

Delete an external key config.

The request is rejected if any workspace still references this config.

#### Parameters

- `ExternalKeyDeleteParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class ExternalKeyDeleteResponse:`

  - `required string ID`

    ID of the deleted External Key.

  - `JsonElement Type constant`

#### Example

```csharp
ExternalKeyDeleteParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var externalKey = await client.Beta.Organization.ExternalKeys.Delete(parameters);

Console.WriteLine(externalKey);
```

##### Response (200)

```json
{
  "id": "ekey_01AbCdEfGhIjKlMnOpQrStUv",
  "type": "external_key_deleted"
}
```

### Validate External Key

`ExternalKeyValidateResponse Beta.Organization.ExternalKeys.Validate(parameters, cancellationToken = default)`

**POST** `/v1/organizations/external_keys/{external_key_id}/validate`

Validate an external key config against the customer's KMS.

Anthropic performs an encrypt/decrypt roundtrip against the configured
KMS key and waits up to 30 seconds for the result. The response status is
`success` if the roundtrip succeeded, or `failure` with an error
message if it failed or timed out.

#### Parameters

- `ExternalKeyValidateParams parameters`

  - `required string externalKeyID`

    ID of the External Key.

    maxLength: 2048

#### Returns

- `class ExternalKeyValidateResponse:`

  Result of a validation roundtrip against the customer's KMS.

  HTTP 200 for both outcomes — the operation completed; `status` says
  whether the key works.

  - `required string? Error`

    Error message when status is `failure`. Null otherwise.

  - `required Status Status`

    `success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

    - `Failure`

    - `Success`

  - `JsonElement Type constant`

#### Example

```csharp
ExternalKeyValidateParams parameters = new()
{
    ExternalKeyID = "external_key_id"
};

var response = await client.Beta.Organization.ExternalKeys.Validate(parameters);

Console.WriteLine(response);
```

##### Response (200)

```json
{
  "error": "error",
  "status": "failure",
  "type": "external_key_validation"
}
```

## Beta › Organization › Federation › Issuers

### Create Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Register an OIDC issuer that Anthropic will trust for workload identity
federation in your organization.

The `jwks` field controls how the issuer's signing keys are obtained and
takes one of three shapes selected by `type`: `discovery` (resolve keys
through OIDC discovery), `explicit_url` (fetch keys from a fixed JWKS
URL), or `inline` (provide a static key set). When `jwks.type` is
`discovery` and no `discovery_base` is set, the issuer URL must be
publicly reachable over HTTPS so Anthropic can fetch the discovery
document; for `explicit_url` and `inline` modes the issuer URL is only
matched as the JWT's `iss` claim and is not fetched.

#### Parameters

- `IssuerCreateParams parameters`

  - `required string issuerUrl`

    Body param: The `iss` claim value to match against.

    minLength: 1

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `bool? checkJti`

    Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Defaults to true. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `Jwks jwks`

    Body param: How signing keys are obtained. Defaults to OIDC discovery.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `long? maxJwtLifetimeSeconds`

    Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Defaults to 3600 (1h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

    maximum: 176400, exclusiveMinimum: 0

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerCreateParams parameters = new()
{
    IssuerUrl = "x",
    Name = "x",
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Create(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Federation Issuers

`IssuerListPage Beta.Organization.Federation.Issuers.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_issuers`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

#### Parameters

- `IssuerListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerListParams parameters = new();

var page = await client.Beta.Organization.Federation.Issuers.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation issuer by its ID (`fdis_...`).

#### Parameters

- `IssuerRetrieveParams parameters`

  - `required string federationIssuerID`

    ID of the federation issuer.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerRetrieveParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Retrieve(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session.

#### Parameters

- `IssuerUpdateParams parameters`

  - `required string federationIssuerID`

    Path param: ID of the federation issuer to update.

  - `bool? checkJti`

    Body param: Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `string? issuerUrl`

    Body param: Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

    minLength: 1

  - `Jwks? jwks`

    Body param: Replaces the entire JWKS configuration.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `bool? jwksPollingDisabled`

    Body param: Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.

  - `long? maxJwtLifetimeSeconds`

    Body param: Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

    maximum: 176400, exclusiveMinimum: 0

  - `string? name`

    Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerUpdateParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Update(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Federation Issuer

`BetaFederationIssuer Beta.Organization.Federation.Issuers.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_issuers/{federation_issuer_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation issuer.

Idempotent; re-archiving returns the issuer with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still references the issuer; archive those rules first (a rule's
issuer cannot be changed), or recreate them against another issuer.

#### Parameters

- `IssuerArchiveParams parameters`

  - `required string federationIssuerID`

    ID of the federation issuer to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationIssuer:`

  Registered external OIDC identity provider.

  Records an external IdP the organization trusts for the RFC 7523
  jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

  - `required string ID`

    Tagged ID of the federation issuer.

  - `required DateTimeOffset? ArchivedAt`

    If set, all rules referencing this issuer reject token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

  - `required bool CheckJti`

    Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

  - `required DateTimeOffset CreatedAt`

    When this issuer was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

  - `required string IssuerUrl`

    The `iss` claim value. Incoming JWTs must match exactly.

  - `required Jwks Jwks`

    How signing keys are obtained for signature verification.

    - `class BetaJwksDiscovery:`

      JWKS via the issuer's OIDC discovery document.

      - `JsonElement Type constant`

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

      - `string? DiscoveryBase`

        Set when the discovery URL differs from `issuer_url`.

    - `class BetaJwksExplicitUrl:`

      JWKS fetched from a fixed endpoint.

      - `JsonElement Type constant`

      - `required string Url`

        JWKS endpoint.

        minLength: 1

      - `string? CACertPem`

        Optional custom CA (PEM) for TLS verification of the JWKS fetch.

        maxLength: 8192

    - `class BetaJwksInline:`

      JWKS supplied directly; no network fetch.

      - `required IReadOnlyList<IReadOnlyDictionary<string, JsonElement>> Keys`

        Inline JWK objects.

        minItems: 1

      - `JsonElement Type constant`

  - `required DateTimeOffset? JwksPollingDisabledAt`

    If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

    format: date-time

  - `required long MaxJwtLifetimeSeconds`

    Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required BetaFederationIssuerPollStatus? PollStatus`

    Status of automatic JWKS polling for a federation issuer.

    Anthropic periodically fetches the issuer's signing keys in the
    background. These fields summarize the most recent fetches so the
    health of the JWKS endpoint can be monitored.

    - `required long ConsecutiveFailures`

      Consecutive fetch failures since the last success.

    - `required DateTimeOffset? LastFetchedAt`

      When the last successful fetch completed.

      format: date-time

    - `required DateTimeOffset? NextPollAt`

      When the next fetch is scheduled. Null if paused.

      format: date-time

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this issuer was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### Example

```csharp
IssuerArchiveParams parameters = new()
{
    FederationIssuerID = "federation_issuer_id"
};

var betaFederationIssuer = await client.Beta.Organization.Federation.Issuers.Archive(parameters);

Console.WriteLine(betaFederationIssuer);
```

##### Response (200)

```json
{
  "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "check_jti": true,
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "issuer_url": "https://token.actions.githubusercontent.com",
  "jwks": {
    "type": "discovery",
    "ca_cert_pem": "ca_cert_pem",
    "discovery_base": "discovery_base"
  },
  "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
  "max_jwt_lifetime_seconds": 0,
  "name": "github-actions",
  "poll_status": {
    "consecutive_failures": 0,
    "last_fetched_at": "2019-12-27T18:11:19.117Z",
    "next_poll_at": "2019-12-27T18:11:19.117Z"
  },
  "type": "federation_issuer",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Beta › Organization › Federation › Rules

### Create Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a federation rule owned by your organization.

The referenced issuer and the target service account must already exist
in the same organization; invalid references are rejected with a 400
error. The workspace reference is validated. Membership is not checked
at rule creation: token exchange resolves a single enabled workspace per
call and is rejected unless the target service account is a member of
that workspace (it is implicitly a member of the default workspace).
Rules on well-known shared issuers (GitHub Actions, GitLab, Buildkite,
Terraform Cloud, Google) must constrain tenant identity via an
identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). OAuth callers may only
manage rules whose `oauth_scope` is `workspace:developer` or
`workspace:inference`; other scopes require a Console session.

#### Parameters

- `RuleCreateParams parameters`

  - `required string issuerID`

    Body param: Tagged ID of the federation issuer.

  - `required BetaFederationRuleMatch match`

    Body param: Conditions the verified JWT must satisfy for this rule to apply. At least one of `subject_prefix` (other than a wildcard-only value like `*`), `claims`, or `condition` is required; `audience` alone is not sufficient.

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `required string oauthScope`

    Body param: Space-separated OAuth scopes. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

    minLength: 1

  - `required BetaServiceAccountTarget target`

    Body param: Identity that tokens minted via this rule act as. Currently always a `service_account` target.

  - `bool appliesToAllWorkspaces`

    Body param: When true, enable this rule for every workspace in the org (including workspaces created later).

  - `IReadOnlyDictionary<string, string>? attributes`

    Body param: CEL expressions `{name: expr}` extracting named values from claims. Not yet supported; any non-empty value is rejected with 400.

  - `string? description`

    Body param: Optional free-text description.

    maxLength: 2000

  - `long tokenLifetimeSeconds`

    Body param: Lifetime in seconds for access tokens minted via this rule (60-86400). Defaults to 3600 (1h). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

    maximum: 86400, minimum: 60

  - `string? workspaceID`

    Body param: Tagged ID of the workspace to enable this rule for. Required unless `applies_to_all_workspaces` is true. Additional workspaces can be added via the `/federation_rules/{federation_rule_id}/workspaces` sub-resource.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `JsonElement Type constant`

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleCreateParams parameters = new()
{
    IssuerID = "issuer_id",
    Match = new()
    {
        Audience = "audience",
        Claims = new Dictionary<string, string>() { { "foo", "string" } },
        Condition = "condition",
        SubjectPrefix = "subject_prefix",
    },
    Name = "x",
    OAuthScope = "x",
    Target = new()
    {
        ServiceAccountID = "svac_01SDCCSbTxrXDpWc1phhtcfK",
        ServiceAccountName = "service_account_name",
    },
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Create(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### List Federation Rules

`RuleListPage Beta.Organization.Federation.Rules.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

#### Parameters

- `RuleListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `string? issuerID`

    Query param: Filter to rules referencing this federation issuer.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `JsonElement Type constant`

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleListParams parameters = new();

var page = await client.Beta.Organization.Federation.Rules.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

### Get Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a federation rule by its ID (`fdrl_...`).

#### Parameters

- `RuleRetrieveParams parameters`

  - `required string federationRuleID`

    ID of the federation rule.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `JsonElement Type constant`

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleRetrieveParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Retrieve(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Update Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Partially update a federation rule.

`issuer_id` is immutable. `match` and `target` are replaced as whole
objects when set. Referenced service accounts and workspaces must exist
in your organization; invalid references are rejected with a 400 error.
Archived rules cannot be updated; this returns 400. Create a new rule
instead. Rules on well-known shared issuers (GitHub Actions, GitLab,
Buildkite, Terraform Cloud, Google) must constrain tenant identity via
an identity-bearing claim, a tenant-pinning subject prefix (such as
`repo:YOUR_ORG/...`), or a CEL condition referencing one of those
identity claims (e.g. `claims.repository_owner`). On these issuers the
requirement is re-checked on every update; if an existing rule's stored
match does not yet constrain tenant identity, any update (even a rename
or description change) must also supply a conforming `match` in the same
request. OAuth callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `RuleUpdateParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule to update.

  - `bool? appliesToAllWorkspaces`

    Body param: When true, enables this rule for every workspace in the org (including workspaces created later). Setting `false` is rejected with 400 if no workspace would remain enabled; a rule with only a legacy `workspace_id` binding continues to mint.

  - `IReadOnlyDictionary<string, string>? attributes`

    Body param: Replaces the CEL expressions `{name: expr}` extracting named values from claims. Send null to clear them. Not yet supported; any non-empty value is rejected with 400.

  - `string? description`

    Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `BetaFederationRuleMatch? match`

    Body param: Does the incoming JWT qualify?

    All populated fields must pass; omitted fields are skipped. At least one
    of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
    or `condition` is required; `audience` alone is not sufficient.

  - `string? name`

    Body param: Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `string? oauthScope`

    Body param: Replaces the space-separated OAuth scopes granted on minted tokens. OAuth callers may only set `workspace:developer` or `workspace:inference`; other scopes (such as `org:admin`) require a Console session.

    minLength: 1

  - `BetaServiceAccountTarget? target`

    Body param: Bind to a fixed service account by ID.

  - `long? tokenLifetimeSeconds`

    Body param: Replaces the lifetime in seconds for access tokens minted via this rule (60-86400). Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

    maximum: 86400, minimum: 60

  - `string? workspaceID`

    Body param: Replaces the existing single workspace enablement (the previous one is removed). Rejected with 400 if the rule is enabled for more than one workspace; use the `/federation_rules/{federation_rule_id}/workspaces` sub-resource instead.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `JsonElement Type constant`

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleUpdateParams parameters = new() { FederationRuleID = "federation_rule_id" };

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Update(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

### Archive Federation Rule

`BetaFederationRule Beta.Organization.Federation.Rules.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `RuleArchiveParams parameters`

  - `required string federationRuleID`

    ID of the federation rule to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRule:`

  Authorization rule binding an external OIDC identity to Anthropic.

  Evaluates the match conditions and mints an OAuth access token for the
  resolved target, scoped to a single workspace where the rule is enabled
  (chosen by the caller at exchange time when the rule is enabled for more
  than one). For rules enabled via `workspace_ids` or
  `applies_to_all_workspaces`, the target service account must be a member
  of that workspace (it is implicitly a member of the default workspace);
  rules carrying only the legacy `workspace_id` binding do not enforce
  this.

  - `required string ID`

    Tagged ID of the federation rule.

  - `required bool AppliesToAllWorkspaces`

    When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

  - `required DateTimeOffset? ArchivedAt`

    If set, this rule is archived and rejects token exchange.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

  - `required IReadOnlyDictionary<string, string>? Attributes`

    CEL expressions extracting named values from claims. Not yet supported; always null.

  - `required DateTimeOffset CreatedAt`

    When this rule was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this rule.

  - `required string? Description`

    Optional free-text description.

  - `required string IssuerID`

    Tagged ID of the issuer whose tokens this rule accepts.

  - `required string? IssuerName`

    Issuer's display name at read time.

  - `required BetaFederationRuleMatch Match`

    Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

    - `string? Audience`

      Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

      maxLength: 1024

    - `IReadOnlyDictionary<string, string>? Claims`

      Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

    - `string? Condition`

      CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

      maxLength: 4096

    - `string? SubjectPrefix`

      Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

      maxLength: 1024

  - `required string Name`

    Admin-chosen slug identifier.

  - `required string OAuthScope`

    Space-separated OAuth scopes granted on the minted token.

  - `required BetaServiceAccountTarget Target`

    Identity that tokens minted via this rule act as. Currently always a `service_account` target.

    - `required string ServiceAccountID`

      Tagged ID of the service account to mint tokens for.

    - `JsonElement Type constant`

    - `string? ServiceAccountName`

      Service account's display name at read time. Ignored on writes.

  - `required long TokenLifetimeSeconds`

    Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this rule was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

  - `required string? WorkspaceID`

    Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

  - `required IReadOnlyList<string> WorkspaceIds`

    Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Example

```csharp
RuleArchiveParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var betaFederationRule = await client.Beta.Organization.Federation.Rules.Archive(parameters);

Console.WriteLine(betaFederationRule);
```

##### Response (200)

```json
{
  "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
  "applies_to_all_workspaces": true,
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "attributes": {
    "foo": "string"
  },
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "issuer_id": "issuer_id",
  "issuer_name": "issuer_name",
  "match": {
    "audience": "audience",
    "claims": {
      "foo": "string"
    },
    "condition": "condition",
    "subject_prefix": "subject_prefix"
  },
  "name": "prod-deploy-pipeline",
  "oauth_scope": "oauth_scope",
  "target": {
    "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
    "type": "service_account",
    "service_account_name": "service_account_name"
  },
  "token_lifetime_seconds": 0,
  "type": "federation_rule",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id",
  "workspace_id": "workspace_id",
  "workspace_ids": [
    "string"
  ]
}
```

## Beta › Organization › Federation › Rules › Workspaces

### Add Federation Rule Workspace

`BetaFederationRuleWorkspace Beta.Organization.Federation.Rules.Workspaces.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Enable a federation rule for a workspace.

Idempotent; re-enabling returns the existing enablement. The rule and
workspace must both belong to your organization. Membership of the
rule's target service account in this workspace is not checked at
enablement: token exchange into this workspace is rejected unless the
target is a member (it is implicitly a member of the default workspace).
Archived rules are rejected with 400. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session.

#### Parameters

- `WorkspaceAddParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `required string workspaceID`

    Body param: Tagged ID of the workspace to enable this rule for.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `required DateTimeOffset CreatedAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged ID of the workspace this rule is enabled for.

  - `required string? WorkspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```csharp
WorkspaceAddParams parameters = new()
{
    FederationRuleID = "federation_rule_id",
    WorkspaceID = "workspace_id",
};

var betaFederationRuleWorkspace = await client.Beta.Organization.Federation.Rules.Workspaces.Add(parameters);

Console.WriteLine(betaFederationRuleWorkspace);
```

##### Response (200)

```json
{
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace",
  "workspace_id": "workspace_id",
  "workspace_name": "workspace_name"
}
```

### List Federation Rule Workspaces

`WorkspaceListPage Beta.Organization.Federation.Rules.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

#### Parameters

- `WorkspaceListParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaFederationRuleWorkspace:`

  - `required DateTimeOffset CreatedAt`

    When this workspace was enabled for the rule.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged ID of the workspace this rule is enabled for.

  - `required string? WorkspaceName`

    Workspace display name. Populated when listing; null in the enable response.

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    FederationRuleID = "federation_rule_id"
};

var page = await client.Beta.Organization.Federation.Rules.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Federation Rule Workspace

`WorkspaceRemoveResponse Beta.Organization.Federation.Rules.Workspaces.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/federation_rules/{federation_rule_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Disable a federation rule for a workspace.

Idempotent; succeeds even if the enablement was already removed. OAuth
callers may only manage rules whose `oauth_scope` is
`workspace:developer` or `workspace:inference`; other scopes require a
Console session.

#### Parameters

- `WorkspaceRemoveParams parameters`

  - `required string federationRuleID`

    Path param: ID of the federation rule.

  - `required string workspaceID`

    Path param: ID of the workspace to disable for.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `required string FederationRuleID`

    Tagged ID of the federation rule.

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged ID of the workspace named in the delete request. Removal is idempotent.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    FederationRuleID = "federation_rule_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.Federation.Rules.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
```

##### Response (200)

```json
{
  "federation_rule_id": "federation_rule_id",
  "type": "federation_rule_workspace_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Invites

### Create Invite

`BetaOrganizationInvite Beta.Organization.Invites.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/invites`

Invite a user to join the organization by email.

On plans that draw members from a finite pool of purchased seats, the invite automatically consumes a seat from the lowest tier with availability; there is no seat-tier parameter. When no seat is free the request fails with a 400 error rather than purchasing a seat.

#### Parameters

- `InviteCreateParams parameters`

  - `required string email`

    Email of the User.

    format: email

  - `required Role role`

    Role for the invited User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `User`

  - `IReadOnlyList<string> rbacGroupIds`

    RBAC group IDs to assign to the User when the Invite is accepted. A non-empty array is accepted only for a Claude Enterprise organization with RBAC groups, and requires the key to carry the `write:rbac_groups` scope.

    maxItems: 100

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `required Status Status`

    Status of the Invite.

    - `Accepted`

    - `Deleted`

    - `Expired`

    - `Pending`

  - `JsonElement Type constant`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteCreateParams parameters = new()
{
    Email = "user@emaildomain.com",
    Role = Role.User,
};

var betaOrganizationInvite = await client.Beta.Organization.Invites.Create(parameters);

Console.WriteLine(betaOrganizationInvite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### List Invites

`InviteListPage Beta.Organization.Invites.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites`

List the organization's invites.

#### Parameters

- `InviteListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by the email address the Invite was sent to. Matches the same way as the Users list's `email` filter (normalized, case-insensitive).

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

  - `IReadOnlyList<Status> statuses`

    Filter by Invite status. Repeatable; values are OR'ed together. Omit to return `pending`, `accepted`, and `expired` Invites alike.

    - `Accepted`

    - `Expired`

    - `Pending`

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `required Status Status`

    Status of the Invite.

    - `Accepted`

    - `Deleted`

    - `Expired`

    - `Pending`

  - `JsonElement Type constant`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteListParams parameters = new();

var page = await client.Beta.Organization.Invites.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
      "accepted_at": "2019-12-27T18:11:19.117Z",
      "email": "user@emaildomain.com",
      "expires_at": "2024-11-20T23:58:27.427722Z",
      "invited_at": "2024-10-30T23:58:27.427722Z",
      "rbac_group_ids": [
        "string"
      ],
      "role": "admin",
      "status": "pending",
      "type": "invite"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get Invite

`BetaOrganizationInvite Beta.Organization.Invites.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/invites/{invite_id}`

Retrieve an invite by ID.

#### Parameters

- `InviteRetrieveParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class BetaOrganizationInvite:`

  - `required string ID`

    ID of the Invite.

  - `required DateTimeOffset? AcceptedAt`

    RFC 3339 datetime string indicating when the Invite was accepted, or null.

    format: date-time

  - `required string Email`

    Email of the User being invited.

  - `required DateTimeOffset ExpiresAt`

    RFC 3339 datetime string indicating when the Invite expires.

    format: date-time

  - `required DateTimeOffset InvitedAt`

    RFC 3339 datetime string indicating when the Invite was created.

    format: date-time

  - `required IReadOnlyList<string> RbacGroupIds`

    RBAC group IDs recorded on the Invite (Claude Enterprise organizations), to be assigned to the User when the Invite is accepted. `[]` when none.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `required Status Status`

    Status of the Invite.

    - `Accepted`

    - `Deleted`

    - `Expired`

    - `Pending`

  - `JsonElement Type constant`

    Object type.

    For Invites, this is always `"invite"`.

#### Example

```csharp
InviteRetrieveParams parameters = new() { InviteID = "invite_id" };

var betaOrganizationInvite = await client.Beta.Organization.Invites.Retrieve(parameters);

Console.WriteLine(betaOrganizationInvite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "accepted_at": "2019-12-27T18:11:19.117Z",
  "email": "user@emaildomain.com",
  "expires_at": "2024-11-20T23:58:27.427722Z",
  "invited_at": "2024-10-30T23:58:27.427722Z",
  "rbac_group_ids": [
    "string"
  ],
  "role": "admin",
  "status": "pending",
  "type": "invite"
}
```

### Delete Invite

`InviteDeleteResponse Beta.Organization.Invites.Delete(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/invites/{invite_id}`

Delete a pending invite.

#### Parameters

- `InviteDeleteParams parameters`

  - `required string inviteID`

    ID of the Invite.

#### Returns

- `class InviteDeleteResponse:`

  - `required string ID`

    ID of the Invite.

  - `JsonElement Type constant`

    Deleted object type.

    For Invites, this is always `"invite_deleted"`.

#### Example

```csharp
InviteDeleteParams parameters = new() { InviteID = "invite_id" };

var invite = await client.Beta.Organization.Invites.Delete(parameters);

Console.WriteLine(invite);
```

##### Response (200)

```json
{
  "id": "invite_015gWxCN9Hfg2QhZwTK7Mdeu",
  "type": "invite_deleted"
}
```

## Beta › Organization › Service Accounts

### Create Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Create a service account.

A service account is a named workload identity that federation rules
target. `organization_role` is `developer` (default) or `admin`; a rule
may only be created or retargeted to grant `org:admin` scope when the
target's `organization_role` is `admin`. Creating an `admin`-role service
account requires an interactive credential (a user OAuth token or a
Console session) — a workload may only create `developer`-role service
accounts.

#### Parameters

- `ServiceAccountCreateParams parameters`

  - `required string name`

    Body param: Slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

    maxLength: 255, minLength: 1

  - `string? description`

    Body param: Optional free-text description.

    maxLength: 2000

  - `OrganizationRole organizationRole`

    Body param: Org-level role. Defaults to `developer`.

    - `Admin`

    - `Developer`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin`

    - `Developer`

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountCreateParams parameters = new() { Name = "ci-deploy-bot" };

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Create(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### List Service Accounts

`ServiceAccountListPage Beta.Organization.ServiceAccounts.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List service accounts in the caller's organization.

Results are ordered by creation time, newest first. Use `limit` and the
`next_page` cursor to paginate; set `include_archived=true` to include
archived service accounts.

#### Parameters

- `ServiceAccountListParams parameters`

  - `bool includeArchived`

    Query param: Include archived resources. Defaults to false.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin`

    - `Developer`

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountListParams parameters = new();

var page = await client.Beta.Organization.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "name": "ci-deploy-bot",
      "organization_role": "admin",
      "type": "service_account",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

### Get Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account by its ID (`svac_...`).

#### Parameters

- `ServiceAccountRetrieveParams parameters`

  - `required string serviceAccountID`

    ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin`

    - `Developer`

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Update Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Update a service account.

Only `description` and `organization_role` are mutable; `name` cannot be
changed. Archived service accounts cannot be updated; this returns 400.
Setting `organization_role` to `admin` (even when unchanged) requires an
interactive credential (a user OAuth token or a Console session).

#### Parameters

- `ServiceAccountUpdateParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account to update.

  - `string? description`

    Body param: Replaces the description. Omit to leave unchanged; send `null` to clear (the field is stored as an empty string).

    maxLength: 2000

  - `OrganizationRole? organizationRole`

    Body param: Replaces the org-level role. Omit or send `null` to leave unchanged.

    - `Admin`

    - `Developer`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin`

    - `Developer`

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

### Archive Service Account

`BetaServiceAccount Beta.Organization.ServiceAccounts.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}/archive`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Archive a service account.

Idempotent; re-archiving returns the service account with its original
`archived_at`. Rejected with 400 if any live (non-archived) federation
rule still targets this service account, same as issuer archival; archive
those rules first or change their target to another service account.

#### Parameters

- `ServiceAccountArchiveParams parameters`

  - `required string serviceAccountID`

    ID of the service account to archive.

  - `IReadOnlyList<AnthropicBeta> betas`

    Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccount:`

  Named non-human identity within the caller's organization.

  A service account is a pure identity: name + org. Authorization lives on
  whatever references it (federation rules).

  - `required string ID`

    Tagged ID of the service account.

  - `required DateTimeOffset? ArchivedAt`

    If set, this service account is archived.

    format: date-time

  - `required string? ArchivedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

  - `required DateTimeOffset CreatedAt`

    When this service account was created.

    format: date-time

  - `required string? CreatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that created this service account.

  - `required string? Description`

    Optional free-text description.

  - `required string Name`

    Admin-chosen slug identifier.

  - `required OrganizationRole OrganizationRole`

    Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

    - `Admin`

    - `Developer`

  - `JsonElement Type constant`

  - `required DateTimeOffset UpdatedAt`

    When this service account was last updated.

    format: date-time

  - `required string? UpdatedByActorID`

    Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### Example

```csharp
ServiceAccountArchiveParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var betaServiceAccount = await client.Beta.Organization.ServiceAccounts.Archive(parameters);

Console.WriteLine(betaServiceAccount);
```

##### Response (200)

```json
{
  "id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
  "archived_at": "2019-12-27T18:11:19.117Z",
  "archived_by_actor_id": "archived_by_actor_id",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "created_by_actor_id": "created_by_actor_id",
  "description": "description",
  "name": "ci-deploy-bot",
  "organization_role": "admin",
  "type": "service_account",
  "updated_at": "2024-10-30T23:58:27.427722Z",
  "updated_by_actor_id": "updated_by_actor_id"
}
```

## Beta › Organization › Service Accounts › Workspaces

### Add Workspace To Service Account

`BetaServiceAccountWorkspaceMember Beta.Organization.ServiceAccounts.Workspaces.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

Mirror of `POST /workspaces/{workspace_id}/service_accounts`, addressed
from the service-account side; both create the same membership. If the
service account is already an explicit member of the workspace, its
`workspace_role` is replaced with the value supplied here. Archived
workspaces return 400. Archived service accounts cannot be added and are
rejected.

#### Parameters

- `WorkspaceAddParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Body param: Tagged workspace ID to add the service account to.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
WorkspaceAddParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.ServiceAccounts.Workspaces.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### List Workspaces For Service Account

`WorkspaceListPage Beta.Organization.ServiceAccounts.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/service_accounts/{service_account_id}/workspaces`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the workspaces a service account is a member of.

Each entry includes the service account's `workspace_role` in that
workspace. Use `limit` and the `next_page` cursor to paginate. When the
service account has no explicit default-workspace membership, the
implicit (`implicit: true`) membership is returned as the first entry on
the first page; with `limit=1` the first page may return up to 2 entries
(the implicit entry plus one explicit membership) so a pagination cursor
can be derived. Memberships are returned only while
the service account is active. Without a `page` cursor, an archived
service account returns an empty list. A `page` cursor that does not
match an active membership returns a 400 invalid-request error. A cursor
stops matching when the membership is removed, the workspace is deleted,
or the service account is archived. Restart pagination from the first
page to recover.

#### Parameters

- `WorkspaceListParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
WorkspaceListParams parameters = new()
{
    ServiceAccountID = "service_account_id"
};

var page = await client.Beta.Organization.ServiceAccounts.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Remove Workspace From Service Account

`WorkspaceRemoveResponse Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/service_accounts/{service_account_id}/workspaces/{workspace_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Mirror of `DELETE /workspaces/{workspace_id}/service_accounts/{service_account_id}`,
addressed from the service-account side. Removal is idempotent (returns
200 even if the membership was already removed). A DELETE against the
implicit default-workspace membership returns 200 but is a no-op and the
membership persists; deleting an explicit default-workspace row reverts
to the implicit `workspace_user` membership. Archived workspaces return
400.

#### Parameters

- `WorkspaceRemoveParams parameters`

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class WorkspaceRemoveResponse:`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
WorkspaceRemoveParams parameters = new()
{
    ServiceAccountID = "service_account_id",
    WorkspaceID = "workspace_id",
};

var workspace = await client.Beta.Organization.ServiceAccounts.Workspaces.Remove(parameters);

Console.WriteLine(workspace);
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Users

### List Users

`UserListPage Beta.Organization.Users.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users`

List the organization's members.

#### Parameters

- `UserListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `string email`

    Filter by user email.

    format: email

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `IReadOnlyList<string> roles`

    Filter to items whose `role` equals one of the supplied values. Repeatable; values are OR'ed together.

    Accepted values depend on the organization type: Console and API organizations accept `user`, `developer`, `billing`, `admin`, and `claude_code_user`; Claude Enterprise organizations accept `user`, `owner`, `primary_owner`, `membership_admin`, and `managed`.

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `JsonElement Type constant`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserListParams parameters = new();

var page = await client.Beta.Organization.Users.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "added_at": "2024-10-30T23:58:27.427722Z",
      "email": "user@emaildomain.com",
      "name": "Jane Doe",
      "role": "admin",
      "type": "user"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Get User

`BetaOrganizationUser Beta.Organization.Users.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/users/{user_id}`

Retrieve a member of the organization by user ID.

#### Parameters

- `UserRetrieveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `JsonElement Type constant`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserRetrieveParams parameters = new() { UserID = "user_id" };

var betaOrganizationUser = await client.Beta.Organization.Users.Retrieve(parameters);

Console.WriteLine(betaOrganizationUser);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Update User

`BetaOrganizationUser Beta.Organization.Users.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/users/{user_id}`

Update a member's organization role.

#### Parameters

- `UserUpdateParams parameters`

  - `required string userID`

    ID of the User.

  - `required Role role`

    New role for the User.

    The accepted values depend on the organization type. Console and API organizations accept `user`, `developer`, `billing`, and `claude_code_user`; `admin` cannot be assigned through the API. Claude Enterprise organizations accept `user` and `managed`.

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `User`

#### Returns

- `class BetaOrganizationUser:`

  - `required string ID`

    ID of the User.

  - `required DateTimeOffset AddedAt`

    RFC 3339 datetime string indicating when the User joined the Organization.

    format: date-time

  - `required string Email`

    Email of the User.

  - `required string Name`

    Name of the User.

  - `required BetaOrganizationRole Role`

    Organization role of the User.

    - `Admin`

    - `Billing`

    - `ClaudeCodeUser`

    - `Developer`

    - `Managed`

    - `MembershipAdmin`

    - `Owner`

    - `PrimaryOwner`

    - `User`

  - `JsonElement Type constant`

    Object type.

    For Users, this is always `"user"`.

#### Example

```csharp
UserUpdateParams parameters = new()
{
    UserID = "user_id",
    Role = Role.User,
};

var betaOrganizationUser = await client.Beta.Organization.Users.Update(parameters);

Console.WriteLine(betaOrganizationUser);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "added_at": "2024-10-30T23:58:27.427722Z",
  "email": "user@emaildomain.com",
  "name": "Jane Doe",
  "role": "admin",
  "type": "user"
}
```

### Remove User

`UserRemoveResponse Beta.Organization.Users.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/users/{user_id}`

Remove a member from the organization.

#### Parameters

- `UserRemoveParams parameters`

  - `required string userID`

    ID of the User.

#### Returns

- `class UserRemoveResponse:`

  - `required string ID`

    ID of the User.

  - `JsonElement Type constant`

    Deleted object type.

    For Users, this is always `"user_deleted"`.

#### Example

```csharp
UserRemoveParams parameters = new() { UserID = "user_id" };

var user = await client.Beta.Organization.Users.Remove(parameters);

Console.WriteLine(user);
```

##### Response (200)

```json
{
  "id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "type": "user_deleted"
}
```

## Beta › Organization › Workspaces

### List Workspaces

`WorkspaceListPage Beta.Organization.Workspaces.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces`

List Workspaces

#### Parameters

- `WorkspaceListParams parameters`

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `bool includeArchived`

    Whether to include Workspaces that have been archived in the response

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type constant`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceListParams parameters = new();

var page = await client.Beta.Organization.Workspaces.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "data_residency": {
        "allowed_inference_geos": "unrestricted",
        "default_inference_geo": "default_inference_geo",
        "workspace_geo": "workspace_geo"
      },
      "display_color": "#6C5BB9",
      "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
      "name": "Workspace Name",
      "tags": {
        "env": "prod",
        "team": "platform"
      },
      "type": "workspace"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace

`BetaWorkspace Beta.Organization.Workspaces.Create(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces`

Create Workspace

#### Parameters

- `WorkspaceCreateParams parameters`

  - `required string name`

    Body param: Name of the Workspace.

    maxLength: 40, minLength: 1

  - `BetaDataResidencyCreateConfig? dataResidency`

    Body param: Data residency configuration for the workspace. If omitted, defaults to `workspace_geo: "us"`, `allowed_inference_geos: "unrestricted"`, and `default_inference_geo: "global"`.

  - `string? displayColor`

    Body param: Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string? externalKeyID`

    Body param: ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `IReadOnlyDictionary<string, string>? tags`

    Body param: User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type constant`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceCreateParams parameters = new() { Name = "x" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Create(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Get Workspace

`BetaWorkspace Beta.Organization.Workspaces.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}`

Get Workspace

#### Parameters

- `WorkspaceRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type constant`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceRetrieveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Retrieve(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Update Workspace

`BetaWorkspace Beta.Organization.Workspaces.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}`

Update Workspace

#### Parameters

- `WorkspaceUpdateParams parameters`

  - `required string workspaceID`

  - `BetaDataResidencyUpdateConfig? dataResidency`

    Data residency configuration for the workspace.

  - `string displayColor`

    Hex color code representing the Workspace in the Anthropic Console.

    maxLength: 7, pattern: ^#[0-9A-Fa-f]{6}$

  - `string externalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `string name`

    Name of the Workspace.

    maxLength: 40, minLength: 1

  - `IReadOnlyDictionary<string, string>? tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type constant`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceUpdateParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Update(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

### Archive Workspace

`BetaWorkspace Beta.Organization.Workspaces.Archive(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/archive`

Archive Workspace

#### Parameters

- `WorkspaceArchiveParams parameters`

  - `required string workspaceID`

#### Returns

- `class BetaWorkspace:`

  - `required string ID`

    ID of the Workspace.

  - `required DateTimeOffset? ArchivedAt`

    RFC 3339 datetime string indicating when the Workspace was archived, or `null` if the Workspace is not archived.

    format: date-time

  - `required string CompartmentID`

    Identifier for this Workspace's encryption compartment. When you configure a
    customer-managed encryption key (CMEK) on AWS, reference this value in your
    KMS key-policy condition so the key is scoped to this compartment. On GCP and
    Azure, Anthropic enforces the compartment binding automatically; you do not
    need to reference this value in your key configuration. See the CMEK integration guide for the
    required key configuration, including the value used during key validation.

  - `required DateTimeOffset CreatedAt`

    RFC 3339 datetime string indicating when the Workspace was created.

    format: date-time

  - `required BetaDataResidency DataResidency`

    Data residency configuration.

    - `required AllowedInferenceGeos AllowedInferenceGeos`

      Permitted inference geo values. 'unrestricted' means all geos are allowed.

      - `IReadOnlyList<string>`

      - `class Unrestricted:`

    - `required string DefaultInferenceGeo`

      Default inference geo applied when requests omit the parameter.

    - `required string WorkspaceGeo`

      Geographic region for workspace data storage. Immutable after creation.

  - `required string DisplayColor`

    Hex color code representing the Workspace in the Anthropic Console.

  - `required string? ExternalKeyID`

    ID of the customer-managed encryption key (CMEK) configuration to use for this
    Workspace. Setting this field requires CMEK to be enabled for your
    organization. When set, data stored for this Workspace is encrypted with the
    referenced key. Create key configurations with the External Keys API. This
    field is write-once: once a key is attached to a Workspace it cannot be
    detached or replaced. To rotate key material, rotate the underlying key on
    your cloud KMS; the `external_key_id` stays the same.

  - `required string Name`

    Name of the Workspace.

  - `required IReadOnlyDictionary<string, string> Tags`

    User-defined tags as string key-value pairs. Keys may not begin with `anthropic`.

  - `JsonElement Type constant`

    Object type.

    For Workspaces, this is always `"workspace"`.

#### Example

```csharp
WorkspaceArchiveParams parameters = new() { WorkspaceID = "workspace_id" };

var betaWorkspace = await client.Beta.Organization.Workspaces.Archive(parameters);

Console.WriteLine(betaWorkspace);
```

##### Response (200)

```json
{
  "id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "archived_at": "2024-11-01T23:59:27.427722Z",
  "compartment_id": "f8a7b6c5-4d3e-4f1a-8b9c-0d1e2f3a4b5c",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "data_residency": {
    "allowed_inference_geos": "unrestricted",
    "default_inference_geo": "default_inference_geo",
    "workspace_geo": "workspace_geo"
  },
  "display_color": "#6C5BB9",
  "external_key_id": "ekey_01SDCCSbTxrXDpWc1phhtcfK",
  "name": "Workspace Name",
  "tags": {
    "env": "prod",
    "team": "platform"
  },
  "type": "workspace"
}
```

## Beta › Organization › Workspaces › Rate Limits

### List Workspace Rate Limits

`RateLimitListPage Beta.Organization.Workspaces.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/rate_limits`

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `required string workspaceID`

    The ID of the workspace.

  - `GroupType? groupType`

    Filter by group type.

    - `Batch`

    - `Files`

    - `ModelGroup`

    - `Skills`

    - `TokenCount`

    - `WebSearch`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaWorkspaceRateLimit:`

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch`

    - `Files`

    - `ModelGroup`

    - `Skills`

    - `TokenCount`

    - `WebSearch`

  - `required IReadOnlyList<BetaWorkspaceRateLimitValue> Limits`

    The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

    - `required long? OrgLimit`

      The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long Value`

      The workspace-level override value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `required string RateLimitID`

    The `id` of the RateLimit group this override applies to.

  - `JsonElement Type constant`

    Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

  - `required string WorkspaceID`

    ID of the Workspace this override applies to.

#### Example

```csharp
RateLimitListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

## Beta › Organization › Workspaces › Members

### List Workspace Members

`MemberListPage Beta.Organization.Workspaces.Members.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members`

List Workspace Members

#### Parameters

- `MemberListParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `string afterID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `string beforeID`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `long limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type constant`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
MemberListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.Members.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "type": "workspace_member",
      "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
      "workspace_role": "workspace_admin"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
}
```

### Create Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members`

Create Workspace Member

#### Parameters

- `MemberAddParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Role of the new Workspace Member. Cannot be `workspace_billing`.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type constant`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
MemberAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_01WCz1FkmYMm4gnmykNKUu3Q",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Add(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Get Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Get Workspace Member

#### Parameters

- `MemberRetrieveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type constant`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
MemberRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Retrieve(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Update Workspace Member

`BetaWorkspaceMember Beta.Organization.Workspaces.Members.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Update Workspace Member

#### Parameters

- `MemberUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the Workspace.

  - `required string userID`

    Path param: ID of the User.

  - `required BetaWorkspaceRole workspaceRole`

    Body param: New workspace role for the User.

#### Returns

- `class BetaWorkspaceMember:`

  - `JsonElement Type constant`

    Object type.

    For Workspace Members, this is always `"workspace_member"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the Workspace Member.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
MemberUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
    WorkspaceRole = BetaWorkspaceRole.WorkspaceAdmin,
};

var betaWorkspaceMember = await client.Beta.Organization.Workspaces.Members.Update(parameters);

Console.WriteLine(betaWorkspaceMember);
```

##### Response (200)

```json
{
  "type": "workspace_member",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ",
  "workspace_role": "workspace_admin"
}
```

### Delete Workspace Member

`MemberRemoveResponse Beta.Organization.Workspaces.Members.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/members/{user_id}`

Delete Workspace Member

#### Parameters

- `MemberRemoveParams parameters`

  - `required string workspaceID`

    ID of the Workspace.

  - `required string userID`

    ID of the User.

#### Returns

- `class MemberRemoveResponse:`

  - `JsonElement Type constant`

    Deleted object type.

    For Workspace Members, this is always `"workspace_member_deleted"`.

  - `required string UserID`

    ID of the User.

  - `required string WorkspaceID`

    ID of the Workspace.

#### Example

```csharp
MemberRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    UserID = "user_id",
};

var member = await client.Beta.Organization.Workspaces.Members.Remove(parameters);

Console.WriteLine(member);
```

##### Response (200)

```json
{
  "type": "workspace_member_deleted",
  "user_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
  "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
}
```

## Beta › Organization › Workspaces › Service Accounts

### List Service Account Workspace Members

`ServiceAccountListPage Beta.Organization.Workspaces.ServiceAccounts.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

List the service accounts that are members of a workspace.

Each entry includes the service account's `workspace_role`. Use `limit`
and the `next_page` cursor to paginate. Archived workspaces return 400;
use `GET /service_accounts/{id}/workspaces` to audit memberships of an
archived workspace. The implicit default-workspace membership is not
included in this list. Memberships of archived service accounts are
omitted from the results.

#### Parameters

- `ServiceAccountListParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `long limit`

    Query param: Number of results per page.

    maximum: 100, minimum: 1

  - `string? page`

    Query param: Opaque cursor from a previous response's `next_page`.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
ServiceAccountListParams parameters = new() { WorkspaceID = "workspace_id" };

var page = await client.Beta.Organization.Workspaces.ServiceAccounts.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "created_by_actor_id": "created_by_actor_id",
      "implicit": true,
      "service_account_id": "service_account_id",
      "type": "service_account_workspace_member",
      "workspace_id": "workspace_id",
      "workspace_role": "workspace_admin"
    }
  ],
  "next_page": "next_page"
}
```

### Create Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Add(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Add a service account to a workspace with the given `workspace_role`.

The role determines what the service account can do in the workspace and
which workspace-scoped permissions it can be granted when authenticating
through federation. Every service account is already an implicit
`workspace_user` member of the default workspace; adding it explicitly
assigns a chosen role. If the service account is already an explicit
member of the workspace, its `workspace_role` is replaced with the
value supplied here. Archived workspaces return 400. Archived service
accounts cannot be added and are rejected.

#### Parameters

- `ServiceAccountAddParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Body param: Tagged service account ID to add.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: Role to assign to the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
ServiceAccountAddParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Add(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Get Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters, cancellationToken = default)`

**GET** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Retrieve a service account's membership in a workspace.

Returns the membership record, including the service account's
`workspace_role` in this workspace. Archived workspaces return 400. For
the default workspace, returns the implicit (`implicit: true`)
membership when no explicit membership exists; an explicitly added
membership is returned with its assigned role. An archived service
account returns 404.

#### Parameters

- `ServiceAccountRetrieveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
ServiceAccountRetrieveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Retrieve(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Update Service Account Workspace Member

`BetaServiceAccountWorkspaceMember Beta.Organization.Workspaces.ServiceAccounts.Update(parameters, cancellationToken = default)`

**POST** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Change a service account's role in a workspace.

The new `workspace_role` replaces the current one. Only explicit
memberships can be updated; to set a role on the implicit
default-workspace membership, add the service account explicitly with
`POST /workspaces/{workspace_id}/service_accounts`. Archived workspaces
return 400. Archived service accounts cannot be updated and are
rejected.

#### Parameters

- `ServiceAccountUpdateParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `required BetaNoBillingWorkspaceRole workspaceRole`

    Body param: New role for the service account in this workspace.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class BetaServiceAccountWorkspaceMember:`

  - `required string? CreatedByActorID`

    Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

  - `required bool? Implicit`

    True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role `workspace_user` and cannot be removed.

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`).

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`).

  - `required BetaWorkspaceRole WorkspaceRole`

    Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

    - `WorkspaceAdmin`

    - `WorkspaceBilling`

    - `WorkspaceDeveloper`

    - `WorkspaceRestrictedDeveloper`

    - `WorkspaceUser`

#### Example

```csharp
ServiceAccountUpdateParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
    WorkspaceRole = BetaNoBillingWorkspaceRole.WorkspaceAdmin,
};

var betaServiceAccountWorkspaceMember = await client.Beta.Organization.Workspaces.ServiceAccounts.Update(parameters);

Console.WriteLine(betaServiceAccountWorkspaceMember);
```

##### Response (200)

```json
{
  "created_by_actor_id": "created_by_actor_id",
  "implicit": true,
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member",
  "workspace_id": "workspace_id",
  "workspace_role": "workspace_admin"
}
```

### Delete Service Account Workspace Member

`ServiceAccountRemoveResponse Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters, cancellationToken = default)`

**DELETE** `/v1/organizations/workspaces/{workspace_id}/service_accounts/{service_account_id}`

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](/docs/en/manage-claude/wif-admin-api).

Remove a service account from a workspace.

Removal is idempotent (returns 200 even if the membership was already
removed). A DELETE against the implicit default-workspace membership
returns 200 but is a no-op and the membership persists; deleting an
explicit default-workspace row reverts to the implicit `workspace_user`
membership. Archived workspaces return 400.

#### Parameters

- `ServiceAccountRemoveParams parameters`

  - `required string workspaceID`

    Path param: ID of the workspace.

  - `required string serviceAccountID`

    Path param: ID of the service account.

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

    - `Compact2026_01_12`

    - `ComputerUse2025_11_24`

    - `McpTunnels2026_06_22`

    - `StructuredOutputs2025_11_13`

    - `TaskBudgets2026_03_13`

    - `ThinkingDisplayUpdates2026_08_18`

    - `CEUserManagement2026_07_13`

#### Returns

- `class ServiceAccountRemoveResponse:`

  - `required string ServiceAccountID`

    Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

  - `JsonElement Type constant`

  - `required string WorkspaceID`

    Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### Example

```csharp
ServiceAccountRemoveParams parameters = new()
{
    WorkspaceID = "workspace_id",
    ServiceAccountID = "service_account_id",
};

var serviceAccount = await client.Beta.Organization.Workspaces.ServiceAccounts.Remove(parameters);

Console.WriteLine(serviceAccount);
```

##### Response (200)

```json
{
  "service_account_id": "service_account_id",
  "type": "service_account_workspace_member_deleted",
  "workspace_id": "workspace_id"
}
```

## Beta › Organization › Rate Limits

### List Organization Rate Limits

`RateLimitListPage Beta.Organization.RateLimits.List(parameters, cancellationToken = default)`

**GET** `/v1/organizations/rate_limits`

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

#### Parameters

- `RateLimitListParams parameters`

  - `GroupType? groupType`

    Filter by group type.

    - `Batch`

    - `Files`

    - `ModelGroup`

    - `Skills`

    - `TokenCount`

    - `WebSearch`

  - `long? limit`

    Maximum number of items to return per page. Ranges from `1` to `1000`.

    When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

    maximum: 1000, minimum: 1

  - `string? model`

    Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

  - `string? page`

    Opaque cursor from a previous response's `next_page`.

#### Returns

- `class BetaOrganizationRateLimit:`

  - `required string ID`

    Stable identifier for this rate-limit group within the organization.

  - `required GroupType GroupType`

    The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

    - `Batch`

    - `Files`

    - `ModelGroup`

    - `Skills`

    - `TokenCount`

    - `WebSearch`

  - `required IReadOnlyList<BetaOrganizationRateLimitValue> Limits`

    The limiter values that apply to this group.

    - `required string Type`

      The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

    - `required long Value`

      The configured limit value for this limiter type.

  - `required IReadOnlyList<string>? Models`

    Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

  - `JsonElement Type constant`

    Object type. Always `rate_limit` for organization rate-limit entries.

#### Example

```csharp
RateLimitListParams parameters = new();

var page = await client.Beta.Organization.RateLimits.List(parameters);
await foreach (var item in page.Paginate())
{
    Console.WriteLine(item);
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```
