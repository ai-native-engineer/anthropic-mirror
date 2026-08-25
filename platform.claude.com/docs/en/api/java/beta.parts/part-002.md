<!-- source: https://platform.claude.com/docs/en/api/java/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/java/beta -->

<!-- chunk-start -->

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `String id`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `String id`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `BetaManagedAgentsTextBlock content`

        Regular text content.

      - `Type type`

      - `Optional<Long> index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `String eventId`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionEvents: union`

  Server-sent event in the session stream.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsStreamSessionEvents;
import com.anthropic.models.beta.sessions.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        StreamResponse<BetaManagedAgentsStreamSessionEvents> betaManagedAgentsStreamSessionEvents = client.beta().sessions().events().streamStreaming("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
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

`BetaManagedAgentsFileResource beta().sessions().resources().add(params, requestOptions = RequestOptions.none())`

**POST** `/v1/sessions/{session_id}/resources`

Add Session Resource

#### Parameters

- `ResourceAddParams params`

  - `Optional<String> sessionId`

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

  - `BetaManagedAgentsFileResourceParams betaManagedAgentsFileResourceParams`

    Mount a file uploaded via the Files API into the session.

#### Returns

- `class BetaManagedAgentsFileResource:`

  - `String id`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String fileId`

  - `String mountPath`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.BetaManagedAgentsFileResourceParams;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsFileResource;
import com.anthropic.models.beta.sessions.resources.ResourceAddParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceAddParams params = ResourceAddParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .betaManagedAgentsFileResourceParams(BetaManagedAgentsFileResourceParams.builder()
                .fileId("file_011CNha8iCJcU1wXNR6q4V8w")
                .type(BetaManagedAgentsFileResourceParams.Type.FILE)
                .build())
            .build();
        BetaManagedAgentsFileResource betaManagedAgentsFileResource = client.beta().sessions().resources().add(params);
    }
}
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

`ResourceListPage beta().sessions().resources().list(params = ResourceListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/resources`

List Session Resources

#### Parameters

- `ResourceListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Maximum number of resources to return per page (max 1000). If omitted, returns all resources.

    format: int32

  - `Optional<String> page`

    Opaque cursor from a previous response's next_page field.

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

#### Returns

- `class BetaManagedAgentsSessionResource: union`

  A memory store attached to an agent session.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type type`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String fileId`

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `String memoryStoreId`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `Optional<Access> access`

      Access mode for an attached memory store.

      - `READ_WRITE("read_write")`

      - `READ_ONLY("read_only")`

    - `Optional<String> description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Optional<String> instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `Optional<String> mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Optional<String> name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceListPage;
import com.anthropic.models.beta.sessions.resources.ResourceListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceListPage page = client.beta().sessions().resources().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
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

`ResourceRetrieveResponse beta().sessions().resources().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/resources/{resource_id}`

Get Session Resource

#### Parameters

- `ResourceRetrieveParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

#### Returns

- `class ResourceRetrieveResponse: union`

  The requested session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type type`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String fileId`

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `String memoryStoreId`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `Optional<Access> access`

      Access mode for an attached memory store.

      - `READ_WRITE("read_write")`

      - `READ_ONLY("read_only")`

    - `Optional<String> description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Optional<String> instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `Optional<String> mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Optional<String> name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveParams;
import com.anthropic.models.beta.sessions.resources.ResourceRetrieveResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceRetrieveParams params = ResourceRetrieveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        ResourceRetrieveResponse resource = client.beta().sessions().resources().retrieve(params);
    }
}
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

`ResourceUpdateResponse beta().sessions().resources().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/sessions/{session_id}/resources/{resource_id}`

Update Session Resource

#### Parameters

- `ResourceUpdateParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

  - `String authorizationToken`

    New authorization token for the resource. Currently only `github_repository` resources support token rotation.

    minLength: 1, maxLength: 4096

#### Returns

- `class ResourceUpdateResponse: union`

  The updated session resource.

  - `class BetaManagedAgentsGitHubRepositoryResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String url`

    - `Optional<Checkout> checkout`

      - `class BetaManagedAgentsBranchCheckout:`

        - `String name`

          Branch name to check out.

          minLength: 1, maxLength: 255

        - `Type type`

      - `class BetaManagedAgentsCommitCheckout:`

        - `String sha`

          Full commit SHA to check out.

          minLength: 7, maxLength: 64

        - `Type type`

  - `class BetaManagedAgentsFileResource:`

    - `String id`

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String fileId`

    - `String mountPath`

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsMemoryStoreResource:`

    A memory store attached to an agent session.

    - `String memoryStoreId`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type type`

    - `Optional<Access> access`

      Access mode for an attached memory store.

      - `READ_WRITE("read_write")`

      - `READ_ONLY("read_only")`

    - `Optional<String> description`

      Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

    - `Optional<String> instructions`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

      maxLength: 4096

    - `Optional<String> mountPath`

      Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

    - `Optional<String> name`

      Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateParams;
import com.anthropic.models.beta.sessions.resources.ResourceUpdateResponse;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceUpdateParams params = ResourceUpdateParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .authorizationToken("ghp_exampletoken")
            .build();
        ResourceUpdateResponse resource = client.beta().sessions().resources().update(params);
    }
}
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

`BetaManagedAgentsDeleteSessionResource beta().sessions().resources().delete(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/sessions/{session_id}/resources/{resource_id}`

Delete Session Resource

#### Parameters

- `ResourceDeleteParams params`

  - `String sessionId`

  - `Optional<String> resourceId`

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

#### Returns

- `class BetaManagedAgentsDeleteSessionResource:`

  Confirmation of resource deletion.

  - `String id`

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.resources.BetaManagedAgentsDeleteSessionResource;
import com.anthropic.models.beta.sessions.resources.ResourceDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ResourceDeleteParams params = ResourceDeleteParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .resourceId("sesrsc_011CZkZBJq5dWxk9fVLNcPht")
            .build();
        BetaManagedAgentsDeleteSessionResource betaManagedAgentsDeleteSessionResource = client.beta().sessions().resources().delete(params);
    }
}
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

`ThreadListPage beta().sessions().threads().list(params = ThreadListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/threads`

List Session Threads

#### Parameters

- `ThreadListParams params`

  - `Optional<String> sessionId`

  - `Optional<Long> limit`

    Maximum results per page. Defaults to 1000.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor from a previous response's next_page. Forward-only.

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `Agent agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `String skillId`

          - `Type type`

          - `String version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `String skillId`

          - `Type type`

          - `String version`

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `List<BetaManagedAgentsAgentToolConfig> configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `Type type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `Type type`

              - `JsonValue type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<Long> maxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<BetaManagedAgentsUserLocation> userLocation`

                Approximate user location for search result localization.

                - `JsonValue type constant`

                  Location precision. Only "approximate" is supported.

                - `Optional<String> city`

                  City name.

                  minLength: 1, maxLength: 255

                - `Optional<String> country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Optional<String> region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Optional<String> timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

            Resolved default configuration for agent tools.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `Type type`

        - `class BetaManagedAgentsMcpToolset:`

          - `List<BetaManagedAgentsMcpToolConfig> configs`

            - `boolean enabled`

            - `String name`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `String mcpServerName`

          - `Type type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `String description`

          - `BetaManagedAgentsCustomToolInputSchema inputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonValue type constant`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

          - `Type type`

      - `Type type`

      - `long version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `String model`

        The advisor model id.

      - `Type type`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `Optional<BetaMonetaryAmount> listCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Optional<Long> webFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `Optional<Long> webSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.ThreadListPage;
import com.anthropic.models.beta.sessions.threads.ThreadListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadListPage page = client.beta().sessions().threads().list("sesn_011CZkZAtmR3yMPDzynEDxu7");
    }
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

`BetaManagedAgentsSessionThread beta().sessions().threads().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}`

Get Session Thread

#### Parameters

- `ThreadRetrieveParams params`

  - `String sessionId`

  - `Optional<String> threadId`

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `Agent agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `String skillId`

          - `Type type`

          - `String version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `String skillId`

          - `Type type`

          - `String version`

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `List<BetaManagedAgentsAgentToolConfig> configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `Type type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `Type type`

              - `JsonValue type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<Long> maxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<BetaManagedAgentsUserLocation> userLocation`

                Approximate user location for search result localization.

                - `JsonValue type constant`

                  Location precision. Only "approximate" is supported.

                - `Optional<String> city`

                  City name.

                  minLength: 1, maxLength: 255

                - `Optional<String> country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Optional<String> region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Optional<String> timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

            Resolved default configuration for agent tools.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `Type type`

        - `class BetaManagedAgentsMcpToolset:`

          - `List<BetaManagedAgentsMcpToolConfig> configs`

            - `boolean enabled`

            - `String name`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `String mcpServerName`

          - `Type type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `String description`

          - `BetaManagedAgentsCustomToolInputSchema inputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonValue type constant`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

          - `Type type`

      - `Type type`

      - `long version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `String model`

        The advisor model id.

      - `Type type`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `Optional<BetaMonetaryAmount> listCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Optional<Long> webFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `Optional<Long> webSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsSessionThread;
import com.anthropic.models.beta.sessions.threads.ThreadRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadRetrieveParams params = ThreadRetrieveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        BetaManagedAgentsSessionThread betaManagedAgentsSessionThread = client.beta().sessions().threads().retrieve(params);
    }
}
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

`BetaManagedAgentsSessionThread beta().sessions().threads().archive(params, requestOptions = RequestOptions.none())`

**POST** `/v1/sessions/{session_id}/threads/{thread_id}/archive`

Archive Session Thread

#### Parameters

- `ThreadArchiveParams params`

  - `String sessionId`

  - `Optional<String> threadId`

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

#### Returns

- `class BetaManagedAgentsSessionThread:`

  An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

  - `String id`

    Unique identifier for this thread.

  - `Agent agent`

    A session-resolved multiagent roster entry.

    - `class BetaManagedAgentsSessionThreadAgent:`

      Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

          - `String skillId`

          - `Type type`

          - `String version`

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

          - `String skillId`

          - `Type type`

          - `String version`

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

          - `List<BetaManagedAgentsAgentToolConfig> configs`

            - `class BetaManagedAgentsBashToolConfig:`

              Configuration for the bash tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                  - `Type type`

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

                  - `Type type`

              - `JsonValue type constant`

            - `class BetaManagedAgentsEditToolConfig:`

              Configuration for the edit tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsReadToolConfig:`

              Configuration for the read tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWriteToolConfig:`

              Configuration for the write tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGlobToolConfig:`

              Configuration for the glob tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsGrepToolConfig:`

              Configuration for the grep tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

            - `class BetaManagedAgentsWebFetchToolConfig:`

              Configuration for the web_fetch tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<Long> maxContentTokens`

                format: int32

            - `class BetaManagedAgentsWebSearchToolConfig:`

              Configuration for the web_search tool.

              - `boolean enabled`

              - `JsonValue name constant`

              - `PermissionPolicy permissionPolicy`

                Permission policy for tool execution.

                - `class BetaManagedAgentsAlwaysAllowPolicy:`

                  Tool calls are automatically approved without user confirmation.

                - `class BetaManagedAgentsAlwaysAskPolicy:`

                  Tool calls require user confirmation before execution.

              - `JsonValue type constant`

              - `Optional<List<String>> allowedDomains`

              - `Optional<List<String>> blockedDomains`

              - `Optional<BetaManagedAgentsUserLocation> userLocation`

                Approximate user location for search result localization.

                - `JsonValue type constant`

                  Location precision. Only "approximate" is supported.

                - `Optional<String> city`

                  City name.

                  minLength: 1, maxLength: 255

                - `Optional<String> country`

                  Two-letter ISO 3166-1 country code, uppercase.

                - `Optional<String> region`

                  Region or state name.

                  minLength: 1, maxLength: 255

                - `Optional<String> timezone`

                  IANA timezone identifier, e.g. "America/Los_Angeles".

                  minLength: 1, maxLength: 255

          - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

            Resolved default configuration for agent tools.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `Type type`

        - `class BetaManagedAgentsMcpToolset:`

          - `List<BetaManagedAgentsMcpToolConfig> configs`

            - `boolean enabled`

            - `String name`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

            Resolved default configuration for all tools from an MCP server.

            - `boolean enabled`

            - `PermissionPolicy permissionPolicy`

              Permission policy for tool execution.

              - `class BetaManagedAgentsAlwaysAllowPolicy:`

                Tool calls are automatically approved without user confirmation.

              - `class BetaManagedAgentsAlwaysAskPolicy:`

                Tool calls require user confirmation before execution.

          - `String mcpServerName`

          - `Type type`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

          - `String description`

          - `BetaManagedAgentsCustomToolInputSchema inputSchema`

            JSON Schema for custom tool input parameters.

            - `JsonValue type constant`

            - `Optional<Properties> properties`

            - `Optional<List<String>> required`

          - `String name`

          - `Type type`

      - `Type type`

      - `long version`

        format: int32

    - `class BetaManagedAgentsAdvisor:`

      Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

      - `String model`

        The advisor model id.

      - `Type type`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> parentThreadId`

    Parent thread that spawned this thread. Null for the primary thread.

  - `String sessionId`

    The session this thread belongs to.

  - `Optional<BetaManagedAgentsSessionThreadStats> stats`

    Timing statistics for a session thread.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds the thread spent actively running. Excludes idle time.

      format: double

    - `Optional<Double> durationSeconds`

      Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

      format: double

    - `Optional<Double> startupSeconds`

      Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

      format: double

  - `BetaManagedAgentsSessionThreadStatus status`

    SessionThreadStatus enum

    - `RUNNING("running")`

    - `IDLE("idle")`

    - `RESCHEDULING("rescheduling")`

    - `TERMINATED("terminated")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsSessionThreadUsage> usage`

    Cumulative token usage for a session thread across all turns.

    - `Optional<Double> activeSeconds`

      Cumulative time in seconds this thread spent in running status. Equal to `stats.active_seconds`; surfaced here so a thread's usage carries every quantity its cost is priced on.

      format: double

    - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

      Prompt-cache creation token usage broken down by cache lifetime.

      - `Optional<Long> ephemeral1hInputTokens`

        Tokens used to create 1-hour ephemeral cache entries.

        format: int32

      - `Optional<Long> ephemeral5mInputTokens`

        Tokens used to create 5-minute ephemeral cache entries.

        format: int32

    - `Optional<Long> cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `Optional<Long> inputTokens`

      Total input tokens consumed across all turns.

      format: int32

    - `Optional<BetaMonetaryAmount> listCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Optional<Long> outputTokens`

      Total output tokens generated across all turns.

      format: int32

    - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

      Cumulative count of server-executed tool invocations, broken down by tool.

      - `Optional<Long> webFetchRequests`

        Number of server-executed web fetch requests.

        format: int32

      - `Optional<Long> webSearchRequests`

        Number of server-executed web search requests.

        format: int32

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsSessionThread;
import com.anthropic.models.beta.sessions.threads.ThreadArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        ThreadArchiveParams params = ThreadArchiveParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        BetaManagedAgentsSessionThread betaManagedAgentsSessionThread = client.beta().sessions().threads().archive(params);
    }
}
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

`EventListPage beta().sessions().threads().events().list(params, requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/events`

List Session Thread Events

#### Parameters

- `EventListParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<Long> limit`

    Query parameter for limit

    format: int32

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

#### Returns

- `class BetaManagedAgentsSessionEvent: union`

  Union type for all event types in a session.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.sessions.threads.events.EventListPage;
import com.anthropic.models.beta.sessions.threads.events.EventListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventListParams params = EventListParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        EventListPage page = client.beta().sessions().threads().events().list(params);
    }
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

