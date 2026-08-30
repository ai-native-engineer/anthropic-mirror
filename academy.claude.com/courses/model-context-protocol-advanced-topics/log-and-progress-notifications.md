<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/log-and-progress-notifications -->

Lesson 3 of 11 · Model Context Protocol: Advanced TopicsLog and progress notifications

3. /[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

# Log and progress notifications

Lesson 37 min

Logging and progress notifications are simple to implement but make a huge difference in user experience when working with MCP servers. They help users understand what's happening during long-running operations instead of wondering if something has broken.

When Claude calls a tool that takes time to complete - like researching a topic or processing data - users typically see nothing until the operation finishes. This can be frustrating because they don't know if the tool is working or has stalled.

With logging and progress notifications enabled, users get real-time feedback showing exactly what's happening behind the scenes. They can see progress bars, status messages, and detailed logs as the operation runs.

## How It Works[](#how-it-works)

In the Python MCP SDK, logging and progress notifications work through the Context argument that's automatically provided to your tool functions. This context object gives you methods to communicate back to the client during execution.

python

```
@mcp.tool(
    name="research",
    description="Research a given topic"
)
async def research(
    topic: str = Field(description="Topic to research"),
    *,
    context: Context
):
    await context.info("About to do research...")
    await context.report_progress(20, 100)
    sources = await do_research(topic)

    await context.info("Writing report...")
    await context.report_progress(70, 100)
    results = await generate_report(sources)

    return results
```

The key methods you'll use are:

* `context.info()` - Send log messages to the client
* `context.report_progress()` - Update progress with current and total values

## Client-Side Implementation[](#client-side-implementation)

On the client side, you need to set up callback functions to handle these notifications. The server emits these messages, but it's up to your client application to decide how to present them to users.

python

```
async def logging_callback(params: LoggingMessageNotificationParams):
    print(params.data)

async def print_progress_callback(
    progress: float, total: float | None, message: str | None
):
    if total is not None:
        percentage = (progress / total) * 100
        print(f"Progress: {progress}/{total} ({percentage:.1f}%)")
    else:
        print(f"Progress: {progress}")

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
            read,
            write,
            logging_callback=logging_callback
        ) as session:
            await session.initialize()

            await session.call_tool(
                name="add",
                arguments={"a": 1, "b": 3},
                progress_callback=print_progress_callback,
            )
```

You provide the logging callback when creating the client session, and the progress callback when making individual tool calls. This gives you flexibility to handle different types of notifications appropriately.

## Presentation Options[](#presentation-options)

How you present these notifications depends on your application type:

* **CLI applications** - Simply print messages and progress to the terminal
* **Web applications** - Use WebSockets, server-sent events, or polling to push updates to the browser
* **Desktop applications** - Update progress bars and status displays in your UI

Remember that implementing these notifications is entirely optional. You can choose to ignore them completely, show only certain types, or present them however makes sense for your application. They're purely user experience enhancements to help users understand what's happening during long-running operations.

[Previous lessonSampling walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling-walkthrough)[Next lessonNotifications walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/notifications-walkthrough)

Lesson 3 of 11 · Model Context Protocol: Advanced TopicsLog and progress notifications

Core MCP features

* [Sampling](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling)
* [Sampling walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/sampling-walkthrough)
* [Log and progress notifications](https://academy.claude.com/courses/model-context-protocol-advanced-topics/log-and-progress-notifications)
* [Notifications walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/notifications-walkthrough)
* [Roots](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots)
* [Roots walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots-walkthrough)

Transports and communication

* [JSON message types](https://academy.claude.com/courses/model-context-protocol-advanced-topics/json-message-types)
* [The STDIO transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-stdio-transport)
* [The StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/the-streamablehttp-transport)
* [StreamableHTTP in depth](https://academy.claude.com/courses/model-context-protocol-advanced-topics/streamablehttp-in-depth)
* [State and the StreamableHTTP transport](https://academy.claude.com/courses/model-context-protocol-advanced-topics/state-and-the-streamablehttp-transport)

Assessment and next steps

* [Assessment on MCP conceptsQuiz](https://academy.claude.com/courses/model-context-protocol-advanced-topics/assessment-on-mcp-concepts)

* [Completion badge](https://academy.claude.com/courses/model-context-protocol-advanced-topics/badge)

* [How It Works](#how-it-works)
* [Client-Side Implementation](#client-side-implementation)
* [Presentation Options](#presentation-options)
