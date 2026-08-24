<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/running-tool-functions -->

Lesson 25 of 65 · Claude with Amazon BedrockRunning tool functions

When Claude responds with a tool use request, your server needs to actually run the requested tool and send the results back. This step involves extracting tool use parts from Claude's response, executing the appropriate functions, and formatting the results properly.

## Handling Multiple Tool Requests

Claude can send multiple tool use parts in a single response. Your code needs to handle this possibility defensively. An assistant message might contain a text part followed by one, two, or even more tool use parts.

![](https://academy.claude.com/assets/media/e9f8f672e5509df4a63b0041d4ad48d777486d186ca6f73b56b8175394ff93e6.png)

The flow works like this: Claude sends a request with JSON schema, receives a tool use part, then your server runs the tool and sends back a tool result part for Claude to provide a final response.

![](https://academy.claude.com/assets/media/b14d578714a8d8f52cfdbac22c60e90e96b3b7176e5d7e50c20247c440d7f54d.png)

## Extracting Tool Use Parts

First, create a function to process all the parts returned from a chat request:

python

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []

    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]
```

This comprehension filters the parts list to only include dictionaries that contain a "toolUse" key, ignoring text parts.

## Running the Actual Tools

Create a helper function to execute the requested tool:

python

```
def run_tool(tool_name, tool_input):
    if tool_name == "get_current_datetime":
        return get_current_datetime(**tool_input)
    else:
        raise Exception(f"Unknown tool name: {tool_name}")
```

The key detail here is using `**tool_input` to splat the dictionary of arguments into your tool function. Claude always returns arguments as a dictionary object, so you need to unpack it properly.

## Creating Tool Result Parts

After running a tool, you need to format the response as a tool result part:

![](https://academy.claude.com/assets/media/9786d7c8d5df5bb39c53002577f5db87d936bd11141a76b1aa43c9989218f283.png)

Tool result parts require three key properties:

* **toolUseId** - Must match the original tool use part's ID
* **content** - The output from your tool, serialized as a string
* **status** - Either "success" or "error"

## Understanding Tool Use IDs

The tool use ID system becomes important when Claude requests multiple tools in parallel. For example, if Claude wants to run a calculator tool twice:

![](https://academy.claude.com/assets/media/eabb90a73e770a487df4094e034ea95de5c45c4add32f652c2a2626bccea1dc3.png) ![](https://academy.claude.com/assets/media/7bf844674b47f636d2c2908bb712dbc882ae2377fdcc392c546b8f45af5e453d.png)

Each tool use gets a unique ID (like "ab3" and "po9"), and your tool results must include the matching IDs so Claude knows which result corresponds to which request.

## Error Handling

Wrap your tool execution in try-catch blocks. Claude is intelligent about tool errors and might adjust its approach if you return proper error information:

python

```
try:
    tool_output = run_tool(tool_name, tool_input)
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": json.dumps(tool_output)}],
            "status": "success"
        }
    }
except Exception as e:
    tool_result_part = {
        "toolResult": {
            "toolUseId": tool_use_id,
            "content": [{"text": f"Error: {e}"}],
            "status": "error"
        }
    }
```

## Complete Implementation

Here's the full function that processes tool requests and returns formatted results:

python

```
def run_tools(parts):
    tool_requests = [part for part in parts if "toolUse" in part]
    tool_result_parts = []

    for tool_request in tool_requests:
        tool_use_id = tool_request["toolUse"]["toolUseId"]
        tool_name = tool_request["toolUse"]["name"]
        tool_input = tool_request["toolUse"]["input"]

        try:
            tool_output = run_tool(tool_name, tool_input)
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": json.dumps(tool_output)}],
                    "status": "success"
                }
            }
        except Exception as e:
            tool_result_part = {
                "toolResult": {
                    "toolUseId": tool_use_id,
                    "content": [{"text": f"Error: {e}"}],
                    "status": "error"
                }
            }

        tool_result_parts.append(tool_result_part)

    return tool_result_parts
```

Once you have the tool result parts, you can send them back to Claude in your next chat request, completing the tool use cycle.
