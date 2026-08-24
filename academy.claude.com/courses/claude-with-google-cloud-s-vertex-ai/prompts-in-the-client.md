<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompts-in-the-client -->

Lesson 58 of 66 · Claude with Google Cloud's Vertex AIPrompts in the client

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

The `get_prompt` method is more interesting because it handles argument interpolation. When we request a specific prompt, we pass arguments that get injected into the prompt function. For example, if our server has a "format" prompt that expects a `doc_id` parameter, we provide that value in the arguments dictionary:

python

```
async def get_prompt(self, prompt_name, args: dict[str, str]):
    result = await self.session().get_prompt(prompt_name, args)
    return result.messages
```

The method returns messages that form a conversation ready to be fed directly into Claude.

## How Prompt Arguments Work

When you define a prompt function in your MCP server, any parameters become available as interpolation variables. The arguments dictionary you pass to `get_prompt` provides values for these parameters. The server then generates the complete prompt with your values substituted in the appropriate places.

![](https://academy.claude.com/assets/media/2c67261e0d3c34f3f98fa84ba91b8acae53cc361101eab1d6c5ed1e9c51bd64e.png)

## Testing the Implementation

Once implemented, you can test prompts through the CLI. When you type a forward slash, available prompts appear as commands. Selecting a prompt like "format" will prompt you to choose values for any required arguments (like selecting a document to format). The system then:

1. Retrieves the prompt with your arguments interpolated
2. Sends the complete prompt to Claude
3. Claude executes any necessary tool calls to fulfill the request
4. Returns the formatted result

![](https://academy.claude.com/assets/media/746dff951e80556b72b3de46baca7a2ebc4171e5921b610ccc0bea3343f653c3.png)

## Prompts in Practice

Prompts define reusable sets of user and assistant messages that clients can invoke. They should be high-quality, well-tested, and relevant to your MCP server's purpose. Think of them as pre-built workflows that combine your server's tools and resources to accomplish specific tasks.

The prompt system creates a clean separation between the prompt logic (defined on the server) and the execution (handled by the client and Claude). This makes it easy to create sophisticated, multi-step workflows that users can trigger with simple commands.
