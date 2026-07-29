<!-- source: https://platform.claude.com/docs/en/api/go/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/go/beta -->

<!-- chunk-start -->

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `Type BetaManagedAgentsScheduleType`

      - `const BetaManagedAgentsScheduleTypeCron BetaManagedAgentsScheduleType = "cron"`

    - `LastRunAt Time`

      A timestamp in RFC 3339 format

    - `UpcomingRunsAt []Time`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `Status BetaManagedAgentsDeploymentStatus`

    Lifecycle status of a deployment.

    - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

    - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

  - `Type BetaManagedAgentsDeploymentType`

    - `const BetaManagedAgentsDeploymentTypeDeployment BetaManagedAgentsDeploymentType = "deployment"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultIDs []string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `type BetaManagedAgentsDeploymentInitialEventUnion interface{…}`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

    A user message sent to the session.

    - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

      Array of content blocks for the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsDeploymentUserMessageEventType`

      - `const BetaManagedAgentsDeploymentUserMessageEventTypeUserMessage BetaManagedAgentsDeploymentUserMessageEventType = "user.message"`

  - `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `Description string`

      What the agent should produce. This is the task specification.

    - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubric struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricType`

          - `const BetaManagedAgentsFileRubricTypeFile BetaManagedAgentsFileRubricType = "file"`

      - `type BetaManagedAgentsTextRubric struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `Type BetaManagedAgentsTextRubricType`

          - `const BetaManagedAgentsTextRubricTypeText BetaManagedAgentsTextRubricType = "text"`

    - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

      - `const BetaManagedAgentsDeploymentUserDefineOutcomeEventTypeUserDefineOutcome BetaManagedAgentsDeploymentUserDefineOutcomeEventType = "user.define_outcome"`

    - `MaxIterations int64`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsSystemContentBlockType`

        - `const BetaManagedAgentsSystemContentBlockTypeText BetaManagedAgentsSystemContentBlockType = "text"`

    - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

      - `const BetaManagedAgentsDeploymentSystemMessageEventTypeSystemMessage BetaManagedAgentsDeploymentSystemMessageEventType = "system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `type BetaManagedAgentsDeploymentInitialEventParamsUnionResp interface{…}`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `type BetaManagedAgentsUserMessageEventParams struct{…}`

    Parameters for sending a user message to the session.

    - `Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp`

      Array of content blocks for the user message.

      - `type BetaManagedAgentsTextBlock struct{…}`

        Regular text content.

        - `Text string`

          The text content.

        - `Type BetaManagedAgentsTextBlockType`

          - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

      - `type BetaManagedAgentsImageBlock struct{…}`

        Image content specified directly as base64 data or as a reference via a URL.

        - `Source BetaManagedAgentsImageBlockSourceUnion`

          Union type for image source variants.

          - `type BetaManagedAgentsBase64ImageSource struct{…}`

            Base64-encoded image data.

            - `Data string`

              Base64-encoded image data.

            - `MediaType string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `Type BetaManagedAgentsBase64ImageSourceType`

              - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

          - `type BetaManagedAgentsURLImageSource struct{…}`

            Image referenced by URL.

            - `Type BetaManagedAgentsURLImageSourceType`

              - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

            - `URL string`

              URL of the image to fetch.

          - `type BetaManagedAgentsFileImageSource struct{…}`

            Image referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileImageSourceType`

              - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

        - `Type BetaManagedAgentsImageBlockType`

          - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

      - `type BetaManagedAgentsDocumentBlock struct{…}`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `Source BetaManagedAgentsDocumentBlockSourceUnion`

          Union type for document source variants.

          - `type BetaManagedAgentsBase64DocumentSource struct{…}`

            Base64-encoded document data.

            - `Data string`

              Base64-encoded document data.

            - `MediaType string`

              MIME type of the document (e.g., "application/pdf").

            - `Type BetaManagedAgentsBase64DocumentSourceType`

              - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

          - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

            Plain text document content.

            - `Data string`

              The plain text content.

            - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

              MIME type of the text content. Must be "text/plain".

              - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

            - `Type BetaManagedAgentsPlainTextDocumentSourceType`

              - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

          - `type BetaManagedAgentsURLDocumentSource struct{…}`

            Document referenced by URL.

            - `Type BetaManagedAgentsURLDocumentSourceType`

              - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

            - `URL string`

              URL of the document to fetch.

          - `type BetaManagedAgentsFileDocumentSource struct{…}`

            Document referenced by file ID.

            - `FileID string`

              ID of a previously uploaded file.

            - `Type BetaManagedAgentsFileDocumentSourceType`

              - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

        - `Type BetaManagedAgentsDocumentBlockType`

          - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

        - `Context string`

          Additional context about the document for the model.

        - `Title string`

          The title of the document.

    - `Type BetaManagedAgentsUserMessageEventParamsType`

      - `const BetaManagedAgentsUserMessageEventParamsTypeUserMessage BetaManagedAgentsUserMessageEventParamsType = "user.message"`

  - `type BetaManagedAgentsUserDefineOutcomeEventParams struct{…}`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `Description string`

      What the agent should produce. This is the task specification.

    - `Rubric BetaManagedAgentsUserDefineOutcomeEventParamsRubricUnionResp`

      Rubric for grading the quality of an outcome.

      - `type BetaManagedAgentsFileRubricParams struct{…}`

        Rubric referenced by a file uploaded via the Files API.

        - `FileID string`

          ID of the rubric file.

        - `Type BetaManagedAgentsFileRubricParamsType`

          - `const BetaManagedAgentsFileRubricParamsTypeFile BetaManagedAgentsFileRubricParamsType = "file"`

      - `type BetaManagedAgentsTextRubricParams struct{…}`

        Rubric content provided inline as text.

        - `Content string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `Type BetaManagedAgentsTextRubricParamsType`

          - `const BetaManagedAgentsTextRubricParamsTypeText BetaManagedAgentsTextRubricParamsType = "text"`

    - `Type BetaManagedAgentsUserDefineOutcomeEventParamsType`

      - `const BetaManagedAgentsUserDefineOutcomeEventParamsTypeUserDefineOutcome BetaManagedAgentsUserDefineOutcomeEventParamsType = "user.define_outcome"`

    - `MaxIterations int64`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `type BetaManagedAgentsSystemMessageEventParamsResp struct{…}`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `Content []BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsSystemContentBlockType`

        - `const BetaManagedAgentsSystemContentBlockTypeText BetaManagedAgentsSystemContentBlockType = "text"`

    - `Type BetaManagedAgentsSystemMessageEventParamsType`

      - `const BetaManagedAgentsSystemMessageEventParamsTypeSystemMessage BetaManagedAgentsSystemMessageEventParamsType = "system.message"`

### Beta Managed Agents Deployment Paused Reason

- `type BetaManagedAgentsDeploymentPausedReasonUnion interface{…}`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

    The caller invoked the pause endpoint on the deployment.

    - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

      - `const BetaManagedAgentsManualDeploymentPausedReasonTypeManual BetaManagedAgentsManualDeploymentPausedReasonType = "manual"`

  - `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

        The deployment's environment was archived.

        - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType = "environment_archived_error"`

      - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

        The deployment's agent was archived.

        - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType = "agent_archived_error"`

      - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

        The deployment's environment no longer exists.

        - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType = "environment_not_found_error"`

      - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

        A vault referenced by the deployment no longer exists.

        - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType = "vault_not_found_error"`

      - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

        A file resource referenced by the deployment no longer exists.

        - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType = "file_not_found_error"`

      - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

        A referenced resource no longer exists and its kind was not reported.

        - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType = "session_resource_not_found_error"`

      - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

        The deployment's workspace was archived.

        - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType = "workspace_archived_error"`

      - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

        The deployment's organization is disabled.

        - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType = "organization_disabled_error"`

      - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

        A memory store referenced by the deployment is archived.

        - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType = "memory_store_archived_error"`

      - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

        A skill referenced by the deployment's agent no longer exists.

        - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType = "skill_not_found_error"`

      - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

        A vault referenced by the deployment is archived.

        - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType = "vault_archived_error"`

      - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsUnknownDeploymentPausedReasonErrorTypeUnknownError BetaManagedAgentsUnknownDeploymentPausedReasonErrorType = "unknown_error"`

      - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType = "self_hosted_resources_unsupported_error"`

      - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

          - `const BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType = "mcp_egress_blocked_error"`

    - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

      - `const BetaManagedAgentsErrorDeploymentPausedReasonTypeError BetaManagedAgentsErrorDeploymentPausedReasonType = "error"`

### Beta Managed Agents Deployment Paused Reason Error

- `type BetaManagedAgentsDeploymentPausedReasonErrorUnion interface{…}`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

    The deployment's environment was archived.

    - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType = "environment_archived_error"`

  - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

    The deployment's agent was archived.

    - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType = "agent_archived_error"`

  - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

    The deployment's environment no longer exists.

    - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType = "environment_not_found_error"`

  - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

    A vault referenced by the deployment no longer exists.

    - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType = "vault_not_found_error"`

  - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

    A file resource referenced by the deployment no longer exists.

    - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType = "file_not_found_error"`

  - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

    A referenced resource no longer exists and its kind was not reported.

    - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType = "session_resource_not_found_error"`

  - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

    The deployment's workspace was archived.

    - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType = "workspace_archived_error"`

  - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

    The deployment's organization is disabled.

    - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType = "organization_disabled_error"`

  - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

    A memory store referenced by the deployment is archived.

    - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType = "memory_store_archived_error"`

  - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

    A skill referenced by the deployment's agent no longer exists.

    - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType = "skill_not_found_error"`

  - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

    A vault referenced by the deployment is archived.

    - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType = "vault_archived_error"`

  - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsUnknownDeploymentPausedReasonErrorTypeUnknownError BetaManagedAgentsUnknownDeploymentPausedReasonErrorType = "unknown_error"`

  - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType = "self_hosted_resources_unsupported_error"`

  - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

      - `const BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType = "mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `type BetaManagedAgentsDeploymentStatus string`

  Lifecycle status of a deployment.

  - `const BetaManagedAgentsDeploymentStatusActive BetaManagedAgentsDeploymentStatus = "active"`

  - `const BetaManagedAgentsDeploymentStatusPaused BetaManagedAgentsDeploymentStatus = "paused"`

### Beta Managed Agents Deployment System Message Event

- `type BetaManagedAgentsDeploymentSystemMessageEvent struct{…}`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `Content []BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `Text string`

      The text content.

    - `Type BetaManagedAgentsSystemContentBlockType`

      - `const BetaManagedAgentsSystemContentBlockTypeText BetaManagedAgentsSystemContentBlockType = "text"`

  - `Type BetaManagedAgentsDeploymentSystemMessageEventType`

    - `const BetaManagedAgentsDeploymentSystemMessageEventTypeSystemMessage BetaManagedAgentsDeploymentSystemMessageEventType = "system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `type BetaManagedAgentsDeploymentUserDefineOutcomeEvent struct{…}`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `Description string`

    What the agent should produce. This is the task specification.

  - `Rubric BetaManagedAgentsDeploymentUserDefineOutcomeEventRubricUnion`

    Rubric for grading the quality of an outcome.

    - `type BetaManagedAgentsFileRubric struct{…}`

      Rubric referenced by a file uploaded via the Files API.

      - `FileID string`

        ID of the rubric file.

      - `Type BetaManagedAgentsFileRubricType`

        - `const BetaManagedAgentsFileRubricTypeFile BetaManagedAgentsFileRubricType = "file"`

    - `type BetaManagedAgentsTextRubric struct{…}`

      Rubric content provided inline as text.

      - `Content string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `Type BetaManagedAgentsTextRubricType`

        - `const BetaManagedAgentsTextRubricTypeText BetaManagedAgentsTextRubricType = "text"`

  - `Type BetaManagedAgentsDeploymentUserDefineOutcomeEventType`

    - `const BetaManagedAgentsDeploymentUserDefineOutcomeEventTypeUserDefineOutcome BetaManagedAgentsDeploymentUserDefineOutcomeEventType = "user.define_outcome"`

  - `MaxIterations int64`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `type BetaManagedAgentsDeploymentUserMessageEvent struct{…}`

  A user message sent to the session.

  - `Content []BetaManagedAgentsDeploymentUserMessageEventContentUnion`

    Array of content blocks for the user message.

    - `type BetaManagedAgentsTextBlock struct{…}`

      Regular text content.

      - `Text string`

        The text content.

      - `Type BetaManagedAgentsTextBlockType`

        - `const BetaManagedAgentsTextBlockTypeText BetaManagedAgentsTextBlockType = "text"`

    - `type BetaManagedAgentsImageBlock struct{…}`

      Image content specified directly as base64 data or as a reference via a URL.

      - `Source BetaManagedAgentsImageBlockSourceUnion`

        Union type for image source variants.

        - `type BetaManagedAgentsBase64ImageSource struct{…}`

          Base64-encoded image data.

          - `Data string`

            Base64-encoded image data.

          - `MediaType string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `Type BetaManagedAgentsBase64ImageSourceType`

            - `const BetaManagedAgentsBase64ImageSourceTypeBase64 BetaManagedAgentsBase64ImageSourceType = "base64"`

        - `type BetaManagedAgentsURLImageSource struct{…}`

          Image referenced by URL.

          - `Type BetaManagedAgentsURLImageSourceType`

            - `const BetaManagedAgentsURLImageSourceTypeURL BetaManagedAgentsURLImageSourceType = "url"`

          - `URL string`

            URL of the image to fetch.

        - `type BetaManagedAgentsFileImageSource struct{…}`

          Image referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

          - `Type BetaManagedAgentsFileImageSourceType`

            - `const BetaManagedAgentsFileImageSourceTypeFile BetaManagedAgentsFileImageSourceType = "file"`

      - `Type BetaManagedAgentsImageBlockType`

        - `const BetaManagedAgentsImageBlockTypeImage BetaManagedAgentsImageBlockType = "image"`

    - `type BetaManagedAgentsDocumentBlock struct{…}`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `Source BetaManagedAgentsDocumentBlockSourceUnion`

        Union type for document source variants.

        - `type BetaManagedAgentsBase64DocumentSource struct{…}`

          Base64-encoded document data.

          - `Data string`

            Base64-encoded document data.

          - `MediaType string`

            MIME type of the document (e.g., "application/pdf").

          - `Type BetaManagedAgentsBase64DocumentSourceType`

            - `const BetaManagedAgentsBase64DocumentSourceTypeBase64 BetaManagedAgentsBase64DocumentSourceType = "base64"`

        - `type BetaManagedAgentsPlainTextDocumentSource struct{…}`

          Plain text document content.

          - `Data string`

            The plain text content.

          - `MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType`

            MIME type of the text content. Must be "text/plain".

            - `const BetaManagedAgentsPlainTextDocumentSourceMediaTypeTextPlain BetaManagedAgentsPlainTextDocumentSourceMediaType = "text/plain"`

          - `Type BetaManagedAgentsPlainTextDocumentSourceType`

            - `const BetaManagedAgentsPlainTextDocumentSourceTypeText BetaManagedAgentsPlainTextDocumentSourceType = "text"`

        - `type BetaManagedAgentsURLDocumentSource struct{…}`

          Document referenced by URL.

          - `Type BetaManagedAgentsURLDocumentSourceType`

            - `const BetaManagedAgentsURLDocumentSourceTypeURL BetaManagedAgentsURLDocumentSourceType = "url"`

          - `URL string`

            URL of the document to fetch.

        - `type BetaManagedAgentsFileDocumentSource struct{…}`

          Document referenced by file ID.

          - `FileID string`

            ID of a previously uploaded file.

          - `Type BetaManagedAgentsFileDocumentSourceType`

            - `const BetaManagedAgentsFileDocumentSourceTypeFile BetaManagedAgentsFileDocumentSourceType = "file"`

      - `Type BetaManagedAgentsDocumentBlockType`

        - `const BetaManagedAgentsDocumentBlockTypeDocument BetaManagedAgentsDocumentBlockType = "document"`

      - `Context string`

        Additional context about the document for the model.

      - `Title string`

        The title of the document.

  - `Type BetaManagedAgentsDeploymentUserMessageEventType`

    - `const BetaManagedAgentsDeploymentUserMessageEventTypeUserMessage BetaManagedAgentsDeploymentUserMessageEventType = "user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

  The deployment's environment was archived.

  - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType = "environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

  The deployment's environment no longer exists.

  - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType = "environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `type BetaManagedAgentsErrorDeploymentPausedReason struct{…}`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `Error BetaManagedAgentsDeploymentPausedReasonErrorUnion`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError struct{…}`

      The deployment's environment was archived.

      - `Type BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonErrorType = "environment_archived_error"`

    - `type BetaManagedAgentsAgentArchivedDeploymentPausedReasonError struct{…}`

      The deployment's agent was archived.

      - `Type BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedDeploymentPausedReasonErrorType = "agent_archived_error"`

    - `type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError struct{…}`

      The deployment's environment no longer exists.

      - `Type BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonErrorType = "environment_not_found_error"`

    - `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType = "vault_not_found_error"`

    - `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType = "file_not_found_error"`

    - `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType = "session_resource_not_found_error"`

    - `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

      The deployment's workspace was archived.

      - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType = "workspace_archived_error"`

    - `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

      The deployment's organization is disabled.

      - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType = "organization_disabled_error"`

    - `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType = "memory_store_archived_error"`

    - `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType = "skill_not_found_error"`

    - `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

      A vault referenced by the deployment is archived.

      - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType = "vault_archived_error"`

    - `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsUnknownDeploymentPausedReasonErrorTypeUnknownError BetaManagedAgentsUnknownDeploymentPausedReasonErrorType = "unknown_error"`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType = "self_hosted_resources_unsupported_error"`

    - `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

        - `const BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType = "mcp_egress_blocked_error"`

  - `Type BetaManagedAgentsErrorDeploymentPausedReasonType`

    - `const BetaManagedAgentsErrorDeploymentPausedReasonTypeError BetaManagedAgentsErrorDeploymentPausedReasonType = "error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsFileNotFoundDeploymentPausedReasonError struct{…}`

  A file resource referenced by the deployment no longer exists.

  - `Type BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundDeploymentPausedReasonErrorType = "file_not_found_error"`

