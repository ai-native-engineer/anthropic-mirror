<!-- part of: https://platform.claude.com/docs/en/api/cli/beta -->

<!-- chunk-start -->
    An incremental update to an event that is still being streamed. Deltas are best-effort and may stop early; when the buffered event with id == event_id is produced it carries the complete content. A model request that ends early (an error or interrupt) produces no buffered event — its terminal span.model_request_end closes the preview. Only sent on stream connections that opt in via event_deltas; never appears in event history.

    - `delta: object { content, type, index }`

      One fragment of the previewed event. The delta type is named for the previewed event's field it streams into: agent.message events stream content_delta fragments, each a partial element of the content array.

      - `content: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

      - `type: "content_delta"`

        - `"content_delta"`

      - `index: optional number`

        Which entry in the previewed event's content array this fragment lands in. Insert content as that entry when the index is new; append to the existing entry otherwise.

    - `event_id: string`

      The id of the event being previewed. Matches event.id on the corresponding event_start and the buffered event that reconciles the preview.

    - `type: "event_delta"`

      - `"event_delta"`

  - `beta_managed_agents_system_message_event: object { id, content, type, processed_at }`

    A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

    - `id: string`

      Unique identifier for this event.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

    - `processed_at: optional string`

      A timestamp in RFC 3339 format

### Example

```cli
ant beta:sessions:threads:events stream \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --thread-id sthr_011CZkZVWa6oIjw0rgXZpnBt
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

`$ ant beta:deployments create`

**post** `/v1/deployments`

Create Deployment

### Parameters

- `--agent: string or BetaManagedAgentsAgentParams`

  Body param: Agent to deploy. Accepts the `agent` ID string, which pins the latest version, or an `agent` object with both id and version specified. The agent must exist and not be archived.

- `--environment-id: string`

  Body param: ID of the `environment` defining the container configuration for sessions created from this deployment.

- `--initial-event: array of BetaManagedAgentsDeploymentInitialEventParams`

  Body param: Events to send to each session immediately after creation. At least 1, maximum 50.

- `--name: string`

  Body param: Human-readable name for the deployment.

- `--description: optional string`

  Body param: Description of what the deployment does.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Resources (e.g. repositories, files) to mount into each session's container. Maximum 500.

- `--schedule: optional object { expression, timezone, type }`

  Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `--vault-id: optional array of string`

  Body param: Vault IDs for stored credentials the agent can use during sessions created from this deployment. Maximum 50.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments create \
  --api-key my-anthropic-api-key \
  --agent string \
  --environment-id x \
  --initial-event "{content: [{text: 'Where is my order #1234?', type: text}], type: user.message}" \
  --name x
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
  ]
}
```

## List Deployments

`$ ant beta:deployments list`

**get** `/v1/deployments`

List Deployments

### Parameters

- `--agent-id: optional string`

  Query param: Filter by agent ID.

- `--created-at-gte: optional string`

  Query param: Return deployments created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return deployments created at or before this time (inclusive).

- `--include-archived: optional boolean`

  Query param: When true, includes archived deployments. Default: false (exclude archived).

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination cursor.

- `--status: optional "active" or "paused"`

  Query param: Filter by status: active or paused. Omit for both. To include archived deployments, use include_archived instead; the two cannot be combined.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListDeploymentsData: object { data, next_page }`

  Paginated list of deployments.

  - `data: array of BetaManagedAgentsDeployment`

    List of deployments.

    - `id: string`

      Unique identifier for this deployment.

    - `agent: object { id, type, version }`

      A resolved agent reference with a concrete version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `description: string`

      Description of what the deployment does.

    - `environment_id: string`

      ID of the `environment` where sessions run.

    - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

      Events sent to each session immediately after creation.

      - `beta_managed_agents_deployment_user_message_event: object { content, type }`

        A user message sent to the session.

        - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

          Array of content blocks for the user message.

          - `beta_managed_agents_text_block: object { text, type }`

            Regular text content.

            - `text: string`

              The text content.

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_image_block: object { source, type }`

            Image content specified directly as base64 data or as a reference via a URL.

            - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

              Union type for image source variants.

              - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

                Base64-encoded image data.

                - `data: string`

                  Base64-encoded image data.

                - `media_type: string`

                  MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

                - `type: "base64"`

                  - `"base64"`

              - `beta_managed_agents_url_image_source: object { type, url }`

                Image referenced by URL.

                - `type: "url"`

                  - `"url"`

                - `url: string`

                  URL of the image to fetch.

              - `beta_managed_agents_file_image_source: object { file_id, type }`

                Image referenced by file ID.

                - `file_id: string`

                  ID of a previously uploaded file.

                - `type: "file"`

                  - `"file"`

            - `type: "image"`

              - `"image"`

          - `beta_managed_agents_document_block: object { source, type, context, title }`

            Document content, either specified directly as base64 data, as text, or as a reference via a URL.

            - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

              Union type for document source variants.

              - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

                Base64-encoded document data.

                - `data: string`

                  Base64-encoded document data.

                - `media_type: string`

                  MIME type of the document (e.g., "application/pdf").

                - `type: "base64"`

                  - `"base64"`

              - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

                Plain text document content.

                - `data: string`

                  The plain text content.

                - `media_type: "text/plain"`

                  MIME type of the text content. Must be "text/plain".

                  - `"text/plain"`

                - `type: "text"`

                  - `"text"`

              - `beta_managed_agents_url_document_source: object { type, url }`

                Document referenced by URL.

                - `type: "url"`

                  - `"url"`

                - `url: string`

                  URL of the document to fetch.

              - `beta_managed_agents_file_document_source: object { file_id, type }`

                Document referenced by file ID.

                - `file_id: string`

                  ID of a previously uploaded file.

                - `type: "file"`

                  - `"file"`

            - `type: "document"`

              - `"document"`

            - `context: optional string`

              Additional context about the document for the model.

            - `title: optional string`

              The title of the document.

        - `type: "user.message"`

          - `"user.message"`

      - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

        An outcome the agent should work toward. The agent begins work on receipt.

        - `description: string`

          What the agent should produce. This is the task specification.

        - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

          Rubric for grading the quality of an outcome.

          - `beta_managed_agents_file_rubric: object { file_id, type }`

            Rubric referenced by a file uploaded via the Files API.

            - `file_id: string`

              ID of the rubric file.

            - `type: "file"`

              - `"file"`

          - `beta_managed_agents_text_rubric: object { content, type }`

            Rubric content provided inline as text.

            - `content: string`

              Rubric content. Plain text or markdown — the grader treats it as freeform text.

            - `type: "text"`

              - `"text"`

        - `type: "user.define_outcome"`

          - `"user.define_outcome"`

        - `max_iterations: optional number`

          Eval→revision cycles before giving up. Default 3, max 20.

      - `beta_managed_agents_deployment_system_message_event: object { content, type }`

        Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

        - `content: array of BetaManagedAgentsSystemContentBlock`

          System content blocks to append. Text-only.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `type: "system.message"`

          - `"system.message"`

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs.

    - `name: string`

      Human-readable name.

    - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

      Why a deployment is paused. Non-null exactly when `status` is `paused`.

      - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

        The caller invoked the pause endpoint on the deployment.

        - `type: "manual"`

          - `"manual"`

      - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

        A scheduled fire recorded a failed run whose error auto-pauses the deployment.

        - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

          The error that triggered an auto-pause. Matches the failed run's `error.type`.

          - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

            The deployment's environment was archived.

            - `type: "environment_archived_error"`

              - `"environment_archived_error"`

          - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

            The deployment's agent was archived.

            - `type: "agent_archived_error"`

              - `"agent_archived_error"`

          - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

            The deployment's environment no longer exists.

            - `type: "environment_not_found_error"`

              - `"environment_not_found_error"`

          - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

            A vault referenced by the deployment no longer exists.

            - `type: "vault_not_found_error"`

              - `"vault_not_found_error"`

          - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

            A file resource referenced by the deployment no longer exists.

            - `type: "file_not_found_error"`

              - `"file_not_found_error"`

          - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

            A referenced resource no longer exists and its kind was not reported.

            - `type: "session_resource_not_found_error"`

              - `"session_resource_not_found_error"`

          - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

            The deployment's workspace was archived.

            - `type: "workspace_archived_error"`

              - `"workspace_archived_error"`

          - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

            The deployment's organization is disabled.

            - `type: "organization_disabled_error"`

              - `"organization_disabled_error"`

          - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

            A memory store referenced by the deployment is archived.

            - `type: "memory_store_archived_error"`

              - `"memory_store_archived_error"`

          - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

            A skill referenced by the deployment's agent no longer exists.

            - `type: "skill_not_found_error"`

              - `"skill_not_found_error"`

          - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

            A vault referenced by the deployment is archived.

            - `type: "vault_archived_error"`

              - `"vault_archived_error"`

          - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

            An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

            - `type: "unknown_error"`

              - `"unknown_error"`

          - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

            The deployment configures resources, but its environment is self-hosted and cannot mount them.

            - `type: "self_hosted_resources_unsupported_error"`

              - `"self_hosted_resources_unsupported_error"`

          - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

            An MCP server host used by the deployment's agent is blocked by the environment's network policy.

            - `type: "mcp_egress_blocked_error"`

              - `"mcp_egress_blocked_error"`

        - `type: "error"`

          - `"error"`

    - `resources: array of BetaManagedAgentsSessionResourceConfig`

      Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

      - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

        A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

        - `type: "github_repository"`

          - `"github_repository"`

        - `url: string`

          Github URL of the repository

        - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

          Branch or commit to check out. Defaults to the repository's default branch.

          - `beta_managed_agents_branch_checkout: object { name, type }`

            - `name: string`

              Branch name to check out.

            - `type: "branch"`

              - `"branch"`

          - `beta_managed_agents_commit_checkout: object { sha, type }`

            - `sha: string`

              Full commit SHA to check out.

            - `type: "commit"`

              - `"commit"`

        - `mount_path: optional string`

          Mount path in the container. Defaults to `/workspace/<repo-name>`.

      - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

        A file mounted into each session's container.

        - `file_id: string`

          ID of a previously uploaded file.

        - `type: "file"`

          - `"file"`

        - `mount_path: optional string`

          Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

      - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

        A memory store attached to each session created from this deployment.

        - `memory_store_id: string`

          The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

        - `type: "memory_store"`

          - `"memory_store"`

        - `access: optional "read_write" or "read_only"`

          Access mode for an attached memory store.

          - `"read_write"`

          - `"read_only"`

        - `instructions: optional string`

          Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

    - `schedule: object { expression, timezone, type, 2 more }`

      5-field POSIX cron schedule with computed runtime timestamps.

      - `expression: string`

        5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

      - `timezone: string`

        IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

      - `type: "cron"`

        - `"cron"`

      - `last_run_at: optional string`

        A timestamp in RFC 3339 format

      - `upcoming_runs_at: optional array of string`

        Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

    - `status: "active" or "paused"`

      Lifecycle status of a deployment.

      - `"active"`

      - `"paused"`

    - `type: "deployment"`

      - `"deployment"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `vault_ids: array of string`

      Vault IDs supplying stored credentials for sessions created from this deployment.

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:deployments list \
  --api-key my-anthropic-api-key
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
      ]
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Deployment

`$ ant beta:deployments retrieve`

**get** `/v1/deployments/{deployment_id}`

Get Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments retrieve \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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
  ]
}
```

## Update Deployment

`$ ant beta:deployments update`

**post** `/v1/deployments/{deployment_id}`

Update Deployment

### Parameters

- `--deployment-id: string`

  Path param: Path parameter deployment_id

- `--agent: optional string or BetaManagedAgentsAgentParams`

  Body param: Agent to deploy. Accepts the `agent` ID string, which re-pins to the latest version, or an `agent` object with both id and version specified. Omit to preserve. Cannot be cleared.

- `--description: optional string`

  Body param: Description. Omit to preserve; send empty string or null to clear.

- `--environment-id: optional string`

  Body param: ID of the `environment` where sessions run. Omit to preserve. Cannot be cleared.

- `--initial-event: optional array of BetaManagedAgentsDeploymentInitialEventParams`

  Body param: Initial events. Full replacement. Omit to preserve. Cannot be cleared. At least 1, maximum 50.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--name: optional string`

  Body param: Human-readable name. Must be non-empty. Omit to preserve. Cannot be cleared.

- `--resource: optional array of BetaManagedAgentsGitHubRepositoryResourceParams or BetaManagedAgentsFileResourceParams or BetaManagedAgentsMemoryStoreResourceParam`

  Body param: Session resources. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 500.

- `--schedule: optional object { expression, timezone, type }`

  Body param: 5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

- `--vault-id: optional array of string`

  Body param: Vault IDs. Full replacement. Omit to preserve; send empty array or null to clear. Maximum 50.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments update \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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
  ]
}
```

## Archive Deployment

`$ ant beta:deployments archive`

**post** `/v1/deployments/{deployment_id}/archive`

Archive Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments archive \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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
  ]
}
```

## Run Deployment Now

`$ ant beta:deployments run`

**post** `/v1/deployments/{deployment_id}/run`

Run Deployment Now

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment_run: object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `beta_managed_agents_environment_archived_run_error: object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `beta_managed_agents_agent_archived_run_error: object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `beta_managed_agents_environment_not_found_run_error: object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `beta_managed_agents_vault_not_found_run_error: object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `beta_managed_agents_vault_archived_run_error: object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `beta_managed_agents_file_not_found_run_error: object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `beta_managed_agents_memory_store_archived_run_error: object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `beta_managed_agents_skill_not_found_run_error: object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `beta_managed_agents_session_resource_not_found_run_error: object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `beta_managed_agents_workspace_archived_run_error: object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `beta_managed_agents_organization_disabled_run_error: object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `beta_managed_agents_session_rate_limited_run_error: object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `beta_managed_agents_session_creation_rejected_run_error: object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `beta_managed_agents_unknown_run_error: object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `beta_managed_agents_self_hosted_resources_unsupported_run_error: object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `beta_managed_agents_mcp_egress_blocked_run_error: object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `beta_managed_agents_manual_trigger_context: object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```cli
ant beta:deployments run \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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

`$ ant beta:deployments pause`

**post** `/v1/deployments/{deployment_id}/pause`

Pause Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments pause \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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
  ]
}
```

## Unpause Deployment

`$ ant beta:deployments unpause`

**post** `/v1/deployments/{deployment_id}/unpause`

Unpause Deployment

### Parameters

- `--deployment-id: string`

  Path parameter deployment_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Example

```cli
ant beta:deployments unpause \
  --api-key my-anthropic-api-key \
  --deployment-id depl_011CZkZcDH3vPqd7xnEfwTai
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
  ]
}
```

## Domain Types

### Beta Managed Agents Agent Archived Deployment Paused Reason Error

- `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

  The deployment's agent was archived.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Cron Schedule

- `beta_managed_agents_cron_schedule: object { expression, timezone, type, 2 more }`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Cron Schedule Params

- `beta_managed_agents_cron_schedule_params: object { expression, timezone, type }`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Deployment

