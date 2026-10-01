<!-- https://anthropic.skilljar.com/model-context-protocol-advanced-topics/291036 -->

1. Tool function receives Context argument

Tool functions automatically receive 'Context' as their last argument. This object has methods for logging and reporting progress to the client.

2. Create logs and progress with context

Throughout your tool function, call the `info()`, `warning()`, `debug()`, or `error()` methods to log different types of messages for the client. Also call the `report_progress()` method to estimate the amount of remaining work for the tool call.

3. Define callbacks on the client

The client needs to define logging and progress callbacks, which will automatically be called whenever the server emits log or progress messages. These callbacks should try to display the provided logging and progress data to the user.

4. Pass callbacks to appropriate functions

Make sure you provide the logging callback to the `ClientSession` and the progress callback to the `call_tool()` function.

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

1

2

3

4

5

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

from mcp.server.fastmcp

import FastMCP, Context

import asyncio

mcp = FastMCP(name="Demo

Server")

@mcp.tool()

async def add(a: int, b:

int, ctx: Context) -> int:

await ctx.info

("Preparing to add...

")

await ctx.

report\_progress(20,

100)

await asyncio.sleep(2)

await ctx.info("OK,

adding...")

await ctx.

report\_progress(80,

100)
