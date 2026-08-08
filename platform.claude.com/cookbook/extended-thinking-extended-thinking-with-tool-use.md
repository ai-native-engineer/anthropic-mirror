<!-- source: https://platform.claude.com/cookbook/extended-thinking-extended-thinking-with-tool-use -->

#  Extended Thinking with Tool Use

##  Table of contents

* [Setup](#setup)
* [Basic example](#basic-example)
* [Multiple tool calls](#multiple-tool-calls-with-thinking)
* [Preserving thinking blocks](#preserving-thinking-blocks)

This notebook demonstrates how to use Claude 3.7 Sonnet's extended thinking feature with tools. The extended thinking feature allows you to see Claude's step-by-step thinking before it provides a final answer, providing transparency into how it decides which tools to use and how it interprets tool results.

When using extended thinking with tool use, the model will show its thinking before making tool requests, but not repeat the thinking process after receiving tool results. Claude will not output another thinking block until after the next non-`tool_result` `user` turn. For more information on extended thinking, see our [documentation(opens in new tab)](https://docs.claude.com/en/docs/build-with-claude/extended-thinking).

##  Setup

First, let's install the necessary packages and set up our environment.



%pip install anthropic



import anthropic

import os

import json

# Global variables for model and token budgets

MODEL\_NAME = "claude-sonnet-4-6"

MAX\_TOKENS = 4000

THINKING\_BUDGET\_TOKENS = 2000

# Set your API key as an environment variable or directly

# os.environ["ANTHROPIC\_API\_KEY"] = "your\_api\_key\_here"

# Initialize the client

client = anthropic.Anthropic()

# Helper functions

def print\_thinking\_response(response):

"""Pretty print a message response with thinking blocks."""

print("\n==== FULL RESPONSE ====")

for block in response.content:

if block.type == "thinking":

print("\n🧠 THINKING BLOCK:")

# Show truncated thinking for readability

print(block.thinking[:500] + "..." if len(block.thinking) > 500 else block.thinking)

print(f"\n[Signature available: {bool(getattr(block, 'signature', None))}]")

if hasattr(block, 'signature') and block.signature:

print(f"[Signature (first 50 chars): {block.signature[:50]}...]")

elif block.type == "redacted\_thinking":

print("\n🔒 REDACTED THINKING BLOCK:")

print(f"[Data length: {len(block.data) if hasattr(block, 'data') else 'N/A'}]")

elif block.type == "text":

print("\n✓ FINAL ANSWER:")

print(block.text)

print("\n==== END RESPONSE ====")

def count\_tokens(messages, tools=None):

"""Count tokens for a given message list with optional tools."""

if tools:

response = client.messages.count\_tokens(

model=MODEL\_NAME,

messages=messages,

tools=tools

)

else:

response = client.messages.count\_tokens(

model=MODEL\_NAME,

messages=messages

)

return response.input\_tokens

##  Single tool calls with thinking

This example demonstrates how to combine thinking and make a single tool call, with a mock weather tool.



def tool\_use\_with\_thinking():

# Define a weather tool

tools = [

{

"name": "weather",

"description": "Get current weather information for a location.",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The location to get weather for."

}

},

"required": ["location"]

}

}

]

def weather(location):

# Mock weather data

weather\_data = {

"New York": {"temperature": 72, "condition": "Sunny"},

"London": {"temperature": 62, "condition": "Cloudy"},

"Tokyo": {"temperature": 80, "condition": "Partly cloudy"},

"Paris": {"temperature": 65, "condition": "Rainy"},

"Sydney": {"temperature": 85, "condition": "Clear"},

"Berlin": {"temperature": 60, "condition": "Foggy"},

}

return weather\_data.get(location, {"error": f"No weather data available for {location}"})

# Initial request with tool use and thinking

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=[{

"role": "user",

"content": "What's the weather like in Paris today?"

}]

)

# Detailed diagnostic output of initial response

print("\n=== INITIAL RESPONSE ===")

print(f"Response ID: {response.id}")

print(f"Stop reason: {response.stop\_reason}")

print(f"Model: {response.model}")

print(f"Content blocks: {len(response.content)} blocks")

for i, block in enumerate(response.content):

print(f"\nBlock {i+1}: Type = {block.type}")

if block.type == "thinking":

print(f"Thinking content: {block.thinking[:150]}...")

print(f"Signature available: {bool(getattr(block, 'signature', None))}")

elif block.type == "text":

print(f"Text content: {block.text}")

elif block.type == "tool\_use":

print(f"Tool: {block.name}")

print(f"Tool input: {block.input}")

print(f"Tool ID: {block.id}")

print("=== END INITIAL RESPONSE ===\n")

# Extract thinking blocks to include in the conversation history

assistant\_blocks = []

for block in response.content:

if block.type in ["thinking", "redacted\_thinking", "tool\_use"]:

assistant\_blocks.append(block)

# Handle tool use if required

full\_conversation = [{

"role": "user",

"content": "What's the weather like in Paris today?"

}]

if response.stop\_reason == "tool\_use":

# Add entire assistant response with thinking blocks and tool use

full\_conversation.append({

"role": "assistant",

"content": assistant\_blocks

})

# Find the tool\_use block

tool\_use\_block = next((block for block in response.content if block.type == "tool\_use"), None)

if tool\_use\_block:

# Execute the tool

print(f"\n=== EXECUTING TOOL ===")

print(f"Tool name: {tool\_use\_block.name}")

print(f"Location to check: {tool\_use\_block.input['location']}")

tool\_result = weather(tool\_use\_block.input["location"])

print(f"Result: {tool\_result}")

print("=== TOOL EXECUTION COMPLETE ===\n")

# Add tool result to conversation

full\_conversation.append({

"role": "user",

"content": [{

"type": "tool\_result",

"tool\_use\_id": tool\_use\_block.id,

"content": json.dumps(tool\_result)

}]

})

# Continue the conversation with the same thinking configuration

print("\n=== SENDING FOLLOW-UP REQUEST WITH TOOL RESULT ===")

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=full\_conversation

)