`BetaManagedAgentsStreamSessionThreadEvents beta().sessions().threads().events().streamStreaming(params, requestOptions = RequestOptions.none())`

**GET** `/v1/sessions/{session_id}/threads/{thread_id}/stream`

Stream Session Thread Events

#### Parameters

- `EventStreamParams params`

  - `String sessionId`

  - `Optional<String> threadId`

  - `Optional<List<BetaManagedAgentsDeltaType>> eventDeltas`

    When set, this connection also receives streaming deltas (`event_start`, `event_delta`) while an event is being produced, before the event itself arrives. Deltas are best-effort; when the final event is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no final event — its terminal `span.model_request_end` closes the preview. Accepts one or more event types to preview and may be repeated: `agent.message` streams `content_delta` fragments; `agent.thinking` is start-only — a signal that the agent has begun extended thinking, concluded by the `agent.thinking` event itself. Only previews of the requested event types are sent.

    - `AGENT_MESSAGE("agent.message")`

    - `AGENT_THINKING("agent.thinking")`

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

#### Returns

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

  Server-sent event in a single thread's stream.

  - `class BetaManagedAgentsUserMessageEvent:`

    A user message event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of content blocks comprising the user message.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source source`

          Union type for image source variants.

          - `class BetaManagedAgentsBase64ImageSource:`

            Base64-encoded image data.

            - `String data`

              Base64-encoded image data.

              minLength: 1

            - `String mediaType`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsUrlImageSource:`

            Image referenced by URL.

            - `Type type`

            - `String url`

              URL of the image to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileImageSource:`

            Image referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source source`

          Union type for document source variants.

          - `class BetaManagedAgentsBase64DocumentSource:`

            Base64-encoded document data.

            - `String data`

              Base64-encoded document data.

              minLength: 1

            - `String mediaType`

              MIME type of the document (e.g., "application/pdf").

              minLength: 1

            - `Type type`

          - `class BetaManagedAgentsPlainTextDocumentSource:`

            Plain text document content.

            - `String data`

              The plain text content.

              minLength: 1

            - `MediaType mediaType`

              MIME type of the text content. Must be "text/plain".

            - `Type type`

          - `class BetaManagedAgentsUrlDocumentSource:`

            Document referenced by URL.

            - `Type type`

            - `String url`

              URL of the document to fetch.

              minLength: 1

          - `class BetaManagedAgentsFileDocumentSource:`

            Document referenced by file ID.

            - `String fileId`

              ID of a previously uploaded file.

              minLength: 1

            - `Type type`

        - `Type type`

        - `Optional<String> context`

          Additional context about the document for the model.

        - `Optional<String> title`

          The title of the document.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

        - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsUserInterruptEvent:`

    An interrupt event that pauses agent execution and returns control to the user.

    - `String id`

      Unique identifier for this event.

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

  - `class BetaManagedAgentsUserToolConfirmationEvent:`

    A tool confirmation event that approves or denies a pending tool execution.

    - `String id`

      Unique identifier for this event.

    - `Result result`

      UserToolConfirmationResult enum

      - `ALLOW("allow")`

      - `DENY("deny")`

    - `String toolUseId`

      The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<String> denyMessage`

      Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

      maxLength: 10000

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

  - `class BetaManagedAgentsUserCustomToolResultEvent:`

    Event sent by the client providing the result of a custom tool execution.

    - `String id`

      Unique identifier for this event.

    - `String customToolUseId`

      The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

        - `BetaManagedAgentsSearchResultCitations citations`

          Citation settings for a search result.

          - `boolean enabled`

            Whether citations are enabled for this search result.

        - `List<BetaManagedAgentsSearchResultContent> content`

          Array of text content blocks from the search result.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `String source`

          The URL source of the search result.

          minLength: 1

        - `String title`

          The title of the search result.

          minLength: 1

        - `Type type`

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsAgentCustomToolUseEvent:`

    Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the custom tool being called.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

  - `class BetaManagedAgentsAgentMessageEvent:`

    An agent response event in the session conversation.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Array of text blocks comprising the agent response.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentThinkingEvent:`

    Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsAgentMcpToolUseEvent:`

    Event emitted when the agent invokes a tool provided by an MCP server.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String mcpServerName`

      Name of the MCP server providing the tool.

    - `String name`

      Name of the MCP tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentMcpToolResultEvent:`

    Event representing the result of an MCP tool execution.

    - `String id`

      Unique identifier for this event.

    - `String mcpToolUseId`

      The id of the `agent.mcp_tool_use` event this result corresponds to.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentToolUseEvent:`

    Event emitted when the agent invokes a built-in agent tool.

    - `String id`

      Unique identifier for this event.

    - `Input input`

      Input parameters for the tool call.

    - `String name`

      Name of the agent tool being used.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<EvaluatedPermission> evaluatedPermission`

      AgentEvaluatedPermission enum

      - `ALLOW("allow")`

      - `ASK("ask")`

      - `DENY("deny")`

    - `Optional<String> sessionThreadId`

      When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

  - `class BetaManagedAgentsAgentToolResultEvent:`

    Event representing the result of an agent tool execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

  - `class BetaManagedAgentsAgentThreadMessageReceivedEvent:`

    Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `String fromSessionThreadId`

      Public `sthr_` ID of the thread that sent the message.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<String> fromAgentName`

      Name of the callable agent this message came from. Absent when received from the primary agent.

  - `class BetaManagedAgentsAgentThreadMessageSentEvent:`

    Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

    - `String id`

      Unique identifier for this event.

    - `List<Content> content`

      Message content blocks.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsRedactedBlock:`

        Placeholder for content withheld by Anthropic model policy.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String toSessionThreadId`

      Public `sthr_` ID of the thread the message was sent to.

    - `Type type`

    - `Optional<String> toAgentName`

      Name of the callable agent this message was sent to. Absent when sent to the primary agent.

  - `class BetaManagedAgentsAgentThreadContextCompactedEvent:`

    Indicates that context compaction (summarization) occurred during the session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionErrorEvent:`

    An error event indicating a problem occurred during session execution.

    - `String id`

      Unique identifier for this event.

    - `Error error`

      An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

      - `class BetaManagedAgentsUnknownError:`

        An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

            - `Type type`

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

            - `Type type`

        - `Type type`

      - `class BetaManagedAgentsModelOverloadedError:`

        The model is currently overloaded. Emitted after automatic retries are exhausted.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRateLimitedError:`

        The model request was rate-limited.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsModelRequestFailedError:`

        A model request failed for a reason other than overload or rate-limiting.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpConnectionFailedError:`

        Failed to connect to an MCP server.

        - `String mcpServerName`

          Name of the MCP server that failed to connect.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsMcpAuthenticationFailedError:`

        Authentication to an MCP server failed.

        - `String mcpServerName`

          Name of the MCP server that failed authentication.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsBillingError:`

        The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

      - `class BetaManagedAgentsCredentialHostUnreachableError:`

        An `environment_variable` credential's `auth.networking.allowed_hosts` includes a host the environment's network policy does not permit.

        - `String credentialId`

          ID of the affected credential.

        - `String message`

          Human-readable error description.

        - `RetryStatus retryStatus`

          What the client should do next in response to this error.

          - `class BetaManagedAgentsRetryStatusRetrying:`

            The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

          - `class BetaManagedAgentsRetryStatusExhausted:`

            This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

          - `class BetaManagedAgentsRetryStatusTerminal:`

            The session encountered a terminal error and will transition to `terminated` state.

        - `Type type`

        - `String vaultId`

          ID of the vault containing the affected credential.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRescheduledEvent:`

    Indicates the session is recovering from an error state and is rescheduled for execution.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusRunningEvent:`

    Indicates the session is actively running and the agent is working.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionStatusIdleEvent:`

    Indicates the agent has paused and is awaiting user input.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

        - `Type type`

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

        - `List<String> eventIds`

          The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

        - `Type type`

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

        - `Type type`

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionStatusTerminatedEvent:`

    Indicates the session has terminated, either due to an error or completion.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadCreatedEvent:`

    Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the callable agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public `sthr_` ID of the newly created thread.

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationStartEvent:`

    Emitted when an outcome evaluation cycle begins.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationEndEvent:`

    Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

    - `String id`

      Unique identifier for this event.

    - `String explanation`

      Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeEvaluationStartId`

      The id of the corresponding `span.outcome_evaluation_start` event.

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String result`

      Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs_revision': criteria not met, another revision cycle follows. 'max_iterations_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

    - `Type type`

    - `BetaManagedAgentsSpanModelUsage usage`

      Token usage for a single model request.

      - `long cacheCreationInputTokens`

        Tokens used to create prompt cache in this request.

        format: int32

      - `long cacheReadInputTokens`

        Tokens read from prompt cache in this request.

        format: int32

      - `long inputTokens`

        Input tokens consumed by this request.

        format: int32

      - `long outputTokens`

        Output tokens generated by this request.

        format: int32

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `class BetaManagedAgentsSpanModelRequestStartEvent:`

    Emitted when a model request is initiated by the agent.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanModelRequestEndEvent:`

    Emitted when a model request completes.

    - `String id`

      Unique identifier for this event.

    - `Optional<Boolean> isError`

      Whether the model request resulted in an error.

    - `String modelRequestStartId`

      The id of the corresponding `span.model_request_start` event.

    - `BetaManagedAgentsSpanModelUsage modelUsage`

      Token usage for a single model request.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent:`

    Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

    - `String id`

      Unique identifier for this event.

    - `long iteration`

      0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

      format: int32

    - `String outcomeId`

      The `outc_` ID of the outcome being evaluated.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsUserDefineOutcomeEvent:`

    Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

    - `String id`

      Unique identifier for this event.

    - `String description`

      What the agent should produce. Copied from the input event.

    - `Optional<Long> maxIterations`

      Evaluate-then-revise cycles before giving up. Default 3, max 20.

      format: int32

    - `String outcomeId`

      Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Rubric rubric`

      Rubric for grading the quality of an outcome.

      - `class BetaManagedAgentsFileRubric:`

        Rubric referenced by a file uploaded via the Files API.

        - `String fileId`

          ID of the rubric file.

        - `Type type`

      - `class BetaManagedAgentsTextRubric:`

        Rubric content provided inline as text.

        - `String content`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsSessionDeletedEvent:`

    Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusRunningEvent:`

    A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that started running.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusIdleEvent:`

    A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that went idle.

    - `StopReason stopReason`

      The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionEndTurn:`

        The agent completed its turn naturally and is ready for the next user message.

      - `class BetaManagedAgentsSessionRequiresAction:`

        The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

      - `class BetaManagedAgentsSessionRetriesExhausted:`

        The turn ended because repeated errors exhausted the retry budget or an error escalated to `retry_status: 'exhausted'`.

      - `class BetaManagedAgentsSessionBudgetReached:`

        The agent stopped because the session's tracked list cost reached its budget, or because its usage includes a model with no list price (which the budget cannot measure). Raise the budget to continue — or, if raising is rejected because a model has no list price, remove the budget.

    - `Type type`

  - `class BetaManagedAgentsSessionThreadStatusTerminatedEvent:`

    A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that terminated.

    - `Type type`

  - `class BetaManagedAgentsUserToolResultEvent:`

    Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

    - `String id`

      Unique identifier for this event.

    - `String toolUseId`

      The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](https://platform.claude.com/docs/en/api/beta/sessions/events/list#beta_managed_agents_session_requires_action.event_ids) `stop_reason.event_ids` field.

    - `Type type`

    - `Optional<List<Content>> content`

      The result content returned by the tool.

      - `class BetaManagedAgentsTextBlock:`

        Regular text content.

      - `class BetaManagedAgentsImageBlock:`

        Image content specified directly as base64 data or as a reference via a URL.

      - `class BetaManagedAgentsDocumentBlock:`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `class BetaManagedAgentsSearchResultBlock:`

        A block containing a web search result.

    - `Optional<Boolean> isError`

      Whether the tool execution resulted in an error.

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> sessionThreadId`

      Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.

  - `class BetaManagedAgentsSessionThreadStatusRescheduledEvent:`

    A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

    - `String id`

      Unique identifier for this event.

    - `String agentName`

      Name of the agent the thread runs.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String sessionThreadId`

      Public sthr_ ID of the thread that is retrying.

    - `Type type`

  - `class BetaManagedAgentsSessionUpdatedEvent:`

    Emitted when an UpdateSession request changed at least one field. Carries only the fields that changed; absent fields were not part of the update. The new configuration applies from the next turn.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `Optional<BetaManagedAgentsSessionAgent> agent`

      Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

      - `String id`

      - `Optional<String> description`

      - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

        - `String name`

        - `Type type`

        - `String url`

      - `BetaManagedAgentsModelConfig model`

        Model identifier and configuration.

        - `BetaManagedAgentsModel id`

          The model that will power your agent.

          See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

          - `CLAUDE_SONNET_5("claude-sonnet-5")`

            High-performance model for coding and agents

          - `CLAUDE_FABLE_5("claude-fable-5")`

            Next generation of intelligence for the hardest knowledge work and coding problems

          - `CLAUDE_OPUS_5("claude-opus-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_8("claude-opus-4-8")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_7("claude-opus-4-7")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_6("claude-opus-4-6")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_6("claude-sonnet-4-6")`

            Best combination of speed and intelligence

          - `CLAUDE_HAIKU_4_5("claude-haiku-4-5")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_HAIKU_4_5_20251001("claude-haiku-4-5-20251001")`

            Fastest model with near-frontier intelligence

          - `CLAUDE_OPUS_4_5("claude-opus-4-5")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_OPUS_4_5_20251101("claude-opus-4-5-20251101")`

            Powerful intelligence for long-running agents and coding

          - `CLAUDE_SONNET_4_5("claude-sonnet-4-5")`

            High-performance model for agents and coding

          - `CLAUDE_SONNET_4_5_20250929("claude-sonnet-4-5-20250929")`

            High-performance model for agents and coding

        - `Optional<Effort> effort`

          How hard Claude works on each turn. Sets `output_config.effort` on every Messages call the session makes.

          - `class BetaManagedAgentsEffortLow:`

            Low effort. Favors latency over reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortMedium:`

            Medium effort. Balances latency and reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortHigh:`

            High effort. Favors reasoning depth.

            - `Type type`

          - `class BetaManagedAgentsEffortXhigh:`

            Extra-high effort. Not all models accept this level.

            - `Type type`

          - `class BetaManagedAgentsEffortMax:`

            Maximum effort. Favors reasoning depth over latency.

            - `Type type`

        - `Optional<String> inferenceGeo`

          Geographic region for model inference. When unset, requests fall through to the workspace's default_inference_geo.

        - `Optional<Speed> speed`

          Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

          - `STANDARD("standard")`

          - `FAST("fast")`

      - `Optional<BetaManagedAgentsSessionMultiagentCoordinator> multiagent`

        Resolved coordinator topology with full agent definitions for each roster member.

        - `List<Agent> agents`

          Full `agent` definitions the coordinator may spawn as session threads.

          - `class BetaManagedAgentsSessionThreadAgent:`

            Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

            - `String id`

            - `Optional<String> description`

            - `List<BetaManagedAgentsMcpServerUrlDefinition> mcpServers`

              - `String name`

              - `Type type`

              - `String url`

            - `BetaManagedAgentsModelConfig model`

              Model identifier and configuration.

            - `String name`

            - `List<Skill> skills`

              - `class BetaManagedAgentsAnthropicSkill:`

                A resolved Anthropic-managed skill.

                - `String skillId`

                - `Type type`

                - `String version`

              - `class BetaManagedAgentsCustomSkill:`

                A resolved user-created custom skill.

                - `String skillId`

                - `Type type`

                - `String version`

            - `Optional<String> system`

            - `List<Tool> tools`

              - `class BetaManagedAgentsAgentToolset20260401:`

                - `List<BetaManagedAgentsAgentToolConfig> configs`

                  - `class BetaManagedAgentsBashToolConfig:`

                    Configuration for the bash tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                        - `Type type`

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                        - `Type type`

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsEditToolConfig:`

                    Configuration for the edit tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsReadToolConfig:`

                    Configuration for the read tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWriteToolConfig:`

                    Configuration for the write tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGlobToolConfig:`

                    Configuration for the glob tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsGrepToolConfig:`

                    Configuration for the grep tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                  - `class BetaManagedAgentsWebFetchToolConfig:`

                    Configuration for the web_fetch tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<Long> maxContentTokens`

                      format: int32

                  - `class BetaManagedAgentsWebSearchToolConfig:`

                    Configuration for the web_search tool.

                    - `boolean enabled`

                    - `JsonValue name constant`

                    - `PermissionPolicy permissionPolicy`

                      Permission policy for tool execution.

                      - `class BetaManagedAgentsAlwaysAllowPolicy:`

                        Tool calls are automatically approved without user confirmation.

                      - `class BetaManagedAgentsAlwaysAskPolicy:`

                        Tool calls require user confirmation before execution.

                    - `JsonValue type constant`

                    - `Optional<List<String>> allowedDomains`

                    - `Optional<List<String>> blockedDomains`

                    - `Optional<BetaManagedAgentsUserLocation> userLocation`

                      Approximate user location for search result localization.

                      - `JsonValue type constant`

                        Location precision. Only "approximate" is supported.

                      - `Optional<String> city`

                        City name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> country`

                        Two-letter ISO 3166-1 country code, uppercase.

                      - `Optional<String> region`

                        Region or state name.

                        minLength: 1, maxLength: 255

                      - `Optional<String> timezone`

                        IANA timezone identifier, e.g. "America/Los_Angeles".

                        minLength: 1, maxLength: 255

                - `BetaManagedAgentsAgentToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for agent tools.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `Type type`

              - `class BetaManagedAgentsMcpToolset:`

                - `List<BetaManagedAgentsMcpToolConfig> configs`

                  - `boolean enabled`

                  - `String name`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `BetaManagedAgentsMcpToolsetDefaultConfig defaultConfig`

                  Resolved default configuration for all tools from an MCP server.

                  - `boolean enabled`

                  - `PermissionPolicy permissionPolicy`

                    Permission policy for tool execution.

                    - `class BetaManagedAgentsAlwaysAllowPolicy:`

                      Tool calls are automatically approved without user confirmation.

                    - `class BetaManagedAgentsAlwaysAskPolicy:`

                      Tool calls require user confirmation before execution.

                - `String mcpServerName`

                - `Type type`

              - `class BetaManagedAgentsCustomTool:`

                A custom tool as returned in API responses.

                - `String description`

                - `BetaManagedAgentsCustomToolInputSchema inputSchema`

                  JSON Schema for custom tool input parameters.

                  - `JsonValue type constant`

                  - `Optional<Properties> properties`

                  - `Optional<List<String>> required`

                - `String name`

                - `Type type`

            - `Type type`

            - `long version`

              format: int32

          - `class BetaManagedAgentsAdvisor:`

            Platform advisor roster entry: a model the session's primary thread may consult mid-turn.

            - `String model`

              The advisor model id.

            - `Type type`

        - `Type type`

      - `String name`

      - `List<Skill> skills`

        - `class BetaManagedAgentsAnthropicSkill:`

          A resolved Anthropic-managed skill.

        - `class BetaManagedAgentsCustomSkill:`

          A resolved user-created custom skill.

      - `Optional<String> system`

      - `List<Tool> tools`

        - `class BetaManagedAgentsAgentToolset20260401:`

        - `class BetaManagedAgentsMcpToolset:`

        - `class BetaManagedAgentsCustomTool:`

          A custom tool as returned in API responses.

      - `Type type`

      - `long version`

        format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

      - `BetaMonetaryAmount maxListCost`

        A monetary amount in a specific currency.

        - `String amount`

          Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

        - `BetaCurrency currency`

          Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

      - `Type type`

    - `Optional<Metadata> metadata`

      The session's full metadata bag after the update. Present when the update set non-empty metadata; absent when metadata was unchanged or cleared to empty.

    - `Optional<String> title`

      The session's new title. Present only when the update changed it.

  - `class BetaManagedAgentsStartEvent:`

    Opens a preview of a buffered event. Carries the previewed event's type and id only. Followed by zero or more event_delta events with the same event id, normally concluded by the buffered event carrying that id. If the producing model request ends without that event (an error or interrupt mid-stream), its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsStartEventPreview event`

      The previewed event's type and id. The event type determines which delta types the preview's event_delta events carry: agent.message events stream content_delta fragments; agent.thinking previews are start-only — no deltas follow, and the buffered agent.thinking with the same id concludes them.

      - `class BetaManagedAgentsAgentMessagePreview:`

        - `String id`

          The id the buffered agent.message will carry if it is emitted. Matches the event_id on this preview's event_delta events.

        - `Type type`

      - `class BetaManagedAgentsAgentThinkingPreview:`

        - `String id`

          The id the buffered agent.thinking will carry if it is emitted. Start-only — no event_delta events follow.

        - `Type type`

    - `Type type`

  - `class BetaManagedAgentsDeltaEvent:`

    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `BetaManagedAgentsDeltaContent delta`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `BetaManagedAgentsTextBlock content`

        Regular text content.

      - `Type type`

      - `Optional<Long> index`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

        format: uint32

    - `String eventId`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `Type type`

  - `class BetaManagedAgentsSystemMessageEvent:`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `String id`

      Unique identifier for this event.

    - `List<BetaManagedAgentsSystemContentBlock> content`

      System content blocks. Text-only.

      - `String text`

        The text content.

        minLength: 1

      - `Type type`

    - `Type type`

    - `Optional<LocalDateTime> processedAt`

      A timestamp in RFC 3339 format

      format: date-time

  - `class BetaManagedAgentsSessionUsageEvent:`

    Periodic snapshot of the session's cumulative usage and tracked list cost.

    - `String id`

      Unique identifier for this event.

    - `LocalDateTime processedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Type type`

    - `BetaManagedAgentsSessionUsageSnapshot usage`

      Point-in-time snapshot of a session's cumulative usage.

      - `Optional<Double> activeSeconds`

        Cumulative time in seconds during which the session had at least one thread in running status. Overlapping activity from concurrent threads is counted once. This is the duration the session's runtime cost is priced on.

        format: double

      - `Optional<BetaManagedAgentsCacheCreationUsage> cacheCreation`

        Prompt-cache creation token usage broken down by cache lifetime.

        - `Optional<Long> ephemeral1hInputTokens`

          Tokens used to create 1-hour ephemeral cache entries.

          format: int32

        - `Optional<Long> ephemeral5mInputTokens`

          Tokens used to create 5-minute ephemeral cache entries.

          format: int32

      - `Optional<Long> cacheReadInputTokens`

        Total tokens read from prompt cache.

        format: int32

      - `Optional<Long> inputTokens`

        Total input tokens consumed across all turns.

        format: int32

      - `Optional<BetaMonetaryAmount> listCost`

        A monetary amount in a specific currency.

      - `Optional<Long> outputTokens`

        Total output tokens generated across all turns.

        format: int32

      - `Optional<BetaManagedAgentsServerToolUsage> serverToolUse`

        Cumulative count of server-executed tool invocations, broken down by tool.

        - `Optional<Long> webFetchRequests`

          Number of server-executed web fetch requests.

          format: int32

        - `Optional<Long> webSearchRequests`

          Number of server-executed web search requests.

          format: int32

    - `Optional<BetaManagedAgentsBudgetLimit> budget`

      A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

- `class BetaManagedAgentsStreamSessionThreadEvents: union`

  Server-sent event in a single thread's stream.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.StreamResponse;
import com.anthropic.models.beta.sessions.threads.BetaManagedAgentsStreamSessionThreadEvents;
import com.anthropic.models.beta.sessions.threads.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        EventStreamParams params = EventStreamParams.builder()
            .sessionId("sesn_011CZkZAtmR3yMPDzynEDxu7")
            .threadId("sthr_011CZkZVWa6oIjw0rgXZpnBt")
            .build();
        StreamResponse<BetaManagedAgentsStreamSessionThreadEvents> betaManagedAgentsStreamSessionThreadEvents = client.beta().sessions().threads().events().streamStreaming(params);
    }
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

