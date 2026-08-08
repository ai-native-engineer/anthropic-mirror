<!-- source: https://platform.claude.com/cookbook/misc-speculative-prompt-caching -->

#  Speculative Prompt Caching

This cookbook demonstrates "Speculative Prompt Caching" - a pattern that reduces time-to-first-token (TTFT) by warming up the cache while users are still formulating their queries.

**Without Speculative Caching:**

1. User types their question (3 seconds)
2. User submits question
3. API loads context into cache AND generates response

**With Speculative Caching:**

1. User starts typing (cache warming begins immediately)
2. User continues typing (cache warming completes in background)
3. User submits question
4. API uses warm cache to generate response

##  Setup

First, let's install the required packages:



%pip install anthropic httpx --quiet



```
Note: you may need to restart the kernel to use updated packages.
```



import asyncio

import copy

import datetime

import time

import httpx

from anthropic import AsyncAnthropic

# Configuration constants

MODEL = "claude-sonnet-4-6"

SQLITE\_SOURCES = {

"btree.h": "https://sqlite.org/src/raw/18e5e7b2124c23426a283523e5f31a4bff029131b795bb82391f9d2f3136fc50?at=btree.h",

"btree.c": "https://sqlite.org/src/raw/63ca6b647342e8cef643863cd0962a542f133e1069460725ba4461dcda92b03c?at=btree.c",

}

DEFAULT\_CLIENT\_ARGS = {

"system": "You are an expert systems programmer helping analyze database internals.",

"max\_tokens": 4096,

"temperature": 0,

}

##  Helper Functions

Let's set up the functions to download our large context and prepare messages:



async def get\_sqlite\_sources() -> dict[str, str]:

print("Downloading SQLite source files...")

source\_files = {}

start\_time = time.time()

async with httpx.AsyncClient(timeout=30.0) as client:

tasks = []

async def download\_file(filename: str, url: str) -> tuple[str, str]:

response = await client.get(url, follow\_redirects=True)

response.raise\_for\_status()

print(f"Successfully downloaded {filename}")

return filename, response.text

for filename, url in SQLITE\_SOURCES.items():

tasks.append(download\_file(filename, url))

results = await asyncio.gather(\*tasks)

source\_files = dict(results)

duration = time.time() - start\_time

print(f"Downloaded {len(source\_files)} files in {duration:.2f} seconds")

return source\_files

async def create\_initial\_message():

sources = await get\_sqlite\_sources()

# Prepare the initial message with the source code as context.

# A Timestamp is included to prevent cache sharing across different runs.

initial\_message = {

"role": "user",

"content": [

{

"type": "text",

"text": f"""

Current time: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Source to Analyze:

btree.h:

```c

{sources["btree.h"]}

```

btree.c:

```c

{sources["btree.c"]}

```""",

"cache\_control": {"type": "ephemeral"},

}

],

}

return initial\_message

async def sample\_one\_token(client: AsyncAnthropic, messages: list):

"""Send a single-token request to warm up the cache"""

args = copy.deepcopy(DEFAULT\_CLIENT\_ARGS)

args["max\_tokens"] = 1

await client.messages.create(

messages=messages,

model=MODEL,

\*\*args,

)

def print\_query\_statistics(response, query\_type: str) -> None:

print(f"\n{query\_type} query statistics:")

print(f"\tInput tokens: {response.usage.input\_tokens}")

print(f"\tOutput tokens: {response.usage.output\_tokens}")

print(f"\tCache read input tokens: {getattr(response.usage, 'cache\_read\_input\_tokens', '---')}")

print(

f"\tCache creation input tokens: {getattr(response.usage, 'cache\_creation\_input\_tokens', '---')}"

)

##  Example 1: Standard Prompt Caching (Without Speculative Caching)

First, let's see how standard prompt caching works. The user types their question, then we send the entire context + question to the API:



async def standard\_prompt\_caching\_demo():

client = AsyncAnthropic()

# Prepare the large context

initial\_message = await create\_initial\_message()

# Simulate user typing time (in real app, this would be actual user input)

print("User is typing their question...")

await asyncio.sleep(3) # Simulate 3 seconds of typing

user\_question = "What is the purpose of the BtShared structure?"

print(f"User submitted: {user\_question}")

# Now send the full request (context + question)

full\_message = copy.deepcopy(initial\_message)

full\_message["content"].append(

{"type": "text", "text": f"Answer the user's question: {user\_question}"}

)

print("\nSending request to API...")

start\_time = time.time()

# Measure time to first token

first\_token\_time = None

async with client.messages.stream(

messages=[full\_message],

model=MODEL,

\*\*DEFAULT\_CLIENT\_ARGS,

) as stream:

async for text in stream.text\_stream:

if first\_token\_time is None and text.strip():

first\_token\_time = time.time() - start\_time

print(f"\n🕐 Time to first token: {first\_token\_time:.2f} seconds")

break

# Get the full response

response = await stream.get\_final\_message()

total\_time = time.time() - start\_time

print(f"Total response time: {total\_time:.2f} seconds")

print\_query\_statistics(response, "Standard Caching")

return first\_token\_time, total\_time



# Run the standard demo

standard\_ttft, standard\_total = await standard\_prompt\_caching\_demo()