### Beta Managed Agents File Resource Config

- `type BetaManagedAgentsFileResourceConfig struct{…}`

  A file mounted into each session's container.

  - `FileID string`

    ID of a previously uploaded file.

  - `Type BetaManagedAgentsFileResourceConfigType`

    - `const BetaManagedAgentsFileResourceConfigTypeFile BetaManagedAgentsFileResourceConfigType = "file"`

  - `MountPath string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

    - `const BetaManagedAgentsGitHubRepositoryResourceConfigTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceConfigType = "github_repository"`

  - `URL string`

    Github URL of the repository

  - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `type BetaManagedAgentsBranchCheckout struct{…}`

      - `Name string`

        Branch name to check out.

      - `Type BetaManagedAgentsBranchCheckoutType`

        - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

    - `type BetaManagedAgentsCommitCheckout struct{…}`

      - `Sha string`

        Full commit SHA to check out.

      - `Type BetaManagedAgentsCommitCheckoutType`

        - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

  - `MountPath string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `type BetaManagedAgentsManualDeploymentPausedReason struct{…}`

  The caller invoked the pause endpoint on the deployment.

  - `Type BetaManagedAgentsManualDeploymentPausedReasonType`

    - `const BetaManagedAgentsManualDeploymentPausedReasonTypeManual BetaManagedAgentsManualDeploymentPausedReasonType = "manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonError struct{…}`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `Type BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedDeploymentPausedReasonErrorType = "mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonError struct{…}`

  A memory store referenced by the deployment is archived.

  - `Type BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedDeploymentPausedReasonErrorType = "memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

  A memory store attached to each session created from this deployment.

  - `MemoryStoreID string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

    - `const BetaManagedAgentsMemoryStoreResourceConfigTypeMemoryStore BetaManagedAgentsMemoryStoreResourceConfigType = "memory_store"`

  - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess`

    Access mode for an attached memory store.

    - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

    - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

  - `Instructions string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonError struct{…}`

  The deployment's organization is disabled.

  - `Type BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledDeploymentPausedReasonErrorType = "organization_disabled_error"`

### Beta Managed Agents Schedule

- `type BetaManagedAgentsSchedule struct{…}`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `Timezone string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `Type BetaManagedAgentsScheduleType`

    - `const BetaManagedAgentsScheduleTypeCron BetaManagedAgentsScheduleType = "cron"`

  - `LastRunAt Time`

    A timestamp in RFC 3339 format

  - `UpcomingRunsAt []Time`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `type BetaManagedAgentsScheduleParamsResp struct{…}`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `Expression string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `Timezone string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `Type BetaManagedAgentsScheduleParamsType`

    - `const BetaManagedAgentsScheduleParamsTypeCron BetaManagedAgentsScheduleParamsType = "cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonError struct{…}`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedDeploymentPausedReasonErrorType = "self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `type BetaManagedAgentsSessionResourceConfigUnion interface{…}`

  A configured session resource. Echoes the input minus write-only credentials.

  - `type BetaManagedAgentsGitHubRepositoryResourceConfig struct{…}`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `Type BetaManagedAgentsGitHubRepositoryResourceConfigType`

      - `const BetaManagedAgentsGitHubRepositoryResourceConfigTypeGitHubRepository BetaManagedAgentsGitHubRepositoryResourceConfigType = "github_repository"`

    - `URL string`

      Github URL of the repository

    - `Checkout BetaManagedAgentsGitHubRepositoryResourceConfigCheckoutUnion`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `type BetaManagedAgentsBranchCheckout struct{…}`

        - `Name string`

          Branch name to check out.

        - `Type BetaManagedAgentsBranchCheckoutType`

          - `const BetaManagedAgentsBranchCheckoutTypeBranch BetaManagedAgentsBranchCheckoutType = "branch"`

      - `type BetaManagedAgentsCommitCheckout struct{…}`

        - `Sha string`

          Full commit SHA to check out.

        - `Type BetaManagedAgentsCommitCheckoutType`

          - `const BetaManagedAgentsCommitCheckoutTypeCommit BetaManagedAgentsCommitCheckoutType = "commit"`

    - `MountPath string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `type BetaManagedAgentsFileResourceConfig struct{…}`

    A file mounted into each session's container.

    - `FileID string`

      ID of a previously uploaded file.

    - `Type BetaManagedAgentsFileResourceConfigType`

      - `const BetaManagedAgentsFileResourceConfigTypeFile BetaManagedAgentsFileResourceConfigType = "file"`

    - `MountPath string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `type BetaManagedAgentsMemoryStoreResourceConfig struct{…}`

    A memory store attached to each session created from this deployment.

    - `MemoryStoreID string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `Type BetaManagedAgentsMemoryStoreResourceConfigType`

      - `const BetaManagedAgentsMemoryStoreResourceConfigTypeMemoryStore BetaManagedAgentsMemoryStoreResourceConfigType = "memory_store"`

    - `Access BetaManagedAgentsMemoryStoreResourceConfigAccess`

      Access mode for an attached memory store.

      - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadWrite BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_write"`

      - `const BetaManagedAgentsMemoryStoreResourceConfigAccessReadOnly BetaManagedAgentsMemoryStoreResourceConfigAccess = "read_only"`

    - `Instructions string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonError struct{…}`

  A referenced resource no longer exists and its kind was not reported.

  - `Type BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundDeploymentPausedReasonErrorType = "session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonError struct{…}`

  A skill referenced by the deployment's agent no longer exists.

  - `Type BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundDeploymentPausedReasonErrorType = "skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `type BetaManagedAgentsUnknownDeploymentPausedReasonError struct{…}`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `Type BetaManagedAgentsUnknownDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsUnknownDeploymentPausedReasonErrorTypeUnknownError BetaManagedAgentsUnknownDeploymentPausedReasonErrorType = "unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `type BetaManagedAgentsVaultArchivedDeploymentPausedReasonError struct{…}`

  A vault referenced by the deployment is archived.

  - `Type BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedDeploymentPausedReasonErrorType = "vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonError struct{…}`

  A vault referenced by the deployment no longer exists.

  - `Type BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundDeploymentPausedReasonErrorType = "vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonError struct{…}`

  The deployment's workspace was archived.

  - `Type BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType`

    - `const BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedDeploymentPausedReasonErrorType = "workspace_archived_error"`

# Deployment Runs

## List Deployment Runs

