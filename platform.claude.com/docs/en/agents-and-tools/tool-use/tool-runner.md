<!-- source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner -->

# Tool Runner (SDK)
Use the SDK's Tool Runner abstraction to handle the agentic loop, error wrapping, and type safety automatically.
Tool Runner handles the agentic loop, error wrapping, and type safety so you don't have to. When you need human-in-the-loop approval, custom logging, or conditional execution, use the [manual loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) instead.
The tool runner provides an out-of-the-box solution for running tools with Claude. The tool runner can simplify most tool use implementations. Instead of manually handling tool calls, tool results, and conversation management, the tool runner automatically:
  * Runs tools when Claude calls them
  * Handles the request/response cycle
  * Manages conversation state
  * Provides type safety and validation

The tool runner is currently in beta and available in the [Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md), [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers), [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp/blob/main/examples/ToolRunnerExample/Program.cs), [Go SDK](https://github.com/anthropics/anthropic-sdk-go/blob/main/tools.md), [Java SDK](https://github.com/anthropics/anthropic-sdk-java/blob/main/anthropic-java-example/src/main/java/com/anthropic/example/BetaToolRunnerExample.java), [PHP SDK](https://github.com/anthropics/anthropic-sdk-php/blob/main/examples/beta/beta_tool_runner.php), and [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby/blob/main/helpers.md#3-auto-looping-tool-runner-beta).
Basic usage
Define tools using the SDK helpers, then use the tool runner to run them.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use the `@beta_tool` decorator to define tools with type hints and docstrings.
If you're using the async client, replace `@beta_tool` with `@beta_async_tool` and define the function with `async def`.

import json
from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def get_weather(location: str, unit: str = "fahrenheit") -> str:
    """Get the current weather in a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: Temperature unit, either 'celsius' or 'fahrenheit'
    """
    return json.dumps({"temperature": "20°C", "condition": "Sunny"})

@beta_tool
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return str(a + b)

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
    ],
)
for message in runner:
    print(message)

The `@beta_tool` decorator inspects the function arguments and docstring to derive the JSON schema for you.
The tool function must return a content block or content block array, including text, images, or document blocks. This allows tools to return rich, multimodal responses. Returned strings are converted to a text content block. If you want to return a structured JSON object to Claude, encode it to a JSON string before returning it. Numbers, Booleans, or other non-string primitives must also be converted to strings.
Iterating over the tool runner
The tool runner is an iterable that yields messages from Claude. This is often referred to as a "tool call loop." Each iteration, the runner checks if Claude requested a tool use. If so, it calls the tool and sends the result back to Claude automatically, then yields the next message from Claude to continue your loop.
You can end the loop at any iteration with a `break` statement. The runner loops until Claude returns a message without a tool use.
If you don't need intermediate messages, you can get the final message directly:
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use `runner.until_done()` to get the final message.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
    ],
)
final_message = runner.until_done()
for block in final_message.content:
    if block.type == "text":
        print(block.text)

