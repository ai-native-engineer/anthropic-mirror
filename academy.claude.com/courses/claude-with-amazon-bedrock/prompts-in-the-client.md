<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/prompts-in-the-client -->

Lesson 57 of 65 · Claude with Amazon BedrockPrompts in the client

The final step in building our MCP client is implementing prompt functionality. This allows us to list all available prompts from the server and retrieve specific prompts with variables interpolated into them.

## Implementing List Prompts

The `list_prompts` method is straightforward. We call the session's list prompts method and return the prompts:

python

```
async def list_prompts(self) -> list[types.Prompt]:
    result = await self.session().list_prompts()
    return result.prompts
```

## Getting Individual Prompts

The `get_prompt` method is more interesting because it handles argument interpolation. When we request a specific prompt, we pass arguments that get injected into the prompt function. For example, if our server has a "format" prompt that expects a `doc_id` parameter, that value gets passed through and interpolated into the actual prompt text.

python

```
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

The method returns messages that form a conversation ready to be fed directly into Claude.

## Testing Prompts in Action

When you run the client and type a forward slash, you'll see available prompts as commands. Selecting a prompt like "format" will prompt you to choose from available documents. The system then:

* Takes the prompt with the document ID interpolated
* Feeds it directly to Claude as a user message
* Claude receives both the instructions and the document ID
* Claude uses available tools to fetch the document content
* Claude responds with the reformatted result

![](https://academy.claude.com/assets/media/24f98aa7f06205838be82bfe92600a6964090589c0811bd7d5eced9f00b4ef01.png)

## How Prompts Work

Prompts define a set of user and assistant messages that can be used by the client. These prompts should be high quality, well-tested, and relevant to the overall purpose of your MCP server.

![](https://academy.claude.com/assets/media/746dff951e80556b72b3de46baca7a2ebc4171e5921b610ccc0bea3343f653c3.png)

The workflow is:

1. Write and evaluate a prompt relevant to your MCP server's purpose
2. Define the prompt inside your MCP server using the `@mcp.prompt` decorator
3. Your client can request that prompt at any time
4. When requesting the prompt, provide arguments that get passed as keyword arguments to the prompt function
5. The function uses those arguments to customize the prompt content

This system creates reusable, parameterized prompts that can be shared across different clients and use cases, making your MCP server more versatile and powerful.
