<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/accessing-resources -->

Lesson 56 of 66 · Claude with Google Cloud's Vertex AIAccessing resources

Resources in MCP allow your server to expose data that can be directly included in prompts, rather than requiring tool calls to access information. This creates a more efficient way to provide context to AI models like Claude.

## Understanding the Resource Flow

![](https://academy.claude.com/assets/media/f2baa6225bba4675d0624954dbe38fc669f17916147b137fb01c305f825c0e83.png)

When a user wants to access resource content, the flow works like this:

* User requests information about a resource (like "@report.pdf")
* Your code needs a list of document names for autocomplete
* MCP Client sends a ReadResourceRequest to the MCP Server
* Server responds with a ReadResourceResult containing the resource data
* Your code can then put this data directly into prompts

## Implementing Resource Reading

To read resources from your MCP client, you'll need to implement a `read_resource` function. First, add the necessary imports:

python

```
import json
from pydantic import AnyUrl
```

The core function makes a request to your MCP session and processes the response:

python

```
async def read_resource(self, uri: str) -> Any:
    result = await self.session().read_resource(AnyUrl(uri))
    resource = result.contents[0]
```

## Handling Different Resource Types

Resources can return different types of content, so you need to check the MIME type and parse accordingly:

python

```
if isinstance(resource, types.TextResourceContents):
    if resource.mimeType == "application/json":
        return json.loads(resource.text)

    return resource.text
```

This approach handles two main scenarios:

* JSON resources that need parsing
* Plain text resources that can be returned as-is

## Testing Resource Access

![](https://academy.claude.com/assets/media/f17435118f01fd2933aa7930a388730b916195763575e2034efcbd9175c00195.png)

You can verify your resource implementation works by testing it in your application. When you type "@" followed by a resource name, you should see an autocomplete list of available resources. Selecting one will include its contents directly in your prompt.

The key advantage of this approach is efficiency - Claude receives the document content immediately without needing to make additional tool calls to access the information.

## Resource vs Tool Usage

Resources are particularly useful when:

* You have static or semi-static content that's frequently referenced
* You want to reduce the number of API calls
* The content should be immediately available in the prompt context

This differs from tools, which are better for dynamic operations or when you need the AI to decide whether to access certain information based on the conversation context.
