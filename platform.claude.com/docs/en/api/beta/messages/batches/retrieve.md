<!-- source: https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve -->

# Retrieve a Message Batch
GET/v1/messages/batches/{message_batch_id}
This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Path ParametersExpand Collapse 
message_batch_id: string
ID of the Message Batch.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#retrieve.message_batch_id)
##### Header ParametersExpand Collapse 
"anthropic-beta": optional array of [AnthropicBeta](https://platform.claude.com/docs/en/api/beta#anthropic_beta)
Optional header to specify the beta version(s) you want to use.
string
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B0%5D)
"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more
"message-batches-2024-09-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B0%5D)
"prompt-caching-2024-07-31"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B1%5D)
"computer-use-2024-10-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B2%5D)
"computer-use-2025-01-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B3%5D)
"pdfs-2024-09-25"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B4%5D)
"token-counting-2024-11-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B5%5D)
"token-efficient-tools-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B6%5D)
"output-128k-2025-02-19"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B7%5D)
"files-api-2025-04-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B8%5D)
"mcp-client-2025-04-04"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B9%5D)
"mcp-client-2025-11-20"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B10%5D)
"dev-full-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B11%5D)
"interleaved-thinking-2025-05-14"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B12%5D)
"code-execution-2025-05-22"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B13%5D)
"extended-cache-ttl-2025-04-11"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B14%5D)
"context-1m-2025-08-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B15%5D)
"context-management-2025-06-27"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B16%5D)
"model-context-window-exceeded-2025-08-26"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B17%5D)
"skills-2025-10-02"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B18%5D)
"fast-mode-2026-02-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B19%5D)
"output-300k-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B20%5D)
"user-profiles-2026-03-24"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B21%5D)
"advisor-tool-2026-03-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B22%5D)
"managed-agents-2026-04-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B23%5D)
"cache-diagnosis-2026-04-07"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B24%5D)
"thinking-token-count-2026-05-13"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B25%5D)
"server-side-fallback-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B26%5D)
"fallback-credit-2026-06-01"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D%5B27%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#anthropic_beta%5B1%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#retrieve.betas)
BetaMessageBatch object { id, archived_at, cancel_initiated_at, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.id)
archived_at: string
RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.archived_at)
cancel_initiated_at: string
RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.cancel_initiated_at)
created_at: string
RFC 3339 datetime string representing the time at which the Message Batch was created.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.created_at)
ended_at: string
RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.
Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.
formatdate-time
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.ended_at)
expires_at: string
RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.expires_at)
processing_status: "in_progress" or "canceling" or "ended"
Processing status of the Message Batch.
"in_progress"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.processing_status%5B0%5D)
"canceling"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.processing_status%5B1%5D)
"ended"
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.processing_status%5B2%5D)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.processing_status)
request_counts: [BetaMessageBatchRequestCounts](https://platform.claude.com/docs/en/api/beta#beta_message_batch_request_counts) { canceled, errored, expired, 2 more } 
Tallies requests within the Message Batch, categorized by their status.
Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.
canceled: number
Number of requests in the Message Batch that have been canceled.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.canceled)
errored: number
Number of requests in the Message Batch that encountered an error.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.errored)
expired: number
Number of requests in the Message Batch that have expired.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.expired)
processing: number
Number of requests in the Message Batch that are processing.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.processing)
succeeded: number
Number of requests in the Message Batch that have completed successfully.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts%20%2B%20\(resource\)%20beta.messages.batches.succeeded)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.request_counts)
results_url: string
URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.
Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.results_url)
type: "message_batch"
Object type.
For Message Batches, this is always `"message_batch"`.
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch.type)
[](https://platform.claude.com/docs/en/api/beta/messages/batches/retrieve#beta_message_batch)
Retrieve a Message Batch
cURL

curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
    -H 'anthropic-beta: message-batches-2024-09-24' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"

  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "archived_at": "2024-08-20T18:37:24.100435Z",
  "cancel_initiated_at": "2024-08-20T18:37:24.100435Z",
  "created_at": "2024-08-20T18:37:24.100435Z",
  "ended_at": "2024-08-20T18:37:24.100435Z",
  "expires_at": "2024-08-20T18:37:24.100435Z",
  "processing_status": "in_progress",
  "request_counts": {
    "canceled": 10,
    "errored": 30,
    "expired": 10,
    "processing": 100,
    "succeeded": 50
  "results_url": "https://api.anthropic.com/v1/messages/batches/msgbatch_013Zva2CMHLNnXjNJJKqJ2EF/results",
  "type": "message_batch"
