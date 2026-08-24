<!-- source: https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots -->

Lesson 5 of 11 · Model Context Protocol: Advanced TopicsRoots

3. /[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

[Model Context Protocol: Advanced Topics](https://academy.claude.com/courses/model-context-protocol-advanced-topics)

# Roots

Lesson 52 min

Roots are a way to grant MCP servers access to specific files and folders on your local machine. Think of them as a permission system that says "Hey, MCP server, you can access these files" - but they do much more than just grant permission.

## The Problem Roots Solve

Without roots, you'd run into a common issue. Imagine you have an MCP server with a video conversion tool that takes a file path and converts an MP4 to MOV format.

![Diagram titled "If roots didn't exist...": an MCP server exposes a convert_video tool that converts a .mp4 video file to .mov and requires a path to a video file on the local machine](https://academy.claude.com/assets/media/66d3ffe272f217a29fd4303500eda429377e1faf736e955ba4eb1beecfa324fb.png)

When a user asks Claude to "convert biking.mp4 to mov format", Claude would call the tool with just the filename. But here's the problem - Claude has no way to search through your entire file system to find where that file actually lives.

![A chat where the user says "Convert biking.mp4 to mov format" next to a local filesystem tree with Movies, Documents, and Photos folders; biking.mp4 is highlighted deep inside Movies/Sports, a location Claude can't see](https://academy.claude.com/assets/media/4afa0dcda9acc081796c2f7085a9c4a065c602e19f7ce1827c11c0fafcc12b58.png)

Your file system might be complex with files scattered across different directories. The user knows the biking.mp4 file is in their Movies folder, but Claude doesn't have that context.

You could solve this by requiring users to always provide full paths, but that's not very user-friendly. Nobody wants to type out complete file paths every time.

## Roots in Action

Here's how the workflow changes with roots:

1. User asks to convert a video file
2. Claude calls `list_roots` to see what directories it can access
3. Claude calls `read_dir` on accessible directories to find the file
4. Once found, Claude calls the conversion tool with the full path

This happens automatically - users can still just say "convert biking.mp4" without providing full paths.

## Security and Boundaries

Roots also provide security by limiting access. If you only grant access to your Desktop folder, the MCP server cannot access files in other locations like Documents or Downloads.

When Claude tries to access a file outside the approved roots, it gets an error and can inform the user that the file isn't accessible from the current server configuration.

## Implementation Details

The MCP SDK doesn't automatically enforce root restrictions - you need to implement this yourself. A typical pattern is to create a helper function like `is_path_allowed()` that:

* Takes a requested file path
* Gets the list of approved roots
* Checks if the requested path falls within one of those roots
* Returns true/false for access permission

You then call this function in any tool that accesses files or directories before performing the actual file operation.

## Key Benefits

* **User-friendly** - Users don't need to provide full file paths
* **Focused search** - Claude only looks in approved directories, making file discovery faster
* **Security** - Prevents accidental access to sensitive files outside approved areas
* **Flexibility** - You can provide roots through tools or inject them directly into prompts

Roots make MCP servers both more powerful and more secure by giving Claude the context it needs to find files while maintaining clear boundaries around what it can access.

[Previous lessonNotifications walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/notifications-walkthrough)[Next lessonRoots walkthrough](https://academy.claude.com/courses/model-context-protocol-advanced-topics/roots-walkthrough)

Lesson 5 of 11 · Model Context Protocol: Advanced TopicsRoots

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

* [The Problem Roots Solve](#the-problem-roots-solve)
* [Roots in Action](#roots-in-action)
* [Security and Boundaries](#security-and-boundaries)
* [Implementation Details](#implementation-details)
* [Key Benefits](#key-benefits)
