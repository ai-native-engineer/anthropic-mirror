<!-- source: https://platform.claude.com/docs/en/managed-agents/dreams -->

# Dreams
Let Claude reflect on past sessions to curate an agent's memory and surface new insights.

Dreaming is a research preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.
Agents write to their [memory stores](https://platform.claude.com/docs/en/managed-agents/memory) as they work, but these writes are local and incremental: over many sessions a memory store accumulates duplicates, contradictions, and stale entries.
**Dreams** let Claude clean that up. A dream reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store: duplicates merged, stale or contradicted entries replaced with the latest value, and new insights surfaced.
The input store is never modified, so you can review the output and discard it if you don't like the result.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. Dreams additionally require the `dreaming-2026-04-21` beta header. The SDK sets these automatically.
How it works
A **dream** is an asynchronous job that takes:
  * a pre-existing **memory store** : the store Claude verifies, deduplicates, and reorganizes, and
  * 1 to 100 **sessions** : past transcripts Claude mines for patterns and insights to fold into the output.

The dream produces another **output memory store** , separate from the input. The output store ID appears in the dream's `outputs[]` once it starts `running`.
Create a dream
curlCLIPythonTypeScriptC#GoJavaPHPRuby

dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-4-8",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
print(dream.id)  # drm_01...

Dreaming inputs include the pre-existing memory store and an array of sessions. The model selected will run the dreaming pipeline; during the research preview `claude-opus-4-8`, `claude-opus-4-7`, and `claude-sonnet-4-6` are supported. You can optionally pass `instructions` to steer the dreaming process; see [Steer with instructions](https://platform.claude.com/docs/en/managed-agents/dreams#steer-with-instructions).
The response is the full `dream` resource with `status: "pending"`:

  "type": "dream",
  "id": "drm_01AbCDefGhIjKlMnOpQrStUv",
  "status": "pending",
  "inputs": [
    { "type": "memory_store", "memory_store_id": "memstore_01Hx..." },
    { "type": "sessions", "session_ids": ["sesn_01...", "sesn_02..."] }
  ],
  "outputs": [],
  "model": { "id": "claude-opus-4-8" },
  "instructions": "Focus on coding-style preferences; ignore one-off debugging notes.",
  "session_id": null,
  "created_at": "2026-04-29T17:04:10Z",
  "ended_at": null,
  "archived_at": null,
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  "error": null


If you only have session transcripts and no existing store, [create an empty memory store](https://platform.claude.com/docs/en/managed-agents/memory#create-a-memory-store) first and pass it as the `memory_store` input.
### 
Steer with instructions
The optional `instructions` field steers what the dreaming pipeline synthesizes. It is applied throughout the pipeline: what to read closely, what to merge or drop, and how to structure the output store.
Use `instructions` for high-level synthesis guidance such as focus areas ("focus on coding-style preferences"), content to preserve unchanged, or output conventions you want applied across the store. The pipeline is a synthesis pass over the inputs, not an editor applied to the text of the store, so imperative directives that target specific lines ("change sentence X to Y", "fix the count in section Z") generally produce no change. To make targeted edits to individual memories, use the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory#view-and-edit-memories) on the output store directly.
Track progress
Dreams run asynchronously and typically take minutes to tens of minutes depending on input size. Poll the dream by ID to check status:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

while dream.status in ("pending", "running"):
    time.sleep(10)
    dream = client.beta.dreams.retrieve(dream.id)
    print(f"status={dream.status} input_tokens={dream.usage.input_tokens}")

### 
Lifecycle  
| `status`  | Meaning  |  
| --- | --- |  
| `pending`  | Dream successfully created and queued.  |  
| `running`  | The pipeline is processing. `usage` updates as work progresses.  |  
| `completed`  | Finished successfully. The `outputs[]` value is the new memory store.  |  
| `failed`  | Dreaming run terminated with an error. The output memory store is left as-is with whatever was written before failure.  |  
| `canceled`  | Dreaming run canceled. The output memory store is left as-is.  |  
### 
Watch the pipeline run
Once a dream is `running`, its `session_id` field points at the underlying [session](https://platform.claude.com/docs/en/managed-agents/sessions) executing the pipeline. You can stream that session's [events](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) to observe what the dream is reading and writing in real time. The session is archived (not deleted) when the dream reaches a terminal state, so the transcript remains available afterward.
Use the output
When `status` reaches `completed`, the `memory_store` entry in `outputs[]` references a fully populated store. It's an ordinary memory store in your workspace. Review it with the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory#view-and-edit-memories) or in the Console, then either:
  * **Leverage it:** attach it to future sessions as a `memory_store` resource in place of (or alongside) the input memory store, or
  * **Discard it:** [delete](https://platform.claude.com/docs/en/api/beta/memory_stores/delete) or [archive](https://platform.claude.com/docs/en/api/beta/memory_stores/archive) it.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

# After the dream ends, the output holds the rebuilt memory store
output_store_id = next(
    output.memory_store_id for output in dream.outputs if output.type == "memory_store"
)

session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    resources=[
        {"type": "memory_store", "memory_store_id": output_store_id},
    ],
)

The dream itself never deletes or modifies its inputs. On `failed` or `canceled` the output store persists with partial contents so you can inspect what was produced before stopping; clean it up via the Memory Stores API if you don't need it.

While a dream is `pending` or `running`, archiving or deleting its output store is rejected with a 400. Archiving or deleting an _input_ store or session mid-run will cause the dream to fail with `input_memory_store_unavailable` or `input_session_unavailable`.
Cancel a dream
Cancel moves a `pending` or `running` dream to `canceled` immediately. Canceling an already-`canceled` dream is an idempotent no-op; canceling a `completed` or `failed` dream returns 400.
After cancellation, the dream's `usage` fields might continue to update for a few seconds while in-flight work winds down. Poll the dream until `usage` stabilizes if you need the final count.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.dreams.cancel(dream.id)

Archive a dream
Archive sets `archived_at` on a dream that has reached a terminal state (`completed`, `failed`, or `canceled`); `status` is left unchanged. Archived dreams are excluded from default list responses but remain readable by ID. Archiving an already-archived dream is an idempotent no-op. Archiving a `pending` or `running` dream returns 400; cancel it first. There is no unarchive.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.dreams.archive(dream.id)

Archiving a dream does not touch its output memory store; manage that separately via the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory).
List dreams
Returns all non-archived dreams in the workspace, newest first. Use `limit` (default 20, max 100) and the `page` cursor to paginate. Pass `include_archived=true` to include archived dreams.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

for listed_dream in client.beta.dreams.list(limit=20):
    print(listed_dream.id, listed_dream.status)

Errors
A non-exhaustive list of possible dreaming errors is below.  
| `error.type`  | When  |  
| --- | --- |  
| `timeout`  | The pipeline exceeded its runtime budget.  |  
| `internal_error`  | Unclassified pipeline failure.  |  
| `memory_store_org_limit_exceeded`  | Your organization hit its memory-store cap while the pipeline was provisioning working storage.  |  
| `input_memory_store_too_large`  | The input memory store exceeds the pipeline's size limit.  |  
| `input_memory_store_unavailable`  | The input memory store was archived or deleted after the dream was created.  |  
| `input_session_unavailable`  | An input session was archived or deleted after the dream was created.  |  
Billing
Dreams are billed at standard API token rates for the model you select; `usage` on the resource reports the exact totals. Cost scales roughly linearly with the number and length of input sessions. Start with a small batch of sessions and scale up once you're satisfied with the curation quality.
Limits  
| Limit  | Value  |  
| --- | --- |  
| Sessions per dream  | 100  |  
|  `instructions` length  | 4,096 characters  |  
| Supported models  |  `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6`  |  
Default rate limits apply to dream creation while this feature is in beta. [Contact support](https://support.claude.com) if you need higher limits.
  * [How it works](https://platform.claude.com/docs/en/managed-agents/dreams#how-it-works)
  * [Create a dream](https://platform.claude.com/docs/en/managed-agents/dreams#create-a-dream)
  * [Steer with instructions](https://platform.claude.com/docs/en/managed-agents/dreams#steer-with-instructions)
  * [Track progress](https://platform.claude.com/docs/en/managed-agents/dreams#track-progress)
  * [Lifecycle](https://platform.claude.com/docs/en/managed-agents/dreams#lifecycle)
  * [Watch the pipeline run](https://platform.claude.com/docs/en/managed-agents/dreams#watch-the-pipeline-run)
  * [Use the output](https://platform.claude.com/docs/en/managed-agents/dreams#use-the-output)
  * [Cancel a dream](https://platform.claude.com/docs/en/managed-agents/dreams#cancel-a-dream)
  * [Archive a dream](https://platform.claude.com/docs/en/managed-agents/dreams#archive-a-dream)
  * [List dreams](https://platform.claude.com/docs/en/managed-agents/dreams#list-dreams)
  * [Errors](https://platform.claude.com/docs/en/managed-agents/dreams#errors)
  * [Billing](https://platform.claude.com/docs/en/managed-agents/dreams#billing)
  * [Limits](https://platform.claude.com/docs/en/managed-agents/dreams#limits)

Managed Agents/Build persistent memory
# Dreams
Let Claude reflect on past sessions to curate an agent's memory and surface new insights.

Dreaming is a research preview feature. [Request access](https://claude.com/form/claude-managed-agents) to try it.
Agents write to their [memory stores](https://platform.claude.com/docs/en/managed-agents/memory) as they work, but these writes are local and incremental: over many sessions a memory store accumulates duplicates, contradictions, and stale entries.
**Dreams** let Claude clean that up. A dream reads an existing memory store alongside past session transcripts, then produces a new, reorganized memory store: duplicates merged, stale or contradicted entries replaced with the latest value, and new insights surfaced.
The input store is never modified, so you can review the output and discard it if you don't like the result.
All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. Dreams additionally require the `dreaming-2026-04-21` beta header. The SDK sets these automatically.
How it works
A **dream** is an asynchronous job that takes:
  * a pre-existing **memory store** : the store Claude verifies, deduplicates, and reorganizes, and
  * 1 to 100 **sessions** : past transcripts Claude mines for patterns and insights to fold into the output.

The dream produces another **output memory store** , separate from the input. The output store ID appears in the dream's `outputs[]` once it starts `running`.
Create a dream
curlCLIPythonTypeScriptC#GoJavaPHPRuby

dream = client.beta.dreams.create(
    inputs=[
        {"type": "memory_store", "memory_store_id": store_id},
        {"type": "sessions", "session_ids": [session_a, session_b]},
    ],
    model="claude-opus-4-8",
    instructions="Focus on coding-style preferences; ignore one-off debugging notes.",
)
print(dream.id)  # drm_01...

Dreaming inputs include the pre-existing memory store and an array of sessions. The model selected will run the dreaming pipeline; during the research preview `claude-opus-4-8`, `claude-opus-4-7`, and `claude-sonnet-4-6` are supported. You can optionally pass `instructions` to steer the dreaming process; see [Steer with instructions](https://platform.claude.com/docs/en/managed-agents/dreams#steer-with-instructions).
The response is the full `dream` resource with `status: "pending"`:

  "type": "dream",
  "id": "drm_01AbCDefGhIjKlMnOpQrStUv",
  "status": "pending",
  "inputs": [
    { "type": "memory_store", "memory_store_id": "memstore_01Hx..." },
    { "type": "sessions", "session_ids": ["sesn_01...", "sesn_02..."] }
  ],
  "outputs": [],
  "model": { "id": "claude-opus-4-8" },
  "instructions": "Focus on coding-style preferences; ignore one-off debugging notes.",
  "session_id": null,
  "created_at": "2026-04-29T17:04:10Z",
  "ended_at": null,
  "archived_at": null,
  "usage": {
    "input_tokens": 0,
    "output_tokens": 0,
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  "error": null


If you only have session transcripts and no existing store, [create an empty memory store](https://platform.claude.com/docs/en/managed-agents/memory#create-a-memory-store) first and pass it as the `memory_store` input.
### 
Steer with instructions
The optional `instructions` field steers what the dreaming pipeline synthesizes. It is applied throughout the pipeline: what to read closely, what to merge or drop, and how to structure the output store.
Use `instructions` for high-level synthesis guidance such as focus areas ("focus on coding-style preferences"), content to preserve unchanged, or output conventions you want applied across the store. The pipeline is a synthesis pass over the inputs, not an editor applied to the text of the store, so imperative directives that target specific lines ("change sentence X to Y", "fix the count in section Z") generally produce no change. To make targeted edits to individual memories, use the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory#view-and-edit-memories) on the output store directly.
Track progress
Dreams run asynchronously and typically take minutes to tens of minutes depending on input size. Poll the dream by ID to check status:
curlCLIPythonTypeScriptC#GoJavaPHPRuby

while dream.status in ("pending", "running"):
    time.sleep(10)
    dream = client.beta.dreams.retrieve(dream.id)
    print(f"status={dream.status} input_tokens={dream.usage.input_tokens}")

### 
Lifecycle  
| `status`  | Meaning  |  
| --- | --- |  
| `pending`  | Dream successfully created and queued.  |  
| `running`  | The pipeline is processing. `usage` updates as work progresses.  |  
| `completed`  | Finished successfully. The `outputs[]` value is the new memory store.  |  
| `failed`  | Dreaming run terminated with an error. The output memory store is left as-is with whatever was written before failure.  |  
| `canceled`  | Dreaming run canceled. The output memory store is left as-is.  |  
### 
Watch the pipeline run
Once a dream is `running`, its `session_id` field points at the underlying [session](https://platform.claude.com/docs/en/managed-agents/sessions) executing the pipeline. You can stream that session's [events](https://platform.claude.com/docs/en/managed-agents/events-and-streaming) to observe what the dream is reading and writing in real time. The session is archived (not deleted) when the dream reaches a terminal state, so the transcript remains available afterward.
Use the output
When `status` reaches `completed`, the `memory_store` entry in `outputs[]` references a fully populated store. It's an ordinary memory store in your workspace. Review it with the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory#view-and-edit-memories) or in the Console, then either:
  * **Leverage it:** attach it to future sessions as a `memory_store` resource in place of (or alongside) the input memory store, or
  * **Discard it:** [delete](https://platform.claude.com/docs/en/api/beta/memory_stores/delete) or [archive](https://platform.claude.com/docs/en/api/beta/memory_stores/archive) it.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

# After the dream ends, the output holds the rebuilt memory store
output_store_id = next(
    output.memory_store_id for output in dream.outputs if output.type == "memory_store"
)

session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=environment_id,
    resources=[
        {"type": "memory_store", "memory_store_id": output_store_id},
    ],
)

The dream itself never deletes or modifies its inputs. On `failed` or `canceled` the output store persists with partial contents so you can inspect what was produced before stopping; clean it up via the Memory Stores API if you don't need it.

While a dream is `pending` or `running`, archiving or deleting its output store is rejected with a 400. Archiving or deleting an _input_ store or session mid-run will cause the dream to fail with `input_memory_store_unavailable` or `input_session_unavailable`.
Cancel a dream
Cancel moves a `pending` or `running` dream to `canceled` immediately. Canceling an already-`canceled` dream is an idempotent no-op; canceling a `completed` or `failed` dream returns 400.
After cancellation, the dream's `usage` fields might continue to update for a few seconds while in-flight work winds down. Poll the dream until `usage` stabilizes if you need the final count.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.dreams.cancel(dream.id)

Archive a dream
Archive sets `archived_at` on a dream that has reached a terminal state (`completed`, `failed`, or `canceled`); `status` is left unchanged. Archived dreams are excluded from default list responses but remain readable by ID. Archiving an already-archived dream is an idempotent no-op. Archiving a `pending` or `running` dream returns 400; cancel it first. There is no unarchive.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

client.beta.dreams.archive(dream.id)

Archiving a dream does not touch its output memory store; manage that separately via the [Memory Stores API](https://platform.claude.com/docs/en/managed-agents/memory).
List dreams
Returns all non-archived dreams in the workspace, newest first. Use `limit` (default 20, max 100) and the `page` cursor to paginate. Pass `include_archived=true` to include archived dreams.
curlCLIPythonTypeScriptC#GoJavaPHPRuby

for listed_dream in client.beta.dreams.list(limit=20):
    print(listed_dream.id, listed_dream.status)

Errors
A non-exhaustive list of possible dreaming errors is below.  
| `error.type`  | When  |  
| --- | --- |  
| `timeout`  | The pipeline exceeded its runtime budget.  |  
| `internal_error`  | Unclassified pipeline failure.  |  
| `memory_store_org_limit_exceeded`  | Your organization hit its memory-store cap while the pipeline was provisioning working storage.  |  
| `input_memory_store_too_large`  | The input memory store exceeds the pipeline's size limit.  |  
| `input_memory_store_unavailable`  | The input memory store was archived or deleted after the dream was created.  |  
| `input_session_unavailable`  | An input session was archived or deleted after the dream was created.  |  
Billing
Dreams are billed at standard API token rates for the model you select; `usage` on the resource reports the exact totals. Cost scales roughly linearly with the number and length of input sessions. Start with a small batch of sessions and scale up once you're satisfied with the curation quality.
Limits  
| Limit  | Value  |  
| --- | --- |  
| Sessions per dream  | 100  |  
|  `instructions` length  | 4,096 characters  |  
| Supported models  |  `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6`  |  
Default rate limits apply to dream creation while this feature is in beta. [Contact support](https://support.claude.com) if you need higher limits.
