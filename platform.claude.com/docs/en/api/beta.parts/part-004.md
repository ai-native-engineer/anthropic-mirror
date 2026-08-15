<!-- source: https://platform.claude.com/docs/en/api/beta -->
<!-- part of: https://platform.claude.com/docs/en/api/beta -->

<!-- chunk-start -->

      - `workspace_id: string`

    - `BetaWebhookEnvironmentDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the environment that triggered the event.

      - `organization_id: string`

      - `type: "environment.deleted"`

        - `"environment.deleted"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreCreatedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.created"`

        - `"memory_store.created"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreArchivedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.archived"`

        - `"memory_store.archived"`

      - `workspace_id: string`

    - `BetaWebhookMemoryStoreDeletedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the memory store that triggered the event.

      - `organization_id: string`

      - `type: "memory_store.deleted"`

        - `"memory_store.deleted"`

      - `workspace_id: string`

    - `BetaWebhookSessionBudgetReachedEventData object { id, organization_id, type, workspace_id }`

      - `id: string`

        ID of the session that triggered the event.

      - `organization_id: string`

      - `type: "session.budget_reached"`

        - `"session.budget_reached"`

      - `workspace_id: string`

  - `type: "event"`

    Object type. Always `event` for webhook payloads.

    - `"event"`