- `beta_managed_agents_deployment: object { id, agent, archived_at, 13 more }`

  A deployment is a configured instance of an agent — it binds the agent to everything needed to run it autonomously: an environment, credentials, initial events, and an optional schedule.

  - `id: string`

    Unique identifier for this deployment.

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `description: string`

    Description of what the deployment does.

  - `environment_id: string`

    ID of the `environment` where sessions run.

  - `initial_events: array of BetaManagedAgentsDeploymentInitialEvent`

    Events sent to each session immediately after creation.

    - `beta_managed_agents_deployment_user_message_event: object { content, type }`

      A user message sent to the session.

      - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

        Array of content blocks for the user message.

        - `beta_managed_agents_text_block: object { text, type }`

          Regular text content.

          - `text: string`

            The text content.

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_image_block: object { source, type }`

          Image content specified directly as base64 data or as a reference via a URL.

          - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

            Union type for image source variants.

            - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

              Base64-encoded image data.

              - `data: string`

                Base64-encoded image data.

              - `media_type: string`

                MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_url_image_source: object { type, url }`

              Image referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the image to fetch.

            - `beta_managed_agents_file_image_source: object { file_id, type }`

              Image referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "image"`

            - `"image"`

        - `beta_managed_agents_document_block: object { source, type, context, title }`

          Document content, either specified directly as base64 data, as text, or as a reference via a URL.

          - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

            Union type for document source variants.

            - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

              Base64-encoded document data.

              - `data: string`

                Base64-encoded document data.

              - `media_type: string`

                MIME type of the document (e.g., "application/pdf").

              - `type: "base64"`

                - `"base64"`

            - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

              Plain text document content.

              - `data: string`

                The plain text content.

              - `media_type: "text/plain"`

                MIME type of the text content. Must be "text/plain".

                - `"text/plain"`

              - `type: "text"`

                - `"text"`

            - `beta_managed_agents_url_document_source: object { type, url }`

              Document referenced by URL.

              - `type: "url"`

                - `"url"`

              - `url: string`

                URL of the document to fetch.

            - `beta_managed_agents_file_document_source: object { file_id, type }`

              Document referenced by file ID.

              - `file_id: string`

                ID of a previously uploaded file.

              - `type: "file"`

                - `"file"`

          - `type: "document"`

            - `"document"`

          - `context: optional string`

            Additional context about the document for the model.

          - `title: optional string`

            The title of the document.

      - `type: "user.message"`

        - `"user.message"`

    - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

      An outcome the agent should work toward. The agent begins work on receipt.

      - `description: string`

        What the agent should produce. This is the task specification.

      - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

        Rubric for grading the quality of an outcome.

        - `beta_managed_agents_file_rubric: object { file_id, type }`

          Rubric referenced by a file uploaded via the Files API.

          - `file_id: string`

            ID of the rubric file.

          - `type: "file"`

            - `"file"`

        - `beta_managed_agents_text_rubric: object { content, type }`

          Rubric content provided inline as text.

          - `content: string`

            Rubric content. Plain text or markdown — the grader treats it as freeform text.

          - `type: "text"`

            - `"text"`

      - `type: "user.define_outcome"`

        - `"user.define_outcome"`

      - `max_iterations: optional number`

        Eval→revision cycles before giving up. Default 3, max 20.

    - `beta_managed_agents_deployment_system_message_event: object { content, type }`

      Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

      - `content: array of BetaManagedAgentsSystemContentBlock`

        System content blocks to append. Text-only.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `type: "system.message"`

        - `"system.message"`

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs.

  - `name: string`

    Human-readable name.

  - `paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

    Why a deployment is paused. Non-null exactly when `status` is `paused`.

    - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

      The caller invoked the pause endpoint on the deployment.

      - `type: "manual"`

        - `"manual"`

    - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

      A scheduled fire recorded a failed run whose error auto-pauses the deployment.

      - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

        The error that triggered an auto-pause. Matches the failed run's `error.type`.

        - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

          The deployment's environment was archived.

          - `type: "environment_archived_error"`

            - `"environment_archived_error"`

        - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

          The deployment's agent was archived.

          - `type: "agent_archived_error"`

            - `"agent_archived_error"`

        - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

          The deployment's environment no longer exists.

          - `type: "environment_not_found_error"`

            - `"environment_not_found_error"`

        - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment no longer exists.

          - `type: "vault_not_found_error"`

            - `"vault_not_found_error"`

        - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

          A file resource referenced by the deployment no longer exists.

          - `type: "file_not_found_error"`

            - `"file_not_found_error"`

        - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

          A referenced resource no longer exists and its kind was not reported.

          - `type: "session_resource_not_found_error"`

            - `"session_resource_not_found_error"`

        - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

          The deployment's workspace was archived.

          - `type: "workspace_archived_error"`

            - `"workspace_archived_error"`

        - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

          The deployment's organization is disabled.

          - `type: "organization_disabled_error"`

            - `"organization_disabled_error"`

        - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

          A memory store referenced by the deployment is archived.

          - `type: "memory_store_archived_error"`

            - `"memory_store_archived_error"`

        - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

          A skill referenced by the deployment's agent no longer exists.

          - `type: "skill_not_found_error"`

            - `"skill_not_found_error"`

        - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

          A vault referenced by the deployment is archived.

          - `type: "vault_archived_error"`

            - `"vault_archived_error"`

        - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

          An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

          - `type: "unknown_error"`

            - `"unknown_error"`

        - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

          The deployment configures resources, but its environment is self-hosted and cannot mount them.

          - `type: "self_hosted_resources_unsupported_error"`

            - `"self_hosted_resources_unsupported_error"`

        - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

          An MCP server host used by the deployment's agent is blocked by the environment's network policy.

          - `type: "mcp_egress_blocked_error"`

            - `"mcp_egress_blocked_error"`

      - `type: "error"`

        - `"error"`

  - `resources: array of BetaManagedAgentsSessionResourceConfig`

    Resources attached to sessions created from this deployment. Echoes the input minus write-only credentials.

    - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

      A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

      - `type: "github_repository"`

        - `"github_repository"`

      - `url: string`

        Github URL of the repository

      - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

        Branch or commit to check out. Defaults to the repository's default branch.

        - `beta_managed_agents_branch_checkout: object { name, type }`

          - `name: string`

            Branch name to check out.

          - `type: "branch"`

            - `"branch"`

        - `beta_managed_agents_commit_checkout: object { sha, type }`

          - `sha: string`

            Full commit SHA to check out.

          - `type: "commit"`

            - `"commit"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/workspace/<repo-name>`.

    - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

      A file mounted into each session's container.

      - `file_id: string`

        ID of a previously uploaded file.

      - `type: "file"`

        - `"file"`

      - `mount_path: optional string`

        Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

    - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

      A memory store attached to each session created from this deployment.

      - `memory_store_id: string`

        The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

      - `type: "memory_store"`

        - `"memory_store"`

      - `access: optional "read_write" or "read_only"`

        Access mode for an attached memory store.

        - `"read_write"`

        - `"read_only"`

      - `instructions: optional string`

        Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

  - `schedule: object { expression, timezone, type, 2 more }`

    5-field POSIX cron schedule with computed runtime timestamps.

    - `expression: string`

      5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

    - `timezone: string`

      IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

    - `type: "cron"`

      - `"cron"`

    - `last_run_at: optional string`

      A timestamp in RFC 3339 format

    - `upcoming_runs_at: optional array of string`

      Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

  - `status: "active" or "paused"`

    Lifecycle status of a deployment.

    - `"active"`

    - `"paused"`

  - `type: "deployment"`

    - `"deployment"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_ids: array of string`

    Vault IDs supplying stored credentials for sessions created from this deployment.

### Beta Managed Agents Deployment Initial Event

- `beta_managed_agents_deployment_initial_event: BetaManagedAgentsDeploymentUserMessageEvent or BetaManagedAgentsDeploymentUserDefineOutcomeEvent or BetaManagedAgentsDeploymentSystemMessageEvent`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `beta_managed_agents_deployment_user_message_event: object { content, type }`

    A user message sent to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

    An outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric: object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `beta_managed_agents_text_rubric: object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `beta_managed_agents_deployment_system_message_event: object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Initial Event Params

- `beta_managed_agents_deployment_initial_event_params: BetaManagedAgentsUserMessageEventParams or BetaManagedAgentsUserDefineOutcomeEventParams or BetaManagedAgentsSystemMessageEventParams`

  An event sent to a session immediately after it is created. Supports `user.message`, `user.define_outcome`, and `system.message`.

  - `beta_managed_agents_user_message_event_params: object { content, type }`

    Parameters for sending a user message to the session.

    - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

      Array of content blocks for the user message.

      - `beta_managed_agents_text_block: object { text, type }`

        Regular text content.

        - `text: string`

          The text content.

        - `type: "text"`

          - `"text"`

      - `beta_managed_agents_image_block: object { source, type }`

        Image content specified directly as base64 data or as a reference via a URL.

        - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

          Union type for image source variants.

          - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

            Base64-encoded image data.

            - `data: string`

              Base64-encoded image data.

            - `media_type: string`

              MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_url_image_source: object { type, url }`

            Image referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the image to fetch.

          - `beta_managed_agents_file_image_source: object { file_id, type }`

            Image referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "image"`

          - `"image"`

      - `beta_managed_agents_document_block: object { source, type, context, title }`

        Document content, either specified directly as base64 data, as text, or as a reference via a URL.

        - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

          Union type for document source variants.

          - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

            Base64-encoded document data.

            - `data: string`

              Base64-encoded document data.

            - `media_type: string`

              MIME type of the document (e.g., "application/pdf").

            - `type: "base64"`

              - `"base64"`

          - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

            Plain text document content.

            - `data: string`

              The plain text content.

            - `media_type: "text/plain"`

              MIME type of the text content. Must be "text/plain".

              - `"text/plain"`

            - `type: "text"`

              - `"text"`

          - `beta_managed_agents_url_document_source: object { type, url }`

            Document referenced by URL.

            - `type: "url"`

              - `"url"`

            - `url: string`

              URL of the document to fetch.

          - `beta_managed_agents_file_document_source: object { file_id, type }`

            Document referenced by file ID.

            - `file_id: string`

              ID of a previously uploaded file.

            - `type: "file"`

              - `"file"`

        - `type: "document"`

          - `"document"`

        - `context: optional string`

          Additional context about the document for the model.

        - `title: optional string`

          The title of the document.

    - `type: "user.message"`

      - `"user.message"`

  - `beta_managed_agents_user_define_outcome_event_params: object { description, rubric, type, max_iterations }`

    Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

    - `description: string`

      What the agent should produce. This is the task specification.

    - `rubric: BetaManagedAgentsFileRubricParams or BetaManagedAgentsTextRubricParams`

      Rubric for grading the quality of an outcome.

      - `beta_managed_agents_file_rubric_params: object { file_id, type }`

        Rubric referenced by a file uploaded via the Files API.

        - `file_id: string`

          ID of the rubric file.

        - `type: "file"`

          - `"file"`

      - `beta_managed_agents_text_rubric_params: object { content, type }`

        Rubric content provided inline as text.

        - `content: string`

          Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

        - `type: "text"`

          - `"text"`

    - `type: "user.define_outcome"`

      - `"user.define_outcome"`

    - `max_iterations: optional number`

      Eval→revision cycles before giving up. Default 3, max 20.

  - `beta_managed_agents_system_message_event_params: object { content, type }`

    Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.

    - `content: array of BetaManagedAgentsSystemContentBlock`

      System content blocks to append. Text-only.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `type: "system.message"`

      - `"system.message"`

### Beta Managed Agents Deployment Paused Reason

- `beta_managed_agents_deployment_paused_reason: BetaManagedAgentsManualDeploymentPausedReason or BetaManagedAgentsErrorDeploymentPausedReason`

  Why a deployment is paused. Non-null exactly when `status` is `paused`.

  - `beta_managed_agents_manual_deployment_paused_reason: object { type }`

    The caller invoked the pause endpoint on the deployment.

    - `type: "manual"`

      - `"manual"`

  - `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

    A scheduled fire recorded a failed run whose error auto-pauses the deployment.

    - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

      The error that triggered an auto-pause. Matches the failed run's `error.type`.

      - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

        The deployment's environment was archived.

        - `type: "environment_archived_error"`

          - `"environment_archived_error"`

      - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

        The deployment's agent was archived.

        - `type: "agent_archived_error"`

          - `"agent_archived_error"`

      - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

        The deployment's environment no longer exists.

        - `type: "environment_not_found_error"`

          - `"environment_not_found_error"`

      - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

        A vault referenced by the deployment no longer exists.

        - `type: "vault_not_found_error"`

          - `"vault_not_found_error"`

      - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

        A file resource referenced by the deployment no longer exists.

        - `type: "file_not_found_error"`

          - `"file_not_found_error"`

      - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

        A referenced resource no longer exists and its kind was not reported.

        - `type: "session_resource_not_found_error"`

          - `"session_resource_not_found_error"`

      - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

        The deployment's workspace was archived.

        - `type: "workspace_archived_error"`

          - `"workspace_archived_error"`

      - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

        The deployment's organization is disabled.

        - `type: "organization_disabled_error"`

          - `"organization_disabled_error"`

      - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

        A memory store referenced by the deployment is archived.

        - `type: "memory_store_archived_error"`

          - `"memory_store_archived_error"`

      - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

        A skill referenced by the deployment's agent no longer exists.

        - `type: "skill_not_found_error"`

          - `"skill_not_found_error"`

      - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

        A vault referenced by the deployment is archived.

        - `type: "vault_archived_error"`

          - `"vault_archived_error"`

      - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

        An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `type: "self_hosted_resources_unsupported_error"`

          - `"self_hosted_resources_unsupported_error"`

      - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `type: "mcp_egress_blocked_error"`

          - `"mcp_egress_blocked_error"`

    - `type: "error"`

      - `"error"`

### Beta Managed Agents Deployment Paused Reason Error

- `beta_managed_agents_deployment_paused_reason_error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

  The error that triggered an auto-pause. Matches the failed run's `error.type`.

  - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

    The deployment's environment was archived.

    - `type: "environment_archived_error"`

      - `"environment_archived_error"`

  - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

    The deployment's agent was archived.

    - `type: "agent_archived_error"`

      - `"agent_archived_error"`

  - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

    The deployment's environment no longer exists.

    - `type: "environment_not_found_error"`

      - `"environment_not_found_error"`

  - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

    A vault referenced by the deployment no longer exists.

    - `type: "vault_not_found_error"`

      - `"vault_not_found_error"`

  - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

    A file resource referenced by the deployment no longer exists.

    - `type: "file_not_found_error"`

      - `"file_not_found_error"`

  - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

    A referenced resource no longer exists and its kind was not reported.

    - `type: "session_resource_not_found_error"`

      - `"session_resource_not_found_error"`

  - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

    The deployment's workspace was archived.

    - `type: "workspace_archived_error"`

      - `"workspace_archived_error"`

  - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

    The deployment's organization is disabled.

    - `type: "organization_disabled_error"`

      - `"organization_disabled_error"`

  - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

    A memory store referenced by the deployment is archived.

    - `type: "memory_store_archived_error"`

      - `"memory_store_archived_error"`

  - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

    A skill referenced by the deployment's agent no longer exists.

    - `type: "skill_not_found_error"`

      - `"skill_not_found_error"`

  - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

    A vault referenced by the deployment is archived.

    - `type: "vault_archived_error"`

      - `"vault_archived_error"`

  - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

    An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

    - `type: "unknown_error"`

      - `"unknown_error"`

  - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

    The deployment configures resources, but its environment is self-hosted and cannot mount them.

    - `type: "self_hosted_resources_unsupported_error"`

      - `"self_hosted_resources_unsupported_error"`

  - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

    An MCP server host used by the deployment's agent is blocked by the environment's network policy.

    - `type: "mcp_egress_blocked_error"`

      - `"mcp_egress_blocked_error"`

### Beta Managed Agents Deployment Status

- `beta_managed_agents_deployment_status: "active" or "paused"`

  Lifecycle status of a deployment.

  - `"active"`

  - `"paused"`

### Beta Managed Agents Deployment System Message Event

- `beta_managed_agents_deployment_system_message_event: object { content, type }`

  Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt.

  - `content: array of BetaManagedAgentsSystemContentBlock`

    System content blocks to append. Text-only.

    - `text: string`

      The text content.

    - `type: "text"`

      - `"text"`

  - `type: "system.message"`

    - `"system.message"`

### Beta Managed Agents Deployment User Define Outcome Event

- `beta_managed_agents_deployment_user_define_outcome_event: object { description, rubric, type, max_iterations }`

  An outcome the agent should work toward. The agent begins work on receipt.

  - `description: string`

    What the agent should produce. This is the task specification.

  - `rubric: BetaManagedAgentsFileRubric or BetaManagedAgentsTextRubric`

    Rubric for grading the quality of an outcome.

    - `beta_managed_agents_file_rubric: object { file_id, type }`

      Rubric referenced by a file uploaded via the Files API.

      - `file_id: string`

        ID of the rubric file.

      - `type: "file"`

        - `"file"`

    - `beta_managed_agents_text_rubric: object { content, type }`

      Rubric content provided inline as text.

      - `content: string`

        Rubric content. Plain text or markdown — the grader treats it as freeform text.

      - `type: "text"`

        - `"text"`

  - `type: "user.define_outcome"`

    - `"user.define_outcome"`

  - `max_iterations: optional number`

    Eval→revision cycles before giving up. Default 3, max 20.

### Beta Managed Agents Deployment User Message Event

- `beta_managed_agents_deployment_user_message_event: object { content, type }`

  A user message sent to the session.

  - `content: array of BetaManagedAgentsTextBlock or BetaManagedAgentsImageBlock or BetaManagedAgentsDocumentBlock`

    Array of content blocks for the user message.

    - `beta_managed_agents_text_block: object { text, type }`

      Regular text content.

      - `text: string`

        The text content.

      - `type: "text"`

        - `"text"`

    - `beta_managed_agents_image_block: object { source, type }`

      Image content specified directly as base64 data or as a reference via a URL.

      - `source: BetaManagedAgentsBase64ImageSource or BetaManagedAgentsURLImageSource or BetaManagedAgentsFileImageSource`

        Union type for image source variants.

        - `beta_managed_agents_base64_image_source: object { data, media_type, type }`

          Base64-encoded image data.

          - `data: string`

            Base64-encoded image data.

          - `media_type: string`

            MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_url_image_source: object { type, url }`

          Image referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the image to fetch.

        - `beta_managed_agents_file_image_source: object { file_id, type }`

          Image referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "image"`

        - `"image"`

    - `beta_managed_agents_document_block: object { source, type, context, title }`

      Document content, either specified directly as base64 data, as text, or as a reference via a URL.

      - `source: BetaManagedAgentsBase64DocumentSource or BetaManagedAgentsPlainTextDocumentSource or BetaManagedAgentsURLDocumentSource or BetaManagedAgentsFileDocumentSource`

        Union type for document source variants.

        - `beta_managed_agents_base64_document_source: object { data, media_type, type }`

          Base64-encoded document data.

          - `data: string`

            Base64-encoded document data.

          - `media_type: string`

            MIME type of the document (e.g., "application/pdf").

          - `type: "base64"`

            - `"base64"`

        - `beta_managed_agents_plain_text_document_source: object { data, media_type, type }`

          Plain text document content.

          - `data: string`

            The plain text content.

          - `media_type: "text/plain"`

            MIME type of the text content. Must be "text/plain".

            - `"text/plain"`

          - `type: "text"`

            - `"text"`

        - `beta_managed_agents_url_document_source: object { type, url }`

          Document referenced by URL.

          - `type: "url"`

            - `"url"`

          - `url: string`

            URL of the document to fetch.

        - `beta_managed_agents_file_document_source: object { file_id, type }`

          Document referenced by file ID.

          - `file_id: string`

            ID of a previously uploaded file.

          - `type: "file"`

            - `"file"`

      - `type: "document"`

        - `"document"`

      - `context: optional string`

        Additional context about the document for the model.

      - `title: optional string`

        The title of the document.

  - `type: "user.message"`

    - `"user.message"`

### Beta Managed Agents Environment Archived Deployment Paused Reason Error

- `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

  The deployment's environment was archived.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Deployment Paused Reason Error

- `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

  The deployment's environment no longer exists.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents Error Deployment Paused Reason

- `beta_managed_agents_error_deployment_paused_reason: object { error, type }`

  A scheduled fire recorded a failed run whose error auto-pauses the deployment.

  - `error: BetaManagedAgentsEnvironmentArchivedDeploymentPausedReasonError or BetaManagedAgentsAgentArchivedDeploymentPausedReasonError or BetaManagedAgentsEnvironmentNotFoundDeploymentPausedReasonError or 11 more`

    The error that triggered an auto-pause. Matches the failed run's `error.type`.

    - `beta_managed_agents_environment_archived_deployment_paused_reason_error: object { type }`

      The deployment's environment was archived.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `beta_managed_agents_agent_archived_deployment_paused_reason_error: object { type }`

      The deployment's agent was archived.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `beta_managed_agents_environment_not_found_deployment_paused_reason_error: object { type }`

      The deployment's environment no longer exists.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

      A vault referenced by the deployment no longer exists.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

      A file resource referenced by the deployment no longer exists.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

      A referenced resource no longer exists and its kind was not reported.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

      The deployment's workspace was archived.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

      The deployment's organization is disabled.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

      A memory store referenced by the deployment is archived.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

      A skill referenced by the deployment's agent no longer exists.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

      A vault referenced by the deployment is archived.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

      An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `type: "error"`

    - `"error"`

### Beta Managed Agents File Not Found Deployment Paused Reason Error

- `beta_managed_agents_file_not_found_deployment_paused_reason_error: object { type }`

  A file resource referenced by the deployment no longer exists.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents File Resource Config

- `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

  A file mounted into each session's container.

  - `file_id: string`

    ID of a previously uploaded file.

  - `type: "file"`

    - `"file"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

### Beta Managed Agents GitHub Repository Resource Config

