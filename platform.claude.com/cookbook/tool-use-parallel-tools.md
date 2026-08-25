<!-- source: https://platform.claude.com/cookbook/tool-use-parallel-tools -->

#  Parallel tool calls on Claude 3.7 Sonnet

Claude 3.7 Sonnet may be less likely to make make parallel tool calls in a response, even when you have not set `disable_parallel_tool_use`. To work around this, we recommend introducing a "batch tool" that can act as a meta-tool to wrap invocations to other tools simultaneously. We find that if this tool is present, the model will use it to simultaneously call multiple tools in parallel for you.

Let's take a look at the problem, and examine this workaround in more detail.

from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-sonnet-4-6"

##  Performing a query with multiple tool calls

Recall that the default behavior is for Claude to be allowed parallel tool calls. Combined with the default `tool_choice` of `auto`, this means that Claude can call any of the specified tools, or call more than one of them in a single assistant turn.

Let's set Claude up with a `get_weather` and `get_time` tool.

def get\_weather(location):

# Pretend to get the weather, and just return a fixed value.

return f"The weather in {location} is 72 degrees and sunny."

def get\_time(location):

# Pretend to get the time, and just return a fixed value.

return f"The time in {location} is 12:32 PM."

weather\_tool = {

"name": "get\_weather",

"description": "Gets the weather for in a given location",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The city and state, e.g. San Francisco, CA",

},

},

"required": ["location"],

},

}

time\_tool = {

"name": "get\_time",

"description": "Gets the time in a given location",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The city and state, e.g. San Francisco, CA",

},

},

"required": ["location"],

},

}

def process\_tool\_call(tool\_name, tool\_input):

if tool\_name == "get\_weather":

return get\_weather(tool\_input["location"])

elif tool\_name == "get\_time":

return get\_time(tool\_input["location"])

else:

raise ValueError(f"Unexpected tool name: {tool\_name}")

Next, let's provide Claude with these tools and perform a query.

def make\_query\_and\_print\_result(messages, tools=None):

response = client.messages.create(

model=MODEL\_NAME,

messages=messages,

max\_tokens=1000,

tool\_choice={"type": "auto"},

tools=tools or [weather\_tool, time\_tool],

)

for block in response.content:

match block.type:

case "text":

print(block.text)

case "tool\_use":

print(f"Tool: {block.name}({block.input})")

case \_:

raise ValueError(f"Unexpected block type: {block.type}")

return response

MESSAGES = [{"role": "user", "content": "What's the weather and time in San Francisco?"}]

response = make\_query\_and\_print\_result(MESSAGES)

```
I'll check the current weather and time in San Francisco for you.
Tool: get_weather({'location': 'San Francisco, CA'})
```

Notice how claude returned with a single tool call for the weather, even though we asked for both?

Let's see what happens if we call the weather tool and proceed.

last\_tool\_call = response.content[1]

MESSAGES.append({"role": "assistant", "content": response.content})

MESSAGES.append(

{

"role": "user",

"content": [

{

"type": "tool\_result",

"tool\_use\_id": last\_tool\_call.id,

"content": process\_tool\_call(response.content[1].name, response.content[1].input),

}

],

}

)

response = make\_query\_and\_print\_result(MESSAGES)

```
Tool: get_time({'location': 'San Francisco, CA'})
```

Notice now that Claude made a second tool call to get the time. While this technically happened immediately, this is potentially wasteful because it required "back and forth" – first Claude asked for the weather, then we had to process it, and *then* Claude asked for the time, and now we have to process *that*.

Claude will still do the right thing with the results, but it may be beneficial to encourage Claude to use both in one call, so we can process it simultaneously.

##  Introducing a batch tool

Let's introduce a `batch_tool`, so that Claude can have an opportunity to use it to combine multiple tool calls into one.

import json

batch\_tool = {

"name": "batch\_tool",

"description": "Invoke multiple other tool calls simultaneously",

"input\_schema": {

"type": "object",

"properties": {

"invocations": {

"type": "array",

"description": "The tool calls to invoke",

"items": {

"types": "object",

"properties": {

"name": {

"types": "string",

"description": "The name of the tool to invoke",

},

"arguments": {

"types": "string",

"description": "The arguments to the tool",

},

},

"required": ["name", "arguments"],

},

}

},

"required": ["invocations"],

},

}

def process\_tool\_with\_maybe\_batch(tool\_name, tool\_input):

if tool\_name == "batch\_tool":

results = []

for invocation in tool\_input["invocations"]:

results.append(

process\_tool\_call(invocation["name"], json.loads(invocation["arguments"]))

)

return "\n".join(results)

else:

return process\_tool\_call(tool\_name, tool\_input)

Now let's try to provide Claude with the existing weather and time tool, along with this new batch tool, and see what happens when we make a query requiring the weather and time.

MESSAGES = [{"role": "user", "content": "What's the weather and time in San Francisco?"}]

response = make\_query\_and\_print\_result(MESSAGES, tools=[weather\_tool, time\_tool, batch\_tool])

```
I can help you check both the weather and the time in San Francisco. Let me get that information for you right away.
Tool: batch_tool({'invocations': [{'name': 'get_weather', 'arguments': '{"location": "San Francisco, CA"}'}, {'name': 'get_time', 'arguments': '{"location": "San Francisco, CA"}'}]})
```

Notice how this time, Claude used the batch tool to query both the time and weather in one go. This allows us to process them simultaneously, potentially improving overall latency to the result.

last\_tool\_call = response.content[1]

MESSAGES.append({"role": "assistant", "content": response.content})

MESSAGES.append(

{

"role": "user",

"content": [

{

"type": "tool\_result",

"tool\_use\_id": last\_tool\_call.id,

"content": process\_tool\_with\_maybe\_batch(

response.content[1].name, response.content[1].input

),

}

],

}

)

response = make\_query\_and\_print\_result(MESSAGES)

```
Here's the information you requested:

Weather in San Francisco, CA: 72 degrees and sunny
Time in San Francisco, CA: 12:32 PM

Is there anything else you'd like to know about San Francisco?
```