`client.Beta.DeploymentRuns.List(ctx, params) (*PageCursor[BetaManagedAgentsDeploymentRun], error)`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `params BetaDeploymentRunListParams`

  - `CreatedAtGt param.Field[Time]`

    Query param: Return runs created strictly after this time (exclusive).

  - `CreatedAtGte param.Field[Time]`

    Query param: Return runs created at or after this time (inclusive).

  - `CreatedAtLt param.Field[Time]`

    Query param: Return runs created strictly before this time (exclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return runs created at or before this time (inclusive).

  - `DeploymentID param.Field[string]`

    Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

  - `HasError param.Field[bool]`

    Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

  - `Limit param.Field[int64]`

    Query param: Maximum results per page. Default 20, maximum 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

  - `TriggerType param.Field[BetaManagedAgentsTriggerType]`

    Query param: Filter runs by what triggered them. Omit to return all runs.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeploymentRun struct{…}`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `ID string`

    Unique identifier for this run (`drun_...`).

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

      - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

    - `Version int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DeploymentID string`

    ID of the deployment that produced this run.

  - `Error BetaManagedAgentsDeploymentRunErrorUnion`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

      The deployment's environment was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

        - `const BetaManagedAgentsEnvironmentArchivedRunErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedRunErrorType = "environment_archived_error"`

    - `type BetaManagedAgentsAgentArchivedRunError struct{…}`

      The deployment's agent was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsAgentArchivedRunErrorType`

        - `const BetaManagedAgentsAgentArchivedRunErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedRunErrorType = "agent_archived_error"`

    - `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

      The deployment's environment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

        - `const BetaManagedAgentsEnvironmentNotFoundRunErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundRunErrorType = "environment_not_found_error"`

    - `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

        - `const BetaManagedAgentsVaultNotFoundRunErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundRunErrorType = "vault_not_found_error"`

    - `type BetaManagedAgentsVaultArchivedRunError struct{…}`

      A vault referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultArchivedRunErrorType`

        - `const BetaManagedAgentsVaultArchivedRunErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedRunErrorType = "vault_archived_error"`

    - `type BetaManagedAgentsFileNotFoundRunError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsFileNotFoundRunErrorType`

        - `const BetaManagedAgentsFileNotFoundRunErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundRunErrorType = "file_not_found_error"`

    - `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

        - `const BetaManagedAgentsMemoryStoreArchivedRunErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedRunErrorType = "memory_store_archived_error"`

    - `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

        - `const BetaManagedAgentsSkillNotFoundRunErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundRunErrorType = "skill_not_found_error"`

    - `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

        - `const BetaManagedAgentsSessionResourceNotFoundRunErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundRunErrorType = "session_resource_not_found_error"`

    - `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

      The deployment's workspace was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

        - `const BetaManagedAgentsWorkspaceArchivedRunErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedRunErrorType = "workspace_archived_error"`

    - `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

      The deployment's organization is disabled.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

        - `const BetaManagedAgentsOrganizationDisabledRunErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledRunErrorType = "organization_disabled_error"`

    - `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

        - `const BetaManagedAgentsSessionRateLimitedRunErrorTypeSessionRateLimitedError BetaManagedAgentsSessionRateLimitedRunErrorType = "session_rate_limited_error"`

    - `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

      The session create request was rejected with a non-retryable validation error.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

        - `const BetaManagedAgentsSessionCreationRejectedRunErrorTypeSessionCreationRejectedError BetaManagedAgentsSessionCreationRejectedRunErrorType = "session_creation_rejected_error"`

    - `type BetaManagedAgentsUnknownRunError struct{…}`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsUnknownRunErrorType`

        - `const BetaManagedAgentsUnknownRunErrorTypeUnknownError BetaManagedAgentsUnknownRunErrorType = "unknown_error"`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

        - `const BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType = "self_hosted_resources_unsupported_error"`

    - `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

        - `const BetaManagedAgentsMCPEgressBlockedRunErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedRunErrorType = "mcp_egress_blocked_error"`

  - `SessionID string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `TriggerContext BetaManagedAgentsTriggerContextUnion`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

      The run was fired by the deployment's cron schedule.

      - `ScheduledAt Time`

        A timestamp in RFC 3339 format

      - `Type BetaManagedAgentsScheduleTriggerContextType`

        - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

    - `type BetaManagedAgentsManualTriggerContext struct{…}`

      The run was started manually by creating a session directly against the deployment.

      - `Type BetaManagedAgentsManualTriggerContextType`

        - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

  - `Type BetaManagedAgentsDeploymentRunType`

    - `const BetaManagedAgentsDeploymentRunTypeDeploymentRun BetaManagedAgentsDeploymentRunType = "deployment_run"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.DeploymentRuns.List(context.TODO(), anthropic.BetaDeploymentRunListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.DeploymentRuns.Get(ctx, deploymentRunID, query) (*BetaManagedAgentsDeploymentRun, error)`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `deploymentRunID string`

- `query BetaDeploymentRunGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeploymentRun struct{…}`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `ID string`

    Unique identifier for this run (`drun_...`).

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

      - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

    - `Version int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DeploymentID string`

    ID of the deployment that produced this run.

  - `Error BetaManagedAgentsDeploymentRunErrorUnion`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

      The deployment's environment was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

        - `const BetaManagedAgentsEnvironmentArchivedRunErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedRunErrorType = "environment_archived_error"`

    - `type BetaManagedAgentsAgentArchivedRunError struct{…}`

      The deployment's agent was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsAgentArchivedRunErrorType`

        - `const BetaManagedAgentsAgentArchivedRunErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedRunErrorType = "agent_archived_error"`

    - `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

      The deployment's environment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

        - `const BetaManagedAgentsEnvironmentNotFoundRunErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundRunErrorType = "environment_not_found_error"`

    - `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

        - `const BetaManagedAgentsVaultNotFoundRunErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundRunErrorType = "vault_not_found_error"`

    - `type BetaManagedAgentsVaultArchivedRunError struct{…}`

      A vault referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultArchivedRunErrorType`

        - `const BetaManagedAgentsVaultArchivedRunErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedRunErrorType = "vault_archived_error"`

    - `type BetaManagedAgentsFileNotFoundRunError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsFileNotFoundRunErrorType`

        - `const BetaManagedAgentsFileNotFoundRunErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundRunErrorType = "file_not_found_error"`

    - `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

        - `const BetaManagedAgentsMemoryStoreArchivedRunErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedRunErrorType = "memory_store_archived_error"`

    - `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

        - `const BetaManagedAgentsSkillNotFoundRunErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundRunErrorType = "skill_not_found_error"`

    - `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

        - `const BetaManagedAgentsSessionResourceNotFoundRunErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundRunErrorType = "session_resource_not_found_error"`

    - `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

      The deployment's workspace was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

        - `const BetaManagedAgentsWorkspaceArchivedRunErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedRunErrorType = "workspace_archived_error"`

    - `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

      The deployment's organization is disabled.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

        - `const BetaManagedAgentsOrganizationDisabledRunErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledRunErrorType = "organization_disabled_error"`

    - `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

        - `const BetaManagedAgentsSessionRateLimitedRunErrorTypeSessionRateLimitedError BetaManagedAgentsSessionRateLimitedRunErrorType = "session_rate_limited_error"`

    - `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

      The session create request was rejected with a non-retryable validation error.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

        - `const BetaManagedAgentsSessionCreationRejectedRunErrorTypeSessionCreationRejectedError BetaManagedAgentsSessionCreationRejectedRunErrorType = "session_creation_rejected_error"`

    - `type BetaManagedAgentsUnknownRunError struct{…}`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsUnknownRunErrorType`

        - `const BetaManagedAgentsUnknownRunErrorTypeUnknownError BetaManagedAgentsUnknownRunErrorType = "unknown_error"`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

        - `const BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType = "self_hosted_resources_unsupported_error"`

    - `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

        - `const BetaManagedAgentsMCPEgressBlockedRunErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedRunErrorType = "mcp_egress_blocked_error"`

  - `SessionID string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `TriggerContext BetaManagedAgentsTriggerContextUnion`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

      The run was fired by the deployment's cron schedule.

      - `ScheduledAt Time`

        A timestamp in RFC 3339 format

      - `Type BetaManagedAgentsScheduleTriggerContextType`

        - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

    - `type BetaManagedAgentsManualTriggerContext struct{…}`

      The run was started manually by creating a session directly against the deployment.

      - `Type BetaManagedAgentsManualTriggerContextType`

        - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

  - `Type BetaManagedAgentsDeploymentRunType`

    - `const BetaManagedAgentsDeploymentRunTypeDeploymentRun BetaManagedAgentsDeploymentRunType = "deployment_run"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsDeploymentRun, err := client.Beta.DeploymentRuns.Get(
    context.TODO(),
    "deployment_run_id",
    anthropic.BetaDeploymentRunGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeploymentRun.ID)
}
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

- `type BetaManagedAgentsAgentArchivedRunError struct{…}`

  The deployment's agent was archived.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsAgentArchivedRunErrorType`

    - `const BetaManagedAgentsAgentArchivedRunErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedRunErrorType = "agent_archived_error"`

### Beta Managed Agents Deployment Run

- `type BetaManagedAgentsDeploymentRun struct{…}`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `ID string`

    Unique identifier for this run (`drun_...`).

  - `Agent BetaManagedAgentsAgentReference`

    A resolved agent reference with a concrete version.

    - `ID string`

    - `Type BetaManagedAgentsAgentReferenceType`

      - `const BetaManagedAgentsAgentReferenceTypeAgent BetaManagedAgentsAgentReferenceType = "agent"`

    - `Version int64`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DeploymentID string`

    ID of the deployment that produced this run.

  - `Error BetaManagedAgentsDeploymentRunErrorUnion`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

      The deployment's environment was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

        - `const BetaManagedAgentsEnvironmentArchivedRunErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedRunErrorType = "environment_archived_error"`

    - `type BetaManagedAgentsAgentArchivedRunError struct{…}`

      The deployment's agent was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsAgentArchivedRunErrorType`

        - `const BetaManagedAgentsAgentArchivedRunErrorTypeAgentArchivedError BetaManagedAgentsAgentArchivedRunErrorType = "agent_archived_error"`

    - `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

      The deployment's environment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

        - `const BetaManagedAgentsEnvironmentNotFoundRunErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundRunErrorType = "environment_not_found_error"`

    - `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

      A vault referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

        - `const BetaManagedAgentsVaultNotFoundRunErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundRunErrorType = "vault_not_found_error"`

    - `type BetaManagedAgentsVaultArchivedRunError struct{…}`

      A vault referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsVaultArchivedRunErrorType`

        - `const BetaManagedAgentsVaultArchivedRunErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedRunErrorType = "vault_archived_error"`

    - `type BetaManagedAgentsFileNotFoundRunError struct{…}`

      A file resource referenced by the deployment no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsFileNotFoundRunErrorType`

        - `const BetaManagedAgentsFileNotFoundRunErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundRunErrorType = "file_not_found_error"`

    - `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

      A memory store referenced by the deployment is archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

        - `const BetaManagedAgentsMemoryStoreArchivedRunErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedRunErrorType = "memory_store_archived_error"`

    - `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

      A skill referenced by the deployment's agent no longer exists.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

        - `const BetaManagedAgentsSkillNotFoundRunErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundRunErrorType = "skill_not_found_error"`

    - `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

      A referenced resource no longer exists and its kind was not reported.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

        - `const BetaManagedAgentsSessionResourceNotFoundRunErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundRunErrorType = "session_resource_not_found_error"`

    - `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

      The deployment's workspace was archived.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

        - `const BetaManagedAgentsWorkspaceArchivedRunErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedRunErrorType = "workspace_archived_error"`

    - `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

      The deployment's organization is disabled.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

        - `const BetaManagedAgentsOrganizationDisabledRunErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledRunErrorType = "organization_disabled_error"`

    - `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

        - `const BetaManagedAgentsSessionRateLimitedRunErrorTypeSessionRateLimitedError BetaManagedAgentsSessionRateLimitedRunErrorType = "session_rate_limited_error"`

    - `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

      The session create request was rejected with a non-retryable validation error.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

        - `const BetaManagedAgentsSessionCreationRejectedRunErrorTypeSessionCreationRejectedError BetaManagedAgentsSessionCreationRejectedRunErrorType = "session_creation_rejected_error"`

    - `type BetaManagedAgentsUnknownRunError struct{…}`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsUnknownRunErrorType`

        - `const BetaManagedAgentsUnknownRunErrorTypeUnknownError BetaManagedAgentsUnknownRunErrorType = "unknown_error"`

    - `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

        - `const BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType = "self_hosted_resources_unsupported_error"`

    - `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `Message string`

        Human-readable error description.

      - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

        - `const BetaManagedAgentsMCPEgressBlockedRunErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedRunErrorType = "mcp_egress_blocked_error"`

  - `SessionID string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `TriggerContext BetaManagedAgentsTriggerContextUnion`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

      The run was fired by the deployment's cron schedule.

      - `ScheduledAt Time`

        A timestamp in RFC 3339 format

      - `Type BetaManagedAgentsScheduleTriggerContextType`

        - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

    - `type BetaManagedAgentsManualTriggerContext struct{…}`

      The run was started manually by creating a session directly against the deployment.

      - `Type BetaManagedAgentsManualTriggerContextType`

        - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

  - `Type BetaManagedAgentsDeploymentRunType`

    - `const BetaManagedAgentsDeploymentRunTypeDeploymentRun BetaManagedAgentsDeploymentRunType = "deployment_run"`

### Beta Managed Agents Environment Archived Run Error

- `type BetaManagedAgentsEnvironmentArchivedRunError struct{…}`

  The deployment's environment was archived.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsEnvironmentArchivedRunErrorType`

    - `const BetaManagedAgentsEnvironmentArchivedRunErrorTypeEnvironmentArchivedError BetaManagedAgentsEnvironmentArchivedRunErrorType = "environment_archived_error"`

### Beta Managed Agents Environment Not Found Run Error

- `type BetaManagedAgentsEnvironmentNotFoundRunError struct{…}`

  The deployment's environment no longer exists.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsEnvironmentNotFoundRunErrorType`

    - `const BetaManagedAgentsEnvironmentNotFoundRunErrorTypeEnvironmentNotFoundError BetaManagedAgentsEnvironmentNotFoundRunErrorType = "environment_not_found_error"`

### Beta Managed Agents File Not Found Run Error

- `type BetaManagedAgentsFileNotFoundRunError struct{…}`

  A file resource referenced by the deployment no longer exists.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsFileNotFoundRunErrorType`

    - `const BetaManagedAgentsFileNotFoundRunErrorTypeFileNotFoundError BetaManagedAgentsFileNotFoundRunErrorType = "file_not_found_error"`

### Beta Managed Agents Manual Trigger Context

- `type BetaManagedAgentsManualTriggerContext struct{…}`

  The run was started manually by creating a session directly against the deployment.

  - `Type BetaManagedAgentsManualTriggerContextType`

    - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

### Beta Managed Agents MCP Egress Blocked Run Error

- `type BetaManagedAgentsMCPEgressBlockedRunError struct{…}`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsMCPEgressBlockedRunErrorType`

    - `const BetaManagedAgentsMCPEgressBlockedRunErrorTypeMCPEgressBlockedError BetaManagedAgentsMCPEgressBlockedRunErrorType = "mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Run Error

- `type BetaManagedAgentsMemoryStoreArchivedRunError struct{…}`

  A memory store referenced by the deployment is archived.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsMemoryStoreArchivedRunErrorType`

    - `const BetaManagedAgentsMemoryStoreArchivedRunErrorTypeMemoryStoreArchivedError BetaManagedAgentsMemoryStoreArchivedRunErrorType = "memory_store_archived_error"`

### Beta Managed Agents Organization Disabled Run Error

- `type BetaManagedAgentsOrganizationDisabledRunError struct{…}`

  The deployment's organization is disabled.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsOrganizationDisabledRunErrorType`

    - `const BetaManagedAgentsOrganizationDisabledRunErrorTypeOrganizationDisabledError BetaManagedAgentsOrganizationDisabledRunErrorType = "organization_disabled_error"`

### Beta Managed Agents Schedule Trigger Context

- `type BetaManagedAgentsScheduleTriggerContext struct{…}`

  The run was fired by the deployment's cron schedule.

  - `ScheduledAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaManagedAgentsScheduleTriggerContextType`

    - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `type BetaManagedAgentsSelfHostedResourcesUnsupportedRunError struct{…}`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType`

    - `const BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorTypeSelfHostedResourcesUnsupportedError BetaManagedAgentsSelfHostedResourcesUnsupportedRunErrorType = "self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Creation Rejected Run Error

- `type BetaManagedAgentsSessionCreationRejectedRunError struct{…}`

  The session create request was rejected with a non-retryable validation error.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsSessionCreationRejectedRunErrorType`

    - `const BetaManagedAgentsSessionCreationRejectedRunErrorTypeSessionCreationRejectedError BetaManagedAgentsSessionCreationRejectedRunErrorType = "session_creation_rejected_error"`

### Beta Managed Agents Session Rate Limited Run Error

- `type BetaManagedAgentsSessionRateLimitedRunError struct{…}`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsSessionRateLimitedRunErrorType`

    - `const BetaManagedAgentsSessionRateLimitedRunErrorTypeSessionRateLimitedError BetaManagedAgentsSessionRateLimitedRunErrorType = "session_rate_limited_error"`

### Beta Managed Agents Session Resource Not Found Run Error

- `type BetaManagedAgentsSessionResourceNotFoundRunError struct{…}`

  A referenced resource no longer exists and its kind was not reported.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsSessionResourceNotFoundRunErrorType`

    - `const BetaManagedAgentsSessionResourceNotFoundRunErrorTypeSessionResourceNotFoundError BetaManagedAgentsSessionResourceNotFoundRunErrorType = "session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Run Error

- `type BetaManagedAgentsSkillNotFoundRunError struct{…}`

  A skill referenced by the deployment's agent no longer exists.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsSkillNotFoundRunErrorType`

    - `const BetaManagedAgentsSkillNotFoundRunErrorTypeSkillNotFoundError BetaManagedAgentsSkillNotFoundRunErrorType = "skill_not_found_error"`

### Beta Managed Agents Trigger Context

- `type BetaManagedAgentsTriggerContextUnion interface{…}`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `type BetaManagedAgentsScheduleTriggerContext struct{…}`

    The run was fired by the deployment's cron schedule.

    - `ScheduledAt Time`

      A timestamp in RFC 3339 format

    - `Type BetaManagedAgentsScheduleTriggerContextType`

      - `const BetaManagedAgentsScheduleTriggerContextTypeSchedule BetaManagedAgentsScheduleTriggerContextType = "schedule"`

  - `type BetaManagedAgentsManualTriggerContext struct{…}`

    The run was started manually by creating a session directly against the deployment.

    - `Type BetaManagedAgentsManualTriggerContextType`

      - `const BetaManagedAgentsManualTriggerContextTypeManual BetaManagedAgentsManualTriggerContextType = "manual"`

### Beta Managed Agents Trigger Type

- `type BetaManagedAgentsTriggerType string`

  What triggered a deployment run.

  - `const BetaManagedAgentsTriggerTypeSchedule BetaManagedAgentsTriggerType = "schedule"`

  - `const BetaManagedAgentsTriggerTypeManual BetaManagedAgentsTriggerType = "manual"`

### Beta Managed Agents Unknown Run Error

- `type BetaManagedAgentsUnknownRunError struct{…}`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsUnknownRunErrorType`

    - `const BetaManagedAgentsUnknownRunErrorTypeUnknownError BetaManagedAgentsUnknownRunErrorType = "unknown_error"`

### Beta Managed Agents Vault Archived Run Error

- `type BetaManagedAgentsVaultArchivedRunError struct{…}`

  A vault referenced by the deployment is archived.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsVaultArchivedRunErrorType`

    - `const BetaManagedAgentsVaultArchivedRunErrorTypeVaultArchivedError BetaManagedAgentsVaultArchivedRunErrorType = "vault_archived_error"`

### Beta Managed Agents Vault Not Found Run Error

- `type BetaManagedAgentsVaultNotFoundRunError struct{…}`

  A vault referenced by the deployment no longer exists.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsVaultNotFoundRunErrorType`

    - `const BetaManagedAgentsVaultNotFoundRunErrorTypeVaultNotFoundError BetaManagedAgentsVaultNotFoundRunErrorType = "vault_not_found_error"`

### Beta Managed Agents Workspace Archived Run Error

- `type BetaManagedAgentsWorkspaceArchivedRunError struct{…}`

  The deployment's workspace was archived.

  - `Message string`

    Human-readable error description.

  - `Type BetaManagedAgentsWorkspaceArchivedRunErrorType`

    - `const BetaManagedAgentsWorkspaceArchivedRunErrorTypeWorkspaceArchivedError BetaManagedAgentsWorkspaceArchivedRunErrorType = "workspace_archived_error"`

# Vaults

## Create Vault

`client.Beta.Vaults.New(ctx, params) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults`

Create Vault

### Parameters

- `params BetaVaultNewParams`

  - `DisplayName param.Field[string]`

    Body param: Human-readable name for the vault. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsVault, err := client.Beta.Vaults.New(context.TODO(), anthropic.BetaVaultNewParams{
    DisplayName: "Example vault",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
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

`client.Beta.Vaults.List(ctx, params) (*PageCursor[BetaManagedAgentsVault], error)`

**get** `/v1/vaults`

List Vaults

### Parameters

- `params BetaVaultListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived vaults in the results.

  - `Limit param.Field[int64]`

    Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination token from a previous `list_vaults` response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Vaults.List(context.TODO(), anthropic.BetaVaultListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Vaults.Get(ctx, vaultID, query) (*BetaManagedAgentsVault, error)`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `vaultID string`

- `query BetaVaultGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsVault, err := client.Beta.Vaults.Get(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
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

`client.Beta.Vaults.Update(ctx, vaultID, params) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `vaultID string`

- `params BetaVaultUpdateParams`

  - `DisplayName param.Field[string]`

    Body param: Updated human-readable name for the vault. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsVault, err := client.Beta.Vaults.Update(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
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

`client.Beta.Vaults.Delete(ctx, vaultID, body) (*BetaManagedAgentsDeletedVault, error)`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `vaultID string`

- `body BetaVaultDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeletedVault struct{…}`

  Confirmation of a deleted vault.

  - `ID string`

    Unique identifier of the deleted vault.

  - `Type BetaManagedAgentsDeletedVaultType`

    - `const BetaManagedAgentsDeletedVaultTypeVaultDeleted BetaManagedAgentsDeletedVaultType = "vault_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsDeletedVault, err := client.Beta.Vaults.Delete(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedVault.ID)
}
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`client.Beta.Vaults.Archive(ctx, vaultID, body) (*BetaManagedAgentsVault, error)`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `vaultID string`

- `body BetaVaultArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsVault, err := client.Beta.Vaults.Archive(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsVault.ID)
}
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

- `type BetaManagedAgentsDeletedVault struct{…}`

  Confirmation of a deleted vault.

  - `ID string`

    Unique identifier of the deleted vault.

  - `Type BetaManagedAgentsDeletedVaultType`

    - `const BetaManagedAgentsDeletedVaultTypeVaultDeleted BetaManagedAgentsDeletedVaultType = "vault_deleted"`

### Beta Managed Agents Vault

- `type BetaManagedAgentsVault struct{…}`

  A vault that stores credentials for use by agents during sessions.

  - `ID string`

    Unique identifier for the vault.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the vault.

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the vault.

  - `Type BetaManagedAgentsVaultType`

    - `const BetaManagedAgentsVaultTypeVault BetaManagedAgentsVaultType = "vault"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `vaultID string`

- `params BetaVaultCredentialNewParams`

  - `Auth param.Field[BetaVaultCredentialNewParamsAuthUnion]`

    Body param: Authentication details for creating a credential.

    - `type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}`

      Parameters for creating an MCP OAuth credential.

      - `AccessToken string`

        OAuth access token.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthCreateParamsType`

        - `const BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthCreateParamsType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshParamsResp`

        OAuth refresh token parameters for creating a credential with refresh support.

        - `ClientID string`

          OAuth client ID.

        - `RefreshToken string`

          OAuth refresh token.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `ClientSecret string`

              OAuth client secret.

            - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

              - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}`

      Parameters for creating a static bearer token credential.

      - `Token string`

        Static bearer token value.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerCreateParamsType`

        - `const BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer BetaManagedAgentsStaticBearerCreateParamsType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableCreateParamsResp struct{…}`

      Parameters for creating an environment variable credential.

      - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

      - `SecretName string`

        Name of the environment variable. Immutable after create.

      - `SecretValue string`

        Secret value. Write-only; never returned in responses.

      - `Type BetaManagedAgentsEnvironmentVariableCreateParamsType`

        - `const BetaManagedAgentsEnvironmentVariableCreateParamsTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableCreateParamsType = "environment_variable"`

      - `InjectionLocation BetaManagedAgentsInjectionLocationParamsResp`

        Where in the outbound request the secret value may be substituted.

        - `Body bool`

          Substitute when the placeholder appears in the request body.

        - `Header bool`

          Substitute when the placeholder appears in a request header value.

  - `DisplayName param.Field[string]`

    Body param: Human-readable name for the credential. Up to 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.New(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultCredentialNewParams{
      Auth: anthropic.BetaVaultCredentialNewParamsAuthUnion{
        OfStaticBearer: &anthropic.BetaManagedAgentsStaticBearerCreateParams{
          Token: "bearer_exampletoken",
          MCPServerURL: "https://example-server.modelcontextprotocol.io/sse",
          Type: anthropic.BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer,
        },
      },
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
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

`client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (*PageCursor[BetaManagedAgentsCredential], error)`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `vaultID string`

- `params BetaVaultCredentialListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived credentials in the results.

  - `Limit param.Field[int64]`

    Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

  - `Page param.Field[string]`

    Query param: Opaque pagination token from a previous `list_credentials` response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Vaults.Credentials.List(
    context.TODO(),
    "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    anthropic.BetaVaultCredentialListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Vaults.Credentials.Get(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialGetParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Get(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialGetParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
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

`client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialUpdateParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Auth param.Field[BetaVaultCredentialUpdateParamsAuthUnion]`

    Body param: Updated authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}`

      Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsMCPOAuthUpdateParamsType`

        - `const BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthUpdateParamsType = "mcp_oauth"`

      - `AccessToken string`

        Updated OAuth access token.

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp`

        Parameters for updating OAuth refresh token configuration.

        - `RefreshToken string`

          Updated OAuth refresh token.

        - `Scope string`

          Updated OAuth scope for the refresh request.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

          Updated HTTP Basic authentication parameters for the token endpoint.

          - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

            Updated HTTP Basic authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

            - `ClientSecret string`

              Updated OAuth client secret.

          - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

            Updated POST body authentication parameters for the token endpoint.

            - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

              - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

            - `ClientSecret string`

              Updated OAuth client secret.

    - `type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}`

      Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

      - `Type BetaManagedAgentsStaticBearerUpdateParamsType`

        - `const BetaManagedAgentsStaticBearerUpdateParamsTypeStaticBearer BetaManagedAgentsStaticBearerUpdateParamsType = "static_bearer"`

      - `Token string`

        Updated static bearer token value.

    - `type BetaManagedAgentsEnvironmentVariableUpdateParamsResp struct{…}`

      Parameters for updating an environment variable credential. `secret_name` is immutable.

      - `Type BetaManagedAgentsEnvironmentVariableUpdateParamsType`

        - `const BetaManagedAgentsEnvironmentVariableUpdateParamsTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableUpdateParamsType = "environment_variable"`

      - `InjectionLocation BetaManagedAgentsInjectionLocationUpdateParamsResp`

        Updated injection location.

        - `Body bool`

          Substitute when the placeholder appears in the request body.

        - `Header bool`

          Substitute when the placeholder appears in a request header value.

      - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

        Updated networking scope. Full replacement.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

          Substitute the secret only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

      - `SecretValue string`

        Updated secret value.

  - `DisplayName param.Field[string]`

    Body param: Updated human-readable name for the credential. 1-255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Update(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialUpdateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
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

`client.Beta.Vaults.Credentials.Delete(ctx, credentialID, params) (*BetaManagedAgentsDeletedCredential, error)`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialDeleteParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeletedCredential struct{…}`

  Confirmation of a deleted credential.

  - `ID string`

    Unique identifier of the deleted credential.

  - `Type BetaManagedAgentsDeletedCredentialType`

    - `const BetaManagedAgentsDeletedCredentialTypeVaultCredentialDeleted BetaManagedAgentsDeletedCredentialType = "vault_credential_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsDeletedCredential, err := client.Beta.Vaults.Credentials.Delete(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialDeleteParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedCredential.ID)
}
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`client.Beta.Vaults.Credentials.Archive(ctx, credentialID, params) (*BetaManagedAgentsCredential, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialArchiveParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsCredential, err := client.Beta.Vaults.Credentials.Archive(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialArchiveParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredential.ID)
}
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

`client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (*BetaManagedAgentsCredentialValidation, error)`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `credentialID string`

- `params BetaVaultCredentialMCPOAuthValidateParams`

  - `VaultID param.Field[string]`

    Path param: Path parameter vault_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsCredentialValidation struct{…}`

  Result of live-probing a credential against its configured MCP server.

  - `CredentialID string`

    Unique identifier of the credential that was validated.

  - `HasRefreshToken bool`

    Whether the credential has a refresh token configured.

  - `MCPProbe BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `Body string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `BodyTruncated bool`

        Whether `body` was truncated.

      - `ContentType string`

        Value of the `Content-Type` response header.

      - `StatusCode int64`

        HTTP status code.

    - `Method string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Refresh BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `Status BetaManagedAgentsRefreshObjectStatus`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"`

      - `const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"`

      - `const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect_error"`

      - `const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no_refresh_token"`

  - `Status BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `const BetaManagedAgentsCredentialValidationStatusValid BetaManagedAgentsCredentialValidationStatus = "valid"`

    - `const BetaManagedAgentsCredentialValidationStatusInvalid BetaManagedAgentsCredentialValidationStatus = "invalid"`

    - `const BetaManagedAgentsCredentialValidationStatusUnknown BetaManagedAgentsCredentialValidationStatus = "unknown"`

  - `Type BetaManagedAgentsCredentialValidationType`

    - `const BetaManagedAgentsCredentialValidationTypeVaultCredentialValidation BetaManagedAgentsCredentialValidationType = "vault_credential_validation"`

  - `ValidatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault containing the credential.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsCredentialValidation, err := client.Beta.Vaults.Credentials.MCPOAuthValidate(
    context.TODO(),
    "vcrd_011CZkZEMt8gZan2iYOQfSkw",
    anthropic.BetaVaultCredentialMCPOAuthValidateParams{
      VaultID: "vlt_011CZkZDLs7fYzm1hXNPeRjv",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsCredentialValidation.CredentialID)
}
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

- `type BetaManagedAgentsCredential struct{…}`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `ID string`

    Unique identifier for the credential.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Auth BetaManagedAgentsCredentialAuthUnion`

    Authentication details for a credential.

    - `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

      OAuth credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

        - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

      - `ExpiresAt Time`

        A timestamp in RFC 3339 format

      - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

        OAuth refresh token configuration returned in credential responses.

        - `ClientID string`

          OAuth client ID.

        - `TokenEndpoint string`

          Token endpoint URL used to refresh the access token.

        - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

          Token endpoint requires no client authentication.

          - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

            Token endpoint requires no client authentication.

            - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

          - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

          - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

            Token endpoint uses POST body authentication with client credentials.

            - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

              - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

        - `Resource string`

          OAuth resource indicator.

        - `Scope string`

          OAuth scope for the refresh request.

    - `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

      Static bearer token credential details for an MCP server.

      - `MCPServerURL string`

        URL of the MCP server this credential authenticates against.

      - `Type BetaManagedAgentsStaticBearerAuthResponseType`

        - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

    - `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

      Environment variable credential details. The secret value is never returned.

      - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

        Where in the outbound request the secret value is substituted.

        - `Body bool`

          Whether the placeholder is substituted in the request body.

        - `Header bool`

          Whether the placeholder is substituted in request header values.

      - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

        Outbound hosts the secret value is substituted on.

        - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

        - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

          The secret is substituted only on requests to the listed hosts.

          - `AllowedHosts []string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

            - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

      - `SecretName string`

        Name of the environment variable.

      - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

        - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata attached to the credential.

  - `Type BetaManagedAgentsCredentialType`

    - `const BetaManagedAgentsCredentialTypeVaultCredential BetaManagedAgentsCredentialType = "vault_credential"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault this credential belongs to.

  - `DisplayName string`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `type BetaManagedAgentsCredentialNetworkingParamsUnionResp interface{…}`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

      - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

  - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

    Substitute the secret only on requests to the listed hosts.

    - `AllowedHosts []string`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

      - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

### Beta Managed Agents Credential Validation

- `type BetaManagedAgentsCredentialValidation struct{…}`

  Result of live-probing a credential against its configured MCP server.

  - `CredentialID string`

    Unique identifier of the credential that was validated.

  - `HasRefreshToken bool`

    Whether the credential has a refresh token configured.

  - `MCPProbe BetaManagedAgentsMCPProbe`

    The failing step of an MCP validation probe.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

      - `Body string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `BodyTruncated bool`

        Whether `body` was truncated.

      - `ContentType string`

        Value of the `Content-Type` response header.

      - `StatusCode int64`

        HTTP status code.

    - `Method string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `Refresh BetaManagedAgentsRefreshObject`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

      An HTTP response captured during a credential validation probe.

    - `Status BetaManagedAgentsRefreshObjectStatus`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"`

      - `const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"`

      - `const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect_error"`

      - `const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no_refresh_token"`

  - `Status BetaManagedAgentsCredentialValidationStatus`

    Overall verdict of a credential validation probe.

    - `const BetaManagedAgentsCredentialValidationStatusValid BetaManagedAgentsCredentialValidationStatus = "valid"`

    - `const BetaManagedAgentsCredentialValidationStatusInvalid BetaManagedAgentsCredentialValidationStatus = "invalid"`

    - `const BetaManagedAgentsCredentialValidationStatusUnknown BetaManagedAgentsCredentialValidationStatus = "unknown"`

  - `Type BetaManagedAgentsCredentialValidationType`

    - `const BetaManagedAgentsCredentialValidationTypeVaultCredentialValidation BetaManagedAgentsCredentialValidationType = "vault_credential_validation"`

  - `ValidatedAt Time`

    A timestamp in RFC 3339 format

  - `VaultID string`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `type BetaManagedAgentsCredentialValidationStatus string`

  Overall verdict of a credential validation probe.

  - `const BetaManagedAgentsCredentialValidationStatusValid BetaManagedAgentsCredentialValidationStatus = "valid"`

  - `const BetaManagedAgentsCredentialValidationStatusInvalid BetaManagedAgentsCredentialValidationStatus = "invalid"`

  - `const BetaManagedAgentsCredentialValidationStatusUnknown BetaManagedAgentsCredentialValidationStatus = "unknown"`

### Beta Managed Agents Deleted Credential

- `type BetaManagedAgentsDeletedCredential struct{…}`

  Confirmation of a deleted credential.

  - `ID string`

    Unique identifier of the deleted credential.

  - `Type BetaManagedAgentsDeletedCredentialType`

    - `const BetaManagedAgentsDeletedCredentialTypeVaultCredentialDeleted BetaManagedAgentsDeletedCredentialType = "vault_credential_deleted"`

### Beta Managed Agents Environment Variable Auth Response

- `type BetaManagedAgentsEnvironmentVariableAuthResponse struct{…}`

  Environment variable credential details. The secret value is never returned.

  - `InjectionLocation BetaManagedAgentsInjectionLocationResponse`

    Where in the outbound request the secret value is substituted.

    - `Body bool`

      Whether the placeholder is substituted in the request body.

    - `Header bool`

      Whether the placeholder is substituted in request header values.

  - `Networking BetaManagedAgentsEnvironmentVariableAuthResponseNetworkingUnion`

    Outbound hosts the secret value is substituted on.

    - `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

        - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

    - `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

      The secret is substituted only on requests to the listed hosts.

      - `AllowedHosts []string`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

        - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

  - `SecretName string`

    Name of the environment variable.

  - `Type BetaManagedAgentsEnvironmentVariableAuthResponseType`

    - `const BetaManagedAgentsEnvironmentVariableAuthResponseTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableAuthResponseType = "environment_variable"`

### Beta Managed Agents Environment Variable Create Params

- `type BetaManagedAgentsEnvironmentVariableCreateParamsResp struct{…}`

  Parameters for creating an environment variable credential.

  - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

    Outbound hosts the secret value is substituted on.

    - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

        - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

    - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

      Substitute the secret only on requests to the listed hosts.

      - `AllowedHosts []string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

        - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

  - `SecretName string`

    Name of the environment variable. Immutable after create.

  - `SecretValue string`

    Secret value. Write-only; never returned in responses.

  - `Type BetaManagedAgentsEnvironmentVariableCreateParamsType`

    - `const BetaManagedAgentsEnvironmentVariableCreateParamsTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableCreateParamsType = "environment_variable"`

  - `InjectionLocation BetaManagedAgentsInjectionLocationParamsResp`

    Where in the outbound request the secret value may be substituted.

    - `Body bool`

      Substitute when the placeholder appears in the request body.

    - `Header bool`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `type BetaManagedAgentsEnvironmentVariableUpdateParamsResp struct{…}`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `Type BetaManagedAgentsEnvironmentVariableUpdateParamsType`

    - `const BetaManagedAgentsEnvironmentVariableUpdateParamsTypeEnvironmentVariable BetaManagedAgentsEnvironmentVariableUpdateParamsType = "environment_variable"`

  - `InjectionLocation BetaManagedAgentsInjectionLocationUpdateParamsResp`

    Updated injection location.

    - `Body bool`

      Substitute when the placeholder appears in the request body.

    - `Header bool`

      Substitute when the placeholder appears in a request header value.

  - `Networking BetaManagedAgentsCredentialNetworkingParamsUnionResp`

    Updated networking scope. Full replacement.

    - `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

        - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

    - `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

      Substitute the secret only on requests to the listed hosts.

      - `AllowedHosts []string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

        - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

  - `SecretValue string`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `type BetaManagedAgentsInjectionLocationParamsResp struct{…}`

  Where in the outbound request the secret value may be substituted.

  - `Body bool`

    Substitute when the placeholder appears in the request body.

  - `Header bool`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `type BetaManagedAgentsInjectionLocationResponse struct{…}`

  Where in the outbound request the secret value is substituted.

  - `Body bool`

    Whether the placeholder is substituted in the request body.

  - `Header bool`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `type BetaManagedAgentsInjectionLocationUpdateParamsResp struct{…}`

  Updated injection location.

  - `Body bool`

    Substitute when the placeholder appears in the request body.

  - `Header bool`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `type BetaManagedAgentsLimitedCredentialNetworkingParamsResp struct{…}`

  Substitute the secret only on requests to the listed hosts.

  - `AllowedHosts []string`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `Type BetaManagedAgentsLimitedCredentialNetworkingParamsType`

    - `const BetaManagedAgentsLimitedCredentialNetworkingParamsTypeLimited BetaManagedAgentsLimitedCredentialNetworkingParamsType = "limited"`

### Beta Managed Agents Limited Credential Networking Response

- `type BetaManagedAgentsLimitedCredentialNetworkingResponse struct{…}`

  The secret is substituted only on requests to the listed hosts.

  - `AllowedHosts []string`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `Type BetaManagedAgentsLimitedCredentialNetworkingResponseType`

    - `const BetaManagedAgentsLimitedCredentialNetworkingResponseTypeLimited BetaManagedAgentsLimitedCredentialNetworkingResponseType = "limited"`

### Beta Managed Agents MCP OAuth Auth Response

- `type BetaManagedAgentsMCPOAuthAuthResponse struct{…}`

  OAuth credential details for an MCP server.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsMCPOAuthAuthResponseType`

    - `const BetaManagedAgentsMCPOAuthAuthResponseTypeMCPOAuth BetaManagedAgentsMCPOAuthAuthResponseType = "mcp_oauth"`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshResponse`

    OAuth refresh token configuration returned in credential responses.

    - `ClientID string`

      OAuth client ID.

    - `TokenEndpoint string`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

      Token endpoint requires no client authentication.

      - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

        Token endpoint requires no client authentication.

        - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

      - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

      - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

        Token endpoint uses POST body authentication with client credentials.

        - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

          - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

    - `Resource string`

      OAuth resource indicator.

    - `Scope string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}`

  Parameters for creating an MCP OAuth credential.

  - `AccessToken string`

    OAuth access token.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsMCPOAuthCreateParamsType`

    - `const BetaManagedAgentsMCPOAuthCreateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthCreateParamsType = "mcp_oauth"`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshParamsResp`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `ClientID string`

      OAuth client ID.

    - `RefreshToken string`

      OAuth refresh token.

    - `TokenEndpoint string`

      Token endpoint URL used to refresh the access token.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

      Token endpoint requires no client authentication.

      - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

        Token endpoint requires no client authentication.

        - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

          - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

      - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `ClientSecret string`

          OAuth client secret.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

      - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

        Token endpoint uses POST body authentication with client credentials.

        - `ClientSecret string`

          OAuth client secret.

        - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

          - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

    - `Resource string`

      OAuth resource indicator.

    - `Scope string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `type BetaManagedAgentsMCPOAuthRefreshParamsResp struct{…}`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `ClientID string`

    OAuth client ID.

  - `RefreshToken string`

    OAuth refresh token.

  - `TokenEndpoint string`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp`

    Token endpoint requires no client authentication.

    - `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

      Token endpoint requires no client authentication.

      - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

        - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

    - `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `ClientSecret string`

        OAuth client secret.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

    - `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

      Token endpoint uses POST body authentication with client credentials.

      - `ClientSecret string`

        OAuth client secret.

      - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

        - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

  - `Resource string`

    OAuth resource indicator.

  - `Scope string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `type BetaManagedAgentsMCPOAuthRefreshResponse struct{…}`

  OAuth refresh token configuration returned in credential responses.

  - `ClientID string`

    OAuth client ID.

  - `TokenEndpoint string`

    Token endpoint URL used to refresh the access token.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion`

    Token endpoint requires no client authentication.

    - `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

      Token endpoint requires no client authentication.

      - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

    - `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

    - `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

      Token endpoint uses POST body authentication with client credentials.

      - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

        - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

  - `Resource string`

    OAuth resource indicator.

  - `Scope string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `type BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp struct{…}`

  Parameters for updating OAuth refresh token configuration.

  - `RefreshToken string`

    Updated OAuth refresh token.

  - `Scope string`

    Updated OAuth scope for the refresh request.

  - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

        - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

      - `ClientSecret string`

        Updated OAuth client secret.

    - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

      Updated POST body authentication parameters for the token endpoint.

      - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

        - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

      - `ClientSecret string`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `Type BetaManagedAgentsMCPOAuthUpdateParamsType`

    - `const BetaManagedAgentsMCPOAuthUpdateParamsTypeMCPOAuth BetaManagedAgentsMCPOAuthUpdateParamsType = "mcp_oauth"`

  - `AccessToken string`

    Updated OAuth access token.

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Refresh BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp`

    Parameters for updating OAuth refresh token configuration.

    - `RefreshToken string`

      Updated OAuth refresh token.

    - `Scope string`

      Updated OAuth scope for the refresh request.

    - `TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionResp`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

          - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

        - `ClientSecret string`

          Updated OAuth client secret.

      - `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

        Updated POST body authentication parameters for the token endpoint.

        - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

          - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

        - `ClientSecret string`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `type BetaManagedAgentsMCPProbe struct{…}`

  The failing step of an MCP validation probe.

  - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `Body string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `BodyTruncated bool`

      Whether `body` was truncated.

    - `ContentType string`

      Value of the `Content-Type` response header.

    - `StatusCode int64`

      HTTP status code.

  - `Method string`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `type BetaManagedAgentsRefreshHTTPResponse struct{…}`

  An HTTP response captured during a credential validation probe.

  - `Body string`

    Response body. May be truncated and has sensitive values scrubbed.

  - `BodyTruncated bool`

    Whether `body` was truncated.

  - `ContentType string`

    Value of the `Content-Type` response header.

  - `StatusCode int64`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `type BetaManagedAgentsRefreshObject struct{…}`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `HTTPResponse BetaManagedAgentsRefreshHTTPResponse`

    An HTTP response captured during a credential validation probe.

    - `Body string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `BodyTruncated bool`

      Whether `body` was truncated.

    - `ContentType string`

      Value of the `Content-Type` response header.

    - `StatusCode int64`

      HTTP status code.

  - `Status BetaManagedAgentsRefreshObjectStatus`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"`

    - `const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"`

    - `const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect_error"`

    - `const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `type BetaManagedAgentsStaticBearerAuthResponse struct{…}`

  Static bearer token credential details for an MCP server.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsStaticBearerAuthResponseType`

    - `const BetaManagedAgentsStaticBearerAuthResponseTypeStaticBearer BetaManagedAgentsStaticBearerAuthResponseType = "static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}`

  Parameters for creating a static bearer token credential.

  - `Token string`

    Static bearer token value.

  - `MCPServerURL string`

    URL of the MCP server this credential authenticates against.

  - `Type BetaManagedAgentsStaticBearerCreateParamsType`

    - `const BetaManagedAgentsStaticBearerCreateParamsTypeStaticBearer BetaManagedAgentsStaticBearerCreateParamsType = "static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `Type BetaManagedAgentsStaticBearerUpdateParamsType`

    - `const BetaManagedAgentsStaticBearerUpdateParamsTypeStaticBearer BetaManagedAgentsStaticBearerUpdateParamsType = "static_bearer"`

  - `Token string`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `ClientSecret string`

    OAuth client secret.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicParamType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicParamType = "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicResponseTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicResponseType = "client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType`

    - `const BetaManagedAgentsTokenEndpointAuthBasicUpdateParamTypeClientSecretBasic BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType = "client_secret_basic"`

  - `ClientSecret string`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}`

  Token endpoint requires no client authentication.

  - `Type BetaManagedAgentsTokenEndpointAuthNoneParamType`

    - `const BetaManagedAgentsTokenEndpointAuthNoneParamTypeNone BetaManagedAgentsTokenEndpointAuthNoneParamType = "none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}`

  Token endpoint requires no client authentication.

  - `Type BetaManagedAgentsTokenEndpointAuthNoneResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthNoneResponseTypeNone BetaManagedAgentsTokenEndpointAuthNoneResponseType = "none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}`

  Token endpoint uses POST body authentication with client credentials.

  - `ClientSecret string`

    OAuth client secret.

  - `Type BetaManagedAgentsTokenEndpointAuthPostParamType`

    - `const BetaManagedAgentsTokenEndpointAuthPostParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostParamType = "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}`

  Token endpoint uses POST body authentication with client credentials.

  - `Type BetaManagedAgentsTokenEndpointAuthPostResponseType`

    - `const BetaManagedAgentsTokenEndpointAuthPostResponseTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostResponseType = "client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}`

  Updated POST body authentication parameters for the token endpoint.

  - `Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType`

    - `const BetaManagedAgentsTokenEndpointAuthPostUpdateParamTypeClientSecretPost BetaManagedAgentsTokenEndpointAuthPostUpdateParamType = "client_secret_post"`

  - `ClientSecret string`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsResp struct{…}`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType`

    - `const BetaManagedAgentsUnrestrictedCredentialNetworkingParamsTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingParamsType = "unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `type BetaManagedAgentsUnrestrictedCredentialNetworkingResponse struct{…}`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `Type BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType`

    - `const BetaManagedAgentsUnrestrictedCredentialNetworkingResponseTypeUnrestricted BetaManagedAgentsUnrestrictedCredentialNetworkingResponseType = "unrestricted"`

# Memory Stores

## Create a memory store

`client.Beta.MemoryStores.New(ctx, params) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `params BetaMemoryStoreNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

  - `Description param.Field[string]`

    Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

  - `Metadata param.Field[map[string, string]]`

    Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.New(context.TODO(), anthropic.BetaMemoryStoreNewParams{
    Name: "x",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
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

`client.Beta.MemoryStores.List(ctx, params) (*PageCursor[BetaManagedAgentsMemoryStore], error)`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `params BetaMemoryStoreListParams`

  - `CreatedAtGte param.Field[Time]`

    Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

  - `CreatedAtLte param.Field[Time]`

    Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

  - `IncludeArchived param.Field[bool]`

    Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

  - `Limit param.Field[int64]`

    Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.MemoryStores.List(context.TODO(), anthropic.BetaMemoryStoreListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (*BetaManagedAgentsMemoryStore, error)`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `memoryStoreID string`

