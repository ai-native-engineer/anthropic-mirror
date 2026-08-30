<!-- source: https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-review -->

Lesson 10 of 10 · Introduction to Model Context ProtocolMCP review

3. /[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

[Introduction to Model Context Protocol](https://academy.claude.com/courses/introduction-to-model-context-protocol)

# MCP review

Lesson 102 min

Now that we've built our MCP server, let's review the three core server primitives and understand when to use each one. The key insight is that each primitive is controlled by a different part of your application stack.

![](https://academy.claude.com/assets/media/bc7ee5fac91b20fa74fcc27bb9255bc41c9fb9c50a15ae60e3bfccc7a1cfad3e.png)

## Tools: Model-Controlled[](#tools-model-controlled)

Tools are controlled entirely by Claude. The AI model decides when to call these functions, and the results are used directly by Claude to accomplish tasks.

Tools are perfect for giving Claude additional capabilities it can use autonomously. When you ask Claude to "calculate the square root of 3 using JavaScript," it's Claude that decides to use a JavaScript execution tool to run the calculation.

## Resources: App-Controlled[](#resources-app-controlled)

Resources are controlled by your application code. Your app decides when to fetch resource data and how to use it - typically for UI elements or to add context to conversations.

In our project, we used resources in two ways:

* Fetching data to populate autocomplete options in the UI
* Retrieving content to augment prompts with additional context

Think of the "Add from Google Drive" feature in Claude's interface - the application code determines which documents to show and handles injecting their content into the chat context.

## Prompts: User-Controlled[](#prompts-user-controlled)

Prompts are triggered by user actions. Users decide when to run these predefined workflows through UI interactions like button clicks, menu selections, or slash commands.

Prompts are ideal for implementing workflows that users can trigger on demand. In Claude's interface, those workflow buttons below the chat input are examples of prompts - predefined, optimized workflows that users can start with a single click.

## Choosing the Right Primitive[](#choosing-the-right-primitive)

Here's a quick decision guide:

* **Need to give Claude new capabilities?** Use tools
* **Need to get data into your app for UI or context?** Use resources
* **Want to create predefined workflows for users?** Use prompts

You can see all three primitives in action in Claude's official interface. The workflow buttons demonstrate prompts, the Google Drive integration shows resources in action, and when Claude executes code or performs calculations, it's using tools behind the scenes.

These are high-level guidelines to help you choose the right primitive for your specific use case. Each serves a different part of your application stack - tools serve the model, resources serve your app, and prompts serve your users.

[Previous lessonFinal assessment on MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/final-assessment-on-mcp)[Up nextCompletion badge](https://academy.claude.com/courses/introduction-to-model-context-protocol/badge)

Lesson 10 of 10 · Introduction to Model Context ProtocolMCP review

Introduction

* [Introducing MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/introducing-mcp)
* [MCP clients](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-clients)

Hands-on with MCP servers

* [Defining tools with MCP](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-tools-with-mcp)
* [The server inspector](https://academy.claude.com/courses/introduction-to-model-context-protocol/the-server-inspector)

Connecting with MCP clients

* [Implementing a client](https://academy.claude.com/courses/introduction-to-model-context-protocol/implementing-a-client)
* [Defining resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-resources)
* [Accessing resources](https://academy.claude.com/courses/introduction-to-model-context-protocol/accessing-resources)
* [Defining prompts](https://academy.claude.com/courses/introduction-to-model-context-protocol/defining-prompts)
* [Prompts in the client](https://academy.claude.com/courses/introduction-to-model-context-protocol/prompts-in-the-client)

Assessment and wrap Up

* [Final assessment on MCPQuiz](https://academy.claude.com/courses/introduction-to-model-context-protocol/final-assessment-on-mcp)
* [MCP review](https://academy.claude.com/courses/introduction-to-model-context-protocol/mcp-review)

* [Completion badge](https://academy.claude.com/courses/introduction-to-model-context-protocol/badge)

* [Tools: Model-Controlled](#tools-model-controlled)
* [Resources: App-Controlled](#resources-app-controlled)
* [Prompts: User-Controlled](#prompts-user-controlled)
* [Choosing the Right Primitive](#choosing-the-right-primitive)