print(f"Follow-up response received. Stop reason: {response.stop\_reason}")

print\_thinking\_response(response)

# Run the example

tool\_use\_with\_thinking()



```
=== INITIAL RESPONSE ===
Response ID: msg_01NhR4vE9nVh2sHs5fXbzji8
Stop reason: tool_use
Model: claude-sonnet-4-6
Content blocks: 3 blocks

Block 1: Type = thinking
Thinking content: The user is asking about the current weather in Paris. I can use the `weather` function to get this information.

The `weather` function requires a "l...
Signature available: True

Block 2: Type = text
Text content: I'll check the current weather in Paris for you.

Block 3: Type = tool_use
Tool: weather
Tool input: {'location': 'Paris'}
Tool ID: toolu_01WaeSyitUGJFaaPe68cJuEv
=== END INITIAL RESPONSE ===

=== EXECUTING TOOL ===
Tool name: weather
Location to check: Paris
Result: {'temperature': 65, 'condition': 'Rainy'}
=== TOOL EXECUTION COMPLETE ===

=== SENDING FOLLOW-UP REQUEST WITH TOOL RESULT ===
Follow-up response received. Stop reason: end_turn

==== FULL RESPONSE ====

✓ FINAL ANSWER:
Currently in Paris, it's 65°F (18°C) and rainy. You might want to bring an umbrella if you're heading out!

==== END RESPONSE ====
```

##  Multiple tool calls with thinking

This example demonstrates how to handle multiple tool calls, such as a mock news and weather service, while observing the thinking process.



def multiple\_tool\_calls\_with\_thinking():

# Define tools

tools = [

{

"name": "weather",

"description": "Get current weather information for a location.",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The location to get weather for."

}

},

"required": ["location"]

}

},

{

"name": "news",

"description": "Get latest news headlines for a topic.",

"input\_schema": {

"type": "object",

"properties": {

"topic": {

"type": "string",

"description": "The topic to get news about."

}

},

"required": ["topic"]

}

}

]

def weather(location):

# Mock weather data

weather\_data = {

"New York": {"temperature": 72, "condition": "Sunny"},

"London": {"temperature": 62, "condition": "Cloudy"},

"Tokyo": {"temperature": 80, "condition": "Partly cloudy"},

"Paris": {"temperature": 65, "condition": "Rainy"},

"Sydney": {"temperature": 85, "condition": "Clear"},

"Berlin": {"temperature": 60, "condition": "Foggy"},

}

return weather\_data.get(location, {"error": f"No weather data available for {location}"})

def news(topic):

# Mock news data