- `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

  A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

  - `type: "github_repository"`

    - `"github_repository"`

  - `url: string`

    Github URL of the repository

  - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

    Branch or commit to check out. Defaults to the repository's default branch.

    - `beta_managed_agents_branch_checkout: object { name, type }`

      - `name: string`

        Branch name to check out.

      - `type: "branch"`

        - `"branch"`

    - `beta_managed_agents_commit_checkout: object { sha, type }`

      - `sha: string`

        Full commit SHA to check out.

      - `type: "commit"`

        - `"commit"`

  - `mount_path: optional string`

    Mount path in the container. Defaults to `/workspace/<repo-name>`.

### Beta Managed Agents Manual Deployment Paused Reason

- `beta_managed_agents_manual_deployment_paused_reason: object { type }`

  The caller invoked the pause endpoint on the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Deployment Paused Reason Error

- `beta_managed_agents_mcp_egress_blocked_deployment_paused_reason_error: object { type }`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Deployment Paused Reason Error

- `beta_managed_agents_memory_store_archived_deployment_paused_reason_error: object { type }`

  A memory store referenced by the deployment is archived.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Memory Store Resource Config

- `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

  A memory store attached to each session created from this deployment.

  - `memory_store_id: string`

    The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

  - `type: "memory_store"`

    - `"memory_store"`

  - `access: optional "read_write" or "read_only"`

    Access mode for an attached memory store.

    - `"read_write"`

    - `"read_only"`

  - `instructions: optional string`

    Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Organization Disabled Deployment Paused Reason Error

- `beta_managed_agents_organization_disabled_deployment_paused_reason_error: object { type }`

  The deployment's organization is disabled.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule

- `beta_managed_agents_schedule: object { expression, timezone, type, 2 more }`

  5-field POSIX cron schedule with computed runtime timestamps.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    IANA timezone identifier (e.g., "America/Los_Angeles", "UTC").

  - `type: "cron"`

    - `"cron"`

  - `last_run_at: optional string`

    A timestamp in RFC 3339 format

  - `upcoming_runs_at: optional array of string`

    Up to 5 timestamps of upcoming cron occurrences. Non-empty for active and paused deployments (reflects what the schedule would do if unpaused); empty once the deployment is archived (`archived_at` set). Each fire is offset by a small per-schedule jitter, so a run will actually start at or shortly after its listed time.

### Beta Managed Agents Schedule Params

- `beta_managed_agents_schedule_params: object { expression, timezone, type }`

  5-field POSIX cron schedule. Literal wall-clock matching in the configured timezone.

  - `expression: string`

    5-field POSIX cron expression: minute hour day-of-month month day-of-week (e.g., "0 9 * * 1-5" for weekdays at 9am). Day-of-week is 0-7 where 0 and 7 both mean Sunday. Extended cron syntax - seconds or year fields, and the special characters L, W, #, and ? - is not supported, nor are predefined shortcuts (@daily).

  - `timezone: string`

    Required. IANA timezone identifier (e.g., "America/Los_Angeles", "UTC"). Validated against the IANA timezone database.

  - `type: "cron"`

    - `"cron"`

### Beta Managed Agents Self Hosted Resources Unsupported Deployment Paused Reason Error

- `beta_managed_agents_self_hosted_resources_unsupported_deployment_paused_reason_error: object { type }`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Resource Config

- `beta_managed_agents_session_resource_config: BetaManagedAgentsGitHubRepositoryResourceConfig or BetaManagedAgentsFileResourceConfig or BetaManagedAgentsMemoryStoreResourceConfig`

  A configured session resource. Echoes the input minus write-only credentials.

  - `beta_managed_agents_github_repository_resource_config: object { type, url, checkout, mount_path }`

    A GitHub repository mounted into each session's container. The authorization token is write-only and never returned.

    - `type: "github_repository"`

      - `"github_repository"`

    - `url: string`

      Github URL of the repository

    - `checkout: optional BetaManagedAgentsBranchCheckout or BetaManagedAgentsCommitCheckout`

      Branch or commit to check out. Defaults to the repository's default branch.

      - `beta_managed_agents_branch_checkout: object { name, type }`

        - `name: string`

          Branch name to check out.

        - `type: "branch"`

          - `"branch"`

      - `beta_managed_agents_commit_checkout: object { sha, type }`

        - `sha: string`

          Full commit SHA to check out.

        - `type: "commit"`

          - `"commit"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/workspace/<repo-name>`.

  - `beta_managed_agents_file_resource_config: object { file_id, type, mount_path }`

    A file mounted into each session's container.

    - `file_id: string`

      ID of a previously uploaded file.

    - `type: "file"`

      - `"file"`

    - `mount_path: optional string`

      Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

  - `beta_managed_agents_memory_store_resource_config: object { memory_store_id, type, access, instructions }`

    A memory store attached to each session created from this deployment.

    - `memory_store_id: string`

      The memory store ID (memstore_...). Must belong to the caller's organization and workspace.

    - `type: "memory_store"`

      - `"memory_store"`

    - `access: optional "read_write" or "read_only"`

      Access mode for an attached memory store.

      - `"read_write"`

      - `"read_only"`

    - `instructions: optional string`

      Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

### Beta Managed Agents Session Resource Not Found Deployment Paused Reason Error

- `beta_managed_agents_session_resource_not_found_deployment_paused_reason_error: object { type }`

  A referenced resource no longer exists and its kind was not reported.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Deployment Paused Reason Error

- `beta_managed_agents_skill_not_found_deployment_paused_reason_error: object { type }`

  A skill referenced by the deployment's agent no longer exists.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Unknown Deployment Paused Reason Error

- `beta_managed_agents_unknown_deployment_paused_reason_error: object { type }`

  An unrecognized error auto-paused the deployment. A fallback variant; matches a run whose `error.type` is `unknown_error`.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Deployment Paused Reason Error

- `beta_managed_agents_vault_archived_deployment_paused_reason_error: object { type }`

  A vault referenced by the deployment is archived.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Deployment Paused Reason Error

- `beta_managed_agents_vault_not_found_deployment_paused_reason_error: object { type }`

  A vault referenced by the deployment no longer exists.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Deployment Paused Reason Error

- `beta_managed_agents_workspace_archived_deployment_paused_reason_error: object { type }`

  The deployment's workspace was archived.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`

# Deployment Runs

## List Deployment Runs

`$ ant beta:deployment-runs list`

**get** `/v1/deployment_runs`

List Deployment Runs

### Parameters

- `--created-at-gt: optional string`

  Query param: Return runs created strictly after this time (exclusive).

- `--created-at-gte: optional string`

  Query param: Return runs created at or after this time (inclusive).

- `--created-at-lt: optional string`

  Query param: Return runs created strictly before this time (exclusive).

- `--created-at-lte: optional string`

  Query param: Return runs created at or before this time (inclusive).

- `--deployment-id: optional string`

  Query param: Filter to a specific deployment. Omit to list across all deployments in the workspace. Filtering by a non-existent deployment_id returns 200 with empty data.

- `--has-error: optional boolean`

  Query param: Filter: true for runs with non-null error, false for runs with non-null session_id. Omit for all.

- `--limit: optional number`

  Query param: Maximum results per page. Default 20, maximum 1000.

- `--page: optional string`

  Query param: Opaque pagination cursor. Pass next_page from the previous response. Invalid or expired cursors return 400.

- `--trigger-type: optional "schedule" or "manual"`

  Query param: Filter runs by what triggered them. Omit to return all runs.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListDeploymentRunsData: object { data, next_page }`

  Paginated list of deployment runs. Sorted by created_at descending (most recent first).

  - `data: array of BetaManagedAgentsDeploymentRun`

    List of deployment runs.

    - `id: string`

      Unique identifier for this run (`drun_...`).

    - `agent: object { id, type, version }`

      A resolved agent reference with a concrete version.

      - `id: string`

      - `type: "agent"`

        - `"agent"`

      - `version: number`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `deployment_id: string`

      ID of the deployment that produced this run.

    - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

      Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

      - `beta_managed_agents_environment_archived_run_error: object { message, type }`

        The deployment's environment was archived.

        - `message: string`

          Human-readable error description.

        - `type: "environment_archived_error"`

          - `"environment_archived_error"`

      - `beta_managed_agents_agent_archived_run_error: object { message, type }`

        The deployment's agent was archived.

        - `message: string`

          Human-readable error description.

        - `type: "agent_archived_error"`

          - `"agent_archived_error"`

      - `beta_managed_agents_environment_not_found_run_error: object { message, type }`

        The deployment's environment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "environment_not_found_error"`

          - `"environment_not_found_error"`

      - `beta_managed_agents_vault_not_found_run_error: object { message, type }`

        A vault referenced by the deployment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "vault_not_found_error"`

          - `"vault_not_found_error"`

      - `beta_managed_agents_vault_archived_run_error: object { message, type }`

        A vault referenced by the deployment is archived.

        - `message: string`

          Human-readable error description.

        - `type: "vault_archived_error"`

          - `"vault_archived_error"`

      - `beta_managed_agents_file_not_found_run_error: object { message, type }`

        A file resource referenced by the deployment no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "file_not_found_error"`

          - `"file_not_found_error"`

      - `beta_managed_agents_memory_store_archived_run_error: object { message, type }`

        A memory store referenced by the deployment is archived.

        - `message: string`

          Human-readable error description.

        - `type: "memory_store_archived_error"`

          - `"memory_store_archived_error"`

      - `beta_managed_agents_skill_not_found_run_error: object { message, type }`

        A skill referenced by the deployment's agent no longer exists.

        - `message: string`

          Human-readable error description.

        - `type: "skill_not_found_error"`

          - `"skill_not_found_error"`

      - `beta_managed_agents_session_resource_not_found_run_error: object { message, type }`

        A referenced resource no longer exists and its kind was not reported.

        - `message: string`

          Human-readable error description.

        - `type: "session_resource_not_found_error"`

          - `"session_resource_not_found_error"`

      - `beta_managed_agents_workspace_archived_run_error: object { message, type }`

        The deployment's workspace was archived.

        - `message: string`

          Human-readable error description.

        - `type: "workspace_archived_error"`

          - `"workspace_archived_error"`

      - `beta_managed_agents_organization_disabled_run_error: object { message, type }`

        The deployment's organization is disabled.

        - `message: string`

          Human-readable error description.

        - `type: "organization_disabled_error"`

          - `"organization_disabled_error"`

      - `beta_managed_agents_session_rate_limited_run_error: object { message, type }`

        Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

        - `message: string`

          Human-readable error description.

        - `type: "session_rate_limited_error"`

          - `"session_rate_limited_error"`

      - `beta_managed_agents_session_creation_rejected_run_error: object { message, type }`

        The session create request was rejected with a non-retryable validation error.

        - `message: string`

          Human-readable error description.

        - `type: "session_creation_rejected_error"`

          - `"session_creation_rejected_error"`

      - `beta_managed_agents_unknown_run_error: object { message, type }`

        An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

        - `message: string`

          Human-readable error description.

        - `type: "unknown_error"`

          - `"unknown_error"`

      - `beta_managed_agents_self_hosted_resources_unsupported_run_error: object { message, type }`

        The deployment configures resources, but its environment is self-hosted and cannot mount them.

        - `message: string`

          Human-readable error description.

        - `type: "self_hosted_resources_unsupported_error"`

          - `"self_hosted_resources_unsupported_error"`

      - `beta_managed_agents_mcp_egress_blocked_run_error: object { message, type }`

        An MCP server host used by the deployment's agent is blocked by the environment's network policy.

        - `message: string`

          Human-readable error description.

        - `type: "mcp_egress_blocked_error"`

          - `"mcp_egress_blocked_error"`

    - `session_id: string`

      Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

    - `trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

      Describes what triggered a deployment run, with trigger-specific metadata.

      - `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

        The run was fired by the deployment's cron schedule.

        - `scheduled_at: string`

          A timestamp in RFC 3339 format

        - `type: "schedule"`

          - `"schedule"`

      - `beta_managed_agents_manual_trigger_context: object { type }`

        The run was started manually by creating a session directly against the deployment.

        - `type: "manual"`

          - `"manual"`

    - `type: "deployment_run"`

      - `"deployment_run"`

  - `next_page: optional string`

    Opaque cursor for the next page. Null when no more results.

### Example

```cli
ant beta:deployment-runs list \
  --api-key my-anthropic-api-key
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

`$ ant beta:deployment-runs retrieve`

**get** `/v1/deployment_runs/{deployment_run_id}`

Get Deployment Run

### Parameters

- `--deployment-run-id: string`

  Path parameter deployment_run_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deployment_run: object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `beta_managed_agents_environment_archived_run_error: object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `beta_managed_agents_agent_archived_run_error: object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `beta_managed_agents_environment_not_found_run_error: object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `beta_managed_agents_vault_not_found_run_error: object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `beta_managed_agents_vault_archived_run_error: object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `beta_managed_agents_file_not_found_run_error: object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `beta_managed_agents_memory_store_archived_run_error: object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `beta_managed_agents_skill_not_found_run_error: object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `beta_managed_agents_session_resource_not_found_run_error: object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `beta_managed_agents_workspace_archived_run_error: object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `beta_managed_agents_organization_disabled_run_error: object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `beta_managed_agents_session_rate_limited_run_error: object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `beta_managed_agents_session_creation_rejected_run_error: object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `beta_managed_agents_unknown_run_error: object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `beta_managed_agents_self_hosted_resources_unsupported_run_error: object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `beta_managed_agents_mcp_egress_blocked_run_error: object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `beta_managed_agents_manual_trigger_context: object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Example

```cli
ant beta:deployment-runs retrieve \
  --api-key my-anthropic-api-key \
  --deployment-run-id deployment_run_id
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

- `beta_managed_agents_agent_archived_run_error: object { message, type }`

  The deployment's agent was archived.

  - `message: string`

    Human-readable error description.

  - `type: "agent_archived_error"`

    - `"agent_archived_error"`

### Beta Managed Agents Deployment Run

- `beta_managed_agents_deployment_run: object { id, agent, created_at, 5 more }`

  A persistent, append-only record of a single deployment execution. Records session creation success or failure — no session lifecycle tracking.

  - `id: string`

    Unique identifier for this run (`drun_...`).

  - `agent: object { id, type, version }`

    A resolved agent reference with a concrete version.

    - `id: string`

    - `type: "agent"`

      - `"agent"`

    - `version: number`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `deployment_id: string`

    ID of the deployment that produced this run.

  - `error: BetaManagedAgentsEnvironmentArchivedRunError or BetaManagedAgentsAgentArchivedRunError or BetaManagedAgentsEnvironmentNotFoundRunError or 13 more`

    Why the run failed to create a session. The type identifies the failure; message is human-readable detail.

    - `beta_managed_agents_environment_archived_run_error: object { message, type }`

      The deployment's environment was archived.

      - `message: string`

        Human-readable error description.

      - `type: "environment_archived_error"`

        - `"environment_archived_error"`

    - `beta_managed_agents_agent_archived_run_error: object { message, type }`

      The deployment's agent was archived.

      - `message: string`

        Human-readable error description.

      - `type: "agent_archived_error"`

        - `"agent_archived_error"`

    - `beta_managed_agents_environment_not_found_run_error: object { message, type }`

      The deployment's environment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "environment_not_found_error"`

        - `"environment_not_found_error"`

    - `beta_managed_agents_vault_not_found_run_error: object { message, type }`

      A vault referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "vault_not_found_error"`

        - `"vault_not_found_error"`

    - `beta_managed_agents_vault_archived_run_error: object { message, type }`

      A vault referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "vault_archived_error"`

        - `"vault_archived_error"`

    - `beta_managed_agents_file_not_found_run_error: object { message, type }`

      A file resource referenced by the deployment no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "file_not_found_error"`

        - `"file_not_found_error"`

    - `beta_managed_agents_memory_store_archived_run_error: object { message, type }`

      A memory store referenced by the deployment is archived.

      - `message: string`

        Human-readable error description.

      - `type: "memory_store_archived_error"`

        - `"memory_store_archived_error"`

    - `beta_managed_agents_skill_not_found_run_error: object { message, type }`

      A skill referenced by the deployment's agent no longer exists.

      - `message: string`

        Human-readable error description.

      - `type: "skill_not_found_error"`

        - `"skill_not_found_error"`

    - `beta_managed_agents_session_resource_not_found_run_error: object { message, type }`

      A referenced resource no longer exists and its kind was not reported.

      - `message: string`

        Human-readable error description.

      - `type: "session_resource_not_found_error"`

        - `"session_resource_not_found_error"`

    - `beta_managed_agents_workspace_archived_run_error: object { message, type }`

      The deployment's workspace was archived.

      - `message: string`

        Human-readable error description.

      - `type: "workspace_archived_error"`

        - `"workspace_archived_error"`

    - `beta_managed_agents_organization_disabled_run_error: object { message, type }`

      The deployment's organization is disabled.

      - `message: string`

        Human-readable error description.

      - `type: "organization_disabled_error"`

        - `"organization_disabled_error"`

    - `beta_managed_agents_session_rate_limited_run_error: object { message, type }`

      Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

      - `message: string`

        Human-readable error description.

      - `type: "session_rate_limited_error"`

        - `"session_rate_limited_error"`

    - `beta_managed_agents_session_creation_rejected_run_error: object { message, type }`

      The session create request was rejected with a non-retryable validation error.

      - `message: string`

        Human-readable error description.

      - `type: "session_creation_rejected_error"`

        - `"session_creation_rejected_error"`

    - `beta_managed_agents_unknown_run_error: object { message, type }`

      An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

      - `message: string`

        Human-readable error description.

      - `type: "unknown_error"`

        - `"unknown_error"`

    - `beta_managed_agents_self_hosted_resources_unsupported_run_error: object { message, type }`

      The deployment configures resources, but its environment is self-hosted and cannot mount them.

      - `message: string`

        Human-readable error description.

      - `type: "self_hosted_resources_unsupported_error"`

        - `"self_hosted_resources_unsupported_error"`

    - `beta_managed_agents_mcp_egress_blocked_run_error: object { message, type }`

      An MCP server host used by the deployment's agent is blocked by the environment's network policy.

      - `message: string`

        Human-readable error description.

      - `type: "mcp_egress_blocked_error"`

        - `"mcp_egress_blocked_error"`

  - `session_id: string`

    Populated on success. Null on creation failure. Exactly one of session_id or error is non-null.

  - `trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

    Describes what triggered a deployment run, with trigger-specific metadata.

    - `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

      The run was fired by the deployment's cron schedule.

      - `scheduled_at: string`

        A timestamp in RFC 3339 format

      - `type: "schedule"`

        - `"schedule"`

    - `beta_managed_agents_manual_trigger_context: object { type }`

      The run was started manually by creating a session directly against the deployment.

      - `type: "manual"`

        - `"manual"`

  - `type: "deployment_run"`

    - `"deployment_run"`

### Beta Managed Agents Environment Archived Run Error

- `beta_managed_agents_environment_archived_run_error: object { message, type }`

  The deployment's environment was archived.

  - `message: string`

    Human-readable error description.

  - `type: "environment_archived_error"`

    - `"environment_archived_error"`

### Beta Managed Agents Environment Not Found Run Error

- `beta_managed_agents_environment_not_found_run_error: object { message, type }`

  The deployment's environment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "environment_not_found_error"`

    - `"environment_not_found_error"`