- `query BetaMemoryStoreGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Get(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
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

`client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreUpdateParams`

  - `Description param.Field[string]`

    Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

  - `Metadata param.Field[map[string, string]]`

    Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

  - `Name param.Field[string]`

    Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Update(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
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

`client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (*BetaManagedAgentsDeletedMemoryStore, error)`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `memoryStoreID string`

- `body BetaMemoryStoreDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeletedMemoryStore struct{…}`

  Confirmation that a `memory_store` was deleted.

  - `ID string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type BetaManagedAgentsDeletedMemoryStoreType`

    - `const BetaManagedAgentsDeletedMemoryStoreTypeMemoryStoreDeleted BetaManagedAgentsDeletedMemoryStoreType = "memory_store_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsDeletedMemoryStore, err := client.Beta.MemoryStores.Delete(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedMemoryStore.ID)
}
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (*BetaManagedAgentsMemoryStore, error)`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `memoryStoreID string`

- `body BetaMemoryStoreArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryStore, err := client.Beta.MemoryStores.Archive(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryStore.ID)
}
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

- `type BetaManagedAgentsDeletedMemoryStore struct{…}`

  Confirmation that a `memory_store` was deleted.

  - `ID string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `Type BetaManagedAgentsDeletedMemoryStoreType`

    - `const BetaManagedAgentsDeletedMemoryStoreTypeMemoryStoreDeleted BetaManagedAgentsDeletedMemoryStoreType = "memory_store_deleted"`

### Beta Managed Agents Memory Store

- `type BetaManagedAgentsMemoryStore struct{…}`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `ID string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Name string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `Type BetaManagedAgentsMemoryStoreType`

    - `const BetaManagedAgentsMemoryStoreTypeMemoryStore BetaManagedAgentsMemoryStoreType = "memory_store"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `Description string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `Metadata map[string, string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (*BetaManagedAgentsMemory, error)`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryNewParams`

  - `Content param.Field[string]`

    Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

  - `Path param.Field[string]`

    Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemory struct{…}`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `ID string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `ContentSizeBytes int64`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `MemoryVersionID string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `Path string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.New(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryNewParams{
      Content: anthropic.String("content"),
      Path: "xx",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
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

`client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (*PageCursor[BetaManagedAgentsMemoryListItemUnion], error)`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryListParams`

  - `Depth param.Field[int64]`

    Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

  - `Limit param.Field[int64]`

    Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

  - `PathPrefix param.Field[string]`

    Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryListItemUnion interface{…}`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `type BetaManagedAgentsMemory struct{…}`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `ID string`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `ContentSha256 string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `ContentSizeBytes int64`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MemoryStoreID string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `MemoryVersionID string`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `Path string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type BetaManagedAgentsMemoryType`

      - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `Content string`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `type BetaManagedAgentsMemoryPrefix struct{…}`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `Path string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type BetaManagedAgentsMemoryPrefixType`

      - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.MemoryStores.Memories.List(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (*BetaManagedAgentsMemory, error)`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryGetParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemory struct{…}`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `ID string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `ContentSizeBytes int64`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `MemoryVersionID string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `Path string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.Get(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryGetParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
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

`client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (*BetaManagedAgentsMemory, error)`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryUpdateParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Content param.Field[string]`

    Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

  - `Path param.Field[string]`

    Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

  - `Precondition param.Field[BetaManagedAgentsPrecondition]`

    Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemory struct{…}`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `ID string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `ContentSizeBytes int64`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `MemoryVersionID string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `Path string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemory, err := client.Beta.MemoryStores.Memories.Update(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryUpdateParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemory.ID)
}
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