`BetaManagedAgentsDeployment beta().deployments().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/deployments`

Create Deployment

#### Parameters

- `DeploymentCreateParams params`

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

  - `Agent agent`

    Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `String environmentId`

    ID of the `environment` defining the container configuration for sessions created from this deployment.

    minLength: 1, maxLength: 128

  - `List<BetaManagedAgentsDeploymentInitialEventParams> initialEvents`

    Events to send to each session immediately after creation. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `String name`

    Human-readable name for the deployment.

    minLength: 1, maxLength: 256

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Optional<String> description`

    Description of what the deployment does.

    maxLength: 2048

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Optional<List<Resource>> resources`

    Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type type`

      - `String url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Optional<BetaManagedAgentsScheduleParams> schedule`

    5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Optional<List<String>> vaultIds`

    Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentCreateParams;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsTextBlock;
import com.anthropic.models.beta.sessions.events.BetaManagedAgentsUserMessageEventParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeploymentCreateParams params = DeploymentCreateParams.builder()
            .agent("string")
            .environmentId("x")
            .addUserMessageInitialEvent(List.of(BetaManagedAgentsUserMessageEventParams.Content.ofText(BetaManagedAgentsTextBlock.builder()
                .text("Where is my order #1234?")
                .type(BetaManagedAgentsTextBlock.Type.TEXT)
                .build())))
            .name("x")
            .build();
        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().create(params);
    }
}
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