### Beta Managed Agents File Not Found Run Error

- `beta_managed_agents_file_not_found_run_error: object { message, type }`

  A file resource referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "file_not_found_error"`

    - `"file_not_found_error"`

### Beta Managed Agents Manual Trigger Context

- `beta_managed_agents_manual_trigger_context: object { type }`

  The run was started manually by creating a session directly against the deployment.

  - `type: "manual"`

    - `"manual"`

### Beta Managed Agents MCP Egress Blocked Run Error

- `beta_managed_agents_mcp_egress_blocked_run_error: object { message, type }`

  An MCP server host used by the deployment's agent is blocked by the environment's network policy.

  - `message: string`

    Human-readable error description.

  - `type: "mcp_egress_blocked_error"`

    - `"mcp_egress_blocked_error"`

### Beta Managed Agents Memory Store Archived Run Error

- `beta_managed_agents_memory_store_archived_run_error: object { message, type }`

  A memory store referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "memory_store_archived_error"`

    - `"memory_store_archived_error"`

### Beta Managed Agents Organization Disabled Run Error

- `beta_managed_agents_organization_disabled_run_error: object { message, type }`

  The deployment's organization is disabled.

  - `message: string`

    Human-readable error description.

  - `type: "organization_disabled_error"`

    - `"organization_disabled_error"`

### Beta Managed Agents Schedule Trigger Context

- `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

  The run was fired by the deployment's cron schedule.

  - `scheduled_at: string`

    A timestamp in RFC 3339 format

  - `type: "schedule"`

    - `"schedule"`

### Beta Managed Agents Self Hosted Resources Unsupported Run Error

- `beta_managed_agents_self_hosted_resources_unsupported_run_error: object { message, type }`

  The deployment configures resources, but its environment is self-hosted and cannot mount them.

  - `message: string`

    Human-readable error description.

  - `type: "self_hosted_resources_unsupported_error"`

    - `"self_hosted_resources_unsupported_error"`

### Beta Managed Agents Session Creation Rejected Run Error

- `beta_managed_agents_session_creation_rejected_run_error: object { message, type }`

  The session create request was rejected with a non-retryable validation error.

  - `message: string`

    Human-readable error description.

  - `type: "session_creation_rejected_error"`

    - `"session_creation_rejected_error"`

### Beta Managed Agents Session Rate Limited Run Error

- `beta_managed_agents_session_rate_limited_run_error: object { message, type }`

  Session creation was rejected due to rate limiting. The schedule keeps firing; subsequent runs may succeed.

  - `message: string`

    Human-readable error description.

  - `type: "session_rate_limited_error"`

    - `"session_rate_limited_error"`

### Beta Managed Agents Session Resource Not Found Run Error

- `beta_managed_agents_session_resource_not_found_run_error: object { message, type }`

  A referenced resource no longer exists and its kind was not reported.

  - `message: string`

    Human-readable error description.

  - `type: "session_resource_not_found_error"`

    - `"session_resource_not_found_error"`

### Beta Managed Agents Skill Not Found Run Error

- `beta_managed_agents_skill_not_found_run_error: object { message, type }`

  A skill referenced by the deployment's agent no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "skill_not_found_error"`

    - `"skill_not_found_error"`

### Beta Managed Agents Trigger Context

- `beta_managed_agents_trigger_context: BetaManagedAgentsScheduleTriggerContext or BetaManagedAgentsManualTriggerContext`

  Describes what triggered a deployment run, with trigger-specific metadata.

  - `beta_managed_agents_schedule_trigger_context: object { scheduled_at, type }`

    The run was fired by the deployment's cron schedule.

    - `scheduled_at: string`

      A timestamp in RFC 3339 format

    - `type: "schedule"`

      - `"schedule"`

  - `beta_managed_agents_manual_trigger_context: object { type }`

    The run was started manually by creating a session directly against the deployment.

    - `type: "manual"`

      - `"manual"`

### Beta Managed Agents Trigger Type

- `beta_managed_agents_trigger_type: "schedule" or "manual"`

  What triggered a deployment run.

  - `"schedule"`

  - `"manual"`

### Beta Managed Agents Unknown Run Error

- `beta_managed_agents_unknown_run_error: object { message, type }`

  An unknown or unexpected error caused the run to fail. A fallback variant; clients that do not recognize a new error type can match on message alone.

  - `message: string`

    Human-readable error description.

  - `type: "unknown_error"`

    - `"unknown_error"`

### Beta Managed Agents Vault Archived Run Error

- `beta_managed_agents_vault_archived_run_error: object { message, type }`

  A vault referenced by the deployment is archived.

  - `message: string`

    Human-readable error description.

  - `type: "vault_archived_error"`

    - `"vault_archived_error"`

### Beta Managed Agents Vault Not Found Run Error

- `beta_managed_agents_vault_not_found_run_error: object { message, type }`

  A vault referenced by the deployment no longer exists.

  - `message: string`

    Human-readable error description.

  - `type: "vault_not_found_error"`

    - `"vault_not_found_error"`

### Beta Managed Agents Workspace Archived Run Error

- `beta_managed_agents_workspace_archived_run_error: object { message, type }`

  The deployment's workspace was archived.

  - `message: string`

    Human-readable error description.

  - `type: "workspace_archived_error"`

    - `"workspace_archived_error"`

# Vaults

## Create Vault

`$ ant beta:vaults create`

**post** `/v1/vaults`

Create Vault

### Parameters

- `--display-name: string`

  Body param: Human-readable name for the vault. 1-255 characters.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata to attach to the vault. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```cli
ant beta:vaults create \
  --api-key my-anthropic-api-key \
  --display-name 'Example vault'
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

`$ ant beta:vaults list`

**get** `/v1/vaults`

List Vaults

### Parameters

- `--include-archived: optional boolean`

  Query param: Whether to include archived vaults in the results.

- `--limit: optional number`

  Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination token from a previous `list_vaults` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListVaultsResponse: object { data, next_page }`

  Response containing a paginated list of vaults.

  - `data: optional array of BetaManagedAgentsVault`

    List of vaults.

    - `id: string`

      Unique identifier for the vault.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `display_name: string`

      Human-readable name for the vault.

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the vault.

    - `type: "vault"`

      - `"vault"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

### Example

```cli
ant beta:vaults list \
  --api-key my-anthropic-api-key
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

`$ ant beta:vaults retrieve`

**get** `/v1/vaults/{vault_id}`

Get Vault

### Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```cli
ant beta:vaults retrieve \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
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

`$ ant beta:vaults update`

**post** `/v1/vaults/{vault_id}`

Update Vault

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--display-name: optional string`

  Body param: Updated human-readable name for the vault. 1-255 characters.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```cli
ant beta:vaults update \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
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

`$ ant beta:vaults delete`

**delete** `/v1/vaults/{vault_id}`

Delete Vault

### Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_vault: object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Example

```cli
ant beta:vaults delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

#### Response

```json
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

## Archive Vault

`$ ant beta:vaults archive`

**post** `/v1/vaults/{vault_id}/archive`

Archive Vault

### Parameters

- `--vault-id: string`

  Path parameter vault_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

### Example

```cli
ant beta:vaults archive \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
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

- `beta_managed_agents_deleted_vault: object { id, type }`

  Confirmation of a deleted vault.

  - `id: string`

    Unique identifier of the deleted vault.

  - `type: "vault_deleted"`

    - `"vault_deleted"`

### Beta Managed Agents Vault

- `beta_managed_agents_vault: object { id, archived_at, created_at, 4 more }`

  A vault that stores credentials for use by agents during sessions.

  - `id: string`

    Unique identifier for the vault.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the vault.

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the vault.

  - `type: "vault"`

    - `"vault"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

# Credentials

## Create Credential

`$ ant beta:vaults:credentials create`

**post** `/v1/vaults/{vault_id}/credentials`

Create Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--auth: BetaManagedAgentsMCPOAuthCreateParams or BetaManagedAgentsStaticBearerCreateParams or BetaManagedAgentsEnvironmentVariableCreateParams`

  Body param: Authentication details for creating a credential.

- `--display-name: optional string`

  Body param: Human-readable name for the credential. Up to 255 characters.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object { body, header }`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```cli
ant beta:vaults:credentials create \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --auth '{token: bearer_exampletoken, mcp_server_url: https://example-server.modelcontextprotocol.io/sse, type: static_bearer}'
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

`$ ant beta:vaults:credentials list`

**get** `/v1/vaults/{vault_id}/credentials`

List Credentials

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--include-archived: optional boolean`

  Query param: Whether to include archived credentials in the results.

- `--limit: optional number`

  Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

- `--page: optional string`

  Query param: Opaque pagination token from a previous `list_credentials` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListCredentialsResponse: object { data, next_page }`

  Response containing a paginated list of credentials.

  - `data: optional array of BetaManagedAgentsCredential`

    List of credentials.

    - `id: string`

      Unique identifier for the credential.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

      Authentication details for a credential.

      - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

        OAuth credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "mcp_oauth"`

          - `"mcp_oauth"`

        - `expires_at: optional string`

          A timestamp in RFC 3339 format

        - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

          OAuth refresh token configuration returned in credential responses.

          - `client_id: string`

            OAuth client ID.

          - `token_endpoint: string`

            Token endpoint URL used to refresh the access token.

          - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

            Token endpoint requires no client authentication.

            - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

              Token endpoint requires no client authentication.

              - `type: "none"`

                - `"none"`

            - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

              Token endpoint uses HTTP Basic authentication with client credentials.

              - `type: "client_secret_basic"`

                - `"client_secret_basic"`

            - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

              Token endpoint uses POST body authentication with client credentials.

              - `type: "client_secret_post"`

                - `"client_secret_post"`

          - `resource: optional string`

            OAuth resource indicator.

          - `scope: optional string`

            OAuth scope for the refresh request.

      - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

        Static bearer token credential details for an MCP server.

        - `mcp_server_url: string`

          URL of the MCP server this credential authenticates against.

        - `type: "static_bearer"`

          - `"static_bearer"`

      - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

        Environment variable credential details. The secret value is never returned.

        - `injection_location: object { body, header }`

          Where in the outbound request the secret value is substituted.

          - `body: boolean`

            Whether the placeholder is substituted in the request body.

          - `header: boolean`

            Whether the placeholder is substituted in request header values.

        - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

          Outbound hosts the secret value is substituted on.

          - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

            The secret is substituted on any host the session's Environment network policy permits egress to.

            - `type: "unrestricted"`

              - `"unrestricted"`

          - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

            The secret is substituted only on requests to the listed hosts.

            - `allowed_hosts: array of string`

              Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

            - `type: "limited"`

              - `"limited"`

        - `secret_name: string`

          Name of the environment variable.

        - `type: "environment_variable"`

          - `"environment_variable"`

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `metadata: map[string]`

      Arbitrary key-value metadata attached to the credential.

    - `type: "vault_credential"`

      - `"vault_credential"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `vault_id: string`

      Identifier of the vault this credential belongs to.

    - `display_name: optional string`

      Human-readable name for the credential.

  - `next_page: optional string`

    Pagination token for the next page, or null if no more results.

### Example

```cli
ant beta:vaults:credentials list \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
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

`$ ant beta:vaults:credentials retrieve`

**get** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Get Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object { body, header }`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```cli
ant beta:vaults:credentials retrieve \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
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

`$ ant beta:vaults:credentials update`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Update Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--auth: optional BetaManagedAgentsMCPOAuthUpdateParams or BetaManagedAgentsStaticBearerUpdateParams or BetaManagedAgentsEnvironmentVariableUpdateParams`

  Body param: Updated authentication details for a credential.

- `--display-name: optional string`

  Body param: Updated human-readable name for the credential. 1-255 characters.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object { body, header }`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```cli
ant beta:vaults:credentials update \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
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

`$ ant beta:vaults:credentials delete`

**delete** `/v1/vaults/{vault_id}/credentials/{credential_id}`

Delete Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_credential: object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Example

```cli
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

#### Response

```json
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

## Archive Credential

`$ ant beta:vaults:credentials archive`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/archive`

Archive Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential: object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object { body, header }`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Example

```cli
ant beta:vaults:credentials archive \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
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

`$ ant beta:vaults:credentials mcp-oauth-validate`

**post** `/v1/vaults/{vault_id}/credentials/{credential_id}/mcp_oauth_validate`

Validate Credential

### Parameters

- `--vault-id: string`

  Path param: Path parameter vault_id

- `--credential-id: string`

  Path param: Path parameter credential_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_credential_validation: object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object { http_response, method }`

    The failing step of an MCP validation probe.

    - `http_response: object { body, body_truncated, content_type, status_code }`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: object { http_response, status }`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: object { body, body_truncated, content_type, status_code }`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Example

```cli
ant beta:vaults:credentials mcp-oauth-validate \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
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

- `beta_managed_agents_credential: object { id, archived_at, auth, 6 more }`

  A credential stored in a vault. Sensitive fields are never returned in responses.

  - `id: string`

    Unique identifier for the credential.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `auth: BetaManagedAgentsMCPOAuthAuthResponse or BetaManagedAgentsStaticBearerAuthResponse or BetaManagedAgentsEnvironmentVariableAuthResponse`

    Authentication details for a credential.

    - `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

      OAuth credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "mcp_oauth"`

        - `"mcp_oauth"`

      - `expires_at: optional string`

        A timestamp in RFC 3339 format

      - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

        OAuth refresh token configuration returned in credential responses.

        - `client_id: string`

          OAuth client ID.

        - `token_endpoint: string`

          Token endpoint URL used to refresh the access token.

        - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

          Token endpoint requires no client authentication.

          - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

            Token endpoint requires no client authentication.

            - `type: "none"`

              - `"none"`

          - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

            Token endpoint uses HTTP Basic authentication with client credentials.

            - `type: "client_secret_basic"`

              - `"client_secret_basic"`

          - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

            Token endpoint uses POST body authentication with client credentials.

            - `type: "client_secret_post"`

              - `"client_secret_post"`

        - `resource: optional string`

          OAuth resource indicator.

        - `scope: optional string`

          OAuth scope for the refresh request.

    - `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

      Static bearer token credential details for an MCP server.

      - `mcp_server_url: string`

        URL of the MCP server this credential authenticates against.

      - `type: "static_bearer"`

        - `"static_bearer"`

    - `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

      Environment variable credential details. The secret value is never returned.

      - `injection_location: object { body, header }`

        Where in the outbound request the secret value is substituted.

        - `body: boolean`

          Whether the placeholder is substituted in the request body.

        - `header: boolean`

          Whether the placeholder is substituted in request header values.

      - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

        Outbound hosts the secret value is substituted on.

        - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

          The secret is substituted on any host the session's Environment network policy permits egress to.

          - `type: "unrestricted"`

            - `"unrestricted"`

        - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

          The secret is substituted only on requests to the listed hosts.

          - `allowed_hosts: array of string`

            Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

          - `type: "limited"`

            - `"limited"`

      - `secret_name: string`

        Name of the environment variable.

      - `type: "environment_variable"`

        - `"environment_variable"`

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata attached to the credential.

  - `type: "vault_credential"`

    - `"vault_credential"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault this credential belongs to.

  - `display_name: optional string`

    Human-readable name for the credential.

### Beta Managed Agents Credential Networking Params

- `beta_managed_agents_credential_networking_params: BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `beta_managed_agents_unrestricted_credential_networking_params: object { type }`

    Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

    - `type: "unrestricted"`

      - `"unrestricted"`

  - `beta_managed_agents_limited_credential_networking_params: object { allowed_hosts, type }`

    Substitute the secret only on requests to the listed hosts.

    - `allowed_hosts: array of string`

      Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

    - `type: "limited"`

      - `"limited"`

### Beta Managed Agents Credential Validation

- `beta_managed_agents_credential_validation: object { credential_id, has_refresh_token, mcp_probe, 5 more }`

  Result of live-probing a credential against its configured MCP server.

  - `credential_id: string`

    Unique identifier of the credential that was validated.

  - `has_refresh_token: boolean`

    Whether the credential has a refresh token configured.

  - `mcp_probe: object { http_response, method }`

    The failing step of an MCP validation probe.

    - `http_response: object { body, body_truncated, content_type, status_code }`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `method: string`

      The MCP method that failed (for example `initialize` or `tools/list`).

  - `refresh: object { http_response, status }`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `http_response: object { body, body_truncated, content_type, status_code }`

      An HTTP response captured during a credential validation probe.

      - `body: string`

        Response body. May be truncated and has sensitive values scrubbed.

      - `body_truncated: boolean`

        Whether `body` was truncated.

      - `content_type: string`

        Value of the `Content-Type` response header.

      - `status_code: number`

        HTTP status code.

    - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

      Outcome of a refresh-token exchange attempted during credential validation.

      - `"succeeded"`

      - `"failed"`

      - `"connect_error"`

      - `"no_refresh_token"`

  - `status: "valid" or "invalid" or "unknown"`

    Overall verdict of a credential validation probe.

    - `"valid"`

    - `"invalid"`

    - `"unknown"`

  - `type: "vault_credential_validation"`

    - `"vault_credential_validation"`

  - `validated_at: string`

    A timestamp in RFC 3339 format

  - `vault_id: string`

    Identifier of the vault containing the credential.

### Beta Managed Agents Credential Validation Status

- `beta_managed_agents_credential_validation_status: "valid" or "invalid" or "unknown"`

  Overall verdict of a credential validation probe.

  - `"valid"`

  - `"invalid"`

  - `"unknown"`

### Beta Managed Agents Deleted Credential

- `beta_managed_agents_deleted_credential: object { id, type }`

  Confirmation of a deleted credential.

  - `id: string`

    Unique identifier of the deleted credential.

  - `type: "vault_credential_deleted"`

    - `"vault_credential_deleted"`

### Beta Managed Agents Environment Variable Auth Response