```
Downloading SQLite source files...
Successfully downloaded btree.h
Successfully downloaded btree.c
Downloaded 2 files in 0.30 seconds
User is typing their question...
User submitted: What is the purpose of the BtShared structure?

Sending request to API...

🕐 Time to first token: 20.87 seconds
Total response time: 28.32 seconds

Standard Caching query statistics:
	Input tokens: 22
	Output tokens: 362
	Cache read input tokens: 0
	Cache creation input tokens: 151629
```

##  Example 2: Speculative Prompt Caching

Now let's see how speculative prompt caching improves TTFT by warming the cache while the user is typing:



async def speculative\_prompt\_caching\_demo():

client = AsyncAnthropic()

# The user has a large amount of context they want to interact with,

# in this case it's the sqlite b-tree implementation (~150k tokens).

initial\_message = await create\_initial\_message()

# Start speculative caching while user is typing

print("User is typing their question...")

print("🔥 Starting cache warming in background...")

# While the user is typing out their question, we sample a single token

# from the context the user is going to be interacting with with explicit

# prompt caching turned on to warm up the cache.

cache\_task = asyncio.create\_task(sample\_one\_token(client, [initial\_message]))

# Simulate user typing time

await asyncio.sleep(3) # Simulate 3 seconds of typing

user\_question = "What is the purpose of the BtShared structure?"

print(f"User submitted: {user\_question}")

# Ensure cache warming is complete

await cache\_task

print("✅ Cache warming completed!")

# Prepare messages for cached query. We make sure we

# reuse the same initial message as was cached to ensure we have a cache hit.

cached\_message = copy.deepcopy(initial\_message)

cached\_message["content"].append(

{"type": "text", "text": f"Answer the user's question: {user\_question}"}

)

print("\nSending request to API (with warm cache)...")

start\_time = time.time()

# Measure time to first token

first\_token\_time = None

async with client.messages.stream(

messages=[cached\_message],

model=MODEL,

\*\*DEFAULT\_CLIENT\_ARGS,

) as stream:

async for text in stream.text\_stream:

if first\_token\_time is None and text.strip():

first\_token\_time = time.time() - start\_time

print(f"\n🚀 Time to first token: {first\_token\_time:.2f} seconds")

break

# Get the full response

response = await stream.get\_final\_message()

total\_time = time.time() - start\_time

print(f"Total response time: {total\_time:.2f} seconds")

print\_query\_statistics(response, "Speculative Caching")

return first\_token\_time, total\_time



# Run the speculative caching demo

speculative\_ttft, speculative\_total = await speculative\_prompt\_caching\_demo()



```
Downloading SQLite source files...
Successfully downloaded btree.h
Successfully downloaded btree.c
Downloaded 2 files in 0.36 seconds
User is typing their question...
🔥 Starting cache warming in background...
User submitted: What is the purpose of the BtShared structure?
✅ Cache warming completed!

Sending request to API (with warm cache)...

🚀 Time to first token: 1.94 seconds
Total response time: 8.40 seconds

Speculative Caching query statistics:
	Input tokens: 22
	Output tokens: 330
	Cache read input tokens: 151629
	Cache creation input tokens: 0
```

##  Performance Comparison

Let's compare the results to see the benefit of speculative caching:



print("=" \* 60)

print("PERFORMANCE COMPARISON")

print("=" \* 60)

print("\nStandard Prompt Caching:")

print(f" Time to First Token: {standard\_ttft:.2f} seconds")

print(f" Total Response Time: {standard\_total:.2f} seconds")

print("\nSpeculative Prompt Caching:")

print(f" Time to First Token: {speculative\_ttft:.2f} seconds")

print(f" Total Response Time: {speculative\_total:.2f} seconds")

ttft\_improvement = (standard\_ttft - speculative\_ttft) / standard\_ttft \* 100

total\_improvement = (standard\_total - speculative\_total) / standard\_total \* 100

print("\n🎯 IMPROVEMENTS:")

print(

f" TTFT Improvement: {ttft\_improvement:.1f}% ({standard\_ttft - speculative\_ttft:.2f}s faster)"

)

print(

f" Total Time Improvement: {total\_improvement:.1f}% ({standard\_total - speculative\_total:.2f}s faster)"

)



```
============================================================
PERFORMANCE COMPARISON
============================================================

Standard Prompt Caching:
  Time to First Token: 20.87 seconds
  Total Response Time: 28.32 seconds

Speculative Prompt Caching:
  Time to First Token: 1.94 seconds
  Total Response Time: 8.40 seconds

🎯 IMPROVEMENTS:
  TTFT Improvement: 90.7% (18.93s faster)
  Total Time Improvement: 70.4% (19.92s faster)
```

##  Key Takeaways

1. **Speculative caching dramatically reduces TTFT** by warming the cache while users are typing
2. **The pattern is most effective** with large contexts (>1000 tokens) that are reused across queries
3. **Implementation is simple** - just send a 1-token request while the user is typing
4. **Cache warming happens in parallel** with user input, effectively "hiding" the cache creation time

##  Best Practices

* Start cache warming as early as possible (e.g., when a user focuses an input field)
* Use exactly the same context for warming and actual requests to ensure cache hits
* Monitor `cache_read_input_tokens` to verify cache hits
* Add timestamps to prevent unwanted cache sharing across sessions
