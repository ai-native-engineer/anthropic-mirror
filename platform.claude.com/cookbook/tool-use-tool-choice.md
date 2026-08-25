<!-- source: https://platform.claude.com/cookbook/tool-use-tool-choice -->

#  Tool choice

Tool use supports a parameter called `tool_choice` that allows you to specify how you want Claude to call tools. In this notebook, we'll take a look at how it works and when to use it. Before going any further, make sure you are comfortable with the basics of tool use with Claude.

When working with the `tool_choice` parameter, we have three possible options:

* `auto` allows Claude to decide whether to call any provided tools or not
* `tool` allows us to force Claude to always use a particular tool
* `any` tells Claude that it must use one of the provided tools, but doesn't force a particular tool

Let's take a look at each option in detail. We'll start by importing the Anthropic SDK:

from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-sonnet-4-6"

##  Auto

Setting `tool_choice` to `auto` allows the model to automatically decide whether to use tools or not. This is the default behavior when working with tools.

To demonstrate this, we're going to provide Claude with a fake web search tool. We will ask Claude questions, some of which would require calling the web search tool and other which Claude should be able to answer on its own.

Let's start by defining a tool called `web_search`. Please note, to keep this demo simple, we're not actually searching the web here:

def web\_search(topic):

print(f"pretending to search the web for {topic}")

web\_search\_tool = {

"name": "web\_search",

"description": "A tool to retrieve up to date information on a given topic by searching the web",

"input\_schema": {

"type": "object",

"properties": {

"topic": {"type": "string", "description": "The topic to search the web for"},

},

"required": ["topic"],

},

}

Next, we write a function that accepts a user\_query and passes it along to Claude, along with the `web_search_tool`.

We also set `tool_choice` to `auto`:

tool\_choice={"type": "auto"}

Here's the complete function:

from datetime import date

def chat\_with\_web\_search(user\_query):

messages = [{"role": "user", "content": user\_query}]

system\_prompt = f"""

Answer as many questions as you can using your existing knowledge.

Only search the web for queries that you can not confidently answer.

Today's date is {date.today().strftime("%B %d %Y")}

If you think a user's question involves something in the future that hasn't happened yet, use the search tool.

"""

response = client.messages.create(

system=system\_prompt,

model=MODEL\_NAME,

messages=messages,

max\_tokens=1000,

tool\_choice={"type": "auto"},

tools=[web\_search\_tool],

)

last\_content\_block = response.content[-1]

if last\_content\_block.type == "text":

print("Claude did NOT call a tool")

print(f"Assistant: {last\_content\_block.text}")

elif last\_content\_block.type == "tool\_use":

print("Claude wants to use a tool")

print(last\_content\_block)

Let's start with a question Claude should be able to answer without using the tool:

chat\_with\_web\_search("What color is the sky?")

```
Claude did NOT call a tool
Assistant: The sky appears blue during the day. This is because the Earth's atmosphere scatters more blue light from the sun than other colors, making the sky look blue.
```

When we ask "What color is the sky?", Claude does not use the tool. Let's try asking something that Claude should use the web search tool to answer:

chat\_with\_web\_search("Who won the 2024 Miami Grand Prix?")

```
Claude wants to use a tool
ToolUseBlock(id='toolu_staging_018nwaaRebX33pHqoZZXDaSw', input={'topic': '2024 Miami Grand Prix winner'}, name='web_search', type='tool_use')
```

When we ask "Who won the 2024 Miami Grand Prix?", Claude uses the web search tool!

Let's try a few more examples:

# Claude should NOT need to use the tool for this:

chat\_with\_web\_search("Who won the superbowl in 2022?")

```
Claude did NOT call a tool
Assistant: The Los Angeles Rams won Super Bowl LVI in 2022, defeating the Cincinnati Bengals by a score of 23-20. The game was played on February 13, 2022 at SoFi Stadium in Inglewood, California.
```