- `beta_managed_agents_environment_variable_auth_response: object { injection_location, networking, secret_name, type }`

  Environment variable credential details. The secret value is never returned.

  - `injection_location: object { body, header }`

    Where in the outbound request the secret value is substituted.

    - `body: boolean`

      Whether the placeholder is substituted in the request body.

    - `header: boolean`

      Whether the placeholder is substituted in request header values.

  - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingResponse or BetaManagedAgentsLimitedCredentialNetworkingResponse`

    Outbound hosts the secret value is substituted on.

    - `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

      The secret is substituted on any host the session's Environment network policy permits egress to.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

      The secret is substituted only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable.

  - `type: "environment_variable"`

    - `"environment_variable"`

### Beta Managed Agents Environment Variable Create Params

- `beta_managed_agents_environment_variable_create_params: object { networking, secret_name, secret_value, 2 more }`

  Parameters for creating an environment variable credential.

  - `networking: BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

    Outbound hosts the secret value is substituted on.

    - `beta_managed_agents_unrestricted_credential_networking_params: object { type }`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `beta_managed_agents_limited_credential_networking_params: object { allowed_hosts, type }`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_name: string`

    Name of the environment variable. Immutable after create.

  - `secret_value: string`

    Secret value. Write-only; never returned in responses.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location: optional object { body, header }`

    Where in the outbound request the secret value may be substituted.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Environment Variable Update Params

- `beta_managed_agents_environment_variable_update_params: object { type, injection_location, networking, secret_value }`

  Parameters for updating an environment variable credential. `secret_name` is immutable.

  - `type: "environment_variable"`

    - `"environment_variable"`

  - `injection_location: optional object { body, header }`

    Updated injection location.

    - `body: optional boolean`

      Substitute when the placeholder appears in the request body.

    - `header: optional boolean`

      Substitute when the placeholder appears in a request header value.

  - `networking: optional BetaManagedAgentsUnrestrictedCredentialNetworkingParams or BetaManagedAgentsLimitedCredentialNetworkingParams`

    Updated networking scope. Full replacement.

    - `beta_managed_agents_unrestricted_credential_networking_params: object { type }`

      Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

      - `type: "unrestricted"`

        - `"unrestricted"`

    - `beta_managed_agents_limited_credential_networking_params: object { allowed_hosts, type }`

      Substitute the secret only on requests to the listed hosts.

      - `allowed_hosts: array of string`

        Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

      - `type: "limited"`

        - `"limited"`

  - `secret_value: optional string`

    Updated secret value.

### Beta Managed Agents Injection Location Params

- `beta_managed_agents_injection_location_params: object { body, header }`

  Where in the outbound request the secret value may be substituted.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Injection Location Response

- `beta_managed_agents_injection_location_response: object { body, header }`

  Where in the outbound request the secret value is substituted.

  - `body: boolean`

    Whether the placeholder is substituted in the request body.

  - `header: boolean`

    Whether the placeholder is substituted in request header values.

### Beta Managed Agents Injection Location Update Params

- `beta_managed_agents_injection_location_update_params: object { body, header }`

  Updated injection location.

  - `body: optional boolean`

    Substitute when the placeholder appears in the request body.

  - `header: optional boolean`

    Substitute when the placeholder appears in a request header value.

### Beta Managed Agents Limited Credential Networking Params

- `beta_managed_agents_limited_credential_networking_params: object { allowed_hosts, type }`

  Substitute the secret only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents Limited Credential Networking Response

- `beta_managed_agents_limited_credential_networking_response: object { allowed_hosts, type }`

  The secret is substituted only on requests to the listed hosts.

  - `allowed_hosts: array of string`

    Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

  - `type: "limited"`

    - `"limited"`

### Beta Managed Agents MCP OAuth Auth Response

- `beta_managed_agents_mcp_oauth_auth_response: object { mcp_server_url, type, expires_at, refresh }`

  OAuth credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

    OAuth refresh token configuration returned in credential responses.

    - `client_id: string`

      OAuth client ID.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

      Token endpoint requires no client authentication.

      - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

        Token endpoint uses POST body authentication with client credentials.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Create Params

- `beta_managed_agents_mcp_oauth_create_params: object { access_token, mcp_server_url, type, 2 more }`

  Parameters for creating an MCP OAuth credential.

  - `access_token: string`

    OAuth access token.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional object { client_id, refresh_token, token_endpoint, 3 more }`

    OAuth refresh token parameters for creating a credential with refresh support.

    - `client_id: string`

      OAuth client ID.

    - `refresh_token: string`

      OAuth refresh token.

    - `token_endpoint: string`

      Token endpoint URL used to refresh the access token.

    - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

      Token endpoint requires no client authentication.

      - `beta_managed_agents_token_endpoint_auth_none_param: object { type }`

        Token endpoint requires no client authentication.

        - `type: "none"`

          - `"none"`

      - `beta_managed_agents_token_endpoint_auth_basic_param: object { client_secret, type }`

        Token endpoint uses HTTP Basic authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

      - `beta_managed_agents_token_endpoint_auth_post_param: object { client_secret, type }`

        Token endpoint uses POST body authentication with client credentials.

        - `client_secret: string`

          OAuth client secret.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

    - `resource: optional string`

      OAuth resource indicator.

    - `scope: optional string`

      OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Params

- `beta_managed_agents_mcp_oauth_refresh_params: object { client_id, refresh_token, token_endpoint, 3 more }`

  OAuth refresh token parameters for creating a credential with refresh support.

  - `client_id: string`

    OAuth client ID.

  - `refresh_token: string`

    OAuth refresh token.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneParam or BetaManagedAgentsTokenEndpointAuthBasicParam or BetaManagedAgentsTokenEndpointAuthPostParam`

    Token endpoint requires no client authentication.

    - `beta_managed_agents_token_endpoint_auth_none_param: object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `beta_managed_agents_token_endpoint_auth_basic_param: object { client_secret, type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `beta_managed_agents_token_endpoint_auth_post_param: object { client_secret, type }`

      Token endpoint uses POST body authentication with client credentials.

      - `client_secret: string`

        OAuth client secret.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Response

- `beta_managed_agents_mcp_oauth_refresh_response: object { client_id, token_endpoint, token_endpoint_auth, 2 more }`

  OAuth refresh token configuration returned in credential responses.

  - `client_id: string`

    OAuth client ID.

  - `token_endpoint: string`

    Token endpoint URL used to refresh the access token.

  - `token_endpoint_auth: BetaManagedAgentsTokenEndpointAuthNoneResponse or BetaManagedAgentsTokenEndpointAuthBasicResponse or BetaManagedAgentsTokenEndpointAuthPostResponse`

    Token endpoint requires no client authentication.

    - `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

      Token endpoint requires no client authentication.

      - `type: "none"`

        - `"none"`

    - `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

      Token endpoint uses HTTP Basic authentication with client credentials.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

    - `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

      Token endpoint uses POST body authentication with client credentials.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

  - `resource: optional string`

    OAuth resource indicator.

  - `scope: optional string`

    OAuth scope for the refresh request.

### Beta Managed Agents MCP OAuth Refresh Update Params

- `beta_managed_agents_mcp_oauth_refresh_update_params: object { refresh_token, scope, token_endpoint_auth }`

  Parameters for updating OAuth refresh token configuration.

  - `refresh_token: optional string`

    Updated OAuth refresh token.

  - `scope: optional string`

    Updated OAuth scope for the refresh request.

  - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

    Updated HTTP Basic authentication parameters for the token endpoint.

    - `beta_managed_agents_token_endpoint_auth_basic_update_param: object { type, client_secret }`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `type: "client_secret_basic"`

        - `"client_secret_basic"`

      - `client_secret: optional string`

        Updated OAuth client secret.

    - `beta_managed_agents_token_endpoint_auth_post_update_param: object { type, client_secret }`

      Updated POST body authentication parameters for the token endpoint.

      - `type: "client_secret_post"`

        - `"client_secret_post"`

      - `client_secret: optional string`

        Updated OAuth client secret.

### Beta Managed Agents MCP OAuth Update Params

- `beta_managed_agents_mcp_oauth_update_params: object { type, access_token, expires_at, refresh }`

  Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

  - `type: "mcp_oauth"`

    - `"mcp_oauth"`

  - `access_token: optional string`

    Updated OAuth access token.

  - `expires_at: optional string`

    A timestamp in RFC 3339 format

  - `refresh: optional object { refresh_token, scope, token_endpoint_auth }`

    Parameters for updating OAuth refresh token configuration.

    - `refresh_token: optional string`

      Updated OAuth refresh token.

    - `scope: optional string`

      Updated OAuth scope for the refresh request.

    - `token_endpoint_auth: optional BetaManagedAgentsTokenEndpointAuthBasicUpdateParam or BetaManagedAgentsTokenEndpointAuthPostUpdateParam`

      Updated HTTP Basic authentication parameters for the token endpoint.

      - `beta_managed_agents_token_endpoint_auth_basic_update_param: object { type, client_secret }`

        Updated HTTP Basic authentication parameters for the token endpoint.

        - `type: "client_secret_basic"`

          - `"client_secret_basic"`

        - `client_secret: optional string`

          Updated OAuth client secret.

      - `beta_managed_agents_token_endpoint_auth_post_update_param: object { type, client_secret }`

        Updated POST body authentication parameters for the token endpoint.

        - `type: "client_secret_post"`

          - `"client_secret_post"`

        - `client_secret: optional string`

          Updated OAuth client secret.

### Beta Managed Agents MCP Probe

- `beta_managed_agents_mcp_probe: object { http_response, method }`

  The failing step of an MCP validation probe.

  - `http_response: object { body, body_truncated, content_type, status_code }`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `method: string`

    The MCP method that failed (for example `initialize` or `tools/list`).

### Beta Managed Agents Refresh HTTP Response

- `beta_managed_agents_refresh_http_response: object { body, body_truncated, content_type, status_code }`

  An HTTP response captured during a credential validation probe.

  - `body: string`

    Response body. May be truncated and has sensitive values scrubbed.

  - `body_truncated: boolean`

    Whether `body` was truncated.

  - `content_type: string`

    Value of the `Content-Type` response header.

  - `status_code: number`

    HTTP status code.

### Beta Managed Agents Refresh Object

- `beta_managed_agents_refresh_object: object { http_response, status }`

  Outcome of a refresh-token exchange attempted during credential validation.

  - `http_response: object { body, body_truncated, content_type, status_code }`

    An HTTP response captured during a credential validation probe.

    - `body: string`

      Response body. May be truncated and has sensitive values scrubbed.

    - `body_truncated: boolean`

      Whether `body` was truncated.

    - `content_type: string`

      Value of the `Content-Type` response header.

    - `status_code: number`

      HTTP status code.

  - `status: "succeeded" or "failed" or "connect_error" or "no_refresh_token"`

    Outcome of a refresh-token exchange attempted during credential validation.

    - `"succeeded"`

    - `"failed"`

    - `"connect_error"`

    - `"no_refresh_token"`

### Beta Managed Agents Static Bearer Auth Response

- `beta_managed_agents_static_bearer_auth_response: object { mcp_server_url, type }`

  Static bearer token credential details for an MCP server.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Create Params

- `beta_managed_agents_static_bearer_create_params: object { token, mcp_server_url, type }`

  Parameters for creating a static bearer token credential.

  - `token: string`

    Static bearer token value.

  - `mcp_server_url: string`

    URL of the MCP server this credential authenticates against.

  - `type: "static_bearer"`

    - `"static_bearer"`

### Beta Managed Agents Static Bearer Update Params

- `beta_managed_agents_static_bearer_update_params: object { type, token }`

  Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

  - `type: "static_bearer"`

    - `"static_bearer"`

  - `token: optional string`

    Updated static bearer token value.

### Beta Managed Agents Token Endpoint Auth Basic Param

- `beta_managed_agents_token_endpoint_auth_basic_param: object { client_secret, type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Response

- `beta_managed_agents_token_endpoint_auth_basic_response: object { type }`

  Token endpoint uses HTTP Basic authentication with client credentials.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

### Beta Managed Agents Token Endpoint Auth Basic Update Param

- `beta_managed_agents_token_endpoint_auth_basic_update_param: object { type, client_secret }`

  Updated HTTP Basic authentication parameters for the token endpoint.

  - `type: "client_secret_basic"`

    - `"client_secret_basic"`

  - `client_secret: optional string`

    Updated OAuth client secret.

### Beta Managed Agents Token Endpoint Auth None Param

- `beta_managed_agents_token_endpoint_auth_none_param: object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth None Response

- `beta_managed_agents_token_endpoint_auth_none_response: object { type }`

  Token endpoint requires no client authentication.

  - `type: "none"`

    - `"none"`

### Beta Managed Agents Token Endpoint Auth Post Param

- `beta_managed_agents_token_endpoint_auth_post_param: object { client_secret, type }`

  Token endpoint uses POST body authentication with client credentials.

  - `client_secret: string`

    OAuth client secret.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Response

- `beta_managed_agents_token_endpoint_auth_post_response: object { type }`

  Token endpoint uses POST body authentication with client credentials.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

### Beta Managed Agents Token Endpoint Auth Post Update Param

- `beta_managed_agents_token_endpoint_auth_post_update_param: object { type, client_secret }`

  Updated POST body authentication parameters for the token endpoint.

  - `type: "client_secret_post"`

    - `"client_secret_post"`

  - `client_secret: optional string`

    Updated OAuth client secret.

### Beta Managed Agents Unrestricted Credential Networking Params

- `beta_managed_agents_unrestricted_credential_networking_params: object { type }`

  Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

  - `type: "unrestricted"`

    - `"unrestricted"`

### Beta Managed Agents Unrestricted Credential Networking Response

- `beta_managed_agents_unrestricted_credential_networking_response: object { type }`

  The secret is substituted on any host the session's Environment network policy permits egress to.

  - `type: "unrestricted"`

    - `"unrestricted"`

# Memory Stores

## Create a memory store

`$ ant beta:memory-stores create`

**post** `/v1/memory_stores`

Create a memory store

### Parameters

- `--name: string`

  Body param: Human-readable name for the store. Required; 1–255 characters; no control characters. The mount-path slug under `/mnt/memory/` is derived from this name (lowercased, non-alphanumeric runs collapsed to a hyphen). Names need not be unique within a workspace.

- `--description: optional string`

  Body param: Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent.

- `--metadata: optional map[string]`

  Body param: Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Not visible to the agent.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_store: object { id, created_at, name, 5 more }`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```cli
ant beta:memory-stores create \
  --api-key my-anthropic-api-key \
  --name x
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

`$ ant beta:memory-stores list`

**get** `/v1/memory_stores`

List memory stores

### Parameters

- `--created-at-gte: optional string`

  Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

- `--created-at-lte: optional string`

  Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

- `--include-archived: optional boolean`

  Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

- `--limit: optional number`

  Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

- `--page: optional string`

  Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryStoresResponse: object { data, next_page }`

  A page of `memory_store` results, ordered by `created_at` descending (newest first).

  - `data: optional array of BetaManagedAgentsMemoryStore`

    Memory stores on this page, newest first. Empty when there are no stores matching the filters.

    - `id: string`

      Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `name: string`

      Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

    - `type: "memory_store"`

      - `"memory_store"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `archived_at: optional string`

      A timestamp in RFC 3339 format

    - `description: optional string`

      Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

    - `metadata: optional map[string]`

      Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

### Example

```cli
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
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

`$ ant beta:memory-stores retrieve`

**get** `/v1/memory_stores/{memory_store_id}`

Retrieve a memory store

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_store: object { id, created_at, name, 5 more }`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```cli
ant beta:memory-stores retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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

`$ ant beta:memory-stores update`

**post** `/v1/memory_stores/{memory_store_id}`

Update a memory store

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--description: optional string`

  Body param: New description for the store, up to 1024 characters. Pass an empty string to clear it.

- `--metadata: optional map[string]`

  Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

- `--name: optional string`

  Body param: New human-readable name for the store. 1–255 characters; no control characters. Renaming changes the slug used for the store's `mount_path` in sessions created after the update.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_store: object { id, created_at, name, 5 more }`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```cli
ant beta:memory-stores update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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

`$ ant beta:memory-stores delete`

**delete** `/v1/memory_stores/{memory_store_id}`

Delete a memory store

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_memory_store: object { id, type }`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Example

```cli
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

#### Response

```json
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

## Archive a memory store

`$ ant beta:memory-stores archive`

**post** `/v1/memory_stores/{memory_store_id}/archive`

Archive a memory store

### Parameters

- `--memory-store-id: string`

  Path parameter memory_store_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_store: object { id, created_at, name, 5 more }`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

### Example

```cli
ant beta:memory-stores archive \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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

- `beta_managed_agents_deleted_memory_store: object { id, type }`

  Confirmation that a `memory_store` was deleted.

  - `id: string`

    ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

  - `type: "memory_store_deleted"`

    - `"memory_store_deleted"`

### Beta Managed Agents Memory Store

- `beta_managed_agents_memory_store: object { id, created_at, name, 5 more }`

  A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

  - `id: string`

    Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `name: string`

    Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

  - `type: "memory_store"`

    - `"memory_store"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `archived_at: optional string`

    A timestamp in RFC 3339 format

  - `description: optional string`

    Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

  - `metadata: optional map[string]`

    Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

# Memories

## Create a memory

`$ ant beta:memory-stores:memories create`

**post** `/v1/memory_stores/{memory_store_id}/memories`

Create a memory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--content: string`

  Body param: UTF-8 text content for the new memory. Maximum 100 kB (102,400 bytes). Required; pass `""` explicitly to create an empty memory.

- `--path: string`

  Body param: Hierarchical path for the new memory, e.g. `/projects/foo/notes.md`. Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive.

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```cli
ant beta:memory-stores:memories create \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --content content \
  --path xx
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

`$ ant beta:memory-stores:memories list`

**get** `/v1/memory_stores/{memory_store_id}/memories`

List memories

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--depth: optional number`

  Query param: `0` (or omitted) returns all descendants below `path_prefix` (recursive). `1` returns immediate children only; deeper entries roll up as `memory_prefix` items. `depth=1` behaves like `ls`; omitting `depth` behaves like `find`.

- `--limit: optional number`

  Query param: Maximum number of items to return per page. Must be between 1 and 100. Defaults to 20 when omitted. Capped at 20 when `view=full`. Both `memory` and `memory_prefix` items count toward the limit.

- `--page: optional string`

  Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

- `--path-prefix: optional string`

  Query param: Optional path prefix filter. Must end with `/` (segment-aligned), e.g., `/notes/`. This value appears in request URLs. Do not include secrets or personally identifiable information.

- `--view: optional "basic" or "full"`

  Query param: Which projection of each `memory` to return. Defaults to `basic` (content omitted). `full` populates `content` on each item and caps `limit` at 20; use this as the bulk-read path for export and sync.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoriesResult: object { data, next_page }`

  Response payload for [List memories](/docs/en/api/beta/memory_stores/memories/list).

  - `data: optional array of BetaManagedAgentsMemoryListItem`

    One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items are returned in a stable, server-defined order.

    - `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

      A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

      - `id: string`

        Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

      - `content_sha256: string`

        Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

      - `content_size_bytes: number`

        Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

      - `created_at: string`

        A timestamp in RFC 3339 format

      - `memory_store_id: string`

        ID of the memory store this memory belongs to (a `memstore_...` value).

      - `memory_version_id: string`

        ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

      - `path: string`

        Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

      - `type: "memory"`

        - `"memory"`

      - `updated_at: string`

        A timestamp in RFC 3339 format

      - `content: optional string`

        The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

    - `beta_managed_agents_memory_prefix: object { path, type }`

      A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

      - `path: string`

        The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

      - `type: "memory_prefix"`

        - `"memory_prefix"`

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```cli
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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