Advanced usage
Within the loop, you can read each response message and modify the runner's state before the next API call. Each iteration follows this lifecycle:
  1. The runner sends a request to the Messages API with its current state.
  2. The runner yields the response message to your loop body.
  3. Your loop body runs. You can read the message and optionally modify the runner's state.
  4. When your loop body returns, the runner checks whether you modified its message history.
     * **If you did not modify message history:** The runner appends the assistant message to its state. If the message contains tool calls, the runner runs them and appends the results. If there are no tool calls, the loop exits.
     * **If you modified message history:** The runner skips its automatic append and uses your state unchanged. See [Taking over message history](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#taking-over-message-history).

Messages APIToolRunnerYour codeMessages APIToolRunnerYour code Your loop body runsalt[Message historyunchanged][Message historychanged]loop[For each iteration]Send request with current stateResponse messageYield messageResumeAppend assistant message,run tools, append results(exit if no tool calls)Use your state unchanged
### 
Taking over message history
By default, the runner manages conversation state for you: after each turn, it appends the assistant message and any tool results to its own message history. You take over message history when you want to retry a turn (discard the response and resend), inject a follow-up message, or build the tool result yourself.
You take over by modifying the runner's messages from inside the loop body. The exact method depends on the SDK; see the per-language tabs that follow.
When you take over for an iteration, the runner does not append the assistant message or tool results from that turn. You become responsible for keeping the conversation valid: append the assistant message and a tool result yourself (if you want the turn to count), modify state conditionally so the loop can still exit when there are no tool calls, and pass `max_iterations` to bound the loop. All seven SDKs support `max_iterations`.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use `generate_tool_call_response()` to inspect or compute the tool result. Calling `append_messages()` inside the loop tells the runner you're managing history yourself, so include the assistant message and tool result in what you append.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    max_iterations=10,
    tools=[get_weather],
    messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()
    if tool_response is not None:
        # append_messages() flags state as modified, so the runner skips its
        # automatic append for this iteration. Append the assistant message and
        # tool result yourself, plus any follow-up.
        runner.append_messages(
            message,
            tool_response,
            {"role": "user", "content": "Please be concise."},
        )
    # When there's no tool call, leave state untouched so the loop exits.

To change request parameters such as `max_tokens` without taking over message history, use `set_messages_params()`. The runner still appends the assistant message and tool result automatically.

for message in runner:
    runner.set_messages_params(lambda params: {**params, "max_tokens": 2048})

### 
Automatic context management
For long-running agentic tasks, the tool runner supports automatic [compaction](https://platform.claude.com/docs/en/build-with-claude/context-editing#client-side-compaction-sdk), which generates summaries when token usage exceeds a threshold so the conversation can continue beyond context window limits.
### 
Debugging tool execution
When a tool throws an exception, the tool runner catches it and returns the error to Claude as a tool result with `is_error: true`. By default, only the exception message is included, not the full stack trace.
To view full stack traces and debug information, set the `ANTHROPIC_LOG` environment variable:

# View info-level logs including tool errors
export ANTHROPIC_LOG=info

# View debug-level logs for more verbose output
export ANTHROPIC_LOG=debug

When enabled, the SDK logs full exception details to your language's standard logging facility, including the complete stack trace when a tool fails.
### 
Intercepting tool errors
By default, tool errors are passed back to Claude, which can then respond appropriately. However, you might want to detect errors and handle them differently, for example, to stop execution early or implement custom error handling.
Use the tool response method to intercept tool results and check for errors before they're sent to Claude:
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[my_tool],
    messages=[{"role": "user", "content": "Run my_tool with the query 'hello'."}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Check if any tool result has an error
        for block in tool_response["content"]:
            if block.get("is_error"):
                # Option 1: Raise an exception to stop the loop
                raise RuntimeError(f"Tool failed: {json.dumps(block['content'])}")

                # Option 2: Log and continue (let Claude handle it)
                # logger.error(f"Tool error: {json.dumps(block['content'])}")

    # Process the message normally
    print(message.content)

### 
Modifying tool results
You can modify tool results before they're sent back to Claude. This is useful for adding metadata such as `cache_control` to enable [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) on tool results, or for transforming the tool output.
Use the tool response method to get the tool result, then modify it before the runner proceeds. Whether you explicitly append the modified result or mutate it in place depends on the SDK; see the code comments in each tab.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[search_documents],
    messages=[
            "role": "user",
            "content": "Search for information about the climate of San Francisco",
    ],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Modify the tool result to add cache control
        for block in tool_response["content"]:
            if block["type"] == "tool_result":
                # Add cache_control to cache this tool result
                block["cache_control"] = {"type": "ephemeral"}

        # Append the modified response (this prevents auto-append of the original)
        runner.append_messages(message, tool_response)

    print(message.content)


Adding `cache_control` to tool results is particularly useful when tools return large amounts of data (such as document search results) that you want to cache for subsequent API calls. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for more details on caching strategies.
Streaming
Enable streaming to process each turn's response incrementally. Each iteration yields a stream object that you can iterate for events.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Set `stream=True` and use `get_final_message()` to get the accumulated message.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[calculate_sum],
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    stream=True,
)

# When streaming, the runner returns BetaMessageStream
for message_stream in runner:
    for event in message_stream:
        print("event:", event)
    print("message:", message_stream.get_final_message())

print(runner.until_done())

Next steps
  * For manual control over the tool-call loop, see [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
  * For running multiple tools concurrently, see [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
  * For the full tool-use workflow, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).

  * [Basic usage](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#basic-usage)
  * [Iterating over the tool runner](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#iterating-over-the-tool-runner)
  * [Advanced usage](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#advanced-usage)
  * [Taking over message history](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#taking-over-message-history)
  * [Automatic context management](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#automatic-context-management)
  * [Debugging tool execution](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#debugging-tool-execution)
  * [Intercepting tool errors](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#intercepting-tool-errors)
  * [Modifying tool results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#modifying-tool-results)
  * [Streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#streaming)
  * [Next steps](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#next-steps)

Messages/Tools
# Tool Runner (SDK)
Use the SDK's Tool Runner abstraction to handle the agentic loop, error wrapping, and type safety automatically.
Tool Runner handles the agentic loop, error wrapping, and type safety so you don't have to. When you need human-in-the-loop approval, custom logging, or conditional execution, use the [manual loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls) instead.
The tool runner provides an out-of-the-box solution for running tools with Claude. The tool runner can simplify most tool use implementations. Instead of manually handling tool calls, tool results, and conversation management, the tool runner automatically:
  * Runs tools when Claude calls them
  * Handles the request/response cycle
  * Manages conversation state
  * Provides type safety and validation

The tool runner is currently in beta and available in the [Python SDK](https://github.com/anthropics/anthropic-sdk-python/blob/main/tools.md), [TypeScript SDK](https://github.com/anthropics/anthropic-sdk-typescript/blob/main/helpers.md#tool-helpers), [C# SDK](https://github.com/anthropics/anthropic-sdk-csharp/blob/main/examples/ToolRunnerExample/Program.cs), [Go SDK](https://github.com/anthropics/anthropic-sdk-go/blob/main/tools.md), [Java SDK](https://github.com/anthropics/anthropic-sdk-java/blob/main/anthropic-java-example/src/main/java/com/anthropic/example/BetaToolRunnerExample.java), [PHP SDK](https://github.com/anthropics/anthropic-sdk-php/blob/main/examples/beta/beta_tool_runner.php), and [Ruby SDK](https://github.com/anthropics/anthropic-sdk-ruby/blob/main/helpers.md#3-auto-looping-tool-runner-beta).
Basic usage
Define tools using the SDK helpers, then use the tool runner to run them.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use the `@beta_tool` decorator to define tools with type hints and docstrings.
If you're using the async client, replace `@beta_tool` with `@beta_async_tool` and define the function with `async def`.

import json
from anthropic import Anthropic, beta_tool

client = Anthropic()

@beta_tool
def get_weather(location: str, unit: str = "fahrenheit") -> str:
    """Get the current weather in a given location.

    Args:
        location: The city and state, e.g. San Francisco, CA
        unit: Temperature unit, either 'celsius' or 'fahrenheit'
    """
    return json.dumps({"temperature": "20°C", "condition": "Sunny"})

@beta_tool
def calculate_sum(a: int, b: int) -> str:
    """Add two numbers together.

    Args:
        a: First number
        b: Second number
    """
    return str(a + b)

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
    ],
)
for message in runner:
    print(message)

The `@beta_tool` decorator inspects the function arguments and docstring to derive the JSON schema for you.
The tool function must return a content block or content block array, including text, images, or document blocks. This allows tools to return rich, multimodal responses. Returned strings are converted to a text content block. If you want to return a structured JSON object to Claude, encode it to a JSON string before returning it. Numbers, Booleans, or other non-string primitives must also be converted to strings.
Iterating over the tool runner
The tool runner is an iterable that yields messages from Claude. This is often referred to as a "tool call loop." Each iteration, the runner checks if Claude requested a tool use. If so, it calls the tool and sends the result back to Claude automatically, then yields the next message from Claude to continue your loop.
You can end the loop at any iteration with a `break` statement. The runner loops until Claude returns a message without a tool use.
If you don't need intermediate messages, you can get the final message directly:
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use `runner.until_done()` to get the final message.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[get_weather, calculate_sum],
    messages=[
            "role": "user",
            "content": "What's the weather like in Paris? Also, what's 15 + 27?",
    ],
)
final_message = runner.until_done()
for block in final_message.content:
    if block.type == "text":
        print(block.text)

Advanced usage
Within the loop, you can read each response message and modify the runner's state before the next API call. Each iteration follows this lifecycle:
  1. The runner sends a request to the Messages API with its current state.
  2. The runner yields the response message to your loop body.
  3. Your loop body runs. You can read the message and optionally modify the runner's state.
  4. When your loop body returns, the runner checks whether you modified its message history.
     * **If you did not modify message history:** The runner appends the assistant message to its state. If the message contains tool calls, the runner runs them and appends the results. If there are no tool calls, the loop exits.
     * **If you modified message history:** The runner skips its automatic append and uses your state unchanged. See [Taking over message history](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner#taking-over-message-history).

Messages APIToolRunnerYour codeMessages APIToolRunnerYour code Your loop body runsalt[Message historyunchanged][Message historychanged]loop[For each iteration]Send request with current stateResponse messageYield messageResumeAppend assistant message,run tools, append results(exit if no tool calls)Use your state unchanged
### 
Taking over message history
By default, the runner manages conversation state for you: after each turn, it appends the assistant message and any tool results to its own message history. You take over message history when you want to retry a turn (discard the response and resend), inject a follow-up message, or build the tool result yourself.
You take over by modifying the runner's messages from inside the loop body. The exact method depends on the SDK; see the per-language tabs that follow.
When you take over for an iteration, the runner does not append the assistant message or tool results from that turn. You become responsible for keeping the conversation valid: append the assistant message and a tool result yourself (if you want the turn to count), modify state conditionally so the loop can still exit when there are no tool calls, and pass `max_iterations` to bound the loop. All seven SDKs support `max_iterations`.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Use `generate_tool_call_response()` to inspect or compute the tool result. Calling `append_messages()` inside the loop tells the runner you're managing history yourself, so include the assistant message and tool result in what you append.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    max_iterations=10,
    tools=[get_weather],
    messages=[{"role": "user", "content": "What's the weather in San Francisco?"}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()
    if tool_response is not None:
        # append_messages() flags state as modified, so the runner skips its
        # automatic append for this iteration. Append the assistant message and
        # tool result yourself, plus any follow-up.
        runner.append_messages(
            message,
            tool_response,
            {"role": "user", "content": "Please be concise."},
        )
    # When there's no tool call, leave state untouched so the loop exits.

To change request parameters such as `max_tokens` without taking over message history, use `set_messages_params()`. The runner still appends the assistant message and tool result automatically.

for message in runner:
    runner.set_messages_params(lambda params: {**params, "max_tokens": 2048})

### 
Automatic context management
For long-running agentic tasks, the tool runner supports automatic [compaction](https://platform.claude.com/docs/en/build-with-claude/context-editing#client-side-compaction-sdk), which generates summaries when token usage exceeds a threshold so the conversation can continue beyond context window limits.
### 
Debugging tool execution
When a tool throws an exception, the tool runner catches it and returns the error to Claude as a tool result with `is_error: true`. By default, only the exception message is included, not the full stack trace.
To view full stack traces and debug information, set the `ANTHROPIC_LOG` environment variable:

# View info-level logs including tool errors
export ANTHROPIC_LOG=info

# View debug-level logs for more verbose output
export ANTHROPIC_LOG=debug

When enabled, the SDK logs full exception details to your language's standard logging facility, including the complete stack trace when a tool fails.
### 
Intercepting tool errors
By default, tool errors are passed back to Claude, which can then respond appropriately. However, you might want to detect errors and handle them differently, for example, to stop execution early or implement custom error handling.
Use the tool response method to intercept tool results and check for errors before they're sent to Claude:
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[my_tool],
    messages=[{"role": "user", "content": "Run my_tool with the query 'hello'."}],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Check if any tool result has an error
        for block in tool_response["content"]:
            if block.get("is_error"):
                # Option 1: Raise an exception to stop the loop
                raise RuntimeError(f"Tool failed: {json.dumps(block['content'])}")

                # Option 2: Log and continue (let Claude handle it)
                # logger.error(f"Tool error: {json.dumps(block['content'])}")

    # Process the message normally
    print(message.content)

### 
Modifying tool results
You can modify tool results before they're sent back to Claude. This is useful for adding metadata such as `cache_control` to enable [prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) on tool results, or for transforming the tool output.
Use the tool response method to get the tool result, then modify it before the runner proceeds. Whether you explicitly append the modified result or mutate it in place depends on the SDK; see the code comments in each tab.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[search_documents],
    messages=[
            "role": "user",
            "content": "Search for information about the climate of San Francisco",
    ],
)

for message in runner:
    tool_response = runner.generate_tool_call_response()

    if tool_response is not None:
        # tool_response is a dict: {"role": "user", "content": [...]}
        # Modify the tool result to add cache control
        for block in tool_response["content"]:
            if block["type"] == "tool_result":
                # Add cache_control to cache this tool result
                block["cache_control"] = {"type": "ephemeral"}

        # Append the modified response (this prevents auto-append of the original)
        runner.append_messages(message, tool_response)

    print(message.content)


Adding `cache_control` to tool results is particularly useful when tools return large amounts of data (such as document search results) that you want to cache for subsequent API calls. See [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) for more details on caching strategies.
Streaming
Enable streaming to process each turn's response incrementally. Each iteration yields a stream object that you can iterate for events.
Python
Python
TypeScript
TypeScript
C#
C#
Go
Go
Java
Java
PHP
PHP
Ruby
Ruby
Set `stream=True` and use `get_final_message()` to get the accumulated message.

runner = client.beta.messages.tool_runner(
    model="claude-opus-4-8",
    max_tokens=1024,
    tools=[calculate_sum],
    messages=[{"role": "user", "content": "What is 15 + 27?"}],
    stream=True,
)

# When streaming, the runner returns BetaMessageStream
for message_stream in runner:
    for event in message_stream:
        print("event:", event)
    print("message:", message_stream.get_final_message())

print(runner.until_done())

Next steps
  * For manual control over the tool-call loop, see [Handle tool calls](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls).
  * For running multiple tools concurrently, see [Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use).
  * For the full tool-use workflow, see [Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools).