# Claude SHOULD use the tool for this:

chat\_with\_web\_search("Who won the superbowl in 2024?")

```
Claude wants to use a tool
ToolUseBlock(id='toolu_staging_016XPwcprHAgYJBtN7A3jLhb', input={'topic': '2024 Super Bowl winner'}, name='web_search', type='tool_use')
```

###  Your Prompt Matters!

When working with `tool_choice` of `auto`, it's important that you spend time to write a detailed prompt. Often, Claude can be over-eager to call tools. Writing a detailed prompt helps Claude determine when to call a tool and when not to. In the above example, we included specific instructions in the system prompt:

system\_prompt=f"""

Answer as many questions as you can using your existing knowledge.

Only search the web for queries that you can not confidently answer.

Today's date is {date.today().strftime("%B %d %Y")}

If you think a user's question involves something in the future that hasn't happened yet, use the search tool.

"""

##  Forcing a specific tool

We can force Claude to use a particular tool using `tool_choice`. In the example below, we've defined two simple tools:

* `print_sentiment_scores` - a tool that "tricks" Claude into generating well-structured JSON output containing sentiment analysis data. For more info on this approach, see [Extracting Structured JSON using Claude and Tool Use(opens in new tab)](https://github.com/anthropics/anthropic-cookbook/blob/main/tool_use/extracting_structured_json.ipynb)
* `calculator` - a very simple calculator tool that takes two numbers and adds them together

tools = [

{

"name": "print\_sentiment\_scores",

"description": "Prints the sentiment scores of a given tweet or piece of text.",

"input\_schema": {

"type": "object",

"properties": {

"positive\_score": {

"type": "number",

"description": "The positive sentiment score, ranging from 0.0 to 1.0.",

},

"negative\_score": {

"type": "number",

"description": "The negative sentiment score, ranging from 0.0 to 1.0.",

},

"neutral\_score": {

"type": "number",

"description": "The neutral sentiment score, ranging from 0.0 to 1.0.",

},

},

"required": ["positive\_score", "negative\_score", "neutral\_score"],

},

},

{

"name": "calculator",

"description": "Adds two number",

"input\_schema": {

"type": "object",

"properties": {

"num1": {"type": "number", "description": "first number to add"},

"num2": {"type": "number", "description": "second number to add"},

},

"required": ["num1", "num2"],

},

},

]

Our goal is to write a function called `analyze_tweet_sentiment` that takes a tweet and prints a basic sentiment analysis of that tweet. Eventually we will "force" Claude to use our sentiment analysis tool, but we'll start by showing what happens when we **do not** force the tool use.

In this first "bad" version of the `analyze_tweet_sentiment` function, we provide Claude with both tools. For the sake of comparison, we'll start by setting tool\_choice to "auto":

tool\_choice={"type": "auto"}

Please note that we are deliberately not providing Claude with a well-written prompt, to make it easier to see the impact of forcing the use of a particular tool.

def analyze\_tweet\_sentiment(query):

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

tool\_choice={"type": "auto"},

messages=[{"role": "user", "content": query}],

)

print(response)

Let's see what happens when we call the function with the tweet "Holy cow, I just made the most incredible meal!"

analyze\_tweet\_sentiment("Holy cow, I just made the most incredible meal!")

```
ToolsBetaMessage(id='msg_staging_01ApgXx7W7qsDugdaRWh6p21', content=[TextBlock(text="That's great to hear! I don't actually have the capability to assess sentiment from text, but it sounds like you're really excited and proud of the incredible meal you made. Cooking something delicious that you're proud of can definitely give a sense of accomplishment and happiness. Well done on creating such an amazing dish!", type='text')], model='claude-sonnet-4-6', role='assistant', stop_reason='end_turn', stop_sequence=None, type='message', usage=Usage(input_tokens=429, output_tokens=69))
```

Claude does not call our sentiment analysis tool:

> "That's great to hear! I don't actually have the capability to assess sentiment from text, but it sounds like you're really excited and proud of the incredible meal you made

Next, let's imagine someone tweets this: "I love my cats! I had four and just adopted 2 more! Guess how many I have now?"

analyze\_tweet\_sentiment(

"I love my cats! I had four and just adopted 2 more! Guess how many I have now?"

)

```
ToolsBetaMessage(id='msg_staging_018gTrwrx6YwBR2jjhdPooVg', content=[TextBlock(text="That's wonderful that you love your cats and adopted two more! To figure out how many cats you have now, I can use the calculator tool:", type='text'), ToolUseBlock(id='toolu_staging_01RFker5oMQoY6jErz5prmZg', input={'num1': 4, 'num2': 2}, name='calculator', type='tool_use')], model='claude-sonnet-4-6', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=442, output_tokens=101))
```

Claude wants to call the calculator tool:

> ToolUseBlock(id='toolu\_staging\_01RFker5oMQoY6jErz5prmZg', input={'num1': 4, 'num2': 2}, name='calculator', type='tool\_use')

Clearly, this current implementation is not doing what we want (mostly because we set it up to fail).

Next, let's force Claude to **always** use the `print_sentiment_scores` tool by updating `tool_choice`:

tool\_choice={"type": "tool", "name": "print\_sentiment\_scores"}

In addition to setting `type` to `tool`, we must provide a particular tool name.

def analyze\_tweet\_sentiment(query):

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

tool\_choice={"type": "tool", "name": "print\_sentiment\_scores"},

messages=[{"role": "user", "content": query}],

)

print(response)

Now if we try prompting Claude with the same prompts from earlier, it's always going to call the `print_sentiment_scores` tool:

analyze\_tweet\_sentiment("Holy cow, I just made the most incredible meal!")

```
ToolsBetaMessage(id='msg_staging_018GtYk8Xvee3w8Eeh6pbgoq', content=[ToolUseBlock(id='toolu_staging_01FMRQ9pZniZqFUGQwTcFU4N', input={'positive_score': 0.9, 'negative_score': 0.0, 'neutral_score': 0.1}, name='print_sentiment_scores', type='tool_use')], model='claude-sonnet-4-6', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=527, output_tokens=79))
```

Claude calls our `print_sentiment_scores` tool:

> ToolUseBlock(id='toolu\_staging\_01FMRQ9pZniZqFUGQwTcFU4N', input={'positive\_score': 0.9, 'negative\_score': 0.0, 'neutral\_score': 0.1}, name='print\_sentiment\_scores', type='tool\_use')

Even if we try to trip up Claude with a "Math-y" tweet, it still always calls the `print_sentiment_scores` tool:

analyze\_tweet\_sentiment(

"I love my cats! I had four and just adopted 2 more! Guess how many I have now?"

)

```
ToolsBetaMessage(id='msg_staging_01RACamfrHdpvLxWaNwDfZEF', content=[ToolUseBlock(id='toolu_staging_01Wb6ZKSwKvqVSKLDAte9cKU', input={'positive_score': 0.8, 'negative_score': 0.0, 'neutral_score': 0.2}, name='print_sentiment_scores', type='tool_use')], model='claude-sonnet-4-6', role='assistant', stop_reason='tool_use', stop_sequence=None, type='message', usage=Usage(input_tokens=540, output_tokens=79))
```

Even though we're forcing Claude to call our `print_sentiment_scores` tool, we should still employ some basic prompt engineering:

def analyze\_tweet\_sentiment(query):

prompt = f"""

Analyze the sentiment in the following tweet:

<tweet>{query}</tweet>

"""

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

tool\_choice={"type": "auto"},

messages=[{"role": "user", "content": prompt}],

)

print(response)

##  Any

The final option for `tool_choice` is `any` which allows us to tell Claude "you must call a tool, but you can pick which one". Imagine we want to create a SMS chatbot using Claude. The only way for this chatbot to actually "communicate" with a user is via SMS text message.