news\_data = {

"technology": [

"New AI breakthrough announced by research lab",

"Tech company releases latest smartphone model",

"Quantum computing reaches milestone achievement"

],

"sports": [

"Local team wins championship game",

"Star player signs record-breaking contract",

"Olympic committee announces host city for 2036"

],

"weather": [

"Storm system developing in the Atlantic",

"Record temperatures recorded across Europe",

"Climate scientists release new research findings"

]

}

return {"headlines": news\_data.get(topic.lower(), ["No news available for this topic"])}

# Initial request

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=[{

"role": "user",

"content": "What's the weather in London, and can you also tell me the latest news about technology?"

}]

)

# Print detailed information about initial response

print("\n=== INITIAL RESPONSE ===")

print(f"Response ID: {response.id}")

print(f"Stop reason: {response.stop\_reason}")

print(f"Model: {response.model}")

print(f"Content blocks: {len(response.content)} blocks")

# Print each content block

for i, block in enumerate(response.content):

print(f"\nBlock {i+1}: Type = {block.type}")

if block.type == "thinking":

print(f"Thinking content: {block.thinking[:150]}...")

print(f"Signature available: {bool(getattr(block, 'signature', None))}")

elif block.type == "text":

print(f"Text content: {block.text}")

elif block.type == "tool\_use":

print(f"Tool: {block.name}")

print(f"Tool input: {block.input}")

print(f"Tool ID: {block.id}")

print("=== END INITIAL RESPONSE ===\n")

# Handle potentially multiple tool calls

full\_conversation = [{

"role": "user",

"content": "What's the weather in London, and can you also tell me the latest news about technology?"

}]

# Track iteration count for multi-turn tool use

iteration = 0

while response.stop\_reason == "tool\_use":

iteration += 1

print(f"\n=== TOOL USE ITERATION {iteration} ===")

# Extract thinking blocks and tool use to include in conversation history

assistant\_blocks = []

for block in response.content:

if block.type in ["thinking", "redacted\_thinking", "tool\_use"]:

assistant\_blocks.append(block)

# Add assistant response with thinking blocks and tool use

full\_conversation.append({

"role": "assistant",

"content": assistant\_blocks

})

# Find the tool\_use block

tool\_use\_block = next((block for block in response.content if block.type == "tool\_use"), None)

if tool\_use\_block:

print(f"\n=== EXECUTING TOOL ===")

print(f"Tool name: {tool\_use\_block.name}")

# Execute the appropriate tool

if tool\_use\_block.name == "weather":

print(f"Location to check: {tool\_use\_block.input['location']}")

tool\_result = weather(tool\_use\_block.input["location"])

elif tool\_use\_block.name == "news":

print(f"Topic to check: {tool\_use\_block.input['topic']}")

tool\_result = news(tool\_use\_block.input["topic"])

else:

tool\_result = {"error": "Unknown tool"}

print(f"Result: {tool\_result}")

print("=== TOOL EXECUTION COMPLETE ===\n")

# Add tool result to conversation

full\_conversation.append({

"role": "user",

"content": [{

"type": "tool\_result",

"tool\_use\_id": tool\_use\_block.id,

"content": json.dumps(tool\_result)

}]

})

# Continue the conversation

print("\n=== SENDING FOLLOW-UP REQUEST WITH TOOL RESULT ===")

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=full\_conversation

)

# Print follow-up response details

print(f"\n=== FOLLOW-UP RESPONSE (ITERATION {iteration}) ===")

print(f"Response ID: {response.id}")

print(f"Stop reason: {response.stop\_reason}")

print(f"Content blocks: {len(response.content)} blocks")

for i, block in enumerate(response.content):

print(f"\nBlock {i+1}: Type = {block.type}")

if block.type == "thinking":

print(f"Thinking content preview: {block.thinking[:100]}...")

elif block.type == "text":

print(f"Text content preview: {block.text[:100]}...")

elif block.type == "tool\_use":

print(f"Tool: {block.name}")

print(f"Tool input preview: {str(block.input)[:100]}")

print(f"=== END FOLLOW-UP RESPONSE (ITERATION {iteration}) ===\n")

if response.stop\_reason != "tool\_use":

print("\n=== FINAL RESPONSE ===")

print\_thinking\_response(response)

print("=== END FINAL RESPONSE ===")

else:

print("No tool\_use block found in response.")

break

# Run the example

multiple\_tool\_calls\_with\_thinking()



