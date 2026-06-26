<!-- source: https://platform.claude.com/docs/en/api/messages/batches/list -->

# List Message Batches
GET/v1/messages/batches
List all Message Batches within a Workspace. Most recently created batches are returned first.
Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)
##### Query ParametersExpand Collapse 
after_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately after this object.
[](https://platform.claude.com/docs/en/api/messages/batches/list#list.after_id)
before_id: optional string
ID of the object to use as a cursor for pagination. When provided, returns the page of results immediately before this object.
[](https://platform.claude.com/docs/en/api/messages/batches/list#list.before_id)
limit: optional number
Number of items to return per page.
Defaults to `20`. Ranges from `1` to `1000`.
maximum1000
minimum1
[](https://platform.claude.com/docs/en/api/messages/batches/list#list.limit)
data: array of [MessageBatch](https://platform.claude.com/docs/en/api/messages#message_batch) { id, archived_at, cancel_initiated_at, 7 more } 
Unique object identifier.
The format and length of IDs may change over time.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.id)
archived_at: string
RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.archived_at)
cancel_initiated_at: string
RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.cancel_initiated_at)
created_at: string
RFC 3339 datetime string representing the time at which the Message Batch was created.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.created_at)
ended_at: string
RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.
Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.
formatdate-time
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.ended_at)
expires_at: string
RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.expires_at)
processing_status: "in_progress" or "canceling" or "ended"
Processing status of the Message Batch.
"in_progress"
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.processing_status%5B0%5D)
"canceling"
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.processing_status%5B1%5D)
"ended"
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.processing_status%5B2%5D)
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.processing_status)
request_counts: [MessageBatchRequestCounts](https://platform.claude.com/docs/en/api/messages#message_batch_request_counts) { canceled, errored, expired, 2 more } 
Tallies requests within the Message Batch, categorized by their status.
Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.
canceled: number
Number of requests in the Message Batch that have been canceled.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.canceled)
errored: number
Number of requests in the Message Batch that encountered an error.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.errored)
expired: number
Number of requests in the Message Batch that have expired.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.expired)
processing: number
Number of requests in the Message Batch that are processing.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.processing)
succeeded: number
Number of requests in the Message Batch that have completed successfully.
This is zero until processing of the entire Message Batch has ended.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts%20%2B%20\(resource\)%20messages.batches.succeeded)
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.request_counts)
results_url: string
URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.
Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.results_url)
type: "message_batch"
Object type.
For Message Batches, this is always `"message_batch"`.
[](https://platform.claude.com/docs/en/api/messages/batches/list#message_batch.type)
[](https://platform.claude.com/docs/en/api/messages/batches/list#list)
first_id: string
First ID in the `data` list. Can be used as the `before_id` for the previous page.
[](https://platform.claude.com/docs/en/api/messages/batches/list#list)
has_more: boolean
Indicates if there are more results in the requested page direction.
[](https://platform.claude.com/docs/en/api/messages/batches/list#list)
last_id: string
Last ID in the `data` list. Can be used as the `after_id` for the next page.
[](https://platform.claude.com/docs/en/api/messages/batches/list#list)
List Message Batches
cURL

curl https://api.anthropic.com/v1/messages/batches \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"

  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"

  "data": [
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
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id"
