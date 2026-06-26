<!-- source: https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python -->

# Python SDK
Install and configure the Anthropic Python SDK with sync and async client support
The Anthropic Python SDK provides convenient access to the Anthropic REST API from Python applications. It supports both synchronous and asynchronous operations, streaming, and integrations with Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS.
For API feature documentation with code examples, see the [API reference](https://platform.claude.com/docs/en/api/overview). This page covers Python-specific SDK features and configuration.
Installation

pip install anthropic

For platform-specific integrations or improved async performance, install with extras:

# For Amazon Bedrock support
pip install "anthropic[bedrock]"

# For Google Cloud support
pip install "anthropic[vertex]"

# For Claude Platform on AWS support
pip install "anthropic[aws]"

# Microsoft Foundry support is included in the base package

# For improved async performance with aiohttp
pip install "anthropic[aiohttp]"

Requirements
Python 3.9 or later is required.
Usage

import os
from anthropic import Anthropic

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
)
print(message.content)


Consider using [python-dotenv](https://pypi.org/project/python-dotenv/) to add `ANTHROPIC_API_KEY="my-anthropic-api-key"` to your `.env` file so that your API key isn't stored in source control.
For authentication options including Workload Identity Federation, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication).
Async usage

import os
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

async def main() -> None:
    message = await client.messages.create(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Hello, Claude",
        ],
        model="claude-opus-4-8",
    )
    print(message.content)

asyncio.run(main())

### 
Using aiohttp for better concurrency
For improved async performance, you can use the `aiohttp` HTTP backend instead of the default `httpx`:

import os
import asyncio
from anthropic import AsyncAnthropic, DefaultAioHttpClient

async def main() -> None:
    async with AsyncAnthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                    "role": "user",
                    "content": "Hello, Claude",
            ],
            model="claude-opus-4-8",
        )
        print(message.content)

asyncio.run(main())

Streaming responses
The SDK provides support for streaming responses using Server-Sent Events (SSE).

client = Anthropic()

stream = client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
    stream=True,
)
for event in stream:
    print(event.type)

The async client uses the exact same interface:

client = AsyncAnthropic()

stream = await client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
    stream=True,
)
async for event in stream:
    print(event.type)

### 
Streaming helpers
The SDK also provides streaming helpers that use context managers and provide access to the accumulated text and the final message:

async def main() -> None:
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Say hello there!",
        ],
        model="claude-opus-4-8",
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)
        print()

        message = await stream.get_final_message()
        print(message.to_json())

asyncio.run(main())

Streaming with `client.messages.stream(...)` exposes various helpers including accumulation and SDK-specific events.
Alternatively, you can use `client.messages.create(..., stream=True)` which only returns an iterable of the events in the stream and uses less memory (it doesn't build up a final message object for you).
Token counting
You can see the exact usage for a given request through the `usage` response property:

message = client.messages.create(...)
print(message.usage)
# Usage(input_tokens=25, output_tokens=13)

You can also count tokens before making a request:

count = client.messages.count_tokens(
    model="claude-opus-4-8", messages=[{"role": "user", "content": "Hello, world"}]
)
print(count.input_tokens)  # 10

Tool use
This SDK provides support for tool use, also known as function calling. For more details, see [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
### 
Tool helpers
The SDK provides helpers for defining and running tools as pure Python functions. The `@beta_tool` decorator generates the tool schema from the function signature and docstring:

import json
from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def get_weather(location: str) -> str:
    """Get the weather for a given location.

    Args:
        location: The city and state, for example, San Francisco, CA
    Returns:
        A JSON-encoded string with the location, temperature, and weather condition.
    """
    return json.dumps(
            "location": location,
            "temperature": "68°F",
            "condition": "Sunny",
    )

# Use the tool_runner to automatically handle tool calls
runner = client.beta.messages.tool_runner(
    max_tokens=1024,
    model="claude-opus-4-8",
    tools=[get_weather],
    messages=[
        {"role": "user", "content": "What is the weather in SF?"},
    ],
)
for message in runner:
    print(message)

On every iteration, an API request is made. If Claude wants to call one of the given tools, it's automatically called, and the result is returned directly to the model in the next iteration.
Message batches
This SDK provides support for the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) under `client.messages.batches`.
### 
Creating a batch
Message Batches takes an array of requests, where each object has a `custom_id` identifier and the same request `params` as the standard Messages API:

client.messages.batches.create(
    requests=[
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hello, world"}],
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hi again, friend"}],
    ]
)

### 
Getting results from a batch
Once a Message Batch has been processed, indicated by `.processing_status == 'ended'`, you can access the results with `.batches.results()`:

client = anthropic.Anthropic()
batch_id = "batch_abc123"
result_stream = client.messages.batches.results(batch_id)
for entry in result_stream:
    if entry.result.type == "succeeded":
        print(entry.result.message.content)

File uploads
Request parameters that correspond to file uploads can be passed in many different forms:
  * A `PathLike` object (for example, `pathlib.Path`)
  * A tuple of `(filename, content, content_type)`
  * A `BinaryIO` file-like object

from pathlib import Path
from anthropic import Anthropic

client = Anthropic()

# Upload using a file path
client.beta.files.upload(
    file=Path("/path/to/file"),
)

# Upload using bytes
client.beta.files.upload(
    file=("file.txt", b"my bytes", "text/plain"),
)

The async client uses the exact same interface. If you pass a `PathLike` instance, the file contents are read asynchronously automatically.
Handling errors
When the library is unable to connect to the API, or if the API returns a non-success status code (i.e., 4xx or 5xx response), a subclass of `APIError` is raised:

import anthropic
# ...
try:
    message = client.messages.create(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Hello, Claude",
        ],
        model="claude-opus-4-8",
    )
