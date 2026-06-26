<!-- source: https://platform.claude.com/docs/en/api/retrieving-message-batches -->

# Retrieve a Message Batch
GET/v1/messages/batches/{message_batch_id}
This endpoint is idempotent and can be used to poll for Message Batch completion. To access the results of a Message Batch, make a request to the `results_url` field in the response.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Path ParametersExpand Collapse 
message_batch_id: string
ID of the Message Batch.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#retrieve.message_batch_id)
MessageBatch object { id, archived_at, cancel_initiated_at, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.id)
archived_at: string
RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.archived_at)
cancel_initiated_at: string
RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.cancel_initiated_at)
created_at: string
RFC 3339 datetime string representing the time at which the Message Batch was created.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.created_at)
ended_at: string
RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.
Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.
formatdate-time
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.ended_at)
expires_at: string
RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.expires_at)
processing_status: "in_progress" or "canceling" or "ended"
Processing status of the Message Batch.
"in_progress"
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.processing_status%5B0%5D)
"canceling"
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.processing_status%5B1%5D)
"ended"
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.processing_status%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.processing_status)
request_counts: [MessageBatchRequestCounts](https://platform.claude.com/docs/en/api/messages#message_batch_request_counts) { canceled, errored, expired, 2 more } 
Tallies requests within the Message Batch, categorized by their status.
Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.
canceled: number
Number of requests in the Message Batch that have been canceled.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.canceled)
errored: number
Number of requests in the Message Batch that encountered an error.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.errored)
expired: number
Number of requests in the Message Batch that have expired.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.expired)
processing: number
Number of requests in the Message Batch that are processing.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.processing)
succeeded: number
Number of requests in the Message Batch that have completed successfully.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.succeeded)
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.request_counts)
results_url: string
URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.
Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.results_url)
type: "message_batch"
Object type.
For Message Batches, this is always `"message_batch"`.
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch.type)
[](https://platform.claude.com/docs/en/api/messages/batches/retrieve#message_batch)
Retrieve a Message Batch
cURL

curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
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