`DeploymentListPage beta().deployments().list(params = DeploymentListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/deployments`

List Deployments

#### Parameters

- `DeploymentListParams params`

  - `Optional<String> agentId`

    Filter by agent ID.

  - `Optional<LocalDateTime> createdAtGte`

    Return deployments created at or after this time (inclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return deployments created at or before this time (inclusive).

    format: date-time

  - `Optional<Boolean> includeArchived`

    When true, includes archived deployments. Default: false (exclude archived).

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 100.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor.

  - `Optional<BetaManagedAgentsDeploymentStatus> status`

    Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

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

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.DeploymentListPage;
import com.anthropic.models.beta.deployments.DeploymentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeploymentListPage page = client.beta().deployments().list();
    }
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

`BetaManagedAgentsDeployment beta().deployments().retrieve(params = DeploymentRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/deployments/{deployment_id}`

Get Deployment

#### Parameters

- `DeploymentRetrieveParams params`

  - `Optional<String> deploymentId`

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

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().retrieve("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`BetaManagedAgentsDeployment beta().deployments().update(params = DeploymentUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/deployments/{deployment_id}`

Update Deployment

#### Parameters

- `DeploymentUpdateParams params`

  - `Optional<String> deploymentId`

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

  - `Optional<Agent> agent`

    Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

    - `String`

    - `class BetaManagedAgentsAgentParams:`

      Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

      - `String id`

        The `agent` ID.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<Long> version`

        The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

        format: int32

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

  - `Optional<String> description`

    Description. Omit to preserve; send empty string or null to clear.

    maxLength: 2048

  - `Optional<String> environmentId`

    ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

    maxLength: 128

  - `Optional<List<BetaManagedAgentsDeploymentInitialEventParams>> initialEvents`

    Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

    - `class BetaManagedAgentsUserMessageEventParams:`

      Parameters for sending a user message to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsUserDefineOutcomeEventParams:`

      Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubricParams:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubricParams:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

            maxLength: 262144

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsSystemMessageEventParams:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<String> name`

    Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

    maxLength: 256

  - `Optional<List<Resource>> resources`

    Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

    - `class BetaManagedAgentsGitHubRepositoryResourceParams:`

      Mount a GitHub repository into the session's container.

      - `String authorizationToken`

        GitHub authorization token used to clone the repository.

        minLength: 1, maxLength: 4096

      - `Type type`

      - `String url`

        Github URL of the repository

        minLength: 1, maxLength: 2048

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsFileResourceParams:`

      Mount a file uploaded via the Files API into the session.

      - `String fileId`

        ID of a previously uploaded file.

        minLength: 1, maxLength: 128

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

        minLength: 1, maxLength: 4096

    - `class BetaManagedAgentsMemoryStoreResourceParam:`

      Parameters for attaching a memory store to an agent session.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

        maxLength: 4096

  - `Optional<BetaManagedAgentsScheduleParams> schedule`

    5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Optional<List<String>> vaultIds`

    Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().update("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`BetaManagedAgentsDeployment beta().deployments().archive(params = DeploymentArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

#### Parameters

- `DeploymentArchiveParams params`

  - `Optional<String> deploymentId`

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

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().archive("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`BetaManagedAgentsDeploymentRun beta().deployments().run(params = DeploymentRunParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

#### Parameters

- `DeploymentRunParams params`

  - `Optional<String> deploymentId`

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

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `String id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String deploymentId`

    ID of the deployment that produced this run.

  - `Optional<Error> error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `String message`

        Human-readable error description.

      - `Type type`

  - `Optional<String> sessionId`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `LocalDateTime scheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Type type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `Type type`

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deploymentruns.BetaManagedAgentsDeploymentRun;
import com.anthropic.models.beta.deployments.DeploymentRunParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeploymentRun betaManagedAgentsDeploymentRun = client.beta().deployments().run("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`BetaManagedAgentsDeployment beta().deployments().pause(params = DeploymentPauseParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

#### Parameters

- `DeploymentPauseParams params`

  - `Optional<String> deploymentId`

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

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentPauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().pause("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`BetaManagedAgentsDeployment beta().deployments().unpause(params = DeploymentUnpauseParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

#### Parameters

- `DeploymentUnpauseParams params`

  - `Optional<String> deploymentId`

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

#### Returns

- `class BetaManagedAgentsDeployment:`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `String id`

    Unique identifier for this deployment.

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Description of what the deployment does.

  - `String environmentId`

    ID of the `environment` where sessions run.

  - `List<BetaManagedAgentsDeploymentInitialEvent> initialEvents`

    Events sent to each session immediately after creation.

    - `class BetaManagedAgentsDeploymentUserMessageEvent:`

      A user message sent to the session.

      - `List<Content> content`

        Array of content blocks for the user message.

        - `class BetaManagedAgentsTextBlock:`

          Regular text content.

          - `String text`

            The text content.

            minLength: 1

          - `Type type`

        - `class BetaManagedAgentsImageBlock:`

          Image content specified directly as base64 data or as a reference via a URL.

          - `Source source`

            Union type for image source variants.

            - `class BetaManagedAgentsBase64ImageSource:`

              Base64-encoded image data.

              - `String data`

                Base64-encoded image data.

                minLength: 1

              - `String mediaType`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsUrlImageSource:`

              Image referenced by URL.

              - `Type type`

              - `String url`

                URL of the image to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileImageSource:`

              Image referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

        - `class BetaManagedAgentsDocumentBlock:`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `Source source`

            Union type for document source variants.

            - `class BetaManagedAgentsBase64DocumentSource:`

              Base64-encoded document data.

              - `String data`

                Base64-encoded document data.

                minLength: 1

              - `String mediaType`

                MIME type of the document (e.g., "application/pdf").

                minLength: 1

              - `Type type`

            - `class BetaManagedAgentsPlainTextDocumentSource:`

              Plain text document content.

              - `String data`

                The plain text content.

                minLength: 1

              - `MediaType mediaType`

                MIME type of the text content. Must be "text/plain".

              - `Type type`

            - `class BetaManagedAgentsUrlDocumentSource:`

              Document referenced by URL.

              - `Type type`

              - `String url`

                URL of the document to fetch.

                minLength: 1

            - `class BetaManagedAgentsFileDocumentSource:`

              Document referenced by file ID.

              - `String fileId`

                ID of a previously uploaded file.

                minLength: 1

              - `Type type`

          - `Type type`

          - `Optional<String> context`

            Additional context about the document for the model.

          - `Optional<String> title`

            The title of the document.

        - `class BetaManagedAgentsRedactedBlock:`

          Placeholder for content withheld by Anthropic model policy.

          - `Type type`

      - `Type type`

    - `class BetaManagedAgentsDeploymentUserDefineOutcomeEvent:`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `String description`

        What the agent should produce. This is the task specification.

      - `Rubric rubric`

        Rubric for grading the quality of an outcome.

        - `class BetaManagedAgentsFileRubric:`

          Rubric referenced by a file uploaded via the Files API.

          - `String fileId`

            ID of the rubric file.

          - `Type type`

        - `class BetaManagedAgentsTextRubric:`

          Rubric content provided inline as text.

          - `String content`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `Type type`

      - `Type type`

      - `Optional<Long> maxIterations`

        Eval→revision cycles before giving up. Default 3, max 20.

        format: int32

    - `class BetaManagedAgentsDeploymentSystemMessageEvent:`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `List<BetaManagedAgentsSystemContentBlock> content`

        System content blocks to append. Text-only.

        - `String text`

          The text content.

          minLength: 1

        - `Type type`

      - `Type type`

  - `Metadata metadata`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `String name`

    Human-readable name.

  - `Optional<BetaManagedAgentsDeploymentPausedReason> pausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `class BetaManagedAgentsManualDeploymentPausedReason:`

      The caller invoked the pause endpoint on the deployment.

      - `Type type`

    - `class BetaManagedAgentsErrorDeploymentPausedReason:`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `BetaManagedAgentsDeploymentPausedReasonError error`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `class BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError:`

          The deployment's environment was archived.

          - `Type type`

        - `class BetaManagedAgentsAgentArchivedDeploymentPausedReasonError:`

          The deployment's agent was archived.

          - `Type type`

        - `class BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError:`

          The deployment's environment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError:`

          A vault referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsFileNotFoundDeploymentPausedReasonError:`

          A file resource referenced by the deployment no longer exists.

          - `Type type`

        - `class BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError:`

          A referenced resource no longer exists and its kind was not reported.

          - `Type type`

        - `class BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError:`

          The deployment's workspace was archived.

          - `Type type`

        - `class BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError:`

          The deployment's organization is disabled.

          - `Type type`

        - `class BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError:`

          A memory store referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError:`

          A skill referenced by the deployment's agent no longer exists.

          - `Type type`

        - `class BetaManagedAgentsVaultArchivedDeploymentPausedReasonError:`

          A vault referenced by the deployment is archived.

          - `Type type`

        - `class BetaManagedAgentsUnknownDeploymentPausedReasonError:`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `Type type`

        - `class BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError:`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `Type type`

        - `class BetaManagedAgentsMcpEgressBlockedDeploymentPausedReasonError:`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `Type type`

      - `Type type`

  - `List<BetaManagedAgentsSessionResourceConfig> resources`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `class BetaManagedAgentsGitHubRepositoryResourceConfig:`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `Type type`

      - `String url`

        Github URL of the repository

      - `Optional<Checkout> checkout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `class BetaManagedAgentsBranchCheckout:`

          - `String name`

            Branch name to check out.

            minLength: 1, maxLength: 255

          - `Type type`

        - `class BetaManagedAgentsCommitCheckout:`

          - `String sha`

            Full commit SHA to check out.

            minLength: 7, maxLength: 64

          - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `class BetaManagedAgentsFileResourceConfig:`

      A file mounted into each session's container.

      - `String fileId`

        ID of a previously uploaded file.

      - `Type type`

      - `Optional<String> mountPath`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `class BetaManagedAgentsMemoryStoreResourceConfig:`

      A memory store attached to each session created from this deployment.

      - `String memoryStoreId`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `Type type`

      - `Optional<Access> access`

        Access mode for an attached memory store.

        - `READ_WRITE("read_write")`

        - `READ_ONLY("read_only")`

      - `Optional<String> instructions`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `Optional<BetaManagedAgentsSchedule> schedule`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `String expression`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      minLength: 1, maxLength: 256

    - `String timezone`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      minLength: 1

    - `Type type`

    - `Optional<LocalDateTime> lastRunAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<List<LocalDateTime>> upcomingRunsAt`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `BetaManagedAgentsDeploymentStatus status`

    Lifecycle status of a deployment.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `List<String> vaultIds`

    Vault IDs supplying stored credentials for sessions created from this deployment.

  - `Optional<BetaManagedAgentsBudgetLimit> budget`

    A hard spend ceiling. The session stops issuing new model requests once the tracked list cost reaches `max_list_cost`.

    - `BetaMonetaryAmount maxListCost`

      A monetary amount in a specific currency.

      - `String amount`

        Amount in minor units of the currency, as an integer decimal string with no leading zeros: "2500" is $25.00 and "50" is fifty cents. A string rather than a number so no float rounding is ever applied.

      - `BetaCurrency currency`

        Uppercase ISO-4217 currency code. `USD` is the only currency currently supported; the accepted set is closed and grows only when a new currency is priced.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deployments.BetaManagedAgentsDeployment;
import com.anthropic.models.beta.deployments.DeploymentUnpauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeployment betaManagedAgentsDeployment = client.beta().deployments().unpause("depl_011CZkZcDH3vPqd7xnEfwTai");
    }
}
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

`DeploymentRunListPage beta().deploymentRuns().list(params = DeploymentRunListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/deployment_runs`

List Deployment Runs

#### Parameters

- `DeploymentRunListParams params`

  - `Optional<LocalDateTime> createdAtGt`

    Return runs created strictly after this time (exclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtGte`

    Return runs created at or after this time (inclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtLt`

    Return runs created strictly before this time (exclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return runs created at or before this time (inclusive).

    format: date-time

  - `Optional<String> deploymentId`

    Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `Optional<Boolean> hasError`

    Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `Optional<Long> limit`

    Maximum results per page. Default 20, maximum 1000.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `Optional<BetaManagedAgentsTriggerType> triggerType`

    Filter runs by what triggered them. Omit to return all runs.

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

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `String id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String deploymentId`

    ID of the deployment that produced this run.

  - `Optional<Error> error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `String message`

        Human-readable error description.

      - `Type type`

  - `Optional<String> sessionId`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `LocalDateTime scheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Type type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `Type type`

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deploymentruns.DeploymentRunListPage;
import com.anthropic.models.beta.deploymentruns.DeploymentRunListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        DeploymentRunListPage page = client.beta().deploymentRuns().list();
    }
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

`BetaManagedAgentsDeploymentRun beta().deploymentRuns().retrieve(params = DeploymentRunRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

#### Parameters

- `DeploymentRunRetrieveParams params`

  - `Optional<String> deploymentRunId`

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

#### Returns

- `class BetaManagedAgentsDeploymentRun:`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `String id`

    Unique identifier for this run (`drun_...`).

  - `BetaManagedAgentsAgentReference agent`

    A resolved agent reference with a concrete version.

    - `String id`

    - `Type type`

    - `long version`

      format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String deploymentId`

    ID of the deployment that produced this run.

  - `Optional<Error> error`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `class BetaManagedAgentsEnvironmentArchivedRunError:`

      The deployment's environment was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsAgentArchivedRunError:`

      The deployment's agent was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentNotFoundRunError:`

      The deployment's environment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultNotFoundRunError:`

      A vault referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsVaultArchivedRunError:`

      A vault referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsFileNotFoundRunError:`

      A file resource referenced by the deployment no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMemoryStoreArchivedRunError:`

      A memory store referenced by the deployment is archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSkillNotFoundRunError:`

      A skill referenced by the deployment's agent no longer exists.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionResourceNotFoundRunError:`

      A referenced resource no longer exists and its kind was not reported.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsWorkspaceArchivedRunError:`

      The deployment's workspace was archived.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsOrganizationDisabledRunError:`

      The deployment's organization is disabled.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionRateLimitedRunError:`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSessionCreationRejectedRunError:`

      The session create request was rejected with a non-retryable validation error.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsUnknownRunError:`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsSelfHostedResourcesUnsupportedRunError:`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `String message`

        Human-readable error description.

      - `Type type`

    - `class BetaManagedAgentsMcpEgressBlockedRunError:`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `String message`

        Human-readable error description.

      - `Type type`

  - `Optional<String> sessionId`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `BetaManagedAgentsTriggerContext triggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `class BetaManagedAgentsScheduleTriggerContext:`

      The run was fired by the deployment's cron schedule.

      - `LocalDateTime scheduledAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Type type`

    - `class BetaManagedAgentsManualTriggerContext:`

      The run was started manually by creating a session directly against the deployment.

      - `Type type`

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.deploymentruns.BetaManagedAgentsDeploymentRun;
import com.anthropic.models.beta.deploymentruns.DeploymentRunRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeploymentRun betaManagedAgentsDeploymentRun = client.beta().deploymentRuns().retrieve("deployment_run_id");
    }
}
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

`BetaManagedAgentsVault beta().vaults().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults`

Create Vault

#### Parameters

- `VaultCreateParams params`

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

  - `String displayName`

    Human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultCreateParams params = VaultCreateParams.builder()
            .displayName("Example vault")
            .build();
        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().create(params);
    }
}
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

`VaultListPage beta().vaults().list(params = VaultListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults`

List Vaults

#### Parameters

- `VaultListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived vaults in the results.

  - `Optional<Long> limit`

    Maximum number of vaults to return per page. Defaults to 20, maximum 100.

    format: int32

  - `Optional<String> page`

    Opaque pagination token from a previous `list_vaults` response.

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

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.VaultListPage;
import com.anthropic.models.beta.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        VaultListPage page = client.beta().vaults().list();
    }
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

`BetaManagedAgentsVault beta().vaults().retrieve(params = VaultRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}`

Get Vault

#### Parameters

- `VaultRetrieveParams params`

  - `Optional<String> vaultId`

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

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().retrieve("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsVault beta().vaults().update(params = VaultUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}`

Update Vault

#### Parameters

- `VaultUpdateParams params`

  - `Optional<String> vaultId`

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

    Updated human-readable name for the vault. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().update("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsDeletedVault beta().vaults().delete(params = VaultDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/vaults/{vault_id}`

Delete Vault

#### Parameters

- `VaultDeleteParams params`

  - `Optional<String> vaultId`

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

#### Returns

- `class BetaManagedAgentsDeletedVault:`

  Confirmation of a deleted vault.

  - `String id`

    Unique identifier of the deleted vault.

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsDeletedVault;
import com.anthropic.models.beta.vaults.VaultDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedVault betaManagedAgentsDeletedVault = client.beta().vaults().delete("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
```

##### Response (200)

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

### Archive Vault

`BetaManagedAgentsVault beta().vaults().archive(params = VaultArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/archive`

Archive Vault

#### Parameters

- `VaultArchiveParams params`

  - `Optional<String> vaultId`

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

#### Returns

- `class BetaManagedAgentsVault:`

  A vault that stores credentials for use by agents during sessions.

  - `String id`

    Unique identifier for the vault.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String displayName`

    Human-readable name for the vault.

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the vault.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.BetaManagedAgentsVault;
import com.anthropic.models.beta.vaults.VaultArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsVault betaManagedAgentsVault = client.beta().vaults().archive("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
}
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

`BetaManagedAgentsCredential beta().vaults().credentials().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials`

Create Credential

#### Parameters

- `CredentialCreateParams params`

  - `Optional<String> vaultId`

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

  - `Auth auth`

    Authentication details for creating a credential.

    - `class BetaManagedAgentsMcpOAuthCreateParams:`

      Parameters for creating an MCP OAuth credential.

      - `String accessToken`

        OAuth access token.

        minLength: 1, maxLength: 8192

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshParams> refresh`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `String clientId`

          OAuth client ID.

          minLength: 1, maxLength: 1024

        - `String refreshToken`

          OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

          minLength: 1, maxLength: 2047

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneParam:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicParam:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostParam:`

            Token endpoint uses POST body authentication with client credentials.

            - `String clientSecret`

              OAuth client secret.

              minLength: 1, maxLength: 512

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

          minLength: 1, maxLength: 2047

        - `Optional<String> scope`

          OAuth scope for the refresh request.

          minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsStaticBearerCreateParams:`

      Parameters for creating a static bearer token credential.

      - `String token`

        Static bearer token value.

        minLength: 1, maxLength: 8192

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

        minLength: 1, maxLength: 2047

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableCreateParams:`

      Parameters for creating an environment variable credential.

      - `BetaManagedAgentsCredentialNetworkingParams networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type type`

      - `String secretName`

        Name of the environment variable. Immutable after create.

        minLength: 1, maxLength: 255

      - `String secretValue`

        Secret value. Write-only; never returned in responses.

        minLength: 1, maxLength: 4096

      - `Type type`

      - `Optional<BetaManagedAgentsInjectionLocationParams> injectionLocation`

        Where in the outbound request the secret value may be substituted.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

  - `Optional<String> displayName`

    Human-readable name for the credential. Up to 255 characters.

    maxLength: 255

  - `Optional<Metadata> metadata`

    Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsStaticBearerCreateParams;
import com.anthropic.models.beta.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .auth(BetaManagedAgentsStaticBearerCreateParams.builder()
                .token("bearer_exampletoken")
                .mcpServerUrl("https://example-server.modelcontextprotocol.io/sse")
                .type(BetaManagedAgentsStaticBearerCreateParams.Type.STATIC_BEARER)
                .build())
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().create(params);
    }
}
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

`CredentialListPage beta().vaults().credentials().list(params = CredentialListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}/credentials`

List Credentials

#### Parameters

- `CredentialListParams params`

  - `Optional<String> vaultId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived credentials in the results.

  - `Optional<Long> limit`

    Maximum number of credentials to return per page. Defaults to 20, maximum 100.

    format: int32

  - `Optional<String> page`

    Opaque pagination token from a previous `list_credentials` response.

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

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.CredentialListPage;
import com.anthropic.models.beta.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().vaults().credentials().list("vlt_011CZkZDLs7fYzm1hXNPeRjv");
    }
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

`BetaManagedAgentsCredential beta().vaults().credentials().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

#### Parameters

- `CredentialRetrieveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialRetrieveParams params = CredentialRetrieveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().retrieve(params);
    }
}
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

`BetaManagedAgentsCredential beta().vaults().credentials().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

#### Parameters

- `CredentialUpdateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

  - `Optional<Auth> auth`

    Updated authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthUpdateParams:`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type type`

      - `Optional<String> accessToken`

        Updated OAuth access token.

        minLength: 1, maxLength: 8192

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshUpdateParams> refresh`

        Parameters for updating OAuth refresh token configuration.

        - `Optional<String> refreshToken`

          Updated OAuth refresh token.

          minLength: 1, maxLength: 4096

        - `Optional<String> scope`

          Updated OAuth scope for the refresh request.

          maxLength: 8192

        - `Optional<TokenEndpointAuth> tokenEndpointAuth`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type type`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

          - `class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:`

            Updated POST body authentication parameters for the token endpoint.

            - `Type type`

            - `Optional<String> clientSecret`

              Updated OAuth client secret.

              minLength: 1, maxLength: 512

    - `class BetaManagedAgentsStaticBearerUpdateParams:`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type type`

      - `Optional<String> token`

        Updated static bearer token value.

        minLength: 1, maxLength: 8192

    - `class BetaManagedAgentsEnvironmentVariableUpdateParams:`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `Type type`

      - `Optional<BetaManagedAgentsInjectionLocationUpdateParams> injectionLocation`

        Updated injection location.

        - `Optional<Boolean> body`

          Substitute when the placeholder appears in the request body.

        - `Optional<Boolean> header`

          Substitute when the placeholder appears in a request header value.

      - `Optional<BetaManagedAgentsCredentialNetworkingParams> networking`

        Updated networking scope. Full replacement.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingParams:`

          Substitute the secret only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type type`

      - `Optional<String> secretValue`

        Updated secret value.

        minLength: 1, maxLength: 4096

  - `Optional<String> displayName`

    Updated human-readable name for the credential. 1-255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialUpdateParams params = CredentialUpdateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().update(params);
    }
}
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

`BetaManagedAgentsDeletedCredential beta().vaults().credentials().delete(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

#### Parameters

- `CredentialDeleteParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

#### Returns

- `class BetaManagedAgentsDeletedCredential:`

  Confirmation of a deleted credential.

  - `String id`

    Unique identifier of the deleted credential.

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsDeletedCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsDeletedCredential betaManagedAgentsDeletedCredential = client.beta().vaults().credentials().delete(params);
    }
}
```

##### Response (200)

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

### Archive Credential

`BetaManagedAgentsCredential beta().vaults().credentials().archive(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

#### Parameters

- `CredentialArchiveParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

#### Returns

- `class BetaManagedAgentsCredential:`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `String id`

    Unique identifier for the credential.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Auth auth`

    Authentication details for a credential.

    - `class BetaManagedAgentsMcpOAuthAuthResponse:`

      OAuth credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

      - `Optional<LocalDateTime> expiresAt`

        A timestamp in RFC 3339 format

        format: date-time

      - `Optional<BetaManagedAgentsMcpOAuthRefreshResponse> refresh`

        OAuth refresh token configuration returned in credential responses.

        - `String clientId`

          OAuth client ID.

        - `String tokenEndpoint`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth tokenEndpointAuth`

          Token endpoint requires no client authentication.

          - `class BetaManagedAgentsTokenEndpointAuthNoneResponse:`

            Token endpoint requires no client authentication.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthBasicResponse:`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type type`

          - `class BetaManagedAgentsTokenEndpointAuthPostResponse:`

            Token endpoint uses POST body authentication with client credentials.

            - `Type type`

        - `Optional<String> resource`

          OAuth resource indicator.

        - `Optional<String> scope`

          OAuth scope for the refresh request.

    - `class BetaManagedAgentsStaticBearerAuthResponse:`

      Static bearer token credential details for an MCP server.

      - `String mcpServerUrl`

        URL of the MCP server this credential authenticates against.

      - `Type type`

    - `class BetaManagedAgentsEnvironmentVariableAuthResponse:`

      Environment variable credential details. The secret value is never returned.

      - `BetaManagedAgentsInjectionLocationResponse injectionLocation`

        Where in the outbound request the secret value is substituted.

        - `boolean body`

          Whether the placeholder is substituted in the request body.

        - `boolean header`

          Whether the placeholder is substituted in request header values.

      - `Networking networking`

        Outbound hosts the secret value is substituted on.

        - `class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type type`

        - `class BetaManagedAgentsLimitedCredentialNetworkingResponse:`

          The secret is substituted only on requests to the listed hosts.

          - `List<String> allowedHosts`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type type`

      - `String secretName`

        Name of the environment variable.

      - `Type type`

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Metadata metadata`

    Arbitrary key-value metadata attached to the credential.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault this credential belongs to.

  - `Optional<String> displayName`

    Human-readable name for the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredential;
import com.anthropic.models.beta.vaults.credentials.CredentialArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialArchiveParams params = CredentialArchiveParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredential betaManagedAgentsCredential = client.beta().vaults().credentials().archive(params);
    }
}
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

`BetaManagedAgentsCredentialValidation beta().vaults().credentials().mcpOAuthValidate(params, requestOptions = RequestOptions.none())`

**POST** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

#### Parameters

- `CredentialMcpOAuthValidateParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

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

#### Returns

- `class BetaManagedAgentsCredentialValidation:`

  Result of live-probing a credential against its configured MCP server.

  - `String credentialId`

    Unique identifier of the credential that was validated.

  - `boolean hasRefreshToken`

    Whether the credential has a refresh token configured.

  - `Optional<BetaManagedAgentsMcpProbe> mcpProbe`

    The failing step of an MCP validation probe.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

      - `String body`

        Response body. May be truncated and has sensitive values scrubbed.

      - `boolean bodyTruncated`

        Whether `body` was truncated.

      - `String contentType`

        Value of the `Content-Type` response header.

      - `long statusCode`

        HTTP status code.

        format: int32

    - `String method`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Optional<BetaManagedAgentsRefreshObject> refresh`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `Optional<BetaManagedAgentsRefreshHttpResponse> httpResponse`

      An HTTP response captured during a credential validation probe.

    - `Status status`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `SUCCEEDED("succeeded")`

      - `FAILED("failed")`

      - `CONNECT_ERROR("connect_error")`

      - `NO_REFRESH_TOKEN("no_refresh_token")`

  - `BetaManagedAgentsCredentialValidationStatus status`

    Overall verdict of a credential validation probe.

    - `VALID("valid")`

    - `INVALID("invalid")`

    - `UNKNOWN("unknown")`

  - `Type type`

  - `LocalDateTime validatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String vaultId`

    Identifier of the vault containing the credential.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.vaults.credentials.BetaManagedAgentsCredentialValidation;
import com.anthropic.models.beta.vaults.credentials.CredentialMcpOAuthValidateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        CredentialMcpOAuthValidateParams params = CredentialMcpOAuthValidateParams.builder()
            .vaultId("vlt_011CZkZDLs7fYzm1hXNPeRjv")
            .credentialId("vcrd_011CZkZEMt8gZan2iYOQfSkw")
            .build();
        BetaManagedAgentsCredentialValidation betaManagedAgentsCredentialValidation = client.beta().vaults().credentials().mcpOAuthValidate(params);
    }
}
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

`BetaManagedAgentsMemoryStore beta().memoryStores().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores`

Create a memory store

#### Parameters

- `MemoryStoreCreateParams params`

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

  - `String name`

    Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

    minLength: 1, maxLength: 255

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

    maxLength: 1024

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreCreateParams params = MemoryStoreCreateParams.builder()
            .name("x")
            .build();
        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().create(params);
    }
}
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

`MemoryStoreListPage beta().memoryStores().list(params = MemoryStoreListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores`

List memory stores

#### Parameters

- `MemoryStoreListParams params`

  - `Optional<LocalDateTime> createdAtGte`

    Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

    format: date-time

  - `Optional<Boolean> includeArchived`

    When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `Optional<Long> limit`

    Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

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

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.MemoryStoreListPage;
import com.anthropic.models.beta.memorystores.MemoryStoreListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryStoreListPage page = client.beta().memoryStores().list();
    }
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

`BetaManagedAgentsMemoryStore beta().memoryStores().retrieve(params = MemoryStoreRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

#### Parameters

- `MemoryStoreRetrieveParams params`

  - `Optional<String> memoryStoreId`

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

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().retrieve("memory_store_id");
    }
}
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

`BetaManagedAgentsMemoryStore beta().memoryStores().update(params = MemoryStoreUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores/{memory_store_id}`

Update a memory store

#### Parameters

- `MemoryStoreUpdateParams params`

  - `Optional<String> memoryStoreId`

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

  - `Optional<String> description`

    New description for the store, up to 1024 characters. Pass an empty string to clear it.

    maxLength: 1024

  - `Optional<Metadata> metadata`

    Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Optional<String> name`

    New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

    minLength: 1, maxLength: 255

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().update("memory_store_id");
    }
}
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

`BetaManagedAgentsDeletedMemoryStore beta().memoryStores().delete(params = MemoryStoreDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

#### Parameters

- `MemoryStoreDeleteParams params`

  - `Optional<String> memoryStoreId`

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

#### Returns

- `class BetaManagedAgentsDeletedMemoryStore:`

  Confirmation that a `memory_store` was deleted.

  - `String id`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsDeletedMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsDeletedMemoryStore betaManagedAgentsDeletedMemoryStore = client.beta().memoryStores().delete("memory_store_id");
    }
}
```

##### Response (200)

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

### Archive a memory store

`BetaManagedAgentsMemoryStore beta().memoryStores().archive(params = MemoryStoreArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

#### Parameters

- `MemoryStoreArchiveParams params`

  - `Optional<String> memoryStoreId`

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

#### Returns

- `class BetaManagedAgentsMemoryStore:`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `String id`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String name`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> description`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Optional<Metadata> metadata`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.BetaManagedAgentsMemoryStore;
import com.anthropic.models.beta.memorystores.MemoryStoreArchiveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaManagedAgentsMemoryStore betaManagedAgentsMemoryStore = client.beta().memoryStores().archive("memory_store_id");
    }
}
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

`BetaManagedAgentsMemory beta().memoryStores().memories().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

#### Parameters

- `MemoryCreateParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

  - `Optional<String> content`

    UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `String path`

    Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

    minLength: 2, maxLength: 1024

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryCreateParams params = MemoryCreateParams.builder()
            .memoryStoreId("memory_store_id")
            .content("content")
            .path("xx")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().create(params);
    }
}
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

`MemoryListPage beta().memoryStores().memories().list(params = MemoryListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}/memories`

List memories

#### Parameters

- `MemoryListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<Long> depth`

    `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

    format: int32

  - `Optional<Long> limit`

    Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

    format: int32

  - `Optional<String> page`

    Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `Optional<String> pathPrefix`

    Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `Optional<BetaManagedAgentsMemoryView> view`

    Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

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

#### Returns

- `class BetaManagedAgentsMemoryListItem: union`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `class BetaManagedAgentsMemory:`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `String id`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `String contentSha256`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `long contentSizeBytes`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      format: int32

    - `LocalDateTime createdAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `String memoryStoreId`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `String memoryVersionId`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `String path`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type type`

    - `LocalDateTime updatedAt`

      A timestamp in RFC 3339 format

      format: date-time

    - `Optional<String> content`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `class BetaManagedAgentsMemoryPrefix:`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `String path`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.MemoryListPage;
import com.anthropic.models.beta.memorystores.memories.MemoryListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryListPage page = client.beta().memoryStores().memories().list("memory_store_id");
    }
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

`BetaManagedAgentsMemory beta().memoryStores().memories().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

#### Parameters

- `MemoryRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryRetrieveParams params = MemoryRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().retrieve(params);
    }
}
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

`BetaManagedAgentsMemory beta().memoryStores().memories().update(params, requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

#### Parameters

- `MemoryUpdateParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

  - `Optional<String> content`

    New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `Optional<String> path`

    New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

    minLength: 2, maxLength: 1024

  - `Optional<BetaManagedAgentsPrecondition> precondition`

    Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

#### Returns

- `class BetaManagedAgentsMemory:`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `String id`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `String contentSha256`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `long contentSizeBytes`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    format: int32

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryStoreId`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `String memoryVersionId`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `String path`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type type`

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> content`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryUpdateParams params = MemoryUpdateParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsMemory betaManagedAgentsMemory = client.beta().memoryStores().memories().update(params);
    }
}
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

`BetaManagedAgentsDeletedMemory beta().memoryStores().memories().delete(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

#### Parameters

- `MemoryDeleteParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryId`

  - `Optional<String> expectedContentSha256`

    Query parameter for expected_content_sha256

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

#### Returns

- `class BetaManagedAgentsDeletedMemory:`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `String id`

    ID of the deleted memory (a `mem_...` value).

  - `Type type`

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memories.BetaManagedAgentsDeletedMemory;
import com.anthropic.models.beta.memorystores.memories.MemoryDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryDeleteParams params = MemoryDeleteParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryId("memory_id")
            .build();
        BetaManagedAgentsDeletedMemory betaManagedAgentsDeletedMemory = client.beta().memoryStores().memories().delete(params);
    }
}
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

`MemoryVersionListPage beta().memoryStores().memoryVersions().list(params = MemoryVersionListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

#### Parameters

- `MemoryVersionListParams params`

  - `Optional<String> memoryStoreId`

  - `Optional<String> apiKeyId`

    Query parameter for api_key_id

  - `Optional<LocalDateTime> createdAtGte`

    Return versions created at or after this time (inclusive).

    format: date-time

  - `Optional<LocalDateTime> createdAtLte`

    Return versions created at or before this time (inclusive).

    format: date-time

  - `Optional<Long> limit`

    Query parameter for limit

    format: int32

  - `Optional<String> memoryId`

    Query parameter for memory_id

  - `Optional<BetaManagedAgentsMemoryVersionOperation> operation`

    Query parameter for operation

  - `Optional<String> page`

    Query parameter for page

  - `Optional<String> serviceAccountId`

    Query parameter for service_account_id

  - `Optional<String> sessionId`

    Query parameter for session_id

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonValue type constant`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListPage;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionListPage page = client.beta().memoryStores().memoryVersions().list("memory_store_id");
    }
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

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

#### Parameters

- `MemoryVersionRetrieveParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

  - `Optional<BetaManagedAgentsMemoryView> view`

    Query parameter for view

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

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonValue type constant`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRetrieveParams params = MemoryVersionRetrieveParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().retrieve(params);
    }
}
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

