<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/introducing-tool-use -->

Lesson 21 of 65 · Claude with Amazon BedrockIntroducing tool use

Tools allow Claude to access information from the outside world, solving one of its key limitations. By default, Claude only has access to information it was trained on, which means it can't provide current information like today's weather or recent news.

![](https://academy.claude.com/assets/media/7692955293ff6d4b030a98a281f9197fd1518ea6b41e9c8d965d5628fa67da8f.png)

When a user asks "What's the weather in San Francisco, California?" Claude will typically respond with "I'm sorry, but I don't have access to up-to-date weather information." Tools fix this problem by creating a bridge between Claude and external data sources.

## How Tool Use Works

The tool use process follows a specific flow that involves multiple back-and-forth communications between your server and Claude:

![](https://academy.claude.com/assets/media/8d6e5b5237acf900f920f9bc54947932fa54381db1740a9f4142de989f26b805.png)

1. **Initial Request:** You send Claude a question along with instructions on how to get extra data
2. **Tool Request:** Claude analyzes the question and asks for specific external data it needs
3. **Data Retrieval:** Your server runs code to fetch the requested information
4. **Final Response:** Claude uses the external data to provide a complete, informed answer

## Weather Example in Practice

Here's how the tool use flow works for a weather query:

![](https://academy.claude.com/assets/media/4e315ccb2014ca3d65e795f6c7ee20a6b77faa99b7d1a77952cb3cff0bd04b96.png)

When a user asks about weather, you include details on how to retrieve current weather data in your initial request to Claude. Claude recognizes it needs current weather information and asks your server to get it. Your server calls a weather API, retrieves the live data, and sends it back to Claude. Finally, Claude combines the original question with the fresh weather data to provide an accurate, current response.

## Implementation Challenges

Tool use can feel confusing because there's a disconnect between the logical flow and how you actually write the code. The implementation doesn't follow the same order as the conceptual steps:

![](https://academy.claude.com/assets/media/ce61ec2a1c32ab584a0044ec5602a73b05717dd23b0758366acb4374e7b4fdfa.png)

In practice, you often need to:

* Write the tool function first
* Create a JSON schema specification
* Handle the ToolUse and ToolResult parts
* Include the schema with your request

This jumping around between different parts of the implementation is why tool use initially seems complex. The key is understanding that each step in the logical flow requires specific code components that you'll build in a different order than they execute.

In the following videos, we'll implement tool use step by step, frequently referencing this flow diagram to keep track of which piece we're currently building.