In the example below, we make a very simple text-messaging assistant that has access to two tools:

* `send_text_to_user` sends a text message to a user
* `get_customer_info` looks up customer data based on a username

The idea is to create a chatbot that always calls one of these tools and never responds with a non-tool response. In all situations, Claude should either respond back by trying to send a text message or calling `get_customer_info` to get more customer information.

Most importantly, we set `tool_choice` to "any":

tool\_choice={"type": "any"}

def send\_text\_to\_user(text):

# Sends a text to the user

# We'll just print out the text to keep things simple:

print(f"TEXT MESSAGE SENT: {text}")

def get\_customer\_info(username):

return {

"username": username,

"email": f"{username}@email.com",

"purchases": [

{"id": 1, "product": "computer mouse"},

{"id": 2, "product": "screen protector"},

{"id": 3, "product": "usb charging cable"},

],

}

tools = [

{

"name": "send\_text\_to\_user",

"description": "Sends a text message to a user",

"input\_schema": {

"type": "object",

"properties": {

"text": {

"type": "string",

"description": "The piece of text to be sent to the user via text message",

},

},

"required": ["text"],

},

},

{

"name": "get\_customer\_info",

"description": "gets information on a customer based on the customer's username. Response includes email, username, and previous purchases. Only call this tool once a user has provided you with their username",

"input\_schema": {

"type": "object",

"properties": {

"username": {

"type": "string",

"description": "The username of the user in question. ",

},

},

"required": ["username"],

},

},

]

system\_prompt = """

All your communication with a user is done via text message.

Only call tools when you have enough information to accurately call them.

Do not call the get\_customer\_info tool until a user has provided you with their username. This is important.

If you do not know a user's username, simply ask a user for their username.

"""

def sms\_chatbot(user\_message):

messages = [{"role": "user", "content": user\_message}]

response = client.messages.create(

system=system\_prompt,

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

tool\_choice={"type": "any"},

messages=messages,

)

if response.stop\_reason == "tool\_use":

last\_content\_block = response.content[-1]

if last\_content\_block.type == "tool\_use":

tool\_name = last\_content\_block.name

tool\_inputs = last\_content\_block.input

print(f"=======Claude Wants To Call The {tool\_name} Tool=======")

if tool\_name == "send\_text\_to\_user":

send\_text\_to\_user(tool\_inputs["text"])

elif tool\_name == "get\_customer\_info":

print(get\_customer\_info(tool\_inputs["username"]))

else:

print("Oh dear, that tool doesn't exist!")

else:

print("No tool was called. This shouldn't happen!")

Let's start simple:

sms\_chatbot("Hey there! How are you?")

```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: Hello! I'm doing well, thanks for asking. How can I assist you today?
```

Claude responds back by calling the `send_text_to_user` tool.

Next, we'll ask Claude something a bit trickier:

sms\_chatbot("I need help looking up an order")

```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: Hi there, to look up your order details I'll need your username first. Can you please provide me with your username?
```

Claude wants to send a text message, asking a user to provide their username.

Now, let's see what happens when we provide Claude with our username:

sms\_chatbot("I need help looking up an order. My username is jenny76")

```
=======Claude Wants To Call The get_customer_info Tool=======
{'username': 'jenny76', 'email': 'jenny76@email.com', 'purchases': [{'id': 1, 'product': 'computer mouse'}, {'id': 2, 'product': 'screen protector'}, {'id': 3, 'product': 'usb charging cable'}]}
```

Claude calls the `get_customer_info` tool, just as we hoped!

Even if we send Claude a gibberish message, it will still call one of our tools:

sms\_chatbot("askdj aksjdh asjkdbhas kjdhas 1+1 ajsdh")

```
=======Claude Wants To Call The send_text_to_user Tool=======
TEXT MESSAGE SENT: I'm afraid I didn't understand your query. Could you please rephrase what you need help with?
```