`BetaManagedAgentsMemoryVersion beta().memoryStores().memoryVersions().redact(params, requestOptions = RequestOptions.none())`

**POST** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

#### Parameters

- `MemoryVersionRedactParams params`

  - `String memoryStoreId`

  - `Optional<String> memoryVersionId`

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

#### Returns

- `class BetaManagedAgentsMemoryVersion:`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `String id`

    Unique identifier for this version (a `memver_...` value).

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String memoryId`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `String memoryStoreId`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `BetaManagedAgentsMemoryVersionOperation operation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `CREATED("created")`

    - `MODIFIED("modified")`

    - `DELETED("deleted")`

  - `Type type`

  - `Optional<String> content`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `Optional<String> contentSha256`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `Optional<Long> contentSizeBytes`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    format: int32

  - `Optional<BetaManagedAgentsActor> createdBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `class BetaManagedAgentsSessionActor:`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `String sessionId`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsApiActor:`

      Attribution for a write made directly via the public API (outside of any session).

      - `String apiKeyId`

        ID of the API key that performed the write. This identifies the key, not the secret.

        minLength: 1

      - `Type type`

    - `class BetaManagedAgentsUserActor:`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type type`

      - `String userId`

        ID of the user who performed the write (a `user_...` value).

        minLength: 1

    - `class BetaManagedAgentsServiceAccountActor:`

      Attribution for a write made by a workload authenticated as a service account, for example via Workload Identity Federation.

      - `String serviceAccountId`

        ID of the service account that performed the write (a `svac_...` value).

        minLength: 1

      - `JsonValue type constant`

  - `Optional<String> path`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `Optional<LocalDateTime> redactedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaManagedAgentsActor> redactedBy`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.memorystores.memoryversions.BetaManagedAgentsMemoryVersion;
import com.anthropic.models.beta.memorystores.memoryversions.MemoryVersionRedactParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        MemoryVersionRedactParams params = MemoryVersionRedactParams.builder()
            .memoryStoreId("memory_store_id")
            .memoryVersionId("memory_version_id")
            .build();
        BetaManagedAgentsMemoryVersion betaManagedAgentsMemoryVersion = client.beta().memoryStores().memoryVersions().redact(params);
    }
}
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

`BetaFileMetadata beta().files().upload(params, requestOptions = RequestOptions.none())`

**POST** `/v1/files`

Upload File

#### Parameters

- `FileUploadParams params`

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

  - `String file`

    The file to upload

    format: binary

#### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `String filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `String mimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `long sizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonValue type constant`

    Object type.

    For files, this is always `"file"`.

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue type constant`

      The type of scope (e.g., `"session"`).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaFileMetadata;