`client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (*BetaManagedAgentsDeletedMemory, error)`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `memoryID string`

- `params BetaMemoryStoreMemoryDeleteParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `ExpectedContentSha256 param.Field[string]`

    Query param: Query parameter for expected_content_sha256

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsDeletedMemory struct{…}`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `ID string`

    ID of the deleted memory (a `mem_...` value).

  - `Type BetaManagedAgentsDeletedMemoryType`

    - `const BetaManagedAgentsDeletedMemoryTypeMemoryDeleted BetaManagedAgentsDeletedMemoryType = "memory_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsDeletedMemory, err := client.Beta.MemoryStores.Memories.Delete(
    context.TODO(),
    "memory_id",
    anthropic.BetaMemoryStoreMemoryDeleteParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsDeletedMemory.ID)
}
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

- `type BetaManagedAgentsConflictError struct{…}`

  - `Type BetaManagedAgentsConflictErrorType`

    - `const BetaManagedAgentsConflictErrorTypeConflictError BetaManagedAgentsConflictErrorType = "conflict_error"`

  - `Message string`

### Beta Managed Agents Content Sha256 Precondition

- `type BetaManagedAgentsContentSha256Precondition struct{…}`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `Type BetaManagedAgentsContentSha256PreconditionType`

    - `const BetaManagedAgentsContentSha256PreconditionTypeContentSha256 BetaManagedAgentsContentSha256PreconditionType = "content_sha256"`

  - `ContentSha256 string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `type BetaManagedAgentsDeletedMemory struct{…}`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `ID string`

    ID of the deleted memory (a `mem_...` value).

  - `Type BetaManagedAgentsDeletedMemoryType`

    - `const BetaManagedAgentsDeletedMemoryTypeMemoryDeleted BetaManagedAgentsDeletedMemoryType = "memory_deleted"`

### Beta Managed Agents Error

- `type BetaManagedAgentsErrorUnion interface{…}`

  - `type BetaInvalidRequestError struct{…}`

    - `Message string`

    - `Type InvalidRequestError`

      - `const InvalidRequestErrorInvalidRequestError InvalidRequestError = "invalid_request_error"`

  - `type BetaAuthenticationError struct{…}`

    - `Message string`

    - `Type AuthenticationError`

      - `const AuthenticationErrorAuthenticationError AuthenticationError = "authentication_error"`

  - `type BetaBillingError struct{…}`

    - `Message string`

    - `Type BillingError`

      - `const BillingErrorBillingError BillingError = "billing_error"`

  - `type BetaPermissionError struct{…}`

    - `Message string`

    - `Type PermissionError`

      - `const PermissionErrorPermissionError PermissionError = "permission_error"`

  - `type BetaNotFoundError struct{…}`

    - `Message string`

    - `Type NotFoundError`

      - `const NotFoundErrorNotFoundError NotFoundError = "not_found_error"`

  - `type BetaRateLimitError struct{…}`

    - `Message string`

    - `Type RateLimitError`

      - `const RateLimitErrorRateLimitError RateLimitError = "rate_limit_error"`

  - `type BetaGatewayTimeoutError struct{…}`

    - `Message string`

    - `Type TimeoutError`

      - `const TimeoutErrorTimeoutError TimeoutError = "timeout_error"`

  - `type BetaAPIError struct{…}`

    - `Message string`

    - `Type APIError`

      - `const APIErrorAPIError APIError = "api_error"`

  - `type BetaOverloadedError struct{…}`

    - `Message string`

    - `Type OverloadedError`

      - `const OverloadedErrorOverloadedError OverloadedError = "overloaded_error"`

  - `type BetaManagedAgentsMemoryPreconditionFailedError struct{…}`

    - `Type BetaManagedAgentsMemoryPreconditionFailedErrorType`

      - `const BetaManagedAgentsMemoryPreconditionFailedErrorTypeMemoryPreconditionFailedError BetaManagedAgentsMemoryPreconditionFailedErrorType = "memory_precondition_failed_error"`

    - `Message string`

  - `type BetaManagedAgentsMemoryPathConflictError struct{…}`

    - `Type BetaManagedAgentsMemoryPathConflictErrorType`

      - `const BetaManagedAgentsMemoryPathConflictErrorTypeMemoryPathConflictError BetaManagedAgentsMemoryPathConflictErrorType = "memory_path_conflict_error"`

    - `ConflictingMemoryID string`

    - `ConflictingPath string`

    - `Message string`

  - `type BetaManagedAgentsConflictError struct{…}`

    - `Type BetaManagedAgentsConflictErrorType`

      - `const BetaManagedAgentsConflictErrorTypeConflictError BetaManagedAgentsConflictErrorType = "conflict_error"`

    - `Message string`

### Beta Managed Agents Memory

- `type BetaManagedAgentsMemory struct{…}`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `ID string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `ContentSizeBytes int64`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryStoreID string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `MemoryVersionID string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `Path string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `Type BetaManagedAgentsMemoryType`

    - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `Content string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `type BetaManagedAgentsMemoryListItemUnion interface{…}`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `type BetaManagedAgentsMemory struct{…}`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `ID string`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `ContentSha256 string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `ContentSizeBytes int64`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `CreatedAt Time`

      A timestamp in RFC 3339 format

    - `MemoryStoreID string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `MemoryVersionID string`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `Path string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `Type BetaManagedAgentsMemoryType`

      - `const BetaManagedAgentsMemoryTypeMemory BetaManagedAgentsMemoryType = "memory"`

    - `UpdatedAt Time`

      A timestamp in RFC 3339 format

    - `Content string`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `type BetaManagedAgentsMemoryPrefix struct{…}`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `Path string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `Type BetaManagedAgentsMemoryPrefixType`

      - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `type BetaManagedAgentsMemoryPathConflictError struct{…}`

  - `Type BetaManagedAgentsMemoryPathConflictErrorType`

    - `const BetaManagedAgentsMemoryPathConflictErrorTypeMemoryPathConflictError BetaManagedAgentsMemoryPathConflictErrorType = "memory_path_conflict_error"`

  - `ConflictingMemoryID string`

  - `ConflictingPath string`

  - `Message string`

### Beta Managed Agents Memory Precondition Failed Error

- `type BetaManagedAgentsMemoryPreconditionFailedError struct{…}`

  - `Type BetaManagedAgentsMemoryPreconditionFailedErrorType`

    - `const BetaManagedAgentsMemoryPreconditionFailedErrorTypeMemoryPreconditionFailedError BetaManagedAgentsMemoryPreconditionFailedErrorType = "memory_precondition_failed_error"`

  - `Message string`

### Beta Managed Agents Memory Prefix

- `type BetaManagedAgentsMemoryPrefix struct{…}`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `Path string`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `Type BetaManagedAgentsMemoryPrefixType`

    - `const BetaManagedAgentsMemoryPrefixTypeMemoryPrefix BetaManagedAgentsMemoryPrefixType = "memory_prefix"`

### Beta Managed Agents Memory View

- `type BetaManagedAgentsMemoryView string`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `const BetaManagedAgentsMemoryViewBasic BetaManagedAgentsMemoryView = "basic"`

  - `const BetaManagedAgentsMemoryViewFull BetaManagedAgentsMemoryView = "full"`

### Beta Managed Agents Precondition

