<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/structured-data-with-tools -->

Lesson 30 of 65 · Claude with Amazon BedrockStructured data with tools

Earlier in this course, we covered how to get structured output from Claude using message pre-fills and stop sequences. While that approach works well and is easy to set up, we can get more reliable output using tools. This method is more complex to implement, but it provides better consistency when extracting structured data like JSON.

## Why Learn Both Approaches?

You might wonder why we didn't just start with tools if they're more reliable. The answer is simple: tools require significantly more setup and complexity. Having both techniques available gives you flexibility - sometimes you'll want the quick prompt-based approach, other times you'll need the reliability that tools provide.

## How Tool-Based Structured Output Works

The core concept is straightforward: instead of asking Claude to format its response as JSON, you create a tool whose input parameters match the exact structure of data you want to extract. Claude then "calls" this tool with the extracted data as arguments.

![](https://academy.claude.com/assets/media/8e31fd40e0bf9e73f3221a900e31b8d200aed886203c8de1ca50d2e965939b60.png)

Here's the process:

1. Write a JSON schema that describes the structure of data you want
2. Create a tool with that schema as its input specification
3. Send your data and the tool schema to Claude
4. Force Claude to use the tool with the `toolChoice` parameter
5. Extract the structured data from the tool call arguments

![](https://academy.claude.com/assets/media/85045c0892b4746f255be062cdee6017dfec318ab23c44d5c0656d829f4978b6.png)

The flow looks like this: your server sends a prompt asking Claude to analyze data and call a specific tool. Claude responds with a tool use message containing the extracted JSON data. At that point, you simply take the data and end the conversation - no follow-up needed.

## Controlling Tool Usage

When using tools for structured output, you want to guarantee that Claude uses your extraction tool. The `toolChoice` parameter gives you three options:

![](https://academy.claude.com/assets/media/99e064378a0c0d2c27917469be7f9f52acabce4b33816f3edfa6be85d85b402a.png)

* `{"toolChoice": {"auto": {}}}` - Model decides if it needs to use a tool (default)
* `{"toolChoice": {"any": {}}}` - Model must use a tool, but can choose which one
* `{"toolChoice": {"tool": {"name": "tool-name"}}}` - Model must use the specified tool

For structured output, you'll almost always want the third option to ensure Claude uses your extraction tool.

## Practical Example

Let's say you want to extract the title, author, and key topics from an article. First, you'd create a tool schema:

python

```
article_details_schema = {
    "toolSpec": {
        "name": "article_details",
        "description": "Extracts key information from an article",
        "inputSchema": {
            "json": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the article"
                    },
                    "author": {
                        "type": "string",
                        "description": "The author's name"
                    },
                    "topics": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of key topics mentioned"
                    }
                },
                "required": ["title", "author", "topics"]
            }
        }
    }
}
```

Then you'd call Claude with your data and force it to use the tool. Our `chat` helper takes the tool name directly as its `tool_choice` argument, so you don't have to build the nested `toolChoice` object yourself:

python

```
messages = []
add_user_message(messages, f"""
Analyze the article below and extract key data. Then call the article_details tool.

<article_text>
{article_text}
</article_text>
""")

result = chat(messages, tools=[article_details_schema], tool_choice="article_details")
```

Claude will respond with a tool use message containing the extracted data in the exact format you specified. The tool call arguments will contain your structured JSON data, ready to use in your application.

## Key Benefits

* More reliable than prompt-based extraction
* Guaranteed structure matching your schema
* No need for message pre-fills or stop sequences
* Built-in validation through the tool schema

The main tradeoff is complexity - you need to write detailed schemas and handle tool responses. But when you need consistent, reliable structured output, tools are the way to go.