import com.anthropic.models.beta.files.FileUploadParams;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileUploadParams params = FileUploadParams.builder()
            .file(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        BetaFileMetadata betaFileMetadata = client.beta().files().upload(params);
    }
}
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
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### List Files

`FileListPage beta().files().list(params = FileListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/files`

List Files

#### Parameters

- `FileListParams params`

  - `Optional<String> afterId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `Optional<String> beforeId`

    ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Optional<Long> limit`

    Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

    maximum: 1000, minimum: 1

  - `Optional<String> scopeId`

    Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

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

#### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `String filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `String mimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `long sizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonValue type constant`

    Object type.

    For files, this is always `"file"`.

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue type constant`

      The type of scope (e.g., `"session"`).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.FileListPage;
import com.anthropic.models.beta.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        FileListPage page = client.beta().files().list();
    }
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

### Download File

`HttpResponse beta().files().download(params = FileDownloadParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/files/{file_id}/content`

Download File

#### Parameters

- `FileDownloadParams params`

  - `Optional<String> fileId`

    ID of the File.

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

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.core.http.HttpResponse;
import com.anthropic.models.beta.files.FileDownloadParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        HttpResponse response = client.beta().files().download("file_id");
    }
}
```

### Get File Metadata

`BetaFileMetadata beta().files().retrieveMetadata(params = FileRetrieveMetadataParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/files/{file_id}`

Get File Metadata

#### Parameters

- `FileRetrieveMetadataParams params`

  - `Optional<String> fileId`

    ID of the File.

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

#### Returns

- `class BetaFileMetadata:`

  - `String id`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `LocalDateTime createdAt`

    RFC 3339 datetime string representing when the file was created.

    format: date-time

  - `String filename`

    Original filename of the uploaded file.

    maxLength: 500, minLength: 1

  - `String mimeType`

    MIME type of the file.

    maxLength: 255, minLength: 1

  - `long sizeBytes`

    Size of the file in bytes.

    minimum: 0

  - `JsonValue type constant`

    Object type.

    For files, this is always `"file"`.

  - `Optional<Boolean> downloadable`

    Whether the file can be downloaded.

  - `Optional<BetaFileScope> scope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `String id`

      The ID of the scoping resource (e.g., the session ID).

    - `JsonValue type constant`

      The type of scope (e.g., `"session"`).

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaFileMetadata;
import com.anthropic.models.beta.files.FileRetrieveMetadataParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaFileMetadata betaFileMetadata = client.beta().files().retrieveMetadata("file_id");
    }
}
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
  "scope": {
    "id": "id",
    "type": "session"
  }
}
```

### Delete File

`BetaDeletedFile beta().files().delete(params = FileDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/files/{file_id}`

Delete File

#### Parameters

- `FileDeleteParams params`

  - `Optional<String> fileId`

    ID of the File.

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

#### Returns

- `class BetaDeletedFile:`

  - `String id`

    ID of the deleted file.

  - `Optional<Type> type`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.files.BetaDeletedFile;
import com.anthropic.models.beta.files.FileDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        BetaDeletedFile betaDeletedFile = client.beta().files().delete("file_id");
    }
}
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