`$ ant beta:memory-stores:memories retrieve`

**get** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Retrieve a memory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```cli
ant beta:memory-stores:memories retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
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

`$ ant beta:memory-stores:memories update`

**post** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Update a memory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--content: optional string`

  Body param: New UTF-8 text content for the memory. Maximum 100 kB (102,400 bytes). Omit to leave the content unchanged (e.g., for a rename-only update).

- `--path: optional string`

  Body param: New path for the memory (a rename). Must start with `/`, contain at least one non-empty segment, and be at most 1,024 bytes. Must not contain empty segments, `.` or `..` segments, control or format characters, and must be NFC-normalized. Paths are case-sensitive. The memory's `id` is preserved across renames. Omit to leave the path unchanged.

- `--precondition: optional object { type, content_sha256 }`

  Body param: Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Example

```cli
ant beta:memory-stores:memories update \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
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

`$ ant beta:memory-stores:memories delete`

**delete** `/v1/memory_stores/{memory_store_id}/memories/{memory_id}`

Delete a memory

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-id: string`

  Path param: Path parameter memory_id

- `--expected-content-sha256: optional string`

  Query param: Query parameter for expected_content_sha256

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_deleted_memory: object { id, type }`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Example

```cli
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
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

- `beta_managed_agents_conflict_error: object { type, message }`

  - `type: "conflict_error"`

    - `"conflict_error"`

  - `message: optional string`

### Beta Managed Agents Content Sha256 Precondition

- `beta_managed_agents_content_sha256_precondition: object { type, content_sha256 }`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

### Beta Managed Agents Deleted Memory

- `beta_managed_agents_deleted_memory: object { id, type }`

  Tombstone returned by [Delete a memory](/docs/en/api/beta/memory_stores/memories/delete). The memory's version history persists and remains listable via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) until the store itself is deleted.

  - `id: string`

    ID of the deleted memory (a `mem_...` value).

  - `type: "memory_deleted"`

    - `"memory_deleted"`

### Beta Managed Agents Error

- `beta_managed_agents_error: BetaInvalidRequestError or BetaAuthenticationError or BetaBillingError or 9 more`

  - `beta_invalid_request_error: object { message, type }`

    - `message: string`

    - `type: "invalid_request_error"`

  - `beta_authentication_error: object { message, type }`

    - `message: string`

    - `type: "authentication_error"`

  - `beta_billing_error: object { message, type }`

    - `message: string`

    - `type: "billing_error"`

  - `beta_permission_error: object { message, type }`

    - `message: string`

    - `type: "permission_error"`

  - `beta_not_found_error: object { message, type }`

    - `message: string`

    - `type: "not_found_error"`

  - `beta_rate_limit_error: object { message, type }`

    - `message: string`

    - `type: "rate_limit_error"`

  - `beta_gateway_timeout_error: object { message, type }`

    - `message: string`

    - `type: "timeout_error"`

  - `beta_api_error: object { message, type }`

    - `message: string`

    - `type: "api_error"`

  - `beta_overloaded_error: object { message, type }`

    - `message: string`

    - `type: "overloaded_error"`

  - `beta_managed_agents_memory_precondition_failed_error: object { type, message }`

    - `type: "memory_precondition_failed_error"`

      - `"memory_precondition_failed_error"`

    - `message: optional string`

  - `beta_managed_agents_memory_path_conflict_error: object { type, conflicting_memory_id, conflicting_path, message }`

    - `type: "memory_path_conflict_error"`

      - `"memory_path_conflict_error"`

    - `conflicting_memory_id: optional string`

    - `conflicting_path: optional string`

    - `message: optional string`

  - `beta_managed_agents_conflict_error: object { type, message }`

    - `type: "conflict_error"`

      - `"conflict_error"`

    - `message: optional string`

### Beta Managed Agents Memory

- `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

  A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

  - `id: string`

    Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

  - `content_sha256: string`

    Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

  - `content_size_bytes: number`

    Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_store_id: string`

    ID of the memory store this memory belongs to (a `memstore_...` value).

  - `memory_version_id: string`

    ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `path: string`

    Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

  - `type: "memory"`

    - `"memory"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `content: optional string`

    The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

### Beta Managed Agents Memory List Item

- `beta_managed_agents_memory_list_item: BetaManagedAgentsMemory or BetaManagedAgentsMemoryPrefix`

  One item in a [List memories](/docs/en/api/beta/memory_stores/memories/list) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

  - `beta_managed_agents_memory: object { id, content_sha256, content_size_bytes, 7 more }`

    A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

    - `id: string`

      Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

    - `content_sha256: string`

      Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

    - `content_size_bytes: number`

      Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_store_id: string`

      ID of the memory store this memory belongs to (a `memstore_...` value).

    - `memory_version_id: string`

      ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

    - `path: string`

      Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

    - `type: "memory"`

      - `"memory"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `content: optional string`

      The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

  - `beta_managed_agents_memory_prefix: object { path, type }`

    A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

    - `path: string`

      The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

    - `type: "memory_prefix"`

      - `"memory_prefix"`

### Beta Managed Agents Memory Path Conflict Error

- `beta_managed_agents_memory_path_conflict_error: object { type, conflicting_memory_id, conflicting_path, message }`

  - `type: "memory_path_conflict_error"`

    - `"memory_path_conflict_error"`

  - `conflicting_memory_id: optional string`

  - `conflicting_path: optional string`

  - `message: optional string`

### Beta Managed Agents Memory Precondition Failed Error

- `beta_managed_agents_memory_precondition_failed_error: object { type, message }`

  - `type: "memory_precondition_failed_error"`

    - `"memory_precondition_failed_error"`

  - `message: optional string`

### Beta Managed Agents Memory Prefix

- `beta_managed_agents_memory_prefix: object { path, type }`

  A rolled-up directory marker returned by [List memories](/docs/en/api/beta/memory_stores/memories/list) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

  - `path: string`

    The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

  - `type: "memory_prefix"`

    - `"memory_prefix"`

### Beta Managed Agents Memory View

- `beta_managed_agents_memory_view: "basic" or "full"`

  Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

  - `"basic"`

  - `"full"`

### Beta Managed Agents Precondition

- `beta_managed_agents_precondition: object { type, content_sha256 }`

  Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

  - `type: "content_sha256"`

    - `"content_sha256"`

  - `content_sha256: optional string`

    Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

# Memory Versions

## List memory versions

`$ ant beta:memory-stores:memory-versions list`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions`

List memory versions

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--api-key-id: optional string`

  Query param: Query parameter for api_key_id

- `--created-at-gte: optional string`

  Query param: Return versions created at or after this time (inclusive).

- `--created-at-lte: optional string`

  Query param: Return versions created at or before this time (inclusive).

- `--limit: optional number`

  Query param: Query parameter for limit

- `--memory-id: optional string`

  Query param: Query parameter for memory_id

- `--operation: optional "created" or "modified" or "deleted"`

  Query param: Query parameter for operation

- `--page: optional string`

  Query param: Query parameter for page

- `--session-id: optional string`

  Query param: Query parameter for session_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaManagedAgentsListMemoryVersionsResult: object { data, next_page }`

  Response payload for [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list).

  - `data: optional array of BetaManagedAgentsMemoryVersion`

    One page of `memory_version` objects, ordered by `created_at` descending (newest first), with `id` as tiebreak.

    - `id: string`

      Unique identifier for this version (a `memver_...` value).

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `memory_id: string`

      ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

    - `memory_store_id: string`

      ID of the memory store this version belongs to (a `memstore_...` value).

    - `operation: "created" or "modified" or "deleted"`

      The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

      - `"created"`

      - `"modified"`

      - `"deleted"`

    - `type: "memory_version"`

      - `"memory_version"`

    - `content: optional string`

      The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

    - `content_sha256: optional string`

      Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `content_size_bytes: optional number`

      Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

    - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `beta_managed_agents_session_actor: object { session_id, type }`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

        - `session_id: string`

          ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

        - `type: "session_actor"`

          - `"session_actor"`

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        Attribution for a write made directly via the public API (outside of any session).

        - `api_key_id: string`

          ID of the API key that performed the write. This identifies the key, not the secret.

        - `type: "api_actor"`

          - `"api_actor"`

      - `beta_managed_agents_user_actor: object { type, user_id }`

        Attribution for a write made by a human user through the Anthropic Console.

        - `type: "user_actor"`

          - `"user_actor"`

        - `user_id: string`

          ID of the user who performed the write (a `user_...` value).

    - `path: optional string`

      The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

    - `redacted_at: optional string`

      A timestamp in RFC 3339 format

    - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

      Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

      - `beta_managed_agents_session_actor: object { session_id, type }`

        Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `beta_managed_agents_api_actor: object { api_key_id, type }`

        Attribution for a write made directly via the public API (outside of any session).

      - `beta_managed_agents_user_actor: object { type, user_id }`

        Attribution for a write made by a human user through the Anthropic Console.

  - `next_page: optional string`

    Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

### Example

```cli
ant beta:memory-stores:memory-versions list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
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

`$ ant beta:memory-stores:memory-versions retrieve`

**get** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}`

Retrieve a memory version

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--view: optional "basic" or "full"`

  Query param: Query parameter for view

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

### Example

```cli
ant beta:memory-stores:memory-versions retrieve \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
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

`$ ant beta:memory-stores:memory-versions redact`

**post** `/v1/memory_stores/{memory_store_id}/memory_versions/{memory_version_id}/redact`

Redact a memory version

### Parameters

- `--memory-store-id: string`

  Path param: Path parameter memory_store_id

- `--memory-version-id: string`

  Path param: Path parameter memory_version_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

### Example

```cli
ant beta:memory-stores:memory-versions redact \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-version-id memory_version_id
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

- `beta_managed_agents_actor: BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

  Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

  - `beta_managed_agents_session_actor: object { session_id, type }`

    Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `session_id: string`

      ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

    - `type: "session_actor"`

      - `"session_actor"`

  - `beta_managed_agents_api_actor: object { api_key_id, type }`

    Attribution for a write made directly via the public API (outside of any session).

    - `api_key_id: string`

      ID of the API key that performed the write. This identifies the key, not the secret.

    - `type: "api_actor"`

      - `"api_actor"`

  - `beta_managed_agents_user_actor: object { type, user_id }`

    Attribution for a write made by a human user through the Anthropic Console.

    - `type: "user_actor"`

      - `"user_actor"`

    - `user_id: string`

      ID of the user who performed the write (a `user_...` value).

### Beta Managed Agents API Actor

- `beta_managed_agents_api_actor: object { api_key_id, type }`

  Attribution for a write made directly via the public API (outside of any session).

  - `api_key_id: string`

    ID of the API key that performed the write. This identifies the key, not the secret.

  - `type: "api_actor"`

    - `"api_actor"`

### Beta Managed Agents Memory Version

