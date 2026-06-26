<!-- source: https://platform.claude.com/docs/en/api/errors -->

# Errors
HTTP errors
The API follows a predictable HTTP error code format:
  * 400 - `invalid_request_error`: There was an issue with the format or content of your request. This error type may also be used for other 4XX status codes not listed in this section.
  * 401 - `authentication_error`: There's an issue with your API key. On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.
  * 402 - `billing_error`: There's an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you're using Claude Platform on AWS.
  * 403 - `permission_error`: Your API key does not have permission to use the specified resource.
  * 404 - `not_found_error`: The requested resource was not found.
  * 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](https://platform.claude.com/docs/en/api/errors#request-size-limits) for per-endpoint maximums.
  * 429 - `rate_limit_error`: Your account has hit a rate limit.
  * 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems.
  * 504 - `timeout_error`: The request timed out while processing. Consider using [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for long-running requests.
  * 529 - `overloaded_error`: The API is temporarily overloaded.

529 errors can occur when APIs experience high traffic across all users.
In rare cases, if your organization has a sharp increase in usage, you might see 429 errors because of acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.

When receiving a [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) response over SSE, it's possible that an error can occur after returning a 200 response, in which case error handling wouldn't follow these standard mechanisms.
Request size limits
The API enforces request size limits to ensure optimal performance:  
| Endpoint type  | Maximum request size  |  
| --- | --- |  
| Messages API  | 32 MB  |  
| Token Counting API  | 32 MB  |  
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | 256 MB  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | 500 MB  |  
If you exceed these limits, you'll receive a 413 `request_too_large` error. On the direct Claude API, this error is returned from Cloudflare before the request reaches the API servers.
Error shapes
Errors are always returned as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:
JSON

  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"

In accordance with the [versioning](https://platform.claude.com/docs/en/api/versioning) policy, the values within these objects may expand, and it is possible that the `type` values will grow over time.
SDK error types
The official SDKs raise typed exceptions for these errors instead of returning raw JSON, and the class names and namespaces differ by language. For example, a 404 surfaces as `anthropic.NotFoundError` in Python, `Anthropic::Errors::NotFoundError` in Ruby, `com.anthropic.errors.NotFoundException` in Java, and as a single `*anthropic.Error` value (branch on `StatusCode`) in Go. Catch the SDK's typed classes rather than string-matching error messages, handling the most specific classes first. Each SDK page documents its full exception hierarchy:
  * [Python](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-errors) · [TypeScript](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript#handling-errors) · [C#](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/csharp#error-handling) · [Go](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go#error-handling) · [Java](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java#error-handling) · [PHP](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#error-handling) · [Ruby](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby#handling-errors)

Request ID
Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. When contacting support about a specific request, include this ID to help quickly resolve your issue.
On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.
The official SDKs provide the Anthropic request ID as a property on top-level response objects, containing the value of the `request-id` header. On Claude Platform on AWS, use the raw-response accessor to also read the AWS request ID from the HTTP headers:
CLIPythonTypeScriptPython (Claude Platform on AWS)TypeScript (Claude Platform on AWS)

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(f"Request ID: {message._request_id}")

For Claude Platform on AWS request-ID examples in other languages, see [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids).
Long requests

Consider using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches) for long running requests, especially those over 10 minutes.
Avoid setting a large `max_tokens` value without using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches):
  * Some networks may drop idle connections after a variable period of time, which can cause the request to fail or timeout without receiving a response from Anthropic.
  * Networks differ in reliability; the [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches) can help you manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, you should be aware that setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.
The [SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) validate that your non-streaming Messages API requests are not expected to exceed a 10 minute timeout and also will set a socket option for TCP keep-alive.
If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` (Python) or `.finalMessage()` (TypeScript) to get the complete `Message` object without writing event-handling code:
PythonTypeScript

with client.messages.stream(
    max_tokens=128000,
    messages=[{"role": "user", "content": "Write a detailed analysis..."}],
    model="claude-opus-4-8",
) as stream:
    message = stream.get_final_message()
print(message.content)

See [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for more details.
Common validation errors
### 
Prefill not supported
Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 do not support prefilling assistant messages. Sending a request with a prefilled last assistant message to any of these models returns a 400 `invalid_request_error`:

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Prefilling assistant messages is not supported for this model."

Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) on models that support it, system prompt instructions, or [`output_config.format`](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-outputs) instead.
### 
Thinking blocks cannot be modified
If the most recent assistant message contains `thinking` or `redacted_thinking` blocks that were edited, reordered, filtered out, or reconstructed before being sent back to the API, the request returns a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.

With tool use, every `thinking` and `redacted_thinking` block from the assistant turn must be passed back exactly as received, including blocks whose `thinking` field is empty. Pass thinking blocks back unchanged, and if your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. See [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#preserving-thinking-blocks) and [Thinking output on Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-output-on-claude-fable-5-and-claude-mythos-5).
### 
Outbound web identity federation disabled (Claude Platform on AWS)
If every request to [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once per AWS account. See [Enable outbound web identity federation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#enable-outbound-web-identity-federation) for details.
  * [HTTP errors](https://platform.claude.com/docs/en/api/errors#http-errors)
  * [Request size limits](https://platform.claude.com/docs/en/api/errors#request-size-limits)
  * [Error shapes](https://platform.claude.com/docs/en/api/errors#error-shapes)
  * [SDK error types](https://platform.claude.com/docs/en/api/errors#sdk-error-types)
  * [Request ID](https://platform.claude.com/docs/en/api/errors#request-id)
  * [Long requests](https://platform.claude.com/docs/en/api/errors#long-requests)
  * [Common validation errors](https://platform.claude.com/docs/en/api/errors#common-validation-errors)
  * [Prefill not supported](https://platform.claude.com/docs/en/api/errors#prefill-not-supported)
  * [Thinking blocks cannot be modified](https://platform.claude.com/docs/en/api/errors#thinking-blocks-cannot-be-modified)
  * [Outbound web identity federation disabled (Claude Platform on AWS)](https://platform.claude.com/docs/en/api/errors#outbound-web-identity-federation-disabled-claude-platform-on-aws)

API reference/Using the API
# Errors
HTTP errors
The API follows a predictable HTTP error code format:
  * 400 - `invalid_request_error`: There was an issue with the format or content of your request. This error type may also be used for other 4XX status codes not listed in this section.
  * 401 - `authentication_error`: There's an issue with your API key. On Claude Platform on AWS, this can also indicate a problem with your AWS credentials or SigV4 signature.
  * 402 - `billing_error`: There's an issue with your billing or payment information. Check your payment details in the [Claude Console](https://platform.claude.com), or in AWS Marketplace if you're using Claude Platform on AWS.
  * 403 - `permission_error`: Your API key does not have permission to use the specified resource.
  * 404 - `not_found_error`: The requested resource was not found.
  * 413 - `request_too_large`: Request exceeds the maximum allowed number of bytes. See [Request size limits](https://platform.claude.com/docs/en/api/errors#request-size-limits) for per-endpoint maximums.
  * 429 - `rate_limit_error`: Your account has hit a rate limit.
  * 500 - `api_error`: An unexpected error has occurred internal to Anthropic's systems.
  * 504 - `timeout_error`: The request timed out while processing. Consider using [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) for long-running requests.
  * 529 - `overloaded_error`: The API is temporarily overloaded.

529 errors can occur when APIs experience high traffic across all users.
In rare cases, if your organization has a sharp increase in usage, you might see 429 errors because of acceleration limits on the API. To avoid hitting acceleration limits, ramp up your traffic gradually and maintain consistent usage patterns.

When receiving a [streaming](https://platform.claude.com/docs/en/build-with-claude/streaming) response over SSE, it's possible that an error can occur after returning a 200 response, in which case error handling wouldn't follow these standard mechanisms.
Request size limits
The API enforces request size limits to ensure optimal performance:  
| Endpoint type  | Maximum request size  |  
| --- | --- |  
| Messages API  | 32 MB  |  
| Token Counting API  | 32 MB  |  
| [Batch API](https://platform.claude.com/docs/en/build-with-claude/batch-processing)  | 256 MB  |  
| [Files API](https://platform.claude.com/docs/en/build-with-claude/files)  | 500 MB  |  
If you exceed these limits, you'll receive a 413 `request_too_large` error. On the direct Claude API, this error is returned from Cloudflare before the request reaches the API servers.
Error shapes
Errors are always returned as JSON, with a top-level `error` object that always includes a `type` and `message` value. The response also includes a `request_id` field for easier tracking and debugging. For example:
JSON

  "type": "error",
  "error": {
    "type": "not_found_error",
    "message": "The requested resource could not be found."
  "request_id": "req_011CSHoEeqs5C35K2UUqR7Fy"

In accordance with the [versioning](https://platform.claude.com/docs/en/api/versioning) policy, the values within these objects may expand, and it is possible that the `type` values will grow over time.
SDK error types
The official SDKs raise typed exceptions for these errors instead of returning raw JSON, and the class names and namespaces differ by language. For example, a 404 surfaces as `anthropic.NotFoundError` in Python, `Anthropic::Errors::NotFoundError` in Ruby, `com.anthropic.errors.NotFoundException` in Java, and as a single `*anthropic.Error` value (branch on `StatusCode`) in Go. Catch the SDK's typed classes rather than string-matching error messages, handling the most specific classes first. Each SDK page documents its full exception hierarchy:
  * [Python](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-errors) · [TypeScript](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/typescript#handling-errors) · [C#](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/csharp#error-handling) · [Go](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go#error-handling) · [Java](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/java#error-handling) · [PHP](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/php#error-handling) · [Ruby](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/ruby#handling-errors)

Request ID
Every API response includes a unique `request-id` header. This header contains a value such as `req_018EeWyXxfu5pfWkrYcMdjWG`. When contacting support about a specific request, include this ID to help quickly resolve your issue.
On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), responses include two request IDs: the AWS request ID (`x-amzn-requestid`, primary, indexed in CloudTrail) and the Anthropic request ID (`request-id`, secondary). Use the AWS request ID for CloudTrail lookups and the Anthropic request ID for Anthropic support tickets.
The official SDKs provide the Anthropic request ID as a property on top-level response objects, containing the value of the `request-id` header. On Claude Platform on AWS, use the raw-response accessor to also read the AWS request ID from the HTTP headers:
CLIPythonTypeScriptPython (Claude Platform on AWS)TypeScript (Claude Platform on AWS)

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
)
print(f"Request ID: {message._request_id}")

For Claude Platform on AWS request-ID examples in other languages, see [Request IDs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#request-ids).
Long requests

Consider using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches) for long running requests, especially those over 10 minutes.
Avoid setting a large `max_tokens` value without using the [streaming Messages API](https://platform.claude.com/docs/en/build-with-claude/streaming) or [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches):
  * Some networks may drop idle connections after a variable period of time, which can cause the request to fail or timeout without receiving a response from Anthropic.
  * Networks differ in reliability; the [Message Batches API](https://platform.claude.com/docs/en/api/creating-message-batches) can help you manage the risk of network issues by allowing you to poll for results rather than requiring an uninterrupted network connection.

If you are building a direct API integration, you should be aware that setting a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/programming.html) can reduce the impact of idle connection timeouts on some networks.
The [SDKs](https://platform.claude.com/docs/en/cli-sdks-libraries/overview) validate that your non-streaming Messages API requests are not expected to exceed a 10 minute timeout and also will set a socket option for TCP keep-alive.
If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` (Python) or `.finalMessage()` (TypeScript) to get the complete `Message` object without writing event-handling code:
PythonTypeScript

with client.messages.stream(
    max_tokens=128000,
    messages=[{"role": "user", "content": "Write a detailed analysis..."}],
    model="claude-opus-4-8",
) as stream:
    message = stream.get_final_message()
print(message.content)

See [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming#get-the-final-message-without-handling-events) for more details.
Common validation errors
### 
Prefill not supported
Claude Fable 5, [Claude Mythos 5](https://anthropic.com/glasswing), [Claude Mythos Preview](https://anthropic.com/glasswing), Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 do not support prefilling assistant messages. Sending a request with a prefilled last assistant message to any of these models returns a 400 `invalid_request_error`:

  "type": "error",
  "error": {
    "type": "invalid_request_error",
    "message": "Prefilling assistant messages is not supported for this model."

Use [structured outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs) on models that support it, system prompt instructions, or [`output_config.format`](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#json-outputs) instead.
### 
Thinking blocks cannot be modified
If the most recent assistant message contains `thinking` or `redacted_thinking` blocks that were edited, reordered, filtered out, or reconstructed before being sent back to the API, the request returns a 400 `invalid_request_error`. The error message starts with the position of the offending block (for example, `messages.1.content.0`) and contains:

`thinking` or `redacted_thinking` blocks in the latest assistant message cannot be modified. These blocks must remain as they were in the original response.

With tool use, every `thinking` and `redacted_thinking` block from the assistant turn must be passed back exactly as received, including blocks whose `thinking` field is empty. Pass thinking blocks back unchanged, and if your application filters content blocks by type before resending, include both `thinking` and `redacted_thinking`. See [Preserving thinking blocks](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#preserving-thinking-blocks) and [Thinking output on Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking#thinking-output-on-claude-fable-5-and-claude-mythos-5).
### 
Outbound web identity federation disabled (Claude Platform on AWS)
If every request to [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) returns `"Outbound web identity federation is disabled for your account"`, run `aws iam enable-outbound-web-identity-federation` once per AWS account. See [Enable outbound web identity federation](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#enable-outbound-web-identity-federation) for details.