`SkillCreateResponse beta().skills().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/skills`

Create Skill

#### Parameters

- `SkillCreateParams params`

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

  - `Optional<String> displayTitle`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

#### Returns

- `class SkillCreateResponse:`

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

#### Example

```java
package com.anthropic.example;

import com.anthropic.client.AnthropicClient;
import com.anthropic.client.okhttp.AnthropicOkHttpClient;
import com.anthropic.models.beta.skills.SkillCreateParams;
import com.anthropic.models.beta.skills.SkillCreateResponse;
import java.io.ByteArrayInputStream;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        AnthropicClient client = AnthropicOkHttpClient.fromEnv();

        SkillCreateParams params = SkillCreateParams.builder()
            .addFile(new ByteArrayInputStream("Example data".getBytes()))
            .build();
        SkillCreateResponse skill = client.beta().skills().create(params);
    }
}
```

##### Response (200)

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

### List Skills

`SkillListPage beta().skills().list(params = SkillListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/skills`

List Skills

#### Parameters

- `SkillListParams params`

  - `Optional<Long> limit`

    Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `Optional<String> page`

    Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `Optional<String> source`

    Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

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

#### Returns

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

#### Example

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

##### Response (200)

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

### Get Skill

`SkillRetrieveResponse beta().skills().retrieve(params = SkillRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/skills/{skill_id}`