- `beta_managed_agents_memory_version: object { id, created_at, memory_id, 10 more }`

  A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

  - `id: string`

    Unique identifier for this version (a `memver_...` value).

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `memory_id: string`

    ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](/docs/en/api/beta/memory_stores/memory_versions/list) to retrieve the full lineage including the `deleted` row.

  - `memory_store_id: string`

    ID of the memory store this version belongs to (a `memstore_...` value).

  - `operation: "created" or "modified" or "deleted"`

    The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

    - `"created"`

    - `"modified"`

    - `"deleted"`

  - `type: "memory_version"`

    - `"memory_version"`

  - `content: optional string`

    The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

  - `content_sha256: optional string`

    Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `content_size_bytes: optional number`

    Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

  - `created_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

      - `session_id: string`

        ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

      - `type: "session_actor"`

        - `"session_actor"`

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

      - `api_key_id: string`

        ID of the API key that performed the write. This identifies the key, not the secret.

      - `type: "api_actor"`

        - `"api_actor"`

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

      - `type: "user_actor"`

        - `"user_actor"`

      - `user_id: string`

        ID of the user who performed the write (a `user_...` value).

  - `path: optional string`

    The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

  - `redacted_at: optional string`

    A timestamp in RFC 3339 format

  - `redacted_by: optional BetaManagedAgentsSessionActor or BetaManagedAgentsAPIActor or BetaManagedAgentsUserActor`

    Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](/docs/en/api/sessions-retrieve).

    - `beta_managed_agents_session_actor: object { session_id, type }`

      Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

    - `beta_managed_agents_api_actor: object { api_key_id, type }`

      Attribution for a write made directly via the public API (outside of any session).

    - `beta_managed_agents_user_actor: object { type, user_id }`

      Attribution for a write made by a human user through the Anthropic Console.

### Beta Managed Agents Memory Version Operation

- `beta_managed_agents_memory_version_operation: "created" or "modified" or "deleted"`

  The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

  - `"created"`

  - `"modified"`

  - `"deleted"`

### Beta Managed Agents Session Actor

- `beta_managed_agents_session_actor: object { session_id, type }`

  Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

  - `session_id: string`

    ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](/docs/en/api/sessions-retrieve) for further provenance.

  - `type: "session_actor"`

    - `"session_actor"`

### Beta Managed Agents User Actor

- `beta_managed_agents_user_actor: object { type, user_id }`

  Attribution for a write made by a human user through the Anthropic Console.

  - `type: "user_actor"`

    - `"user_actor"`

  - `user_id: string`

    ID of the user who performed the write (a `user_...` value).

# Files

## Upload File

`$ ant beta:files upload`

**post** `/v1/files`

Upload File

### Parameters

- `--file: string`

  Body param: The file to upload

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `file_metadata: object { id, created_at, filename, 5 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional object { id, type }`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

### Example

```cli
ant beta:files upload \
  --api-key my-anthropic-api-key \
  --file 'Example data'
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

`$ ant beta:files list`

**get** `/v1/files`

List Files

### Parameters

- `--after-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.

- `--before-id: optional string`

  Query param: ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--scope-id: optional string`

  Query param: Filter by scope ID. Only returns files associated with the specified scope (e.g., a session ID).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaFileListResponse: object { data, first_id, has_more, last_id }`

  - `data: array of FileMetadata`

    List of file metadata objects.

    - `id: string`

      Unique object identifier.

      The format and length of IDs may change over time.

    - `created_at: string`

      RFC 3339 datetime string representing when the file was created.

    - `filename: string`

      Original filename of the uploaded file.

    - `mime_type: string`

      MIME type of the file.

    - `size_bytes: number`

      Size of the file in bytes.

    - `type: "file"`

      Object type.

      For files, this is always `"file"`.

    - `downloadable: optional boolean`

      Whether the file can be downloaded.

    - `scope: optional object { id, type }`

      The scope of this file, indicating the context in which it was created (e.g., a session).

      - `id: string`

        The ID of the scoping resource (e.g., the session ID).

      - `type: "session"`

        The type of scope (e.g., `"session"`).

  - `first_id: optional string`

    ID of the first file in this page of results.

  - `has_more: optional boolean`

    Whether there are more results available.

  - `last_id: optional string`

    ID of the last file in this page of results.

### Example

```cli
ant beta:files list \
  --api-key my-anthropic-api-key
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

`$ ant beta:files download`

**get** `/v1/files/{file_id}/content`

Download File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `unnamed_schema_0: file path`

### Example

```cli
ant beta:files download \
  --api-key my-anthropic-api-key \
  --file-id file_id
```

## Get File Metadata

`$ ant beta:files retrieve-metadata`

**get** `/v1/files/{file_id}`

Get File Metadata

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `file_metadata: object { id, created_at, filename, 5 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional object { id, type }`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

### Example

```cli
ant beta:files retrieve-metadata \
  --api-key my-anthropic-api-key \
  --file-id file_id
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

`$ ant beta:files delete`

**delete** `/v1/files/{file_id}`

Delete File

### Parameters

- `--file-id: string`

  ID of the File.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### Example

```cli
ant beta:files delete \
  --api-key my-anthropic-api-key \
  --file-id file_id
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

- `beta_file_scope: object { id, type }`

  - `id: string`

    The ID of the scoping resource (e.g., the session ID).

  - `type: "session"`

    The type of scope (e.g., `"session"`).

### Deleted File

- `deleted_file: object { id, type }`

  - `id: string`

    ID of the deleted file.

  - `type: optional "file_deleted"`

    Deleted object type.

    For file deletion, this is always `"file_deleted"`.

    - `"file_deleted"`

### File Metadata

- `file_metadata: object { id, created_at, filename, 5 more }`

  - `id: string`

    Unique object identifier.

    The format and length of IDs may change over time.

  - `created_at: string`

    RFC 3339 datetime string representing when the file was created.

  - `filename: string`

    Original filename of the uploaded file.

  - `mime_type: string`

    MIME type of the file.

  - `size_bytes: number`

    Size of the file in bytes.

  - `type: "file"`

    Object type.

    For files, this is always `"file"`.

  - `downloadable: optional boolean`

    Whether the file can be downloaded.

  - `scope: optional object { id, type }`

    The scope of this file, indicating the context in which it was created (e.g., a session).

    - `id: string`

      The ID of the scoping resource (e.g., the session ID).

    - `type: "session"`

      The type of scope (e.g., `"session"`).

# Skills

## Create Skill

`$ ant beta:skills create`

**post** `/v1/skills`

Create Skill

### Parameters

- `--file: array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--display-title: optional string`

  Body param: Display title for the skill.

  This is a human-readable label that is not included in the prompt sent to the model.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillNewResponse: object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```cli
ant beta:skills create \
  --api-key my-anthropic-api-key \
  --file 'Example data'
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

`$ ant beta:skills list`

**get** `/v1/skills`

List Skills

### Parameters

- `--limit: optional number`

  Query param: Number of results to return per page.

  Maximum value is 100. Defaults to 20.

- `--page: optional string`

  Query param: Pagination token for fetching a specific page of results.

  Pass the value from a previous response's `next_page` field to get the next page of results.

- `--source: optional string`

  Query param: Filter skills by source.

  If provided, only skills from the specified source will be returned:

  * `"custom"`: only return user-created skills
  * `"anthropic"`: only return Anthropic-created skills

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListSkillsResponse: object { data, has_more, next_page }`

  - `data: array of object { id, created_at, display_title, 4 more }`

    List of skills.

    - `id: string`

      Unique identifier for the skill.

      The format and length of IDs may change over time.

    - `created_at: string`

      ISO 8601 timestamp of when the skill was created.

    - `display_title: string`

      Display title for the skill.

      This is a human-readable label that is not included in the prompt sent to the model.

    - `latest_version: string`

      The latest version identifier for the skill.

      This represents the most recent version of the skill that has been created.

    - `source: string`

      Source of the skill.

      This may be one of the following values:

      * `"custom"`: the skill was created by a user
      * `"anthropic"`: the skill was created by Anthropic

    - `type: string`

      Object type.

      For Skills, this is always `"skill"`.

    - `updated_at: string`

      ISO 8601 timestamp of when the skill was last updated.

  - `has_more: boolean`

    Whether there are more results available.

    If `true`, there are additional results that can be fetched using the `next_page` token.

  - `next_page: string`

    Token for fetching the next page of results.

    If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

### Example

```cli
ant beta:skills list \
  --api-key my-anthropic-api-key
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

`$ ant beta:skills retrieve`

**get** `/v1/skills/{skill_id}`

Get Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillGetResponse: object { id, created_at, display_title, 4 more }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill was created.

  - `display_title: string`

    Display title for the skill.

    This is a human-readable label that is not included in the prompt sent to the model.

  - `latest_version: string`

    The latest version identifier for the skill.

    This represents the most recent version of the skill that has been created.

  - `source: string`

    Source of the skill.

    This may be one of the following values:

    * `"custom"`: the skill was created by a user
    * `"anthropic"`: the skill was created by Anthropic

  - `type: string`

    Object type.

    For Skills, this is always `"skill"`.

  - `updated_at: string`

    ISO 8601 timestamp of when the skill was last updated.

### Example

```cli
ant beta:skills retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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

`$ ant beta:skills delete`

**delete** `/v1/skills/{skill_id}`

Delete Skill

### Parameters

- `--skill-id: string`

  Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillDeleteResponse: object { id, type }`

  - `id: string`

    Unique identifier for the skill.

    The format and length of IDs may change over time.

  - `type: string`

    Deleted object type.

    For Skills, this is always `"skill_deleted"`.

### Example

```cli
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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

`$ ant beta:skills:versions create`

**post** `/v1/skills/{skill_id}/versions`

Create Skill Version

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--file: array of string`

  Body param: Files to upload for the skill.

  All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillVersionNewResponse: object { id, created_at, description, 5 more }`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```cli
ant beta:skills:versions create \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --file 'Example data'
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

`$ ant beta:skills:versions list`

**get** `/v1/skills/{skill_id}/versions`

List Skill Versions

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--limit: optional number`

  Query param: Number of items to return per page.

  Defaults to `20`. Ranges from `1` to `1000`.

- `--page: optional string`

  Query param: Optionally set to the `next_page` token from the previous response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListSkillVersionsResponse: object { data, has_more, next_page }`

  - `data: array of object { id, created_at, description, 5 more }`

    List of skill versions.

    - `id: string`

      Unique identifier for the skill version.

      The format and length of IDs may change over time.

    - `created_at: string`

      ISO 8601 timestamp of when the skill version was created.

    - `description: string`

      Description of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `directory: string`

      Directory name of the skill version.

      This is the top-level directory name that was extracted from the uploaded files.

    - `name: string`

      Human-readable name of the skill version.

      This is extracted from the SKILL.md file in the skill upload.

    - `skill_id: string`

      Identifier for the skill that this version belongs to.

    - `type: string`

      Object type.

      For Skill Versions, this is always `"skill_version"`.

    - `version: string`

      Version identifier for the skill.

      Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `has_more: boolean`

    Indicates if there are more results in the requested page direction.

  - `next_page: string`

    Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### Example

```cli
ant beta:skills:versions list \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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

`$ ant beta:skills:versions download`

**get** `/v1/skills/{skill_id}/versions/{version}/content`

Download a skill version's content as a zip archive.

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `unnamed_schema_1: file path`

### Example

```cli
ant beta:skills:versions download \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

## Get Skill Version

`$ ant beta:skills:versions retrieve`

**get** `/v1/skills/{skill_id}/versions/{version}`

Get Skill Version

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillVersionGetResponse: object { id, created_at, description, 5 more }`

  - `id: string`

    Unique identifier for the skill version.

    The format and length of IDs may change over time.

  - `created_at: string`

    ISO 8601 timestamp of when the skill version was created.

  - `description: string`

    Description of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `directory: string`

    Directory name of the skill version.

    This is the top-level directory name that was extracted from the uploaded files.

  - `name: string`

    Human-readable name of the skill version.

    This is extracted from the SKILL.md file in the skill upload.

  - `skill_id: string`

    Identifier for the skill that this version belongs to.

  - `type: string`

    Object type.

    For Skill Versions, this is always `"skill_version"`.

  - `version: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

### Example

```cli
ant beta:skills:versions retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
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

`$ ant beta:skills:versions delete`

**delete** `/v1/skills/{skill_id}/versions/{version}`

Delete Skill Version

### Parameters

- `--skill-id: string`

  Path param: Unique identifier for the skill.

  The format and length of IDs may change over time.

- `--version: string`

  Path param: Version identifier for the skill.

  Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaSkillVersionDeleteResponse: object { id, type }`

  - `id: string`

    Version identifier for the skill.

    Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

  - `type: string`

    Deleted object type.

    For Skill Versions, this is always `"skill_version_deleted"`.

### Example

```cli
ant beta:skills:versions delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
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

`$ ant beta:user-profiles create`

**post** `/v1/user_profiles`

Create User Profile

### Parameters

- `--external-id: optional string`

  Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

- `--metadata: optional map[string]`

  Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

- `--name: optional string`

  Body param: Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

- `--relationship: optional "external" or "resold" or "internal"`

  Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```cli
ant beta:user-profiles create \
  --api-key my-anthropic-api-key
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

`$ ant beta:user-profiles list`

**get** `/v1/user_profiles`

List User Profiles

### Parameters

- `--limit: optional number`

  Query param: Query parameter for limit

- `--order: optional "asc" or "desc"`

  Query param: Query parameter for order

- `--page: optional string`

  Query param: Query parameter for page

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListUserProfilesResponse: object { data, next_page }`

  - `data: array of BetaUserProfile`

    User profiles on this page.

    - `id: string`

      Unique identifier for this user profile, prefixed `uprof_`.

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `metadata: map[string]`

      Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

    - `relationship: "external" or "resold" or "internal"`

      How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

      - `"external"`

      - `"resold"`

      - `"internal"`

    - `trust_grants: map[BetaUserProfileTrustGrant]`

      Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

      - `status: "active" or "pending" or "rejected"`

        Status of the trust grant.

        - `"active"`

        - `"pending"`

        - `"rejected"`

    - `type: "user_profile"`

      Object type. Always `user_profile`.

      - `"user_profile"`

    - `updated_at: string`

      A timestamp in RFC 3339 format

    - `external_id: optional string`

      Platform's own identifier for this user. Not enforced unique.

    - `name: optional string`

      Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

  - `next_page: string`

    Cursor for the next page, or `null` when there are no more results.

### Example

```cli
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
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

`$ ant beta:user-profiles retrieve`

**get** `/v1/user_profiles/{user_profile_id}`

Get User Profile

### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```cli
ant beta:user-profiles retrieve \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
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

`$ ant beta:user-profiles update`

**post** `/v1/user_profiles/{user_profile_id}`

Update User Profile

### Parameters

- `--user-profile-id: string`

  Path param: Path parameter user_profile_id

- `--external-id: optional string`

  Body param: If present, replaces the stored external_id. Omit to leave unchanged. Maximum 255 characters.

- `--metadata: optional map[string]`

  Body param: Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

- `--name: optional string`

  Body param: If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

- `--relationship: optional "external" or "resold" or "internal"`

  Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile: object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Example

```cli
ant beta:user-profiles update \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
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

`$ ant beta:user-profiles create-enrollment-url`

**post** `/v1/user_profiles/{user_profile_id}/enrollment_url`

Create Enrollment URL

### Parameters

- `--user-profile-id: string`

  Path parameter user_profile_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_user_profile_enrollment_url: object { expires_at, type, url }`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Example

```cli
ant beta:user-profiles create-enrollment-url \
  --api-key my-anthropic-api-key \
  --user-profile-id uprof_011CZkZCu8hGbp5mYRQgUmz9
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

- `beta_user_profile: object { id, created_at, metadata, 6 more }`

  - `id: string`

    Unique identifier for this user profile, prefixed `uprof_`.

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `metadata: map[string]`

    Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

  - `relationship: "external" or "resold" or "internal"`

    How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

    - `"external"`

    - `"resold"`

    - `"internal"`

  - `trust_grants: map[BetaUserProfileTrustGrant]`

    Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

    - `status: "active" or "pending" or "rejected"`

      Status of the trust grant.

      - `"active"`

      - `"pending"`

      - `"rejected"`

  - `type: "user_profile"`

    Object type. Always `user_profile`.

    - `"user_profile"`

  - `updated_at: string`

    A timestamp in RFC 3339 format

  - `external_id: optional string`

    Platform's own identifier for this user. Not enforced unique.

  - `name: optional string`

    Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

### Beta User Profile Enrollment URL

- `beta_user_profile_enrollment_url: object { expires_at, type, url }`

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `type: "enrollment_url"`

    Object type. Always `enrollment_url`.

    - `"enrollment_url"`

  - `url: string`

    Enrollment URL to send to the end user. Valid until `expires_at`.

### Beta User Profile Trust Grant

- `beta_user_profile_trust_grant: object { status }`

  - `status: "active" or "pending" or "rejected"`

    Status of the trust grant.

    - `"active"`

    - `"pending"`

    - `"rejected"`

# Dreams

## Create a Dream

`$ ant beta:dreams create`

**post** `/v1/dreams`

Create a Dream

### Parameters

- `--input: array of BetaDreamInput`

  Body param

- `--model: string or BetaDreamModelConfigParam`

  Body param: Model identifier and configuration applied to every pipeline stage.

- `--instructions: optional string`

  Body param

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_dream: object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: object { message, type }`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `beta_dream_sessions_input: object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: object { id, speed }`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```cli
ant beta:dreams create \
  --api-key my-anthropic-api-key \
  --input '{memory_store_id: x, type: memory_store}' \
  --model string
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

`$ ant beta:dreams list`

**get** `/v1/dreams`

List Dreams

### Parameters

- `--created-at-gt: optional string`

  Query param: Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

- `--created-at-lt: optional string`

  Query param: Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

- `--include-archived: optional boolean`

  Query param: Query parameter for include_archived

- `--limit: optional number`

  Query param: Query parameter for limit

- `--page: optional string`

  Query param: Query parameter for page

- `--status: optional array of BetaDreamStatus`

  Query param: Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListDreamsResponse: object { data, next_page }`

  - `data: array of BetaDream`

    - `id: string`

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `ended_at: string`

      A timestamp in RFC 3339 format

    - `error: object { message, type }`

      Failure detail for a Dream whose `status` is `failed`.

      - `message: string`

      - `type: string`

    - `inputs: array of BetaDreamInput`

      - `beta_dream_memory_store_input: object { memory_store_id, type }`

        An input memory store the dream reads from. The dream never mutates this store.

        - `memory_store_id: string`

        - `type: "memory_store"`

          - `"memory_store"`

      - `beta_dream_sessions_input: object { session_ids, type }`

        Input session transcripts the dream reads.

        - `session_ids: array of string`

        - `type: "sessions"`

          - `"sessions"`

    - `instructions: string`

    - `model: object { id, speed }`

      Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

      - `id: string`

        Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

      - `speed: optional "standard" or "fast"`

        Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

        - `"standard"`

        - `"fast"`

    - `outputs: array of BetaDreamOutput`

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `session_id: string`

    - `status: "pending" or "running" or "completed" or 2 more`

      Lifecycle status of a Dream.

      - `"pending"`

      - `"running"`

      - `"completed"`

      - `"failed"`

      - `"canceled"`

    - `type: "dream"`

      - `"dream"`

    - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

      Cumulative token usage for the dream across every pipeline stage.

      - `cache_creation_input_tokens: number`

        Total tokens used to create prompt-cache entries (sum of all TTL tiers).

      - `cache_read_input_tokens: number`

        Total tokens read from prompt cache.

      - `input_tokens: number`

        Total uncached input tokens consumed across every pipeline stage.

      - `output_tokens: number`

        Total output tokens generated across every pipeline stage.

  - `next_page: string`

### Example

```cli
ant beta:dreams list \
  --api-key my-anthropic-api-key
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

`$ ant beta:dreams retrieve`

**get** `/v1/dreams/{dream_id}`

Get a Dream

### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_dream: object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: object { message, type }`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `beta_dream_sessions_input: object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: object { id, speed }`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```cli
ant beta:dreams retrieve \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
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

`$ ant beta:dreams cancel`

**post** `/v1/dreams/{dream_id}/cancel`

Cancel a Dream

### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_dream: object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: object { message, type }`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `beta_dream_sessions_input: object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: object { id, speed }`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```cli
ant beta:dreams cancel \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
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

`$ ant beta:dreams archive`

**post** `/v1/dreams/{dream_id}/archive`

Archive a Dream

### Parameters

- `--dream-id: string`

  Path parameter dream_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_dream: object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: object { message, type }`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `beta_dream_sessions_input: object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: object { id, speed }`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Example

```cli
ant beta:dreams archive \
  --api-key my-anthropic-api-key \
  --dream-id dream_id
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

- `beta_dream: object { id, archived_at, created_at, 10 more }`

  An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

  - `id: string`

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `ended_at: string`

    A timestamp in RFC 3339 format

  - `error: object { message, type }`

    Failure detail for a Dream whose `status` is `failed`.

    - `message: string`

    - `type: string`

  - `inputs: array of BetaDreamInput`

    - `beta_dream_memory_store_input: object { memory_store_id, type }`

      An input memory store the dream reads from. The dream never mutates this store.

      - `memory_store_id: string`

      - `type: "memory_store"`

        - `"memory_store"`

    - `beta_dream_sessions_input: object { session_ids, type }`

      Input session transcripts the dream reads.

      - `session_ids: array of string`

      - `type: "sessions"`

        - `"sessions"`

  - `instructions: string`

  - `model: object { id, speed }`

    Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

    - `id: string`

      Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

    - `speed: optional "standard" or "fast"`

      Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

      - `"standard"`

      - `"fast"`

  - `outputs: array of BetaDreamOutput`

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `session_id: string`

  - `status: "pending" or "running" or "completed" or 2 more`

    Lifecycle status of a Dream.

    - `"pending"`

    - `"running"`

    - `"completed"`

    - `"failed"`

    - `"canceled"`

  - `type: "dream"`

    - `"dream"`

  - `usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

    Cumulative token usage for the dream across every pipeline stage.

    - `cache_creation_input_tokens: number`

      Total tokens used to create prompt-cache entries (sum of all TTL tiers).

    - `cache_read_input_tokens: number`

      Total tokens read from prompt cache.

    - `input_tokens: number`

      Total uncached input tokens consumed across every pipeline stage.

    - `output_tokens: number`

      Total output tokens generated across every pipeline stage.

### Beta Dream Error

- `beta_dream_error: object { message, type }`

  Failure detail for a Dream whose `status` is `failed`.

  - `message: string`

  - `type: string`

### Beta Dream Input

- `beta_dream_input: BetaDreamMemoryStoreInput or BetaDreamSessionsInput`

  An input memory store the dream reads from. The dream never mutates this store.

  - `beta_dream_memory_store_input: object { memory_store_id, type }`

    An input memory store the dream reads from. The dream never mutates this store.

    - `memory_store_id: string`

    - `type: "memory_store"`

      - `"memory_store"`

  - `beta_dream_sessions_input: object { session_ids, type }`

    Input session transcripts the dream reads.

    - `session_ids: array of string`

    - `type: "sessions"`

      - `"sessions"`

### Beta Dream Memory Store Input

- `beta_dream_memory_store_input: object { memory_store_id, type }`

  An input memory store the dream reads from. The dream never mutates this store.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Memory Store Output

- `beta_dream_memory_store_output: object { memory_store_id, type }`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Model Config

- `beta_dream_model_config: object { id, speed }`

  Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

  - `id: string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Model Config Param

- `beta_dream_model_config_param: object { id, speed }`

  Model identifier and configuration applied to every pipeline stage.

  - `id: string`

    Model identifier, e.g. "claude-opus-4-7". 1-256 characters.

  - `speed: optional "standard" or "fast"`

    Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

    - `"standard"`

    - `"fast"`

### Beta Dream Output

- `beta_dream_output: object { memory_store_id, type }`

  An output memory store the dream writes consolidated memories into.

  - `memory_store_id: string`

  - `type: "memory_store"`

    - `"memory_store"`

### Beta Dream Sessions Input

- `beta_dream_sessions_input: object { session_ids, type }`

  Input session transcripts the dream reads.

  - `session_ids: array of string`

  - `type: "sessions"`

    - `"sessions"`

### Beta Dream Status

- `beta_dream_status: "pending" or "running" or "completed" or 2 more`

  Lifecycle status of a Dream.

  - `"pending"`

  - `"running"`

  - `"completed"`

  - `"failed"`

  - `"canceled"`

### Beta Dream Usage

- `beta_dream_usage: object { cache_creation_input_tokens, cache_read_input_tokens, input_tokens, output_tokens }`

  Cumulative token usage for the dream across every pipeline stage.

  - `cache_creation_input_tokens: number`

    Total tokens used to create prompt-cache entries (sum of all TTL tiers).

  - `cache_read_input_tokens: number`

    Total tokens read from prompt cache.

  - `input_tokens: number`

    Total uncached input tokens consumed across every pipeline stage.

  - `output_tokens: number`

    Total output tokens generated across every pipeline stage.

# Tunnels

## Create Tunnel

`$ ant beta:tunnels create`

**post** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Creates a tunnel. Creation allocates a fresh hostname and provisions the tunnel; it is not idempotent. The new tunnel rejects MCP traffic until at least one CA certificate is added.

### Parameters

- `--display-name: optional string`

  Body param: Optional human-readable name for the tunnel (1-255 characters).

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel: object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

### Example

```cli
ant beta:tunnels create \
  --api-key my-anthropic-api-key
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

`$ ant beta:tunnels retrieve`

**get** `/v1/tunnels/{tunnel_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel by ID.

### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel: object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

### Example

```cli
ant beta:tunnels retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

`$ ant beta:tunnels list`

**get** `/v1/tunnels`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists tunnels. Results are ordered by creation time, newest first; archived tunnels are excluded unless include_archived is set.

### Parameters

- `--include-archived: optional boolean`

  Query param: Whether to include archived tunnels in the results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum number of tunnels to return per page. Defaults to 20, maximum 1000.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous `list_tunnels` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListTunnelsResponse: object { data, next_page }`

  A paginated list of tunnels.

  - `data: array of BetaTunnel`

    List of tunnels, ordered by created_at descending.

    - `id: string`

      Unique identifier for the tunnel, prefixed with `tnl_`.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `display_name: string`

      Human-readable name for the tunnel (1-255 characters). Null if unset.

    - `domain: string`

      Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

    - `type: "tunnel"`

  - `next_page: string`

    Pagination cursor for the next page, or null if no more results.

### Example

```cli
ant beta:tunnels list \
  --api-key my-anthropic-api-key
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

`$ ant beta:tunnels archive`

**post** `/v1/tunnels/{tunnel_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel. Archival is irreversible: every non-archived certificate on the tunnel is archived in the same operation, the hostname is retired and never re-allocated, and the tunnel token is invalidated. Retrying against an already-archived tunnel returns the existing record unchanged.

### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel: object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

### Example

```cli
ant beta:tunnels archive \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

`$ ant beta:tunnels reveal-token`

**post** `/v1/tunnels/{tunnel_id}/reveal_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Reveals a tunnel's connector token. The value is fetched live on each call; Anthropic does not store it. Repeated calls return the same value until the token is rotated. Exposed as POST so the token does not appear in intermediary access logs.

### Parameters

- `--tunnel-id: string`

  Path parameter tunnel_id

- `--beta: optional array of AnthropicBeta`

  Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel_token: object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

### Example

```cli
ant beta:tunnels reveal-token \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

`$ ant beta:tunnels rotate-token`

**post** `/v1/tunnels/{tunnel_id}/rotate_token`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Rotates a tunnel's connector token. Rotation invalidates the current token for new connections and returns a fresh value; established connections are not severed. A connector restarted after rotation must use the new value.

### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--reason: optional string`

  Body param: Optional free-text reason for the rotation, recorded for audit.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel_token: object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

### Example

```cli
ant beta:tunnels rotate-token \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

- `beta_tunnel: object { id, archived_at, created_at, 3 more }`

  An MCP tunnel.

  - `id: string`

    Unique identifier for the tunnel, prefixed with `tnl_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `display_name: string`

    Human-readable name for the tunnel (1-255 characters). Null if unset.

  - `domain: string`

    Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

  - `type: "tunnel"`

### Beta Tunnel Token

- `beta_tunnel_token: object { id, tunnel_token, type }`

  A tunnel's connector token.

  - `id: string`

    Stable identifier for the current token value. Changes when the token is rotated.

  - `tunnel_token: string`

    The connector token used to run the tunnel. Treat as a credential.

  - `type: "tunnel_token"`

# Certificates

## Create Tunnel Certificate

`$ ant beta:tunnels:certificates create`

**post** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Registers a public CA certificate on a tunnel. Anthropic verifies the gateway's server certificate against this CA when it terminates the inner TLS session. A tunnel holds at most two non-archived certificates.

### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--ca-certificate-pem: string`

  Body param: PEM-encoded X.509 CA certificate. Must contain exactly one certificate and no private-key material. Maximum 8KB.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel_certificate: object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

### Example

```cli
ant beta:tunnels:certificates create \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --ca-certificate-pem ca_certificate_pem
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

`$ ant beta:tunnels:certificates retrieve`

**get** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Fetches a tunnel certificate by ID.

### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--certificate-id: string`

  Path param: Path parameter certificate_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel_certificate: object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

### Example

```cli
ant beta:tunnels:certificates retrieve \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --certificate-id certificate_id
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

`$ ant beta:tunnels:certificates list`

**get** `/v1/tunnels/{tunnel_id}/certificates`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Lists the certificates registered on a tunnel. Archived certificates are excluded unless include_archived is set.

### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--include-archived: optional boolean`

  Query param: Whether to include archived certificates in the results. Defaults to false.

- `--limit: optional number`

  Query param: Maximum number of certificates to return per page. Defaults to 20, maximum 1000.

- `--page: optional string`

  Query param: Opaque pagination cursor from a previous `list_tunnel_certificates` response.

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `BetaListTunnelCertificatesResponse: object { data, next_page }`

  The tunnel's certificates.

  - `data: array of BetaTunnelCertificate`

    List of certificates, ordered by created_at descending.

    - `id: string`

      Unique identifier for the certificate, prefixed with `tcrt_`.

    - `archived_at: string`

      A timestamp in RFC 3339 format

    - `created_at: string`

      A timestamp in RFC 3339 format

    - `expires_at: string`

      A timestamp in RFC 3339 format

    - `fingerprint: string`

      Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

    - `tunnel_id: string`

      ID of the tunnel the certificate is registered against.

    - `type: "tunnel_certificate"`

  - `next_page: string`

    Pagination cursor for the next page, or null if no more results.

### Example

```cli
ant beta:tunnels:certificates list \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id
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

`$ ant beta:tunnels:certificates archive`

**post** `/v1/tunnels/{tunnel_id}/certificates/{certificate_id}/archive`

The Tunnels API is in research preview. It requires the `anthropic-beta: mcp-tunnels-2026-06-22` header and may change without a deprecation period. It supersedes the Admin API endpoints at `/v1/organizations/tunnels`, which remain available during a migration window.

Archives a tunnel certificate, removing it from the set Anthropic trusts for the tunnel. The certificate record is retained. Archiving the last non-archived certificate is permitted; the tunnel rejects MCP traffic until a new certificate is added.

### Parameters

- `--tunnel-id: string`

  Path param: Path parameter tunnel_id

- `--certificate-id: string`

  Path param: Path parameter certificate_id

- `--beta: optional array of AnthropicBeta`

  Header param: Optional header to specify the beta version(s) you want to use.

### Returns

- `beta_tunnel_certificate: object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

### Example

```cli
ant beta:tunnels:certificates archive \
  --api-key my-anthropic-api-key \
  --tunnel-id tunnel_id \
  --certificate-id certificate_id
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

- `beta_tunnel_certificate: object { id, archived_at, created_at, 4 more }`

  A CA certificate attached to a tunnel.

  - `id: string`

    Unique identifier for the certificate, prefixed with `tcrt_`.

  - `archived_at: string`

    A timestamp in RFC 3339 format

  - `created_at: string`

    A timestamp in RFC 3339 format

  - `expires_at: string`

    A timestamp in RFC 3339 format

  - `fingerprint: string`

    Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

  - `tunnel_id: string`

    ID of the tunnel the certificate is registered against.

  - `type: "tunnel_certificate"`

# Webhooks

## Domain Types

### Beta Webhook Agent Archived Event Data

- `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.archived"`

  - `workspace_id: string`

### Beta Webhook Agent Created Event Data

- `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.created"`

  - `workspace_id: string`

### Beta Webhook Agent Deleted Event Data

- `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.deleted"`

  - `workspace_id: string`

### Beta Webhook Agent Updated Event Data

- `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the agent that triggered the event.

  - `organization_id: string`

  - `type: "agent.updated"`

  - `workspace_id: string`

### Beta Webhook Deployment Archived Event Data

- `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.archived"`

  - `workspace_id: string`

### Beta Webhook Deployment Created Event Data

- `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.created"`

  - `workspace_id: string`

### Beta Webhook Deployment Deleted Event Data

- `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.deleted"`

  - `workspace_id: string`

### Beta Webhook Deployment Paused Event Data

- `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.paused"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Failed Event Data

- `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.failed"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Started Event Data

- `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.started"`

  - `workspace_id: string`

### Beta Webhook Deployment Run Succeeded Event Data

- `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment run that triggered the event.

  - `organization_id: string`

  - `type: "deployment_run.succeeded"`

  - `workspace_id: string`

### Beta Webhook Deployment Unpaused Event Data

- `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.unpaused"`

  - `workspace_id: string`

### Beta Webhook Deployment Updated Event Data

- `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the deployment that triggered the event.

  - `organization_id: string`

  - `type: "deployment.updated"`

  - `workspace_id: string`

### Beta Webhook Environment Archived Event Data

- `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.archived"`

  - `workspace_id: string`

### Beta Webhook Environment Created Event Data

- `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.created"`

  - `workspace_id: string`

### Beta Webhook Environment Deleted Event Data

- `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.deleted"`

  - `workspace_id: string`

### Beta Webhook Environment Updated Event Data

- `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the environment that triggered the event.

  - `organization_id: string`

  - `type: "environment.updated"`

  - `workspace_id: string`

### Beta Webhook Event

- `beta_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

      - `workspace_id: string`

    - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

      - `workspace_id: string`

    - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

      - `workspace_id: string`

    - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

      - `workspace_id: string`

    - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

      - `workspace_id: string`

    - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

      - `workspace_id: string`

    - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

      - `workspace_id: string`

    - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

      - `workspace_id: string`

    - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

      - `workspace_id: string`

    - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

      - `workspace_id: string`

    - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

      - `workspace_id: string`

    - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

### Beta Webhook Event Data

- `beta_webhook_event_data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

  - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.created"`

    - `workspace_id: string`

  - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.pending"`

    - `workspace_id: string`

  - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.running"`

    - `workspace_id: string`

  - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.idled"`

    - `workspace_id: string`

  - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.requires_action"`

    - `workspace_id: string`

  - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.archived"`

    - `workspace_id: string`

  - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.deleted"`

    - `workspace_id: string`

  - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_rescheduled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_run_started"`

    - `workspace_id: string`

  - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.status_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_created"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_idled"`

    - `workspace_id: string`

  - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `session_thread_id: string`

      ID of the session thread this event refers to.

    - `type: "session.thread_terminated"`

    - `workspace_id: string`

  - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.outcome_evaluation_ended"`

    - `workspace_id: string`

  - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.created"`

    - `workspace_id: string`

  - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.archived"`

    - `workspace_id: string`

  - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the vault that triggered the event.

    - `organization_id: string`

    - `type: "vault.deleted"`

    - `workspace_id: string`

  - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.created"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.archived"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.deleted"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

    - `id: string`

      ID of the vault credential that triggered the event.

    - `organization_id: string`

    - `type: "vault_credential.refresh_failed"`

    - `vault_id: string`

      ID of the vault that owns this credential.

    - `workspace_id: string`

  - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the session that triggered the event.

    - `organization_id: string`

    - `type: "session.updated"`

    - `workspace_id: string`

  - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.created"`

    - `workspace_id: string`

  - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.archived"`

    - `workspace_id: string`

  - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.deleted"`

    - `workspace_id: string`

  - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.paused"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.failed"`

    - `workspace_id: string`

  - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.created"`

    - `workspace_id: string`

  - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.updated"`

    - `workspace_id: string`

  - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.unpaused"`

    - `workspace_id: string`

  - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the agent that triggered the event.

    - `organization_id: string`

    - `type: "agent.updated"`

    - `workspace_id: string`

  - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.archived"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.started"`

    - `workspace_id: string`

  - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment that triggered the event.

    - `organization_id: string`

    - `type: "deployment.deleted"`

    - `workspace_id: string`

  - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the deployment run that triggered the event.

    - `organization_id: string`

    - `type: "deployment_run.succeeded"`

    - `workspace_id: string`

  - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.created"`

    - `workspace_id: string`

  - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.updated"`

    - `workspace_id: string`

  - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.archived"`

    - `workspace_id: string`

  - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the environment that triggered the event.

    - `organization_id: string`

    - `type: "environment.deleted"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.created"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.archived"`

    - `workspace_id: string`

  - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

    - `id: string`

      ID of the memory store that triggered the event.

    - `organization_id: string`

    - `type: "memory_store.deleted"`

    - `workspace_id: string`

### Beta Webhook Memory Store Archived Event Data

- `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.archived"`

  - `workspace_id: string`

### Beta Webhook Memory Store Created Event Data

- `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.created"`

  - `workspace_id: string`

### Beta Webhook Memory Store Deleted Event Data

- `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the memory store that triggered the event.

  - `organization_id: string`

  - `type: "memory_store.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Archived Event Data

- `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.archived"`

  - `workspace_id: string`

### Beta Webhook Session Created Event Data

- `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.created"`

  - `workspace_id: string`

### Beta Webhook Session Deleted Event Data

- `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.deleted"`

  - `workspace_id: string`

### Beta Webhook Session Idled Event Data

- `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.idled"`

  - `workspace_id: string`

### Beta Webhook Session Outcome Evaluation Ended Event Data

- `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.outcome_evaluation_ended"`

  - `workspace_id: string`

### Beta Webhook Session Pending Event Data

- `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.pending"`

  - `workspace_id: string`

### Beta Webhook Session Requires Action Event Data

- `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.requires_action"`

  - `workspace_id: string`

### Beta Webhook Session Running Event Data

- `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.running"`

  - `workspace_id: string`

### Beta Webhook Session Status Idled Event Data

- `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_idled"`

  - `workspace_id: string`

### Beta Webhook Session Status Rescheduled Event Data

- `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_rescheduled"`

  - `workspace_id: string`

### Beta Webhook Session Status Run Started Event Data

- `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_run_started"`

  - `workspace_id: string`

### Beta Webhook Session Status Terminated Event Data

- `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.status_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Thread Created Event Data

- `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_created"`

  - `workspace_id: string`

### Beta Webhook Session Thread Idled Event Data

- `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_idled"`

  - `workspace_id: string`

### Beta Webhook Session Thread Terminated Event Data

- `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `session_thread_id: string`

    ID of the session thread this event refers to.

  - `type: "session.thread_terminated"`

  - `workspace_id: string`

### Beta Webhook Session Updated Event Data

- `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the session that triggered the event.

  - `organization_id: string`

  - `type: "session.updated"`

  - `workspace_id: string`

### Beta Webhook Vault Archived Event Data

- `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.archived"`

  - `workspace_id: string`

### Beta Webhook Vault Created Event Data

- `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.created"`

  - `workspace_id: string`

### Beta Webhook Vault Credential Archived Event Data

- `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.archived"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Created Event Data

- `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.created"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Deleted Event Data

- `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.deleted"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Credential Refresh Failed Event Data

- `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

  - `id: string`

    ID of the vault credential that triggered the event.

  - `organization_id: string`

  - `type: "vault_credential.refresh_failed"`

  - `vault_id: string`

    ID of the vault that owns this credential.

  - `workspace_id: string`

### Beta Webhook Vault Deleted Event Data

- `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

  - `id: string`

    ID of the vault that triggered the event.

  - `organization_id: string`

  - `type: "vault.deleted"`

  - `workspace_id: string`

### Unwrap Webhook Event

- `unwrap_webhook_event: object { id, created_at, data, type }`

  - `id: string`

    Unique event identifier for idempotency.

  - `created_at: string`

    RFC 3339 timestamp when the event occurred.

  - `data: BetaWebhookSessionCreatedEventData or BetaWebhookSessionPendingEventData or BetaWebhookSessionRunningEventData or 40 more`

    - `beta_webhook_session_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.created"`

      - `workspace_id: string`

    - `beta_webhook_session_pending_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.pending"`

      - `workspace_id: string`

    - `beta_webhook_session_running_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.running"`

      - `workspace_id: string`

    - `beta_webhook_session_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.idled"`

      - `workspace_id: string`

    - `beta_webhook_session_requires_action_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.requires_action"`

      - `workspace_id: string`

    - `beta_webhook_session_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.archived"`

      - `workspace_id: string`

    - `beta_webhook_session_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.deleted"`

      - `workspace_id: string`

    - `beta_webhook_session_status_rescheduled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_rescheduled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_run_started"`

      - `workspace_id: string`

    - `beta_webhook_session_status_idled_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_status_terminated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.status_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_created_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_created"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_idled_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_idled"`

      - `workspace_id: string`

    - `beta_webhook_session_thread_terminated_event_data: object { id, organization_id, session_thread_id, 2 more }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `session_thread_id: string`

        ID of the session thread this event refers to.

      - `type: "session.thread_terminated"`

      - `workspace_id: string`

    - `beta_webhook_session_outcome_evaluation_ended_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.outcome_evaluation_ended"`

      - `workspace_id: string`

    - `beta_webhook_vault_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.created"`

      - `workspace_id: string`

    - `beta_webhook_vault_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.archived"`

      - `workspace_id: string`

    - `beta_webhook_vault_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the vault that triggered the event.

      - `organization_id: string`

      - `type: "vault.deleted"`

      - `workspace_id: string`

    - `beta_webhook_vault_credential_created_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.created"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_archived_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.archived"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_deleted_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.deleted"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_vault_credential_refresh_failed_event_data: object { id, organization_id, type, 2 more }`

      - `id: string`

        ID of the vault credential that triggered the event.

      - `organization_id: string`

      - `type: "vault_credential.refresh_failed"`

      - `vault_id: string`

        ID of the vault that owns this credential.

      - `workspace_id: string`

    - `beta_webhook_session_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.updated"`

      - `workspace_id: string`

    - `beta_webhook_agent_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.created"`

      - `workspace_id: string`

    - `beta_webhook_agent_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.archived"`

      - `workspace_id: string`

    - `beta_webhook_agent_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_paused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.paused"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_failed_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.failed"`

      - `workspace_id: string`

    - `beta_webhook_deployment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.created"`

      - `workspace_id: string`

    - `beta_webhook_deployment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_unpaused_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.unpaused"`

      - `workspace_id: string`

    - `beta_webhook_agent_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the agent that triggered the event.

      - `organization_id: string`

      - `type: "agent.updated"`

      - `workspace_id: string`

    - `beta_webhook_deployment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.archived"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_started_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.started"`

      - `workspace_id: string`

    - `beta_webhook_deployment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment that triggered the event.

      - `organization_id: string`

      - `type: "deployment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_deployment_run_succeeded_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the deployment run that triggered the event.

      - `organization_id: string`

      - `type: "deployment_run.succeeded"`

      - `workspace_id: string`

    - `beta_webhook_environment_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.created"`

      - `workspace_id: string`

    - `beta_webhook_environment_updated_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.updated"`

      - `workspace_id: string`

    - `beta_webhook_environment_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.archived"`

      - `workspace_id: string`

    - `beta_webhook_environment_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_created_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_archived_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

      - `workspace_id: string`

    - `beta_webhook_memory_store_deleted_event_data: object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.
