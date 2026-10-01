<!-- https://anthropic.skilljar.com/model-context-protocol-advanced-topics/295172 -->

1. Initiating sampling

On the server, during a tool call, run the `create_message()` method, passing in some messages that you wish to send to a language model.

2. Sampling callbacks

On the client, you must implement a sampling callback. It will receive a list of messages provided by the server.

3. Message formats

The list of messages provided by the server are formatted for communication in MCP. The individual messages aren't guaranteed to be compatible with whatever LLM SDK you are using.

For example, if you're using the Anthropic SDK, you'll have to write a little bit of conversion logic to turn the MCP messages into a format compatible with Anthropic's SDK.

4. Returning generated text

After generating text with the LLM, you'll return a `CreateMessageResult`, which contains the generated text.

5. Connecting the callback

Don't forget: the callback on the client needs to be passed into the `ClientSession` call.

6. Getting the result

After the client has generated and returned some text, it will be sent to the server. You can do anything with this text:

* Use it as part of a workflow in your tool
* Decide to make another sampling call
* Return the generated text

← Previous Next →

### Files

📄
.gitignore

📄
client.py

📄
pyproject.toml

📄
README.md

📄
server.py

server.py×

6

7

8

9

10

11

12

13

14

15

16

17

@mcp.tool()

async def summarize

(text\_to\_summarize: str,

ctx: Context):

prompt = f"""

Please summarize

the following

text:

{text\_to\_summarize

}

"""

result = await ctx.

session.create\_message

(

messages=[

SamplingMessag

e(

role="user

",

content=Te

xtContent

(type="tex

t",

text=promp

t)
