<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/how-computer-use-works -->

Lesson 64 of 65 · Claude with Amazon BedrockHow Computer Use works

Computer use in Claude works exactly like regular tool use - it's built on the same foundation you're already familiar with. The key difference is that instead of calling a weather API or database function, Claude is making requests to control a computer interface.

## Tool Use Refresher

Before diving into computer use, let's quickly review how standard tool use works. When you want Claude to use a tool, you send a request that includes both a user message and a tool schema. The tool schema describes the additional functionality you want to expose to Claude.

![](https://academy.claude.com/assets/media/f4d077c8292d0a37e95c2ddca623e45dbac42d8ef11e281a3d89e7b135059873.png)

Here's the typical flow:

1. You send Claude a question along with available tool schemas
2. Claude analyzes the request and decides it needs to use a tool
3. Claude responds with a tool use request containing the tool name and required inputs
4. Your server executes the tool function and returns the result
5. You send the tool result back to Claude

![](https://academy.claude.com/assets/media/d9d83a6056318aa99872c9bb70b721797ba4223cbf93c0144b7509b761317648.png)

For example, if you ask about weather in San Francisco, Claude might call a `get_weather` function with the location parameter, your server fetches the weather data, and you return the result to Claude.

![](https://academy.claude.com/assets/media/b58e95288655e5f2490b8be8b68ad763c8cbc0964b650cf39c9c78851ab87581.png)

## Computer Use: Same Flow, Different Tool

Computer use follows this exact same pattern. The difference is in what the "tool" actually does - instead of fetching weather data, it simulates computer interactions like mouse clicks and keyboard input.

![](https://academy.claude.com/assets/media/7c359ef8d7714fbf80176d332343ccebb580752c41150025ac825314669c02ee.png)

When you enable computer use, you send Claude a special tool schema that gets automatically expanded behind the scenes. What starts as a simple schema on your end becomes a comprehensive interface that tells Claude it can perform actions like:

* Mouse movements and clicks
* Keyboard input and key combinations
* Taking screenshots
* Scrolling and other interface interactions

![](https://academy.claude.com/assets/media/3cb7af73c4a24c1861183ce69a0372cbf06e92950c492e522512c7c9fccb8d07.png)

The tool schema you send is minimal, but it automatically converts into a detailed specification that includes all the computer interaction capabilities Claude needs.

![](https://academy.claude.com/assets/media/106668c3e02cf97566f702349a7ac220bacc904b69c30f81009bc7ded4e5c8a0.png)

## The Technical Implementation

To make computer use work, you need a computing environment that can programmatically execute the actions Claude requests. The reference implementation uses a Docker container running Firefox, along with code that can simulate keypresses and mouse movements.

When Claude decides to interact with the computer, it sends a tool use request just like any other tool. Your server receives this request and executes the corresponding action in the containerized environment - whether that's clicking a button, typing text, or taking a screenshot.

The important thing to understand is that Claude isn't directly controlling a computer. It's making tool requests, and your infrastructure translates those requests into actual computer interactions.

## Getting Started

You don't need to build this infrastructure from scratch. Anthropic provides a reference implementation that handles all the complex parts for you.

![](https://academy.claude.com/assets/media/e8bf080606418b4207fb62709feecd446df055a93b12908794314c52df123bfc.png)

To set up computer use, you need:

1. A Docker runtime installed on your system
2. An AWS profile configured locally (usually "default")
3. The reference implementation from the Anthropic quickstarts repository

Once you have these prerequisites, you can start the Docker container with a single command. This gives you access to the same interface shown in the demonstrations - a chat interface on the left where you can talk to Claude, and a browser environment on the right where Claude can interact with web pages and applications.

![](https://academy.claude.com/assets/media/95ea027141baec80d881a0cae3713ede1ad920c6a2dd8bdc65e1421b3f8e675c.png)

The setup process is straightforward, and the full setup guide is available in the Anthropic quickstarts repository on GitHub. This reference implementation provides everything you need to start experimenting with Claude's computer use capabilities in a safe, contained environment.