```
=== INITIAL RESPONSE ===
Response ID: msg_01VwqpBMARVoTP1H8Ytvmvsb
Stop reason: tool_use
Model: claude-sonnet-4-6
Content blocks: 3 blocks

Block 1: Type = thinking
Thinking content: The user is asking for two pieces of information:
1. The weather in London
2. The latest news about technology

Let me check what tools I have availab...
Signature available: True

Block 2: Type = text
Text content: I'll get that information for you right away.

Block 3: Type = tool_use
Tool: weather
Tool input: {'location': 'London'}
Tool ID: toolu_016xHQWMR4JsKtWvH9nbsZyA
=== END INITIAL RESPONSE ===

=== TOOL USE ITERATION 1 ===

=== EXECUTING TOOL ===
Tool name: weather
Location to check: London
Result: {'temperature': 62, 'condition': 'Cloudy'}
=== TOOL EXECUTION COMPLETE ===

=== SENDING FOLLOW-UP REQUEST WITH TOOL RESULT ===

=== FOLLOW-UP RESPONSE (ITERATION 1) ===
Response ID: msg_01EhR96Z2Z2t5EDhuWeodUod
Stop reason: tool_use
Content blocks: 1 blocks

Block 1: Type = tool_use
Tool: news
Tool input preview: {'topic': 'technology'}
=== END FOLLOW-UP RESPONSE (ITERATION 1) ===

=== TOOL USE ITERATION 2 ===

=== EXECUTING TOOL ===
Tool name: news
Topic to check: technology
Result: {'headlines': ['New AI breakthrough announced by research lab', 'Tech company releases latest smartphone model', 'Quantum computing reaches milestone achievement']}
=== TOOL EXECUTION COMPLETE ===

=== SENDING FOLLOW-UP REQUEST WITH TOOL RESULT ===

=== FOLLOW-UP RESPONSE (ITERATION 2) ===
Response ID: msg_01WUEfC4UxPFaJaktjVDMJEN
Stop reason: end_turn
Content blocks: 1 blocks

Block 1: Type = text
Text content preview: Here's the information you requested:

## Weather in London
Currently, it's 62°F and cloudy in Londo...
=== END FOLLOW-UP RESPONSE (ITERATION 2) ===

=== FINAL RESPONSE ===

==== FULL RESPONSE ====

✓ FINAL ANSWER:
Here's the information you requested:

## Weather in London
Currently, it's 62°F and cloudy in London.

## Latest Technology News Headlines
- New AI breakthrough announced by research lab
- Tech company releases latest smartphone model
- Quantum computing reaches milestone achievement

==== END RESPONSE ====
=== END FINAL RESPONSE ===
```

##  Preserving thinking blocks

When working with extended thinking and tools, make sure to:

1. **Preserve thinking block signatures**: Each thinking block contains a cryptographic signature that validates the conversation context. These signatures must be included when passing thinking blocks back to Claude.
2. **Avoid modifying prior context**: The API will reject requests if any previous content (including thinking blocks) is modified when submitting a new request with tool results.
3. **Handle both thinking and redacted\_thinking blocks**: Both types of blocks must be preserved in the conversation history, even if the content of redacted blocks is not human readable.

For more details on extended thinking without tools, see the main "Extended Thinking" notebook.



def thinking\_block\_preservation\_example():

# Define a simple weather tool

tools = [

{

"name": "weather",

"description": "Get current weather information for a location.",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The location to get weather for."

}

},

"required": ["location"]

}

}

]

def weather(location):

# Mock weather data

weather\_data = {

"New York": {"temperature": 72, "condition": "Sunny"},

"London": {"temperature": 62, "condition": "Cloudy"},

"Tokyo": {"temperature": 80, "condition": "Partly cloudy"},

"Paris": {"temperature": 65, "condition": "Rainy"},

"Sydney": {"temperature": 85, "condition": "Clear"},

"Berlin": {"temperature": 60, "condition": "Foggy"},

}

return weather\_data.get(location, {"error": f"No weather data available for {location}"})

# Initial request with tool use and thinking

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=[{

"role": "user",

"content": "What's the weather like in Berlin right now?"

}]

)

# Extract blocks from response

thinking\_blocks = [b for b in response.content if b.type == "thinking"]

tool\_use\_blocks = [b for b in response.content if b.type == "tool\_use"]

print("\n=== INITIAL RESPONSE ===")

print(f"Response contains:")

print(f"- {len(thinking\_blocks)} thinking blocks")

print(f"- {len(tool\_use\_blocks)} tool use blocks")

# Check if tool use was triggered

if tool\_use\_blocks:

tool\_block = tool\_use\_blocks[0]

print(f"\nTool called: {tool\_block.name}")

print(f"Location to check: {tool\_block.input['location']}")

# Execute the tool

tool\_result = weather(tool\_block.input["location"])

print(f"Tool result: {tool\_result}")

# First, let's try WITHOUT including the thinking block

print("\n=== TEST 1: WITHOUT thinking block ===")

try:

# Notice we're only including the tool\_use block, not the thinking block

partial\_blocks = tool\_use\_blocks

incomplete\_response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=[

{"role": "user", "content": "What's the weather like in Berlin right now?"},

{"role": "assistant", "content": partial\_blocks},

{"role": "user", "content": [{

"type": "tool\_result",

"tool\_use\_id": tool\_block.id,

"content": json.dumps(tool\_result)

}]}

]

)

print("SUCCESS: Response received without thinking block (not expected)")

except Exception as e:

print(f"ERROR: {e}")

print("This demonstrates that thinking blocks must be preserved")

# Now try WITH the thinking block included (correct approach)

print("\n=== TEST 2: WITH thinking block (correct approach) ===")

try:

# Include all blocks from the response

complete\_blocks = thinking\_blocks + tool\_use\_blocks

complete\_response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=MAX\_TOKENS,

thinking={

"type": "enabled",

"budget\_tokens": THINKING\_BUDGET\_TOKENS

},

tools=tools,

messages=[

{"role": "user", "content": "What's the weather like in Berlin right now?"},

{"role": "assistant", "content": complete\_blocks},

{"role": "user", "content": [{

"type": "tool\_result",

"tool\_use\_id": tool\_block.id,

"content": json.dumps(tool\_result)

}]}

]

)

print("SUCCESS: Response received with thinking blocks included")

# Check if second response has thinking blocks

second\_thinking = [b for b in complete\_response.content if b.type == "thinking"]

second\_text = [b for b in complete\_response.content if b.type == "text"]

print(f"\nSecond response contains:")

print(f"- {len(second\_thinking)} thinking blocks")

print(f"- {len(second\_text)} text blocks")

if second\_text:

print(f"\nFinal answer: {second\_text[0].text}")

print("\nNote: The second response after tool use doesn't contain thinking blocks.")

print("This is expected behavior - thinking is shown before tool use but not after receiving tool results.")

except Exception as e:

print(f"ERROR: {e}")

# Uncomment to run the example

thinking\_block\_preservation\_example()



```
=== INITIAL RESPONSE ===
Response contains:
- 1 thinking blocks
- 1 tool use blocks

Tool called: weather
Location to check: Berlin
Tool result: {'temperature': 60, 'condition': 'Foggy'}

=== TEST 1: WITHOUT thinking block ===
ERROR: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'messages.1.content.0.type: Expected `thinking` or `redacted_thinking`, but found `tool_use`. When `thinking` is enabled, a final `assistant` message must start with a thinking block (preceeding the lastmost set of `tool_use` and `tool_result` blocks). We recommend you include thinking blocks from previous turns. To avoid this requirement, disable `thinking`. Please consult our documentation at https://docs.claude.com/en/docs/build-with-claude/extended-thinking'}}
This demonstrates that thinking blocks must be preserved

=== TEST 2: WITH thinking block (correct approach) ===
SUCCESS: Response received with thinking blocks included

Second response contains:
- 0 thinking blocks
- 1 text blocks

Final answer: Currently in Berlin, it's foggy with a temperature of 60°F (about 15.5°C).

Note: The second response after tool use doesn't contain thinking blocks.
This is expected behavior - thinking is shown before tool use but not after receiving tool results.
```

##  Conclusion

This notebook shows how to combine Claude's extended thinking feature with tool use. Key benefits include:

1. Transparency into Claude's thinking process when using tools
2. Visibility into how Claude decides when to use tools versus internal knowledge
3. Better understanding of multi-step tasks that involve multiple tool calls
4. Insight into how Claude interprets tool results and incorporates them into responses

When using extended thinking with tools, keep in mind:

* Set appropriate thinking budgets for complex tasks (minimum 1,024 tokens)
* Always preserve thinking blocks and their signatures when passing tool results
* Include both normal and redacted thinking blocks in the conversation history
* Ensure that system prompts, tools, and thinking configurations match between calls
* Expect that tool result turns will not contain additional thinking blocks
* Tool use and thinking together can increase token usage and response time