except anthropic.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx
except anthropic.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except anthropic.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)

Error codes are as follows:  
| Status Code  | Error Type  |  
| --- | --- |  
| 400  | `BadRequestError`  |  
| 401  | `AuthenticationError`  |  
| 403  | `PermissionDeniedError`  |  
| 404  | `NotFoundError`  |  
| 409  | `ConflictError`  |  
| 422  | `UnprocessableEntityError`  |  
| 429  | `RateLimitError`  |  
| >=500  | `InternalServerError`  |  
| N/A  | `APIConnectionError`  |  
Request IDs
> For more information on debugging requests, see [Request ID](https://platform.claude.com/docs/en/api/errors#request-id).
All object responses in the SDK provide a `_request_id` property which is added from the `request-id` response header so that you can quickly log failing requests and report them back to Anthropic.

message = client.messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)
print(message._request_id)  # e.g., req_018EeWyXxfu5pfWkrYcMdjWG

Unlike other properties that use an `_` prefix, the `_request_id` property is public. Unless documented otherwise, all other `_` prefix properties, methods, and modules are private.
Retries
Certain errors are automatically retried 2 times by default, with a short exponential backoff. Connection errors (for example, because of a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, and >=500 Internal errors are all retried by default.
You can use the `max_retries` option to configure or disable this:

# Configure the default for all requests:
client = Anthropic(
    max_retries=0,  # default is 2
)

# Or, configure per-request:
client.with_options(max_retries=5).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

Timeouts
By default requests time out after 10 minutes. You can configure this with a `timeout` option, which accepts a float or an `httpx.Timeout` object:

import httpx
from anthropic import Anthropic

# Configure the default for all requests:
client = Anthropic(
    timeout=20.0,  # 20 seconds (default is 10 minutes)
)

# More granular control:
client = Anthropic(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

On timeout, an `APITimeoutError` is thrown.
Note that requests which time out will be [retried twice by default](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#retries).
Long requests

Consider using the streaming [Messages API](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#streaming-responses) for longer running requests.
Avoid setting a large `max_tokens` value without using streaming. Some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#timeouts) without receiving a response from Anthropic.
The SDK will throw a `ValueError` if a non-streaming request is expected to take longer than approximately 10 minutes. Passing `stream=True` or overriding the `timeout` option at the client or request level disables this error.
An expected request latency longer than the [timeout](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#timeouts) for a non-streaming request will result in the client terminating the connection and retrying without receiving a response.
The SDK sets a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html) option to reduce the impact of idle connection timeouts on some networks. This can be overridden by passing a custom `http_client` option to the client.
Auto-pagination
List methods in the Claude API are paginated. You can use the `for` syntax to iterate through items across all pages:

client = Anthropic()

all_batches = []
# Automatically fetches more pages as needed.
for batch in client.messages.batches.list(limit=20):
    all_batches.append(batch)
print(all_batches)

For async iteration:

async def main() -> None:
    all_batches = []
    async for batch in client.messages.batches.list(limit=20):
        all_batches.append(batch)
    print(all_batches)

asyncio.run(main())

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

first_page = await client.messages.batches.list(limit=20)

if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.

Or work directly with the returned data:

first_page = await client.messages.batches.list(limit=20)

print(f"next page cursor: {first_page.last_id}")
for batch in first_page.data:
    print(batch.id)

# Remove `await` for non-async usage.

Default headers
The SDK automatically sends the `anthropic-version` header set to `2023-06-01`.
If you need to, you can override it by setting default headers on the client object or per-request.

Overriding default headers may result in incorrect types and other unexpected or undefined behavior in the SDK.

# Set default headers for all requests on the client
client = Anthropic(
    default_headers={"anthropic-version": "My-Custom-Value"},
)

# Or override per-request
client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
    extra_headers={"anthropic-version": "My-Custom-Value"},
)

Type system
### 
Request parameters
Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also have helper methods for things like serializing back into JSON ([`v1`](https://docs.pydantic.dev/1.10/usage/models/), [`v2`](https://docs.pydantic.dev/latest/concepts/serialization/)).
Typed requests and responses provide autocomplete and documentation within your editor. If you'd like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.
### 
Response models
To convert a Pydantic model to a dictionary, use the helper methods:

message = client.messages.create(...)

# Convert to JSON string
json_str = message.to_json()

# Convert to dictionary
data = message.to_dict()

### 
Handling null vs missing fields
In responses, you can distinguish between fields that are explicitly `null` versus fields that were not returned (missing):

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
)
if response.my_field is None:
    if "my_field" not in response.model_fields_set:
        print("field was not in the response")
    else:
        print("field was null")

Advanced usage
### 
Accessing raw response data (for example, headers)
The "raw" `Response` returned by `httpx` can be accessed through the `.with_raw_response` property on the client. This is useful for accessing response headers or other metadata:

client = Anthropic()

response = client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

print(response.headers.get("request-id"))
message = (
    response.parse()
)  # get the object that `messages.create()` would have returned
print(message.content)

These methods return an `APIResponse` object.
### 
Streaming response body
The `.with_raw_response` approach eagerly reads the full response body when you make the request. To stream the response body instead, use `.with_streaming_response`, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()`, or `.parse()`. In the async client, these are async methods.

with client.messages.with_streaming_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
) as response:
    print(response.headers.get("request-id"))

    for line in response.iter_lines():
        print(line)

The context manager is required so that the response will reliably be closed.
### 
Logging
The SDK uses the standard library `logging` module.
You can enable logging by setting the environment variable `ANTHROPIC_LOG` to `debug` or `info`:

export ANTHROPIC_LOG=debug

### 
Making custom/undocumented requests
This library is typed for convenient access to the documented API. If you need to access undocumented endpoints, params, or response properties, the library can still be used.
#### 
Undocumented endpoints
To make requests to undocumented endpoints, you can use `client.get`, `client.post`, and other HTTP verbs. Options on the client, such as retries, will be respected when making these requests.

import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.json())

#### 
Undocumented request params
If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request options.

The `extra_` parameters override documented parameters of the same name. For security reasons, ensure these methods are only used with trusted input data.
#### 
Undocumented response properties
To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You can also get all extra fields on the Pydantic model as a dict with `response.model_extra`.
### 
Configuring the HTTP client
You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including support for proxies and transports:

import httpx
from anthropic import Anthropic, DefaultHttpxClient

client = Anthropic(
    # Or use the `ANTHROPIC_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)

You can also customize the client on a per-request basis by using `with_options()`:

client.with_options(http_client=DefaultHttpxClient(...))

Use `DefaultHttpxClient` and `DefaultAsyncHttpxClient` instead of raw `httpx.Client` and `httpx.AsyncClient` to ensure the SDK's default configuration (timeouts, connection limits, etc.) is preserved.
### 
Managing HTTP resources
By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

with Anthropic() as client:
    message = client.messages.create(...)

# HTTP client is automatically closed

Beta features
Beta features are available before general release to get early feedback and test new functionality. You can check the availability of all of Claude's capabilities and tools in the [build with Claude overview](https://platform.claude.com/docs/en/build-with-claude/overview).
You can access most beta API features through the `beta` property of the client. To enable a particular beta feature, you need to add the appropriate [beta header](https://platform.claude.com/docs/en/api/beta-headers) to the `betas` field when creating a message.
For example, to use the [Files API](https://platform.claude.com/docs/en/build-with-claude/files):

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": "file_abc123",
            ],
    ],
    betas=["files-api-2025-04-14"],
)

Platform integrations
For detailed platform setup guides with code examples, see:
  * [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
  * [Amazon Bedrock (legacy)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)
  * [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)
  * [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
  * [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)

All five client classes are included in the base `anthropic` package:  
| Provider  | Client  | Extra dependencies  |  
| --- | --- | --- |  
| Bedrock  | `from anthropic import AnthropicBedrockMantle`  | `pip install "anthropic[bedrock]"`  |  
| Bedrock (`bedrock-runtime` path)  | `from anthropic import AnthropicBedrock`  | `pip install "anthropic[bedrock]"`  |  
| Agent Platform  | `from anthropic import AnthropicVertex`  | `pip install "anthropic[vertex]"`  |  
| Foundry  | `from anthropic import AnthropicFoundry`  | None  |  
| Claude Platform on AWS  | `from anthropic import AnthropicAWS`  | `pip install "anthropic[aws]"`  |  
The `AnthropicAWS` client is in beta. Pass `workspace_id` to the constructor or set the `ANTHROPIC_AWS_WORKSPACE_ID` environment variable.
Use `AnthropicBedrockMantle` for new projects; `AnthropicBedrock` remains for existing applications using the Bedrock `InvokeModel` API.
Semantic versioning
This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:
  1. Changes that only affect static types, without breaking runtime behavior.
  2. Changes to library internals which are technically public but not intended or documented for external use.
  3. Changes that aren't expected to impact the vast majority of users in practice.

### 
Determining the installed version
If you've upgraded to the latest version but aren't seeing new features you were expecting, your Python environment is likely still using an older version. You can determine the version being used at runtime with:

print(anthropic.__version__)

Additional resources
  * [GitHub repository](https://github.com/anthropics/anthropic-sdk-python)
  * [API reference](https://platform.claude.com/docs/en/api/overview)
  * [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming)
  * [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)

  * [Installation](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#installation)
  * [Requirements](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#requirements)
  * [Usage](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#usage)
  * [Async usage](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#async-usage)
  * [Using aiohttp for better concurrency](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#using-aiohttp-for-better-concurrency)
  * [Streaming responses](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#streaming-responses)
  * [Streaming helpers](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#streaming-helpers)
  * [Token counting](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#token-counting)
  * [Tool use](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#tool-use)
  * [Tool helpers](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#tool-helpers)
  * [Message batches](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#message-batches)
  * [Creating a batch](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#creating-a-batch)
  * [Getting results from a batch](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#getting-results-from-a-batch)
  * [File uploads](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#file-uploads)
  * [Handling errors](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-errors)
  * [Request IDs](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#request-ids)
  * [Retries](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#retries)
  * [Timeouts](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#timeouts)
  * [Long requests](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#long-requests)
  * [Auto-pagination](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#auto-pagination)
  * [Default headers](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#default-headers)
  * [Type system](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#type-system)
  * [Request parameters](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#request-parameters)
  * [Response models](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#response-models)
  * [Handling null vs missing fields](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#handling-null-vs-missing-fields)
  * [Advanced usage](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#advanced-usage)
  * [Accessing raw response data (for example, headers)](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#accessing-raw-response-data-for-example-headers)
  * [Streaming response body](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#streaming-response-body)
  * [Logging](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#logging)
  * [Making custom/undocumented requests](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#making-custom-undocumented-requests)
  * [Configuring the HTTP client](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#configuring-the-http-client)
  * [Managing HTTP resources](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#managing-http-resources)
  * [Beta features](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#beta-features)
  * [Platform integrations](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#platform-integrations)
  * [Semantic versioning](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#semantic-versioning)
  * [Determining the installed version](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#determining-the-installed-version)
  * [Additional resources](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#additional-resources)

CLI, SDKs, and libraries/Client SDKs
# Python SDK
Install and configure the Anthropic Python SDK with sync and async client support
The Anthropic Python SDK provides convenient access to the Anthropic REST API from Python applications. It supports both synchronous and asynchronous operations, streaming, and integrations with Amazon Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS.
For API feature documentation with code examples, see the [API reference](https://platform.claude.com/docs/en/api/overview). This page covers Python-specific SDK features and configuration.
Installation

pip install anthropic

For platform-specific integrations or improved async performance, install with extras:

# For Amazon Bedrock support
pip install "anthropic[bedrock]"

# For Google Cloud support
pip install "anthropic[vertex]"

# For Claude Platform on AWS support
pip install "anthropic[aws]"

# Microsoft Foundry support is included in the base package

# For improved async performance with aiohttp
pip install "anthropic[aiohttp]"

Requirements
Python 3.9 or later is required.
Usage

import os
from anthropic import Anthropic

client = Anthropic(
    # This is the default and can be omitted
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

message = client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
)
print(message.content)


Consider using [python-dotenv](https://pypi.org/project/python-dotenv/) to add `ANTHROPIC_API_KEY="my-anthropic-api-key"` to your `.env` file so that your API key isn't stored in source control.
For authentication options including Workload Identity Federation, see [Authentication](https://platform.claude.com/docs/en/manage-claude/authentication).
Async usage

import os
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

async def main() -> None:
    message = await client.messages.create(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Hello, Claude",
        ],
        model="claude-opus-4-8",
    )
    print(message.content)

asyncio.run(main())

### 
Using aiohttp for better concurrency
For improved async performance, you can use the `aiohttp` HTTP backend instead of the default `httpx`:

import os
import asyncio
from anthropic import AsyncAnthropic, DefaultAioHttpClient

async def main() -> None:
    async with AsyncAnthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"),
        http_client=DefaultAioHttpClient(),
    ) as client:
        message = await client.messages.create(
            max_tokens=1024,
            messages=[
                    "role": "user",
                    "content": "Hello, Claude",
            ],
            model="claude-opus-4-8",
        )
        print(message.content)

asyncio.run(main())

Streaming responses
The SDK provides support for streaming responses using Server-Sent Events (SSE).

client = Anthropic()

stream = client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
    stream=True,
)
for event in stream:
    print(event.type)

The async client uses the exact same interface:

client = AsyncAnthropic()

stream = await client.messages.create(
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": "Hello, Claude",
    ],
    model="claude-opus-4-8",
    stream=True,
)
async for event in stream:
    print(event.type)

### 
Streaming helpers
The SDK also provides streaming helpers that use context managers and provide access to the accumulated text and the final message:

async def main() -> None:
    async with client.messages.stream(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Say hello there!",
        ],
        model="claude-opus-4-8",
    ) as stream:
        async for text in stream.text_stream:
            print(text, end="", flush=True)
        print()

        message = await stream.get_final_message()
        print(message.to_json())

asyncio.run(main())

Streaming with `client.messages.stream(...)` exposes various helpers including accumulation and SDK-specific events.
Alternatively, you can use `client.messages.create(..., stream=True)` which only returns an iterable of the events in the stream and uses less memory (it doesn't build up a final message object for you).
Token counting
You can see the exact usage for a given request through the `usage` response property:

message = client.messages.create(...)
print(message.usage)
# Usage(input_tokens=25, output_tokens=13)

You can also count tokens before making a request:

count = client.messages.count_tokens(
    model="claude-opus-4-8", messages=[{"role": "user", "content": "Hello, world"}]
)
print(count.input_tokens)  # 10

Tool use
This SDK provides support for tool use, also known as function calling. For more details, see [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview).
### 
Tool helpers
The SDK provides helpers for defining and running tools as pure Python functions. The `@beta_tool` decorator generates the tool schema from the function signature and docstring:

import json
from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def get_weather(location: str) -> str:
    """Get the weather for a given location.

    Args:
        location: The city and state, for example, San Francisco, CA
    Returns:
        A JSON-encoded string with the location, temperature, and weather condition.
    """
    return json.dumps(
            "location": location,
            "temperature": "68°F",
            "condition": "Sunny",
    )

# Use the tool_runner to automatically handle tool calls
runner = client.beta.messages.tool_runner(
    max_tokens=1024,
    model="claude-opus-4-8",
    tools=[get_weather],
    messages=[
        {"role": "user", "content": "What is the weather in SF?"},
    ],
)
for message in runner:
    print(message)

On every iteration, an API request is made. If Claude wants to call one of the given tools, it's automatically called, and the result is returned directly to the model in the next iteration.
Message batches
This SDK provides support for the [Message Batches API](https://platform.claude.com/docs/en/build-with-claude/batch-processing) under `client.messages.batches`.
### 
Creating a batch
Message Batches takes an array of requests, where each object has a `custom_id` identifier and the same request `params` as the standard Messages API:

client.messages.batches.create(
    requests=[
            "custom_id": "my-first-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hello, world"}],
            "custom_id": "my-second-request",
            "params": {
                "model": "claude-opus-4-8",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": "Hi again, friend"}],
    ]
)

### 
Getting results from a batch
Once a Message Batch has been processed, indicated by `.processing_status == 'ended'`, you can access the results with `.batches.results()`:

client = anthropic.Anthropic()
batch_id = "batch_abc123"
result_stream = client.messages.batches.results(batch_id)
for entry in result_stream:
    if entry.result.type == "succeeded":
        print(entry.result.message.content)

File uploads
Request parameters that correspond to file uploads can be passed in many different forms:
  * A `PathLike` object (for example, `pathlib.Path`)
  * A tuple of `(filename, content, content_type)`
  * A `BinaryIO` file-like object

from pathlib import Path
from anthropic import Anthropic

client = Anthropic()

# Upload using a file path
client.beta.files.upload(
    file=Path("/path/to/file"),
)

# Upload using bytes
client.beta.files.upload(
    file=("file.txt", b"my bytes", "text/plain"),
)

The async client uses the exact same interface. If you pass a `PathLike` instance, the file contents are read asynchronously automatically.
Handling errors
When the library is unable to connect to the API, or if the API returns a non-success status code (i.e., 4xx or 5xx response), a subclass of `APIError` is raised:

import anthropic
# ...
try:
    message = client.messages.create(
        max_tokens=1024,
        messages=[
                "role": "user",
                "content": "Hello, Claude",
        ],
        model="claude-opus-4-8",
    )
except anthropic.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx
except anthropic.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except anthropic.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)

Error codes are as follows:  
| Status Code  | Error Type  |  
| --- | --- |  
| 400  | `BadRequestError`  |  
| 401  | `AuthenticationError`  |  
| 403  | `PermissionDeniedError`  |  
| 404  | `NotFoundError`  |  
| 409  | `ConflictError`  |  
| 422  | `UnprocessableEntityError`  |  
| 429  | `RateLimitError`  |  
| >=500  | `InternalServerError`  |  
| N/A  | `APIConnectionError`  |  
Request IDs
> For more information on debugging requests, see [Request ID](https://platform.claude.com/docs/en/api/errors#request-id).
All object responses in the SDK provide a `_request_id` property which is added from the `request-id` response header so that you can quickly log failing requests and report them back to Anthropic.

message = client.messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)
print(message._request_id)  # e.g., req_018EeWyXxfu5pfWkrYcMdjWG

Unlike other properties that use an `_` prefix, the `_request_id` property is public. Unless documented otherwise, all other `_` prefix properties, methods, and modules are private.
Retries
Certain errors are automatically retried 2 times by default, with a short exponential backoff. Connection errors (for example, because of a network connectivity problem), 408 Request Timeout, 409 Conflict, 429 Rate Limit, and >=500 Internal errors are all retried by default.
You can use the `max_retries` option to configure or disable this:

# Configure the default for all requests:
client = Anthropic(
    max_retries=0,  # default is 2
)

# Or, configure per-request:
client.with_options(max_retries=5).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

Timeouts
By default requests time out after 10 minutes. You can configure this with a `timeout` option, which accepts a float or an `httpx.Timeout` object:

import httpx
from anthropic import Anthropic

# Configure the default for all requests:
client = Anthropic(
    timeout=20.0,  # 20 seconds (default is 10 minutes)
)

# More granular control:
client = Anthropic(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).messages.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

On timeout, an `APITimeoutError` is thrown.
Note that requests which time out will be [retried twice by default](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#retries).
Long requests

Consider using the streaming [Messages API](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#streaming-responses) for longer running requests.
Avoid setting a large `max_tokens` value without using streaming. Some networks may drop idle connections after a certain period of time, which can cause the request to fail or [timeout](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#timeouts) without receiving a response from Anthropic.
The SDK will throw a `ValueError` if a non-streaming request is expected to take longer than approximately 10 minutes. Passing `stream=True` or overriding the `timeout` option at the client or request level disables this error.
An expected request latency longer than the [timeout](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/python#timeouts) for a non-streaming request will result in the client terminating the connection and retrying without receiving a response.
The SDK sets a [TCP socket keep-alive](https://tldp.org/HOWTO/TCP-Keepalive-HOWTO/overview.html) option to reduce the impact of idle connection timeouts on some networks. This can be overridden by passing a custom `http_client` option to the client.
Auto-pagination
List methods in the Claude API are paginated. You can use the `for` syntax to iterate through items across all pages:

client = Anthropic()

all_batches = []
# Automatically fetches more pages as needed.
for batch in client.messages.batches.list(limit=20):
    all_batches.append(batch)
print(all_batches)

For async iteration:

async def main() -> None:
    all_batches = []
    async for batch in client.messages.batches.list(limit=20):
        all_batches.append(batch)
    print(all_batches)

asyncio.run(main())

Alternatively, you can use the `.has_next_page()`, `.next_page_info()`, or `.get_next_page()` methods for more granular control working with pages:

first_page = await client.messages.batches.list(limit=20)

if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.

Or work directly with the returned data:

first_page = await client.messages.batches.list(limit=20)

print(f"next page cursor: {first_page.last_id}")
for batch in first_page.data:
    print(batch.id)

# Remove `await` for non-async usage.

Default headers
The SDK automatically sends the `anthropic-version` header set to `2023-06-01`.
If you need to, you can override it by setting default headers on the client object or per-request.

Overriding default headers may result in incorrect types and other unexpected or undefined behavior in the SDK.

# Set default headers for all requests on the client
client = Anthropic(
    default_headers={"anthropic-version": "My-Custom-Value"},
)

# Or override per-request
client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
    extra_headers={"anthropic-version": "My-Custom-Value"},
)

Type system
### 
Request parameters
Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also have helper methods for things like serializing back into JSON ([`v1`](https://docs.pydantic.dev/1.10/usage/models/), [`v2`](https://docs.pydantic.dev/latest/concepts/serialization/)).
Typed requests and responses provide autocomplete and documentation within your editor. If you'd like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.
### 
Response models
To convert a Pydantic model to a dictionary, use the helper methods:

message = client.messages.create(...)

# Convert to JSON string
json_str = message.to_json()

# Convert to dictionary
data = message.to_dict()

### 
Handling null vs missing fields
In responses, you can distinguish between fields that are explicitly `null` versus fields that were not returned (missing):

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
)
if response.my_field is None:
    if "my_field" not in response.model_fields_set:
        print("field was not in the response")
    else:
        print("field was null")

Advanced usage
### 
Accessing raw response data (for example, headers)
The "raw" `Response` returned by `httpx` can be accessed through the `.with_raw_response` property on the client. This is useful for accessing response headers or other metadata:

client = Anthropic()

response = client.messages.with_raw_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
)

print(response.headers.get("request-id"))
message = (
    response.parse()
)  # get the object that `messages.create()` would have returned
print(message.content)

These methods return an `APIResponse` object.
### 
Streaming response body
The `.with_raw_response` approach eagerly reads the full response body when you make the request. To stream the response body instead, use `.with_streaming_response`, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()`, or `.parse()`. In the async client, these are async methods.

with client.messages.with_streaming_response.create(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello, Claude"}],
    model="claude-opus-4-8",
) as response:
    print(response.headers.get("request-id"))

    for line in response.iter_lines():
        print(line)

The context manager is required so that the response will reliably be closed.
### 
Logging
The SDK uses the standard library `logging` module.
You can enable logging by setting the environment variable `ANTHROPIC_LOG` to `debug` or `info`:

export ANTHROPIC_LOG=debug

### 
Making custom/undocumented requests
This library is typed for convenient access to the documented API. If you need to access undocumented endpoints, params, or response properties, the library can still be used.
#### 
Undocumented endpoints
To make requests to undocumented endpoints, you can use `client.get`, `client.post`, and other HTTP verbs. Options on the client, such as retries, will be respected when making these requests.

import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.json())

#### 
Undocumented request params
If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request options.

The `extra_` parameters override documented parameters of the same name. For security reasons, ensure these methods are only used with trusted input data.
#### 
Undocumented response properties
To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You can also get all extra fields on the Pydantic model as a dict with `response.model_extra`.
### 
Configuring the HTTP client
You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including support for proxies and transports:

import httpx
from anthropic import Anthropic, DefaultHttpxClient

client = Anthropic(
    # Or use the `ANTHROPIC_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)

You can also customize the client on a per-request basis by using `with_options()`:

client.with_options(http_client=DefaultHttpxClient(...))

Use `DefaultHttpxClient` and `DefaultAsyncHttpxClient` instead of raw `httpx.Client` and `httpx.AsyncClient` to ensure the SDK's default configuration (timeouts, connection limits, etc.) is preserved.
### 
Managing HTTP resources
By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

with Anthropic() as client:
    message = client.messages.create(...)

# HTTP client is automatically closed

Beta features
Beta features are available before general release to get early feedback and test new functionality. You can check the availability of all of Claude's capabilities and tools in the [build with Claude overview](https://platform.claude.com/docs/en/build-with-claude/overview).
You can access most beta API features through the `beta` property of the client. To enable a particular beta feature, you need to add the appropriate [beta header](https://platform.claude.com/docs/en/api/beta-headers) to the `betas` field when creating a message.
For example, to use the [Files API](https://platform.claude.com/docs/en/build-with-claude/files):

client = Anthropic()

response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    messages=[
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                    "type": "document",
                    "source": {
                        "type": "file",
                        "file_id": "file_abc123",
            ],
    ],
    betas=["files-api-2025-04-14"],
)

Platform integrations
For detailed platform setup guides with code examples, see:
  * [Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)
  * [Amazon Bedrock (legacy)](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)
  * [Google Cloud](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)
  * [Microsoft Foundry](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)
  * [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)

All five client classes are included in the base `anthropic` package:  
| Provider  | Client  | Extra dependencies  |  
| --- | --- | --- |  
| Bedrock  | `from anthropic import AnthropicBedrockMantle`  | `pip install "anthropic[bedrock]"`  |  
| Bedrock (`bedrock-runtime` path)  | `from anthropic import AnthropicBedrock`  | `pip install "anthropic[bedrock]"`  |  
| Agent Platform  | `from anthropic import AnthropicVertex`  | `pip install "anthropic[vertex]"`  |  
| Foundry  | `from anthropic import AnthropicFoundry`  | None  |  
| Claude Platform on AWS  | `from anthropic import AnthropicAWS`  | `pip install "anthropic[aws]"`  |  
The `AnthropicAWS` client is in beta. Pass `workspace_id` to the constructor or set the `ANTHROPIC_AWS_WORKSPACE_ID` environment variable.
Use `AnthropicBedrockMantle` for new projects; `AnthropicBedrock` remains for existing applications using the Bedrock `InvokeModel` API.
Semantic versioning
This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:
  1. Changes that only affect static types, without breaking runtime behavior.
  2. Changes to library internals which are technically public but not intended or documented for external use.
  3. Changes that aren't expected to impact the vast majority of users in practice.

### 
Determining the installed version
If you've upgraded to the latest version but aren't seeing new features you were expecting, your Python environment is likely still using an older version. You can determine the version being used at runtime with:

print(anthropic.__version__)

Additional resources
  * [GitHub repository](https://github.com/anthropics/anthropic-sdk-python)
  * [API reference](https://platform.claude.com/docs/en/api/overview)
  * [Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming)
  * [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