- `type BetaManagedAgentsPrecondition struct{…}`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `Type BetaManagedAgentsPreconditionType`

    - `const BetaManagedAgentsPreconditionTypeContentSha256 BetaManagedAgentsPreconditionType = "content_sha256"`

  - `ContentSha256 string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (*PageCursor[BetaManagedAgentsMemoryVersion], error)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `memoryStoreID string`

- `params BetaMemoryStoreMemoryVersionListParams`

  - `APIKeyID param.Field[string]`

    Query param: Query parameter for api_key_id

  - `CreatedAtGte param.Field[Time]`

    Query param: Return versions created at or after this time (inclusive).

  - `CreatedAtLte param.Field[Time]`

    Query param: Return versions created at or before this time (inclusive).

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `MemoryID param.Field[string]`

    Query param: Query parameter for memory_id

  - `Operation param.Field[BetaManagedAgentsMemoryVersionOperation]`

    Query param: Query parameter for operation

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `SessionID param.Field[string]`

    Query param: Query parameter for session_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryVersion struct{…}`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `CreatedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

  - `Path string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.MemoryStores.MemoryVersions.List(
    context.TODO(),
    "memory_store_id",
    anthropic.BetaMemoryStoreMemoryVersionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `memoryVersionID string`

- `params BetaMemoryStoreMemoryVersionGetParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `View param.Field[BetaManagedAgentsMemoryView]`

    Query param: Query parameter for view

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryVersion struct{…}`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `CreatedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

  - `Path string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Get(
    context.TODO(),
    "memory_version_id",
    anthropic.BetaMemoryStoreMemoryVersionGetParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
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

`client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (*BetaManagedAgentsMemoryVersion, error)`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `memoryVersionID string`

- `params BetaMemoryStoreMemoryVersionRedactParams`

  - `MemoryStoreID param.Field[string]`

    Path param: Path parameter memory_store_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaManagedAgentsMemoryVersion struct{…}`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `CreatedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

  - `Path string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsMemoryVersion, err := client.Beta.MemoryStores.MemoryVersions.Redact(
    context.TODO(),
    "memory_version_id",
    anthropic.BetaMemoryStoreMemoryVersionRedactParams{
      MemoryStoreID: "memory_store_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsMemoryVersion.ID)
}
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

- `type BetaManagedAgentsActorUnion interface{…}`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `type BetaManagedAgentsSessionActor struct{…}`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `SessionID string`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `Type BetaManagedAgentsSessionActorType`

      - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

  - `type BetaManagedAgentsAPIActor struct{…}`

    Attribution for a write made directly via the public API (outside of any session).

    - `APIKeyID string`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `Type BetaManagedAgentsAPIActorType`

      - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

  - `type BetaManagedAgentsUserActor struct{…}`

    Attribution for a write made by a human user through the Anthropic Console.

    - `Type BetaManagedAgentsUserActorType`

      - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

    - `UserID string`

      ID of the user who performed the write (a `user_...` value).

### Beta Managed Agents API Actor

- `type BetaManagedAgentsAPIActor struct{…}`

  Attribution for a write made directly via the public API (outside of any session).

  - `APIKeyID string`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `Type BetaManagedAgentsAPIActorType`

    - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

### Beta Managed Agents Memory Version

- `type BetaManagedAgentsMemoryVersion struct{…}`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `ID string`

    Unique identifier for this version (a `memver_...` value).

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `MemoryID string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `MemoryStoreID string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `Operation BetaManagedAgentsMemoryVersionOperation`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

    - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

    - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

  - `Type BetaManagedAgentsMemoryVersionType`

    - `const BetaManagedAgentsMemoryVersionTypeMemoryVersion BetaManagedAgentsMemoryVersionType = "memory_version"`

  - `Content string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `ContentSha256 string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `ContentSizeBytes int64`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `CreatedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `type BetaManagedAgentsSessionActor struct{…}`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `SessionID string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `Type BetaManagedAgentsSessionActorType`

        - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

    - `type BetaManagedAgentsAPIActor struct{…}`

      Attribution for a write made directly via the public API (outside of any session).

      - `APIKeyID string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `Type BetaManagedAgentsAPIActorType`

        - `const BetaManagedAgentsAPIActorTypeAPIActor BetaManagedAgentsAPIActorType = "api_actor"`

    - `type BetaManagedAgentsUserActor struct{…}`

      Attribution for a write made by a human user through the Anthropic Console.

      - `Type BetaManagedAgentsUserActorType`

        - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

      - `UserID string`

        ID of the user who performed the write (a `user_...` value).

  - `Path string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `RedactedAt Time`

    A timestamp in RFC 3339 format

  - `RedactedBy BetaManagedAgentsActorUnion`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

### Beta Managed Agents Memory Version Operation

- `type BetaManagedAgentsMemoryVersionOperation string`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `const BetaManagedAgentsMemoryVersionOperationCreated BetaManagedAgentsMemoryVersionOperation = "created"`

  - `const BetaManagedAgentsMemoryVersionOperationModified BetaManagedAgentsMemoryVersionOperation = "modified"`

  - `const BetaManagedAgentsMemoryVersionOperationDeleted BetaManagedAgentsMemoryVersionOperation = "deleted"`

### Beta Managed Agents Session Actor

- `type BetaManagedAgentsSessionActor struct{…}`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `SessionID string`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `Type BetaManagedAgentsSessionActorType`

    - `const BetaManagedAgentsSessionActorTypeSessionActor BetaManagedAgentsSessionActorType = "session_actor"`

### Beta Managed Agents User Actor

- `type BetaManagedAgentsUserActor struct{…}`

  Attribution for a write made by a human user through the Anthropic Console.

  - `Type BetaManagedAgentsUserActorType`

    - `const BetaManagedAgentsUserActorTypeUserActor BetaManagedAgentsUserActorType = "user_actor"`

  - `UserID string`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`client.Beta.Files.Upload(ctx, params) (*FileMetadata, error)`

**post** `/v1/files`

Upload File

### Parameters

- `params BetaFileUploadParams`

  - `File param.Field[Reader]`

    Body param: The file to upload

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type FileMetadata struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `CreatedAt Time`

    RFC 3339 datetime string representing when the file was created.

  - `Filename string`

    Original filename of the uploaded file.

  - `MimeType string`

    MIME type of the file.

  - `SizeBytes int64`

    Size of the file in bytes.

  - `Type File`

    Object type.

    For files, this is always `"file"`.

    - `const FileFile File = "file"`

  - `Downloadable bool`

    Whether the file can be downloaded.

  - `Scope BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `ID string`

      The ID of the scoping resource (e.g., the session ID).

    - `Type Session`

      The type of scope (e.g., `"session"`).

      - `const SessionSession Session = "session"`

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  fileMetadata, err := client.Beta.Files.Upload(context.TODO(), anthropic.BetaFileUploadParams{
    File: io.Reader(bytes.NewBuffer([]byte("Example data"))),
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fileMetadata.ID)
}
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

`client.Beta.Files.List(ctx, params) (*Page[FileMetadata], error)`

**get** `/v1/files`

List Files

### Parameters

- `params BetaFileListParams`

  - `AfterID param.Field[string]`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

  - `BeforeID param.Field[string]`

    Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

  - `Limit param.Field[int64]`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `ScopeID param.Field[string]`

    Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type FileMetadata struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `CreatedAt Time`

    RFC 3339 datetime string representing when the file was created.

  - `Filename string`

    Original filename of the uploaded file.

  - `MimeType string`

    MIME type of the file.

  - `SizeBytes int64`

    Size of the file in bytes.

  - `Type File`

    Object type.

    For files, this is always `"file"`.

    - `const FileFile File = "file"`

  - `Downloadable bool`

    Whether the file can be downloaded.

  - `Scope BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `ID string`

      The ID of the scoping resource (e.g., the session ID).

    - `Type Session`

      The type of scope (e.g., `"session"`).

      - `const SessionSession Session = "session"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Files.List(context.TODO(), anthropic.BetaFileListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Files.Download(ctx, fileID, query) (*Response, error)`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `fileID string`

  ID of the File.

- `query BetaFileDownloadParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaFileDownloadResponse interface{…}`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  response, err := client.Beta.Files.Download(
    context.TODO(),
    "file_id",
    anthropic.BetaFileDownloadParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

## Get File Metadata

`client.Beta.Files.GetMetadata(ctx, fileID, query) (*FileMetadata, error)`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `fileID string`

  ID of the File.

- `query BetaFileGetMetadataParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type FileMetadata struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `CreatedAt Time`

    RFC 3339 datetime string representing when the file was created.

  - `Filename string`

    Original filename of the uploaded file.

  - `MimeType string`

    MIME type of the file.

  - `SizeBytes int64`

    Size of the file in bytes.

  - `Type File`

    Object type.

    For files, this is always `"file"`.

    - `const FileFile File = "file"`

  - `Downloadable bool`

    Whether the file can be downloaded.

  - `Scope BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `ID string`

      The ID of the scoping resource (e.g., the session ID).

    - `Type Session`

      The type of scope (e.g., `"session"`).

      - `const SessionSession Session = "session"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  fileMetadata, err := client.Beta.Files.GetMetadata(
    context.TODO(),
    "file_id",
    anthropic.BetaFileGetMetadataParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", fileMetadata.ID)
}
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

`client.Beta.Files.Delete(ctx, fileID, body) (*DeletedFile, error)`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `fileID string`

  ID of the File.

- `body BetaFileDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type DeletedFile struct{…}`

  - `ID string`

    ID of the deleted file.

  - `Type DeletedFileType`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `const DeletedFileTypeFileDeleted DeletedFileType = "file_deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  deletedFile, err := client.Beta.Files.Delete(
    context.TODO(),
    "file_id",
    anthropic.BetaFileDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", deletedFile.ID)
}
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

- `type BetaFileScope struct{…}`

  - `ID string`

    The ID of the scoping resource (e.g., the session ID).

  - `Type Session`

    The type of scope (e.g., `"session"`).

    - `const SessionSession Session = "session"`

### Deleted File

- `type DeletedFile struct{…}`

  - `ID string`

    ID of the deleted file.

  - `Type DeletedFileType`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `const DeletedFileTypeFileDeleted DeletedFileType = "file_deleted"`

### File Metadata

- `type FileMetadata struct{…}`

  - `ID string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `CreatedAt Time`

    RFC 3339 datetime string representing when the file was created.

  - `Filename string`

    Original filename of the uploaded file.

  - `MimeType string`

    MIME type of the file.

  - `SizeBytes int64`

    Size of the file in bytes.

  - `Type File`

    Object type.

    For files, this is always `"file"`.

    - `const FileFile File = "file"`

  - `Downloadable bool`

    Whether the file can be downloaded.

  - `Scope BetaFileScope`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `ID string`

      The ID of the scoping resource (e.g., the session ID).

    - `Type Session`

      The type of scope (e.g., `"session"`).

      - `const SessionSession Session = "session"`

# Skills

## Create Skill

`client.Beta.Skills.New(ctx, params) (*BetaSkillNewResponse, error)`

**post** `/v1/skills`

Create Skill

### Parameters

- `params BetaSkillNewParams`

  - `Files param.Field[[]Reader]`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `DisplayTitle param.Field[string]`

    Body param: Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillNewResponse struct{…}`

  - `ID string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill was created.

  - `DisplayTitle string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `LatestVersion string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `Source string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `Type string`

    Object type.

    For Skills, this is always `"skill"`.

  - `UpdatedAt string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  skill, err := client.Beta.Skills.New(context.TODO(), anthropic.BetaSkillNewParams{
    Files: []io.Reader{io.Reader(bytes.NewBuffer([]byte("Example data")))},
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
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

## List Skills

`client.Beta.Skills.List(ctx, params) (*PageCursor[BetaSkillListResponse], error)`

**get** `/v1/skills`

List Skills

### Parameters

- `params BetaSkillListParams`

  - `Limit param.Field[int64]`

    Query param: Number of results to return per page.

    Maximum value is 100. Defaults to 20.

  - `Page param.Field[string]`

    Query param: Pagination token for fetching a specific page of results.

    Pass the value from a previous response's `next_page` field to get the next page of results.

  - `Source param.Field[string]`

    Query param: Filter skills by source.

    If provided, only skills from the specified source will be returned:

    * `"custom"`: only return user-created skills
    * `"anthropic"`: only return Anthropic-created skills

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillListResponse struct{…}`

  - `ID string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill was created.

  - `DisplayTitle string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `LatestVersion string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `Source string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `Type string`

    Object type.

    For Skills, this is always `"skill"`.

  - `UpdatedAt string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Skills.List(context.TODO(), anthropic.BetaSkillListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Skills.Get(ctx, skillID, query) (*BetaSkillGetResponse, error)`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `skillID string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `query BetaSkillGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillGetResponse struct{…}`

  - `ID string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill was created.

  - `DisplayTitle string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `LatestVersion string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `Source string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `Type string`

    Object type.

    For Skills, this is always `"skill"`.

  - `UpdatedAt string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  skill, err := client.Beta.Skills.Get(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
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

`client.Beta.Skills.Delete(ctx, skillID, body) (*BetaSkillDeleteResponse, error)`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `skillID string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `body BetaSkillDeleteParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillDeleteResponse struct{…}`

  - `ID string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Type string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  skill, err := client.Beta.Skills.Delete(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillDeleteParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", skill.ID)
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

`client.Beta.Skills.Versions.New(ctx, skillID, params) (*BetaSkillVersionNewResponse, error)`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `skillID string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params BetaSkillVersionNewParams`

  - `Files param.Field[[]Reader]`

    Body param: Files to upload for the skill.

    All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillVersionNewResponse struct{…}`

  - `ID string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill version was created.

  - `Description string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `Directory string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `Name string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `SkillID string`

    Identifier for the skill that this version belongs to.

  - `Type string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `Version string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```go
package main

import (
  "bytes"
  "context"
  "fmt"
  "io"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  version, err := client.Beta.Skills.Versions.New(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillVersionNewParams{
      Files: []io.Reader{io.Reader(bytes.NewBuffer([]byte("Example data")))},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", version.ID)
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

`client.Beta.Skills.Versions.List(ctx, skillID, params) (*PageCursor[BetaSkillVersionListResponse], error)`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `skillID string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `params BetaSkillVersionListParams`

  - `Limit param.Field[int64]`

    Query param: Number of items to return per page.

    Defaults to `20`. Ranges from `1` to `1000`.

  - `Page param.Field[string]`

    Query param: Optionally set to the `next_page` token from the previous response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillVersionListResponse struct{…}`

  - `ID string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill version was created.

  - `Description string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `Directory string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `Name string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `SkillID string`

    Identifier for the skill that this version belongs to.

  - `Type string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `Version string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Skills.Versions.List(
    context.TODO(),
    "skill_id",
    anthropic.BetaSkillVersionListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Skills.Versions.Download(ctx, version, params) (*Response, error)`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `version string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params BetaSkillVersionDownloadParams`

  - `SkillID param.Field[string]`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillVersionDownloadResponse interface{…}`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  response, err := client.Beta.Skills.Versions.Download(
    context.TODO(),
    "version",
    anthropic.BetaSkillVersionDownloadParams{
      SkillID: "skill_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

## Get Skill Version

`client.Beta.Skills.Versions.Get(ctx, version, params) (*BetaSkillVersionGetResponse, error)`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `version string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params BetaSkillVersionGetParams`

  - `SkillID param.Field[string]`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillVersionGetResponse struct{…}`

  - `ID string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `CreatedAt string`

    ISO 8601 timestamp of when the skill version was created.

  - `Description string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `Directory string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `Name string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `SkillID string`

    Identifier for the skill that this version belongs to.

  - `Type string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `Version string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  version, err := client.Beta.Skills.Versions.Get(
    context.TODO(),
    "version",
    anthropic.BetaSkillVersionGetParams{
      SkillID: "skill_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", version.ID)
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

`client.Beta.Skills.Versions.Delete(ctx, version, params) (*BetaSkillVersionDeleteResponse, error)`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `version string`

  Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `params BetaSkillVersionDeleteParams`

  - `SkillID param.Field[string]`

    Path param: Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaSkillVersionDeleteResponse struct{…}`

  - `ID string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `Type string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  version, err := client.Beta.Skills.Versions.Delete(
    context.TODO(),
    "version",
    anthropic.BetaSkillVersionDeleteParams{
      SkillID: "skill_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", version.ID)
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

`client.Beta.UserProfiles.New(ctx, params) (*BetaUserProfile, error)`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `params BetaUserProfileNewParams`

  - `ExternalID param.Field[string]`

    Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

  - `Name param.Field[string]`

    Body param: Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

  - `Relationship param.Field[BetaUserProfileNewParamsRelationship]`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileNewParamsRelationshipExternal BetaUserProfileNewParamsRelationship = "external"`

    - `const BetaUserProfileNewParamsRelationshipResold BetaUserProfileNewParamsRelationship = "resold"`

    - `const BetaUserProfileNewParamsRelationshipInternal BetaUserProfileNewParamsRelationship = "internal"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaUserProfile, err := client.Beta.UserProfiles.New(context.TODO(), anthropic.BetaUserProfileNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaUserProfile.ID)
}
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

`client.Beta.UserProfiles.List(ctx, params) (*PageCursor[BetaUserProfile], error)`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `params BetaUserProfileListParams`

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Order param.Field[BetaUserProfileListParamsOrder]`

    Query param: Query parameter for order

    - `const BetaUserProfileListParamsOrderAsc BetaUserProfileListParamsOrder = "asc"`

    - `const BetaUserProfileListParamsOrderDesc BetaUserProfileListParamsOrder = "desc"`

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.UserProfiles.List(context.TODO(), anthropic.BetaUserProfileListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.UserProfiles.Get(ctx, userProfileID, query) (*BetaUserProfile, error)`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `userProfileID string`

- `query BetaUserProfileGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaUserProfile, err := client.Beta.UserProfiles.Get(
    context.TODO(),
    "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    anthropic.BetaUserProfileGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaUserProfile.ID)
}
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

`client.Beta.UserProfiles.Update(ctx, userProfileID, params) (*BetaUserProfile, error)`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `userProfileID string`

- `params BetaUserProfileUpdateParams`

  - `ExternalID param.Field[string]`

    Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

  - `Metadata param.Field[map[string, string]]`

    Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

  - `Name param.Field[string]`

    Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

  - `Relationship param.Field[BetaUserProfileUpdateParamsRelationship]`

    Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileUpdateParamsRelationshipExternal BetaUserProfileUpdateParamsRelationship = "external"`

    - `const BetaUserProfileUpdateParamsRelationshipResold BetaUserProfileUpdateParamsRelationship = "resold"`

    - `const BetaUserProfileUpdateParamsRelationshipInternal BetaUserProfileUpdateParamsRelationship = "internal"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaUserProfile, err := client.Beta.UserProfiles.Update(
    context.TODO(),
    "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    anthropic.BetaUserProfileUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaUserProfile.ID)
}
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

`client.Beta.UserProfiles.NewEnrollmentURL(ctx, userProfileID, body) (*BetaUserProfileEnrollmentURL, error)`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `userProfileID string`

- `body BetaUserProfileNewEnrollmentURLParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaUserProfileEnrollmentURL struct{…}`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaUserProfileEnrollmentURLType`

    Object type. Always `enrollment_url`.

    - `const BetaUserProfileEnrollmentURLTypeEnrollmentURL BetaUserProfileEnrollmentURLType = "enrollment_url"`

  - `URL string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaUserProfileEnrollmentURL, err := client.Beta.UserProfiles.NewEnrollmentURL(
    context.TODO(),
    "uprof_011CZkZCu8hGbp5mYRQgUmz9",
    anthropic.BetaUserProfileNewEnrollmentURLParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaUserProfileEnrollmentURL.ExpiresAt)
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

- `type BetaUserProfile struct{…}`

  - `ID string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `Metadata map[string, string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `Relationship BetaUserProfileRelationship`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `const BetaUserProfileRelationshipExternal BetaUserProfileRelationship = "external"`

    - `const BetaUserProfileRelationshipResold BetaUserProfileRelationship = "resold"`

    - `const BetaUserProfileRelationshipInternal BetaUserProfileRelationship = "internal"`

  - `TrustGrants map[string, BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `Status BetaUserProfileTrustGrantStatus`

      Status of the trust grant.

      - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

      - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

      - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

  - `Type BetaUserProfileType`

    Object type. Always `user_profile`.

    - `const BetaUserProfileTypeUserProfile BetaUserProfileType = "user_profile"`

  - `UpdatedAt Time`

    A timestamp in RFC 3339 format

  - `ExternalID string`

    Platform's own identifier for this user. Not enforced unique.

  - `Name string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Beta User Profile Enrollment URL

- `type BetaUserProfileEnrollmentURL struct{…}`

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Type BetaUserProfileEnrollmentURLType`

    Object type. Always `enrollment_url`.

    - `const BetaUserProfileEnrollmentURLTypeEnrollmentURL BetaUserProfileEnrollmentURLType = "enrollment_url"`

  - `URL string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `type BetaUserProfileTrustGrant struct{…}`

  - `Status BetaUserProfileTrustGrantStatus`

    Status of the trust grant.

    - `const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"`

    - `const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"`

    - `const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"`

# Dreams

## Create a Dream

`client.Beta.Dreams.New(ctx, params) (*BetaDream, error)`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `params BetaDreamNewParams`

  - `Inputs param.Field[[]BetaDreamInputUnion]`

    Body param

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Model param.Field[BetaDreamNewParamsModelUnion]`

    Body param: Model identifier and configuration applied to every pipeline stage.

    - `string`

    - `type BetaDreamModelConfigParamResp struct{…}`

      Model identifier and configuration applied to every pipeline stage.

      - `ID string`

        Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

      - `Speed BetaDreamModelConfigParamSpeed`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `const BetaDreamModelConfigParamSpeedStandard BetaDreamModelConfigParamSpeed = "standard"`

        - `const BetaDreamModelConfigParamSpeedFast BetaDreamModelConfigParamSpeed = "fast"`

  - `Instructions param.Field[string]`

    Body param

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaDream, err := client.Beta.Dreams.New(context.TODO(), anthropic.BetaDreamNewParams{
    Inputs: []anthropic.BetaDreamInputUnionParam{anthropic.BetaDreamInputUnionParam{
      OfMemoryStore: &anthropic.BetaDreamMemoryStoreInputParam{
        MemoryStoreID: "x",
        Type: anthropic.BetaDreamMemoryStoreInputTypeMemoryStore,
      },
    }},
    Model: anthropic.BetaDreamNewParamsModelUnion{
      OfString: anthropic.String("string"),
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaDream.ID)
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

`client.Beta.Dreams.List(ctx, params) (*PageCursor[BetaDream], error)`

**get** `/v1/dreams`

List Dreams

### Parameters

- `params BetaDreamListParams`

  - `CreatedAtGt param.Field[Time]`

    Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

  - `CreatedAtLt param.Field[Time]`

    Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

  - `IncludeArchived param.Field[bool]`

    Query param: Query parameter for include_archived

  - `Limit param.Field[int64]`

    Query param: Query parameter for limit

  - `Page param.Field[string]`

    Query param: Query parameter for page

  - `Statuses param.Field[[]BetaDreamStatus]`

    Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Dreams.List(context.TODO(), anthropic.BetaDreamListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Dreams.Get(ctx, dreamID, query) (*BetaDream, error)`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `dreamID string`

- `query BetaDreamGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaDream, err := client.Beta.Dreams.Get(
    context.TODO(),
    "dream_id",
    anthropic.BetaDreamGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaDream.ID)
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

`client.Beta.Dreams.Cancel(ctx, dreamID, body) (*BetaDream, error)`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `dreamID string`

- `body BetaDreamCancelParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaDream, err := client.Beta.Dreams.Cancel(
    context.TODO(),
    "dream_id",
    anthropic.BetaDreamCancelParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaDream.ID)
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

`client.Beta.Dreams.Archive(ctx, dreamID, body) (*BetaDream, error)`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `dreamID string`

- `body BetaDreamArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaDream, err := client.Beta.Dreams.Archive(
    context.TODO(),
    "dream_id",
    anthropic.BetaDreamArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaDream.ID)
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

- `type BetaDream struct{…}`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `ID string`

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `EndedAt Time`

    A timestamp in RFC 3339 format

  - `Error BetaDreamError`

    Failure detail for a Dream whose `status` is `failed`.

    - `Message string`

    - `Type string`

  - `Inputs []BetaDreamInputUnion`

    - `type BetaDreamMemoryStoreInput struct{…}`

      An input memory store the dream reads from. The dream never mutates this store.

      - `MemoryStoreID string`

      - `Type BetaDreamMemoryStoreInputType`

        - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

    - `type BetaDreamSessionsInput struct{…}`

      Input session transcripts the dream reads.

      - `SessionIDs []string`

      - `Type BetaDreamSessionsInputType`

        - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

  - `Instructions string`

  - `Model BetaDreamModelConfig`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `ID string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `Speed BetaDreamModelConfigSpeed`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

      - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

  - `Outputs []BetaDreamOutput`

    - `MemoryStoreID string`

    - `Type BetaDreamOutputType`

      - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

  - `SessionID string`

  - `Status BetaDreamStatus`

    Lifecycle status of a Dream.

    - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

    - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

    - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

    - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

    - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

  - `Type BetaDreamType`

    - `const BetaDreamTypeDream BetaDreamType = "dream"`

  - `Usage BetaDreamUsage`

    Cumulative token usage for the dream across every pipeline stage.

    - `CacheCreationInputTokens int64`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `CacheReadInputTokens int64`

      Total tokens read from prompt cache.

    - `InputTokens int64`

      Total uncached input tokens consumed across every pipeline stage.

    - `OutputTokens int64`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `type BetaDreamError struct{…}`

  Failure detail for a Dream whose `status` is `failed`.

  - `Message string`

  - `Type string`

### Beta Dream Input

- `type BetaDreamInputUnion interface{…}`

  An input memory store the dream reads from. The dream never mutates this store.

  - `type BetaDreamMemoryStoreInput struct{…}`

    An input memory store the dream reads from. The dream never mutates this store.

    - `MemoryStoreID string`

    - `Type BetaDreamMemoryStoreInputType`

      - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

  - `type BetaDreamSessionsInput struct{…}`

    Input session transcripts the dream reads.

    - `SessionIDs []string`

    - `Type BetaDreamSessionsInputType`

      - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

### Beta Dream Memory Store Input

- `type BetaDreamMemoryStoreInput struct{…}`

  An input memory store the dream reads from. The dream never mutates this store.

  - `MemoryStoreID string`

  - `Type BetaDreamMemoryStoreInputType`

    - `const BetaDreamMemoryStoreInputTypeMemoryStore BetaDreamMemoryStoreInputType = "memory_store"`

### Beta Dream Memory Store Output

- `type BetaDreamMemoryStoreOutput struct{…}`

  An output memory store the dream writes consolidated memories into.

  - `MemoryStoreID string`

  - `Type BetaDreamMemoryStoreOutputType`

    - `const BetaDreamMemoryStoreOutputTypeMemoryStore BetaDreamMemoryStoreOutputType = "memory_store"`

### Beta Dream Model Config

- `type BetaDreamModelConfig struct{…}`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `ID string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `Speed BetaDreamModelConfigSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaDreamModelConfigSpeedStandard BetaDreamModelConfigSpeed = "standard"`

    - `const BetaDreamModelConfigSpeedFast BetaDreamModelConfigSpeed = "fast"`

### Beta Dream Model Config Param

- `type BetaDreamModelConfigParamResp struct{…}`

  Model identifier and configuration applied to every pipeline stage.

  - `ID string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `Speed BetaDreamModelConfigParamSpeed`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `const BetaDreamModelConfigParamSpeedStandard BetaDreamModelConfigParamSpeed = "standard"`

    - `const BetaDreamModelConfigParamSpeedFast BetaDreamModelConfigParamSpeed = "fast"`

### Beta Dream Output

- `type BetaDreamOutput struct{…}`

  An output memory store the dream writes consolidated memories into.

  - `MemoryStoreID string`

  - `Type BetaDreamOutputType`

    - `const BetaDreamOutputTypeMemoryStore BetaDreamOutputType = "memory_store"`

### Beta Dream Sessions Input

- `type BetaDreamSessionsInput struct{…}`

  Input session transcripts the dream reads.

  - `SessionIDs []string`

  - `Type BetaDreamSessionsInputType`

    - `const BetaDreamSessionsInputTypeSessions BetaDreamSessionsInputType = "sessions"`

### Beta Dream Status

- `type BetaDreamStatus string`

  Lifecycle status of a Dream.

  - `const BetaDreamStatusPending BetaDreamStatus = "pending"`

  - `const BetaDreamStatusRunning BetaDreamStatus = "running"`

  - `const BetaDreamStatusCompleted BetaDreamStatus = "completed"`

  - `const BetaDreamStatusFailed BetaDreamStatus = "failed"`

  - `const BetaDreamStatusCanceled BetaDreamStatus = "canceled"`

### Beta Dream Usage

- `type BetaDreamUsage struct{…}`

  Cumulative token usage for the dream across every pipeline stage.

  - `CacheCreationInputTokens int64`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `CacheReadInputTokens int64`

    Total tokens read from prompt cache.

  - `InputTokens int64`

    Total uncached input tokens consumed across every pipeline stage.

  - `OutputTokens int64`

    Total output tokens generated across every pipeline stage.

# Tunnels

## Create Tunnel

`client.Beta.Tunnels.New(ctx, params) (*BetaTunnel, error)`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `params BetaTunnelNewParams`

  - `DisplayName param.Field[string]`

    Body param: Optional human-readable name for the tunnel (1-255 characters).

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnel, err := client.Beta.Tunnels.New(context.TODO(), anthropic.BetaTunnelNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnel.ID)
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

`client.Beta.Tunnels.Get(ctx, tunnelID, query) (*BetaTunnel, error)`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `tunnelID string`

- `query BetaTunnelGetParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnel, err := client.Beta.Tunnels.Get(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelGetParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnel.ID)
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

`client.Beta.Tunnels.List(ctx, params) (*PageCursor[BetaTunnel], error)`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `params BetaTunnelListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived tunnels in the results. Defaults to false.

  - `Limit param.Field[int64]`

    Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous `list_tunnels` response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Tunnels.List(context.TODO(), anthropic.BetaTunnelListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Tunnels.Archive(ctx, tunnelID, body) (*BetaTunnel, error)`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `tunnelID string`

- `body BetaTunnelArchiveParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnel, err := client.Beta.Tunnels.Archive(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelArchiveParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnel.ID)
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

`client.Beta.Tunnels.RevealToken(ctx, tunnelID, body) (*BetaTunnelToken, error)`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `tunnelID string`

- `body BetaTunnelRevealTokenParams`

  - `Betas param.Field[[]AnthropicBeta]`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnelToken, err := client.Beta.Tunnels.RevealToken(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelRevealTokenParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnelToken.ID)
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

`client.Beta.Tunnels.RotateToken(ctx, tunnelID, params) (*BetaTunnelToken, error)`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `tunnelID string`

- `params BetaTunnelRotateTokenParams`

  - `Reason param.Field[string]`

    Body param: Optional free-text reason for the rotation, recorded for audit.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnelToken, err := client.Beta.Tunnels.RotateToken(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelRotateTokenParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnelToken.ID)
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

- `type BetaTunnel struct{…}`

  An MCP tunnel.

  - `ID string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `DisplayName string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `Domain string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `Type Tunnel`

    - `const TunnelTunnel Tunnel = "tunnel"`

### Beta Tunnel Token

- `type BetaTunnelToken struct{…}`

  A tunnel's connector token.

  - `ID string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `TunnelToken string`

    The connector token used to run the tunnel. Treat as a credential.

  - `Type TunnelToken`

    - `const TunnelTokenTunnelToken TunnelToken = "tunnel_token"`

# Certificates

## Create Tunnel Certificate

`client.Beta.Tunnels.Certificates.New(ctx, tunnelID, params) (*BetaTunnelCertificate, error)`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `tunnelID string`

- `params BetaTunnelCertificateNewParams`

  - `CaCertificatePem param.Field[string]`

    Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.New(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelCertificateNewParams{
      CaCertificatePem: "ca_certificate_pem",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnelCertificate.ID)
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

`client.Beta.Tunnels.Certificates.Get(ctx, certificateID, params) (*BetaTunnelCertificate, error)`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `certificateID string`

- `params BetaTunnelCertificateGetParams`

  - `TunnelID param.Field[string]`

    Path param: Path parameter tunnel_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.Get(
    context.TODO(),
    "certificate_id",
    anthropic.BetaTunnelCertificateGetParams{
      TunnelID: "tunnel_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnelCertificate.ID)
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

`client.Beta.Tunnels.Certificates.List(ctx, tunnelID, params) (*PageCursor[BetaTunnelCertificate], error)`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `tunnelID string`

- `params BetaTunnelCertificateListParams`

  - `IncludeArchived param.Field[bool]`

    Query param: Whether to include archived certificates in the results. Defaults to false.

  - `Limit param.Field[int64]`

    Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

  - `Page param.Field[string]`

    Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  page, err := client.Beta.Tunnels.Certificates.List(
    context.TODO(),
    "tunnel_id",
    anthropic.BetaTunnelCertificateListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Tunnels.Certificates.Archive(ctx, certificateID, params) (*BetaTunnelCertificate, error)`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `certificateID string`

- `params BetaTunnelCertificateArchiveParams`

  - `TunnelID param.Field[string]`

    Path param: Path parameter tunnel_id

  - `Betas param.Field[[]AnthropicBeta]`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

### Returns

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaTunnelCertificate, err := client.Beta.Tunnels.Certificates.Archive(
    context.TODO(),
    "certificate_id",
    anthropic.BetaTunnelCertificateArchiveParams{
      TunnelID: "tunnel_id",
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaTunnelCertificate.ID)
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

- `type BetaTunnelCertificate struct{…}`

  A CA certificate attached to a tunnel.

  - `ID string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `ArchivedAt Time`

    A timestamp in RFC 3339 format

  - `CreatedAt Time`

    A timestamp in RFC 3339 format

  - `ExpiresAt Time`

    A timestamp in RFC 3339 format

  - `Fingerprint string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `TunnelID string`

    ID of the tunnel the certificate is registered against.

  - `Type TunnelCertificate`

    - `const TunnelCertificateTunnelCertificate TunnelCertificate = "tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `type BetaWebhookAgentArchivedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentArchived`

    - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

  - `WorkspaceID string`

### Beta Webhook Agent Created Event Data

- `type BetaWebhookAgentCreatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentCreated`

    - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

  - `WorkspaceID string`

### Beta Webhook Agent Deleted Event Data

- `type BetaWebhookAgentDeletedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentDeleted`

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

  - `WorkspaceID string`

### Beta Webhook Agent Updated Event Data

- `type BetaWebhookAgentUpdatedEventData struct{…}`

  - `ID string`

    ID of the agent that triggered the event.

  - `OrganizationID string`

  - `Type AgentUpdated`

    - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

  - `WorkspaceID string`

### Beta Webhook Deployment Archived Event Data

- `type BetaWebhookDeploymentArchivedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentArchived`

    - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

  - `WorkspaceID string`

### Beta Webhook Deployment Created Event Data

- `type BetaWebhookDeploymentCreatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentCreated`

    - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

  - `WorkspaceID string`

### Beta Webhook Deployment Deleted Event Data

- `type BetaWebhookDeploymentDeletedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentDeleted`

    - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Deployment Paused Event Data

- `type BetaWebhookDeploymentPausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentPaused`

    - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Failed Event Data

- `type BetaWebhookDeploymentRunFailedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunFailed`

    - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Started Event Data

- `type BetaWebhookDeploymentRunStartedEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunStarted`

    - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

  - `WorkspaceID string`

### Beta Webhook Deployment Run Succeeded Event Data

- `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

  - `ID string`

    ID of the deployment run that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentRunSucceeded`

    - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

  - `WorkspaceID string`

### Beta Webhook Deployment Unpaused Event Data

- `type BetaWebhookDeploymentUnpausedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUnpaused`

    - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

  - `WorkspaceID string`

### Beta Webhook Deployment Updated Event Data

- `type BetaWebhookDeploymentUpdatedEventData struct{…}`

  - `ID string`

    ID of the deployment that triggered the event.

  - `OrganizationID string`

  - `Type DeploymentUpdated`

    - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

  - `WorkspaceID string`

### Beta Webhook Environment Archived Event Data

- `type BetaWebhookEnvironmentArchivedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentArchived`

    - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

  - `WorkspaceID string`

### Beta Webhook Environment Created Event Data

- `type BetaWebhookEnvironmentCreatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentCreated`

    - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

  - `WorkspaceID string`

### Beta Webhook Environment Deleted Event Data

- `type BetaWebhookEnvironmentDeletedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentDeleted`

    - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

  - `WorkspaceID string`

### Beta Webhook Environment Updated Event Data

- `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

  - `ID string`

    ID of the environment that triggered the event.

  - `OrganizationID string`

  - `Type EnvironmentUpdated`

    - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

  - `WorkspaceID string`

### Beta Webhook Event

- `type BetaWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentDeleted`

        - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`

### Beta Webhook Event Data

- `type BetaWebhookEventDataUnion interface{…}`

  - `type BetaWebhookSessionCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionCreated`

      - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionPendingEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionPending`

      - `const SessionPendingSessionPending SessionPending = "session.pending"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRunningEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRunning`

      - `const SessionRunningSessionRunning SessionRunning = "session.running"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionIdled`

      - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionRequiresActionEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionRequiresAction`

      - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionArchivedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionArchived`

      - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionDeletedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionDeleted`

      - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRescheduled`

      - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusRunStarted`

      - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusIdled`

      - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionStatusTerminated`

      - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadCreated`

      - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadIdledEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadIdled`

      - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `SessionThreadID string`

      ID of the session thread this event refers to.

    - `Type SessionThreadTerminated`

      - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

    - `WorkspaceID string`

  - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionOutcomeEvaluationEnded`

      - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCreatedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultCreated`

      - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultArchivedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultArchived`

      - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultDeletedEventData struct{…}`

    - `ID string`

      ID of the vault that triggered the event.

    - `OrganizationID string`

    - `Type VaultDeleted`

      - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialCreated`

      - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialArchived`

      - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialDeleted`

      - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

    - `ID string`

      ID of the vault credential that triggered the event.

    - `OrganizationID string`

    - `Type VaultCredentialRefreshFailed`

      - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

    - `VaultID string`

      ID of the vault that owns this credential.

    - `WorkspaceID string`

  - `type BetaWebhookSessionUpdatedEventData struct{…}`

    - `ID string`

      ID of the session that triggered the event.

    - `OrganizationID string`

    - `Type SessionUpdated`

      - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentCreatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentCreated`

      - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentArchivedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentArchived`

      - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentDeletedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentDeleted`

      - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentPausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentPaused`

      - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunFailed`

      - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentCreatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentCreated`

      - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUpdated`

      - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentUnpaused`

      - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

    - `WorkspaceID string`

  - `type BetaWebhookAgentUpdatedEventData struct{…}`

    - `ID string`

      ID of the agent that triggered the event.

    - `OrganizationID string`

    - `Type AgentUpdated`

      - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentArchivedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentArchived`

      - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunStarted`

      - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentDeletedEventData struct{…}`

    - `ID string`

      ID of the deployment that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentDeleted`

      - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

    - `ID string`

      ID of the deployment run that triggered the event.

    - `OrganizationID string`

    - `Type DeploymentRunSucceeded`

      - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentCreated`

      - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentUpdated`

      - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentArchived`

      - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

    - `ID string`

      ID of the environment that triggered the event.

    - `OrganizationID string`

    - `Type EnvironmentDeleted`

      - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreCreated`

      - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreArchived`

      - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

    - `WorkspaceID string`

  - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

    - `ID string`

      ID of the memory store that triggered the event.

    - `OrganizationID string`

    - `Type MemoryStoreDeleted`

      - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

    - `WorkspaceID string`

### Beta Webhook Memory Store Archived Event Data

- `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreArchived`

    - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Created Event Data

- `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreCreated`

    - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

  - `WorkspaceID string`

### Beta Webhook Memory Store Deleted Event Data

- `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

  - `ID string`

    ID of the memory store that triggered the event.

  - `OrganizationID string`

  - `Type MemoryStoreDeleted`

    - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Archived Event Data

- `type BetaWebhookSessionArchivedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionArchived`

    - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

  - `WorkspaceID string`

### Beta Webhook Session Created Event Data

- `type BetaWebhookSessionCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionCreated`

    - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

  - `WorkspaceID string`

### Beta Webhook Session Deleted Event Data

- `type BetaWebhookSessionDeletedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionDeleted`

    - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

  - `WorkspaceID string`

### Beta Webhook Session Idled Event Data

- `type BetaWebhookSessionIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionIdled`

    - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

  - `WorkspaceID string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionOutcomeEvaluationEnded`

    - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

  - `WorkspaceID string`

### Beta Webhook Session Pending Event Data

- `type BetaWebhookSessionPendingEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionPending`

    - `const SessionPendingSessionPending SessionPending = "session.pending"`

  - `WorkspaceID string`

### Beta Webhook Session Requires Action Event Data

- `type BetaWebhookSessionRequiresActionEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRequiresAction`

    - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

  - `WorkspaceID string`

### Beta Webhook Session Running Event Data

- `type BetaWebhookSessionRunningEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionRunning`

    - `const SessionRunningSessionRunning SessionRunning = "session.running"`

  - `WorkspaceID string`

### Beta Webhook Session Status Idled Event Data

- `type BetaWebhookSessionStatusIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusIdled`

    - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Rescheduled Event Data

- `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRescheduled`

    - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

  - `WorkspaceID string`

### Beta Webhook Session Status Run Started Event Data

- `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusRunStarted`

    - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

  - `WorkspaceID string`

### Beta Webhook Session Status Terminated Event Data

- `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionStatusTerminated`

    - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Created Event Data

- `type BetaWebhookSessionThreadCreatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadCreated`

    - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Idled Event Data

- `type BetaWebhookSessionThreadIdledEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadIdled`

    - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

  - `WorkspaceID string`

### Beta Webhook Session Thread Terminated Event Data

- `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `SessionThreadID string`

    ID of the session thread this event refers to.

  - `Type SessionThreadTerminated`

    - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

  - `WorkspaceID string`

### Beta Webhook Session Updated Event Data

- `type BetaWebhookSessionUpdatedEventData struct{…}`

  - `ID string`

    ID of the session that triggered the event.

  - `OrganizationID string`

  - `Type SessionUpdated`

    - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

  - `WorkspaceID string`

### Beta Webhook Vault Archived Event Data

- `type BetaWebhookVaultArchivedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultArchived`

    - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

  - `WorkspaceID string`

### Beta Webhook Vault Created Event Data

- `type BetaWebhookVaultCreatedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultCreated`

    - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

  - `WorkspaceID string`

### Beta Webhook Vault Credential Archived Event Data

- `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialArchived`

    - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Created Event Data

- `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialCreated`

    - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Deleted Event Data

- `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialDeleted`

    - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

  - `ID string`

    ID of the vault credential that triggered the event.

  - `OrganizationID string`

  - `Type VaultCredentialRefreshFailed`

    - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

  - `VaultID string`

    ID of the vault that owns this credential.

  - `WorkspaceID string`

### Beta Webhook Vault Deleted Event Data

- `type BetaWebhookVaultDeletedEventData struct{…}`

  - `ID string`

    ID of the vault that triggered the event.

  - `OrganizationID string`

  - `Type VaultDeleted`

    - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

  - `WorkspaceID string`

### Unwrap Webhook Event

- `type UnwrapWebhookEvent struct{…}`

  - `ID string`

    Unique event identifier for idempotency.

  - `CreatedAt Time`

    RFC 3339 timestamp when the event occurred.

  - `Data BetaWebhookEventDataUnion`

    - `type BetaWebhookSessionCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionCreated`

        - `const SessionCreatedSessionCreated SessionCreated = "session.created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionPendingEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionPending`

        - `const SessionPendingSessionPending SessionPending = "session.pending"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRunningEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRunning`

        - `const SessionRunningSessionRunning SessionRunning = "session.running"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionIdled`

        - `const SessionIdledSessionIdled SessionIdled = "session.idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionRequiresActionEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionRequiresAction`

        - `const SessionRequiresActionSessionRequiresAction SessionRequiresAction = "session.requires_action"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionArchivedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionArchived`

        - `const SessionArchivedSessionArchived SessionArchived = "session.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionDeletedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionDeleted`

        - `const SessionDeletedSessionDeleted SessionDeleted = "session.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRescheduledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRescheduled`

        - `const SessionStatusRescheduledSessionStatusRescheduled SessionStatusRescheduled = "session.status_rescheduled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusRunStartedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusRunStarted`

        - `const SessionStatusRunStartedSessionStatusRunStarted SessionStatusRunStarted = "session.status_run_started"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusIdled`

        - `const SessionStatusIdledSessionStatusIdled SessionStatusIdled = "session.status_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionStatusTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionStatusTerminated`

        - `const SessionStatusTerminatedSessionStatusTerminated SessionStatusTerminated = "session.status_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadCreatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadCreated`

        - `const SessionThreadCreatedSessionThreadCreated SessionThreadCreated = "session.thread_created"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadIdledEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadIdled`

        - `const SessionThreadIdledSessionThreadIdled SessionThreadIdled = "session.thread_idled"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionThreadTerminatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `SessionThreadID string`

        ID of the session thread this event refers to.

      - `Type SessionThreadTerminated`

        - `const SessionThreadTerminatedSessionThreadTerminated SessionThreadTerminated = "session.thread_terminated"`

      - `WorkspaceID string`

    - `type BetaWebhookSessionOutcomeEvaluationEndedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionOutcomeEvaluationEnded`

        - `const SessionOutcomeEvaluationEndedSessionOutcomeEvaluationEnded SessionOutcomeEvaluationEnded = "session.outcome_evaluation_ended"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCreatedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultCreated`

        - `const VaultCreatedVaultCreated VaultCreated = "vault.created"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultArchivedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultArchived`

        - `const VaultArchivedVaultArchived VaultArchived = "vault.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultDeletedEventData struct{…}`

      - `ID string`

        ID of the vault that triggered the event.

      - `OrganizationID string`

      - `Type VaultDeleted`

        - `const VaultDeletedVaultDeleted VaultDeleted = "vault.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialCreatedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialCreated`

        - `const VaultCredentialCreatedVaultCredentialCreated VaultCredentialCreated = "vault_credential.created"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialArchivedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialArchived`

        - `const VaultCredentialArchivedVaultCredentialArchived VaultCredentialArchived = "vault_credential.archived"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialDeletedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialDeleted`

        - `const VaultCredentialDeletedVaultCredentialDeleted VaultCredentialDeleted = "vault_credential.deleted"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookVaultCredentialRefreshFailedEventData struct{…}`

      - `ID string`

        ID of the vault credential that triggered the event.

      - `OrganizationID string`

      - `Type VaultCredentialRefreshFailed`

        - `const VaultCredentialRefreshFailedVaultCredentialRefreshFailed VaultCredentialRefreshFailed = "vault_credential.refresh_failed"`

      - `VaultID string`

        ID of the vault that owns this credential.

      - `WorkspaceID string`

    - `type BetaWebhookSessionUpdatedEventData struct{…}`

      - `ID string`

        ID of the session that triggered the event.

      - `OrganizationID string`

      - `Type SessionUpdated`

        - `const SessionUpdatedSessionUpdated SessionUpdated = "session.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentCreatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentCreated`

        - `const AgentCreatedAgentCreated AgentCreated = "agent.created"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentArchivedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentArchived`

        - `const AgentArchivedAgentArchived AgentArchived = "agent.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentDeletedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentDeleted`

        - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentPausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentPaused`

        - `const DeploymentPausedDeploymentPaused DeploymentPaused = "deployment.paused"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunFailedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunFailed`

        - `const DeploymentRunFailedDeploymentRunFailed DeploymentRunFailed = "deployment_run.failed"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentCreatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentCreated`

        - `const DeploymentCreatedDeploymentCreated DeploymentCreated = "deployment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUpdatedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUpdated`

        - `const DeploymentUpdatedDeploymentUpdated DeploymentUpdated = "deployment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentUnpausedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentUnpaused`

        - `const DeploymentUnpausedDeploymentUnpaused DeploymentUnpaused = "deployment.unpaused"`

      - `WorkspaceID string`

    - `type BetaWebhookAgentUpdatedEventData struct{…}`

      - `ID string`

        ID of the agent that triggered the event.

      - `OrganizationID string`

      - `Type AgentUpdated`

        - `const AgentUpdatedAgentUpdated AgentUpdated = "agent.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentArchivedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentArchived`

        - `const DeploymentArchivedDeploymentArchived DeploymentArchived = "deployment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunStartedEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunStarted`

        - `const DeploymentRunStartedDeploymentRunStarted DeploymentRunStarted = "deployment_run.started"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentDeletedEventData struct{…}`

      - `ID string`

        ID of the deployment that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentDeleted`

        - `const DeploymentDeletedDeploymentDeleted DeploymentDeleted = "deployment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookDeploymentRunSucceededEventData struct{…}`

      - `ID string`

        ID of the deployment run that triggered the event.

      - `OrganizationID string`

      - `Type DeploymentRunSucceeded`

        - `const DeploymentRunSucceededDeploymentRunSucceeded DeploymentRunSucceeded = "deployment_run.succeeded"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentCreatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentCreated`

        - `const EnvironmentCreatedEnvironmentCreated EnvironmentCreated = "environment.created"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentUpdatedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentUpdated`

        - `const EnvironmentUpdatedEnvironmentUpdated EnvironmentUpdated = "environment.updated"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentArchivedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentArchived`

        - `const EnvironmentArchivedEnvironmentArchived EnvironmentArchived = "environment.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookEnvironmentDeletedEventData struct{…}`

      - `ID string`

        ID of the environment that triggered the event.

      - `OrganizationID string`

      - `Type EnvironmentDeleted`

        - `const EnvironmentDeletedEnvironmentDeleted EnvironmentDeleted = "environment.deleted"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreCreatedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreCreated`

        - `const MemoryStoreCreatedMemoryStoreCreated MemoryStoreCreated = "memory_store.created"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreArchivedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreArchived`

        - `const MemoryStoreArchivedMemoryStoreArchived MemoryStoreArchived = "memory_store.archived"`

      - `WorkspaceID string`

    - `type BetaWebhookMemoryStoreDeletedEventData struct{…}`

      - `ID string`

        ID of the memory store that triggered the event.

      - `OrganizationID string`

      - `Type MemoryStoreDeleted`

        - `const MemoryStoreDeletedMemoryStoreDeleted MemoryStoreDeleted = "memory_store.deleted"`

      - `WorkspaceID string`

  - `Type Event`

    Object type. Always `event` for webhook payloads.

    - `const EventEvent Event = "event"`