Get Skill

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### Delete Skill

`SkillDeleteResponse beta().skills().delete(params = SkillDeleteParams.none(), requestOptions = RequestOptions.none())`

**DELETE** `/v1/skills/{skill_id}`

Delete Skill

#### Parameters

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

#### Returns

- `class SkillDeleteResponse:`

  - `String id`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `String type`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

#### Example

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

##### Response (200)

```json
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

## Beta › Skills › Versions

### Create Skill Version

`VersionCreateResponse beta().skills().versions().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/skills/{skill_id}/versions`

Create Skill Version

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### List Skill Versions

`VersionListPage beta().skills().versions().list(params = VersionListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/skills/{skill_id}/versions`

List Skill Versions

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### Download Skill Version Content

`HttpResponse beta().skills().versions().download(params, requestOptions = RequestOptions.none())`

**GET** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

#### Parameters

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

#### Example

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

### Get Skill Version

`VersionRetrieveResponse beta().skills().versions().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

#### Parameters

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

#### Returns

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

#### Example

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

##### Response (200)

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

### Delete Skill Version

`VersionDeleteResponse beta().skills().versions().delete(params, requestOptions = RequestOptions.none())`

**DELETE** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

#### Parameters

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

#### Returns

- `class VersionDeleteResponse:`

  - `String id`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `String type`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

#### Example

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

##### Response (200)

```json
{
  "id": "1759178010641129",
  "type": "type"
}
```

## Beta › User Profiles

### Create User Profile

`BetaUserProfile beta().userProfiles().create(params = UserProfileCreateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/user_profiles`

Create User Profile

#### Parameters

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

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `Optional<String> name`

    Optional for all profiles. Real-world name of the entity this profile represents (company or individual); for a resold-to company (`relationship` `resold` / `access_type` `passthrough`), that company's name where known. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

#### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

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

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

#### Example

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

`UserProfileListPage beta().userProfiles().list(params = UserProfileListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/user_profiles`

List User Profiles

#### Parameters

- `UserProfileListParams params`

  - `Optional<Long> limit`

    Query parameter for limit

    format: int32

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

#### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

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

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

#### Example

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

`BetaUserProfile beta().userProfiles().retrieve(params = UserProfileRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/user_profiles/{user_profile_id}`

Get User Profile

#### Parameters

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

#### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

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

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

#### Example

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

`BetaUserProfile beta().userProfiles().update(params = UserProfileUpdateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/user_profiles/{user_profile_id}`

Update User Profile

#### Parameters

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

    minLength: 1, maxLength: 255

  - `Optional<Metadata> metadata`

    Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `Optional<String> name`

    If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

    minLength: 1, maxLength: 255

  - `Optional<Relationship> relationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `EXTERNAL("external")`

    - `RESOLD("resold")`

    - `INTERNAL("internal")`

#### Returns

- `class BetaUserProfile:`

  - `String id`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

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

  - `LocalDateTime updatedAt`

    A timestamp in RFC 3339 format

    format: date-time

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

#### Example

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

`BetaUserProfileEnrollmentUrl beta().userProfiles().createEnrollmentUrl(params = UserProfileCreateEnrollmentUrlParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

#### Parameters

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

#### Returns

- `class BetaUserProfileEnrollmentUrl:`

  - `LocalDateTime expiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Type type`

    Object type. Always `enrollment_url`.

  - `String url`

    Enrollment URL to send to the end user. Valid until `expires_at`.

#### Example

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

`BetaDream beta().dreams().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/dreams`

Create a Dream

#### Parameters

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

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Model model`

    Model identifier and configuration applied to every pipeline stage.

    - `String`

    - `class BetaDreamModelConfigParam:`

      Model identifier and configuration applied to every pipeline stage.

      - `String id`

        Model identifier, e.g. "claude-opus-5". 1-256 characters.

        minLength: 1, maxLength: 256

      - `Optional<Speed> speed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `STANDARD("standard")`

        - `FAST("fast")`

  - `Optional<String> instructions`

    minLength: 1, maxLength: 4096

  - `Optional<BetaOutputBehavior> outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

`DreamListPage beta().dreams().list(params = DreamListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/dreams`

List Dreams

#### Parameters

- `DreamListParams params`

  - `Optional<LocalDateTime> createdAtGt`

    Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

    format: date-time

  - `Optional<LocalDateTime> createdAtLt`

    Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

    format: date-time

  - `Optional<Boolean> includeArchived`

    Query parameter for include_archived

  - `Optional<Long> limit`

    Query parameter for limit

    format: int32

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

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

`BetaDream beta().dreams().retrieve(params = DreamRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/dreams/{dream_id}`

Get a Dream

#### Parameters

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

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

`BetaDream beta().dreams().cancel(params = DreamCancelParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

#### Parameters

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

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

`BetaDream beta().dreams().archive(params = DreamArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/dreams/{dream_id}/archive`

Archive a Dream

#### Parameters

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

#### Returns

- `class BetaDream:`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `String id`

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> endedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<BetaDreamError> error`

    Failure detail for a Dream whose `status` is `failed`.

    - `String message`

    - `String type`

  - `List<BetaDreamInput> inputs`

    - `class BetaDreamMemoryStoreInput:`

      An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output_behavior {type: "update_existing"} the job consolidates this store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

    - `class BetaDreamSessionsInput:`

      Input session transcripts the dream reads.

      - `List<String> sessionIds`

      - `Type type`

  - `Optional<String> instructions`

  - `BetaDreamModelConfig model`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `String id`

      Model identifier, e.g. "claude-opus-5". 1-256 characters.

      minLength: 1, maxLength: 256

    - `Optional<Speed> speed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `STANDARD("standard")`

      - `FAST("fast")`

  - `BetaOutputBehavior outputBehavior`

    The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

    - `class BetaOutputBehaviorCreateNew:`

      The default destination: the job creates a new output memory store as a clone of the memory_store input and writes the consolidated memories into it. The input store is never mutated.

      - `Type type`

    - `class BetaOutputBehaviorUpdateExisting:`

      The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory_store input, so the job consolidates the store in place.

      - `String memoryStoreId`

        minLength: 1

      - `Type type`

  - `List<BetaDreamOutput> outputs`

    - `String memoryStoreId`

    - `Type type`

  - `Optional<String> sessionId`

  - `BetaDreamStatus status`

    Lifecycle status of a Dream.

    - `PENDING("pending")`

    - `RUNNING("running")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `CANCELED("canceled")`

  - `Type type`

  - `BetaDreamUsage usage`

    Cumulative token usage for the dream across every pipeline stage.

    - `long cacheCreationInputTokens`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      format: int32

    - `long cacheReadInputTokens`

      Total tokens read from prompt cache.

      format: int32

    - `long inputTokens`

      Total uncached input tokens consumed across every pipeline stage.

      format: int32

    - `long outputTokens`

      Total output tokens generated across every pipeline stage.

      format: int32

#### Example

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

`BetaTunnel beta().tunnels().create(params = TunnelCreateParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

#### Parameters

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

    minLength: 1, maxLength: 255

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue type constant`

#### Example

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

`BetaTunnel beta().tunnels().retrieve(params = TunnelRetrieveParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

#### Parameters

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

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue type constant`

#### Example

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

`TunnelListPage beta().tunnels().list(params = TunnelListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

#### Parameters

- `TunnelListParams params`

  - `Optional<Boolean> includeArchived`

    Whether to include archived tunnels in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

    format: int32

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

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue type constant`

#### Example

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

`BetaTunnel beta().tunnels().archive(params = TunnelArchiveParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

#### Parameters

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

#### Returns

- `class BetaTunnel:`

  An MCP tunnel.

  - `String id`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<String> displayName`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `String domain`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `JsonValue type constant`

#### Example

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

`BetaTunnelToken beta().tunnels().revealToken(params = TunnelRevealTokenParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

#### Parameters

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

#### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue type constant`

#### Example

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

##### Response (200)

```json
{
  "id": "id",
  "tunnel_token": "tunnel_token",
  "type": "tunnel_token"
}
```

### Rotate Tunnel Token

`BetaTunnelToken beta().tunnels().rotateToken(params = TunnelRotateTokenParams.none(), requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

#### Parameters

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

    maxLength: 1024

#### Returns

- `class BetaTunnelToken:`

  A tunnel's connector token.

  - `String id`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `String tunnelToken`

    The connector token used to run the tunnel. Treat as a credential.

  - `JsonValue type constant`

#### Example

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

`BetaTunnelCertificate beta().tunnels().certificates().create(params, requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

#### Parameters

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

    maxLength: 8192

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue type constant`

#### Example

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

`BetaTunnelCertificate beta().tunnels().certificates().retrieve(params, requestOptions = RequestOptions.none())`

**GET** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

#### Parameters

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

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue type constant`

#### Example

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

`CertificateListPage beta().tunnels().certificates().list(params = CertificateListParams.none(), requestOptions = RequestOptions.none())`

**GET** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

#### Parameters

- `CertificateListParams params`

  - `Optional<String> tunnelId`

  - `Optional<Boolean> includeArchived`

    Whether to include archived certificates in the results. Defaults to false.

  - `Optional<Long> limit`

    Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

    format: int32

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

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue type constant`

#### Example

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

`BetaTunnelCertificate beta().tunnels().certificates().archive(params, requestOptions = RequestOptions.none())`

**POST** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

#### Parameters

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

#### Returns

- `class BetaTunnelCertificate:`

  A CA certificate attached to a tunnel.

  - `String id`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `Optional<LocalDateTime> archivedAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `LocalDateTime createdAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `Optional<LocalDateTime> expiresAt`

    A timestamp in RFC 3339 format

    format: date-time

  - `String fingerprint`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `String tunnelId`

    ID of the tunnel the certificate is registered against.

  - `JsonValue type constant`

#### Example

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
