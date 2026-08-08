<!-- source: https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings -->

#  Tool Search with Embeddings: Scaling Claude to Thousands of Tools

Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical.

Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single `tool_search` tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools.

**By the end of this cookbook, you'll be able to:**

* Implement client-side tool search to scale Claude applications from dozens to thousands of tools
* Use semantic embeddings to dynamically discover relevant tools based on task context
* Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems)

This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools.

##  Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

* Python fundamentals - comfortable with functions, dictionaries, and basic data structures
* Basic understanding of Claude tool use - we recommend reading the [Tool Use Guide(opens in new tab)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) first

**Required Tools**

* Python 3.11 or higher
* Anthropic API key ([get one here(opens in new tab)](https://docs.anthropic.com/claude/reference/getting-started-with-the-api))

##  Setup

First, install the required dependencies:



# Note: we use -q to avoid printing too much to stdout

# Use --only-binary to avoid build issues with pythran

%pip install --only-binary :all: -q anthropic sentence-transformers numpy python-dotenv



```
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)

Note: you may need to restart the kernel to use updated packages.
```

Ensure your `.env` file contains:



ANTHROPIC\_API\_KEY=your\_key\_here

Load your environment variables and configure the client:



import json

import random

from datetime import datetime, timedelta

from typing import Any

import anthropic

import numpy as np

from dotenv import load\_dotenv

from sentence\_transformers import SentenceTransformer

# Load environment variables from .env file

load\_dotenv()

# Define model constant for easy updates

MODEL = "claude-sonnet-4-6"

# Initialize Claude client (API key loaded from environment)

claude\_client = anthropic.Anthropic()

# Load the SentenceTransformer model

# all-MiniLM-L6-v2 is a lightweight model with 384 dimensional embeddings

# It will be downloaded from HuggingFace on first use

print("Loading SentenceTransformer model...")

embedding\_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("✓ Clients initialized successfully")



```
Loading SentenceTransformer model...
✓ Clients initialized successfully
```

##  Define Tool Library

Before we can implement semantic search, we need tools to search through. We'll create a library of 8 tools across two categories: Weather and Finance.

In production applications, you might manage hundreds or thousands of tools across your internal APIs, database operations, or third-party integrations. The semantic search approach scales to these larger libraries without modification - we're using a small set here purely for demonstration clarity.



# Define our tool library with 2 domains

TOOL\_LIBRARY = [

# Weather Tools

{

"name": "get\_weather",

"description": "Get the current weather in a given location",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The city and state, e.g. San Francisco, CA",

},

"unit": {

"type": "string",

"enum": ["celsius", "fahrenheit"],

"description": "The unit of temperature",

},

},

"required": ["location"],

},

},

{

"name": "get\_forecast",

"description": "Get the weather forecast for multiple days ahead",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "The city and state",

},

"days": {

"type": "number",

"description": "Number of days to forecast (1-10)",

},

},

"required": ["location", "days"],

},

},

{

"name": "get\_timezone",

"description": "Get the current timezone and time for a location",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "City name or timezone identifier",

}

},

"required": ["location"],

},

},

{

"name": "get\_air\_quality",

"description": "Get current air quality index and pollutant levels for a location",

"input\_schema": {

"type": "object",

"properties": {

"location": {

"type": "string",

"description": "City name or coordinates",

}

},

"required": ["location"],

},

},

# Finance Tools

{

"name": "get\_stock\_price",

"description": "Get the current stock price and market data for a given ticker symbol",

"input\_schema": {

"type": "object",

"properties": {

"ticker": {

"type": "string",

"description": "Stock ticker symbol (e.g., AAPL, GOOGL)",

},

"include\_history": {

"type": "boolean",

"description": "Include historical data",

},

},

"required": ["ticker"],

},

},

{

"name": "convert\_currency",

"description": "Convert an amount from one currency to another using current exchange rates",

"input\_schema": {

"type": "object",

"properties": {

"amount": {

"type": "number",

"description": "Amount to convert",

},

"from\_currency": {

"type": "string",

"description": "Source currency code (e.g., USD)",

},

"to\_currency": {

"type": "string",

"description": "Target currency code (e.g., EUR)",

},

},

"required": ["amount", "from\_currency", "to\_currency"],

},

},

{

"name": "calculate\_compound\_interest",

"description": "Calculate compound interest for investments over time",

"input\_schema": {

"type": "object",

"properties": {

"principal": {

"type": "number",

"description": "Initial investment amount",

},

"rate": {

"type": "number",

"description": "Annual interest rate (as percentage)",

},

"years": {"type": "number", "description": "Number of years"},

"frequency": {

"type": "string",

"enum": ["daily", "monthly", "quarterly", "annually"],

"description": "Compounding frequency",

},

},

"required": ["principal", "rate", "years"],

},

},

{

"name": "get\_market\_news",

"description": "Get recent financial news and market updates for a specific company or sector",

"input\_schema": {

"type": "object",

"properties": {

"query": {

"type": "string",

"description": "Company name, ticker symbol, or sector",

},

"limit": {

"type": "number",

"description": "Maximum number of news articles to return",

},

},

"required": ["query"],

},

},

]

print(f"✓ Defined {len(TOOL\_LIBRARY)} tools in the library")



```
✓ Defined 8 tools in the library
```

##  Create Tool Embeddings

Semantic search works by comparing the *meaning* of text, rather than just searching for keywords. To enable this, we need to convert each tool definition into an **embedding vector** that captures its semantic meaning.

Since our tool definitions are structured JSON objects with names, descriptions, and parameters, we first convert each tool into a human-readable text representation, then generate embedding vectors using SentenceTransformer's `all-MiniLM-L6-v2` model.

We picked this model because it is:

* **Lightweight and fast** (only 384 dimensions vs 768+ for larger models)
* **Runs locally** without requiring API calls
* **Sufficient for tool search** (you can experiment with larger models for better accuracy)

Let's start by creating a function that converts tool definitions into searchable text:



def tool\_to\_text(tool: dict[str, Any]) -> str:

"""

Convert a tool definition into a text representation for embedding.

Combines the tool name, description, and parameter information.

"""

text\_parts = [

f"Tool: {tool['name']}",

f"Description: {tool['description']}",

]

# Add parameter information

if "input\_schema" in tool and "properties" in tool["input\_schema"]:

params = tool["input\_schema"]["properties"]

param\_descriptions = []

for param\_name, param\_info in params.items():

param\_desc = param\_info.get("description", "")

param\_type = param\_info.get("type", "")

param\_descriptions.append(f"{param\_name} ({param\_type}): {param\_desc}")

if param\_descriptions:

text\_parts.append("Parameters: " + ", ".join(param\_descriptions))

return "\n".join(text\_parts)

# Test with one tool

sample\_text = tool\_to\_text(TOOL\_LIBRARY[0])

print("Sample tool text representation:")

print(sample\_text)



```
Sample tool text representation:
Tool: get_weather
Description: Get the current weather in a given location
Parameters: location (string): The city and state, e.g. San Francisco, CA, unit (string): The unit of temperature
```

Now let's create embeddings for all our tools:



# Create embeddings for all tools

print("Creating embeddings for all tools...")

tool\_texts = [tool\_to\_text(tool) for tool in TOOL\_LIBRARY]

# Embed all tools at once using SentenceTransformer

# The model returns normalized embeddings by default

tool\_embeddings = embedding\_model.encode(tool\_texts, convert\_to\_numpy=True)

print(f"✓ Created embeddings with shape: {tool\_embeddings.shape}")

print(f" - {tool\_embeddings.shape[0]} tools")

print(f" - {tool\_embeddings.shape[1]} dimensions per embedding")



```
Creating embeddings for all tools...
✓ Created embeddings with shape: (8, 384)
  - 8 tools
  - 384 dimensions per embedding
```

##  Implement Tool Search

With our tools embedded as vectors, we can now implement semantic search. If two pieces of text have similar meanings, their embedding vectors will be close together in vector space. We measure this "closeness" using **cosine similarity**.

The search process:

1. **Embed the query**: Convert Claude's natural language search request into the same vector space as our tools
2. **Calculate similarity**: Compute cosine similarity between the query vector and each tool vector
3. **Rank and return**: Sort tools by similarity score and return the top N matches

With semantic search, Claude can search using natural language like "I need to check the weather" or "calculate investment returns" rather than exact tool names.

Let's implement the search function and test it with a sample query:



def search\_tools(query: str, top\_k: int = 5) -> list[dict[str, Any]]:

"""

Search for tools using semantic similarity.

Args:

query: Natural language description of what tool is needed

top\_k: Number of top tools to return

Returns:

List of tool definitions most relevant to the query

"""

# Embed the query using SentenceTransformer

query\_embedding = embedding\_model.encode(query, convert\_to\_numpy=True)

# Calculate cosine similarity using dot product

# SentenceTransformer returns normalized embeddings, so dot product = cosine similarity

similarities = np.dot(tool\_embeddings, query\_embedding)

# Get top k indices

top\_indices = np.argsort(similarities)[-top\_k:][::-1]

# Return the corresponding tools with their scores

results = []

for idx in top\_indices:

results.append({"tool": TOOL\_LIBRARY[idx], "similarity\_score": float(similarities[idx])})

return results

# Test the search function

test\_query = "I need to check the weather"

test\_results = search\_tools(test\_query, top\_k=3)

print(f"Search query: '{test\_query}'\n")

print("Top 3 matching tools:")

for i, result in enumerate(test\_results, 1):

tool\_name = result["tool"]["name"]

score = result["similarity\_score"]

print(f"{i}. {tool\_name} (similarity: {score:.3f})")



```
Search query: 'I need to check the weather'

Top 3 matching tools:
1. get_weather (similarity: 0.560)
2. get_forecast (similarity: 0.508)
3. get_air_quality (similarity: 0.401)
```

##  Define the tool\_search Tool

Now we'll implement the **meta-tool** that allows Claude to discover other tools on demand. When Claude needs a capability it doesn't have, it searches for it using this `tool_search` tool, receives the tool definitions in the result, and can use those newly discovered tools immediately.

This is the only tool we provide to Claude initially:



# The tool\_search tool definition

TOOL\_SEARCH\_DEFINITION = {

"name": "tool\_search",

"description": "Search for available tools that can help with a task. Returns tool definitions for matching tools. Use this when you need a tool but don't have it available yet.",

"input\_schema": {

"type": "object",

"properties": {

"query": {

"type": "string",

"description": "Natural language description of what kind of tool you need (e.g., 'weather information', 'currency conversion', 'stock prices')",

},

"top\_k": {

"type": "number",

"description": "Number of tools to return (default: 5)",

},

},

"required": ["query"],

},

}

print("✓ Tool search definition created")



```
✓ Tool search definition created
```

Now let's implement the handler that processes `tool_search` calls from Claude and returns discovered tools:



def handle\_tool\_search(query: str, top\_k: int = 5) -> list[dict[str, Any]]:

"""

Handle a tool\_search invocation and return tool references.

Returns a list of tool\_reference content blocks for discovered tools.

"""

# Search for relevant tools

results = search\_tools(query, top\_k=top\_k)

# Create tool\_reference objects instead of full definitions

tool\_references = [

{"type": "tool\_reference", "tool\_name": result["tool"]["name"]} for result in results

]

print(f"\n🔍 Tool search: '{query}'")

print(f" Found {len(tool\_references)} tools:")

for i, result in enumerate(results, 1):

print(f" {i}. {result['tool']['name']} (similarity: {result['similarity\_score']:.3f})")

return tool\_references

# Test the handler

test\_result = handle\_tool\_search("stock market data", top\_k=3)

print(f"\nReturned {len(test\_result)} tool references:")

for ref in test\_result:

print(f" {ref}")



```
🔍 Tool search: 'stock market data'
   Found 3 tools:
   1. get_stock_price (similarity: 0.524)
   2. get_market_news (similarity: 0.469)
   3. calculate_compound_interest (similarity: 0.244)

Returned 3 tool references:
  {'type': 'tool_reference', 'tool_name': 'get_stock_price'}
  {'type': 'tool_reference', 'tool_name': 'get_market_news'}
  {'type': 'tool_reference', 'tool_name': 'calculate_compound_interest'}
```

##  Mock Tool Execution

For this demonstration, we'll create mock responses for tool executions. In a real application, these would call actual APIs or services:



def mock\_tool\_execution(tool\_name: str, tool\_input: dict[str, Any]) -> str:

"""

Generate realistic mock responses for tool executions.

Args:

tool\_name: Name of the tool being executed

tool\_input: Input parameters for the tool

Returns:

Mock response string appropriate for the tool

"""

# Weather tools

if tool\_name == "get\_weather":

location = tool\_input.get("location", "Unknown")

unit = tool\_input.get("unit", "fahrenheit")

temp = random.randint(15, 30) if unit == "celsius" else random.randint(60, 85)

conditions = random.choice(["sunny", "partly cloudy", "cloudy", "rainy"])

return json.dumps(

{

"location": location,

"temperature": temp,

"unit": unit,

"conditions": conditions,

"humidity": random.randint(40, 80),

"wind\_speed": random.randint(5, 20),

}

)

elif tool\_name == "get\_forecast":

location = tool\_input.get("location", "Unknown")

days = int(tool\_input.get("days", 5))

forecast = []

for i in range(days):

date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")

forecast.append(

{

"date": date,

"high": random.randint(20, 30),

"low": random.randint(10, 20),

"conditions": random.choice(["sunny", "cloudy", "rainy", "partly cloudy"]),

}

)

return json.dumps({"location": location, "forecast": forecast})

elif tool\_name == "get\_timezone":

location = tool\_input.get("location", "Unknown")

return json.dumps(

{

"location": location,

"timezone": "UTC+9",

"current\_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

"utc\_offset": "+09:00",

}

)

elif tool\_name == "get\_air\_quality":

location = tool\_input.get("location", "Unknown")

aqi = random.randint(20, 150)

categories = {

(0, 50): "Good",

(51, 100): "Moderate",

(101, 150): "Unhealthy for Sensitive Groups",

}

category = next(cat for (low, high), cat in categories.items() if low <= aqi <= high)

return json.dumps(

{

"location": location,

"aqi": aqi,

"category": category,

"pollutants": {

"pm25": random.randint(5, 50),

"pm10": random.randint(10, 100),

"o3": random.randint(20, 80),

},

}

)

# Finance tools

elif tool\_name == "get\_stock\_price":

ticker = tool\_input.get("ticker", "UNKNOWN")

return json.dumps(

{

"ticker": ticker,

"price": round(random.uniform(100, 500), 2),

"change": round(random.uniform(-5, 5), 2),

"change\_percent": round(random.uniform(-2, 2), 2),

"volume": random.randint(1000000, 10000000),

"market\_cap": f"${random.randint(100, 1000)}B",

}

)

elif tool\_name == "convert\_currency":

amount = tool\_input.get("amount", 0)

from\_currency = tool\_input.get("from\_currency", "USD")

to\_currency = tool\_input.get("to\_currency", "EUR")

# Mock exchange rate

rate = random.uniform(0.8, 1.2)

converted = round(amount \* rate, 2)

return json.dumps(

{

"original\_amount": amount,

"from\_currency": from\_currency,

"to\_currency": to\_currency,

"exchange\_rate": round(rate, 4),

"converted\_amount": converted,

}

)

elif tool\_name == "calculate\_compound\_interest":

principal = tool\_input.get("principal", 0)

rate = tool\_input.get("rate", 0)

years = tool\_input.get("years", 0)

frequency = tool\_input.get("frequency", "monthly")

# Calculate compound interest

n\_map = {"daily": 365, "monthly": 12, "quarterly": 4, "annually": 1}

n = n\_map.get(frequency, 12)

final\_amount = principal \* (1 + rate / 100 / n) \*\* (n \* years)

interest\_earned = final\_amount - principal

return json.dumps(

{

"principal": principal,

"rate": rate,

"years": years,

"compounding\_frequency": frequency,

"final\_amount": round(final\_amount, 2),

"interest\_earned": round(interest\_earned, 2),

}

)

elif tool\_name == "get\_market\_news":

query = tool\_input.get("query", "")

limit = tool\_input.get("limit", 5)

news = []

for i in range(min(limit, 5)):

news.append(

{

"title": f"{query} - News Article {i + 1}",

"source": random.choice(

[

"Bloomberg",

"Reuters",

"Financial Times",

"Wall Street Journal",

]

),

"published": (datetime.now() - timedelta(hours=random.randint(1, 24))).strftime(

"%Y-%m-%d %H:%M"

),

"summary": f"Latest developments regarding {query}...",

}

)

return json.dumps({"query": query, "articles": news, "count": len(news)})

# Default fallback

else:

return json.dumps(

{

"status": "executed",

"tool": tool\_name,

"message": f"Tool {tool\_name} executed successfully with input: {json.dumps(tool\_input)}",

}

)

print("✓ Mock tool execution function created")



```
✓ Mock tool execution function created
```

##  Implement Conversation Loop

Now let's put it all together! We'll create a conversation loop that handles the complete tool search workflow.

**The conversation flow:**

1. Claude starts with only the `tool_search` tool available
2. When Claude calls `tool_search`, we run semantic search and return matching tool definitions
3. Claude can then use the discovered tools immediately
4. When Claude calls a discovered tool, we execute it (using mock responses for this demo)
5. The loop continues until Claude has a final answer



def run\_tool\_search\_conversation(user\_message: str, max\_turns: int = 5) -> None:

"""

Run a conversation with Claude using the tool search pattern.

Args:

user\_message: The initial user message

max\_turns: Maximum number of conversation turns

"""

print(f"\n{'=' \* 80}")

print(f"USER: {user\_message}")

print(f"{'=' \* 80}\n")

# Initialize conversation with only tool\_search available

messages = [{"role": "user", "content": user\_message}]

for turn in range(max\_turns):

print(f"\n--- Turn {turn + 1} ---")

# Call Claude with current message history

response = claude\_client.messages.create(

model=MODEL,

max\_tokens=1024,

tools=TOOL\_LIBRARY + [TOOL\_SEARCH\_DEFINITION],

messages=messages,

# IMPORTANT: This beta header enables tool definitions in tool results

extra\_headers={"anthropic-beta": "advanced-tool-use-2025-11-20"},

)

# Add assistant's response to messages

messages.append({"role": "assistant", "content": response.content})

# Check if we're done

if response.stop\_reason == "end\_turn":

print("\n✓ Conversation complete\n")

# Print final response

for block in response.content:

if block.type == "text":

print(f"ASSISTANT: {block.text}")

break

# Handle tool uses

if response.stop\_reason == "tool\_use":

tool\_results = []

for block in response.content:

if block.type == "text":

print(f"\nASSISTANT: {block.text}")

elif block.type == "tool\_use":

tool\_name = block.name

tool\_input = block.input

tool\_use\_id = block.id

print(f"\n🔧 Tool invocation: {tool\_name}")

print(f" Input: {json.dumps(tool\_input, indent=2)}")

if tool\_name == "tool\_search":

# Handle tool search

query = tool\_input["query"]

top\_k = tool\_input.get("top\_k", 5)

# Get tool references

tool\_references = handle\_tool\_search(query, top\_k)

# Create tool result with tool\_reference content blocks

tool\_results.append(

{

"type": "tool\_result",

"tool\_use\_id": tool\_use\_id,

"content": tool\_references,

}

)

else:

# Execute the discovered tool with mock data

mock\_result = mock\_tool\_execution(tool\_name, tool\_input)

# Print a preview of the result

if len(mock\_result) > 150:

print(f" ✅ Mock result: {mock\_result[:150]}...")

else:

print(f" ✅ Mock result: {mock\_result}")

tool\_results.append(

{

"type": "tool\_result",

"tool\_use\_id": tool\_use\_id,

"content": mock\_result,

}

)

# Add tool results to messages

if tool\_results:

messages.append({"role": "user", "content": tool\_results})

else:

print(f"\nUnexpected stop reason: {response.stop\_reason}")

break

print(f"\n{'=' \* 80}\n")

print("✓ Conversation loop implemented")



```
✓ Conversation loop implemented
```

##  Example 1: Weather Query

Let's test with a simple weather question. Claude should:

1. Call `tool_search` to find weather tools
2. Receive weather tool definitions in the result
3. Use one of the discovered tools



run\_tool\_search\_conversation("What's the weather like in Tokyo?")



```
================================================================================
USER: What's the weather like in Tokyo?
================================================================================

--- Turn 1 ---

🔧 Tool invocation: get_weather
   Input: {
  "location": "Tokyo"
}
   ✅ Mock result: {"location": "Tokyo", "temperature": 75, "unit": "fahrenheit", "conditions": "partly cloudy", "humidity": 61, "wind_speed": 9}

--- Turn 2 ---

✓ Conversation complete

ASSISTANT: The weather in Tokyo is currently:
- **Temperature:** 75°F (about 24°C)
- **Conditions:** Partly cloudy
- **Humidity:** 61%
- **Wind Speed:** 9 mph

It's a pleasant day with comfortable temperatures and some cloud cover!

================================================================================
```

##  Example 2: Finance Query

Let's try a financial calculation query that requires discovering and using finance tools:



run\_tool\_search\_conversation(

"If I invest $10,000 at 5% annual interest for 10 years with monthly compounding, how much will I have?"

)



```
================================================================================
USER: If I invest $10,000 at 5% annual interest for 10 years with monthly compounding, how much will I have?
================================================================================

--- Turn 1 ---

🔧 Tool invocation: calculate_compound_interest
   Input: {
  "principal": 10000,
  "rate": 5,
  "years": 10,
  "frequency": "monthly"
}
   ✅ Mock result: {"principal": 10000, "rate": 5, "years": 10, "compounding_frequency": "monthly", "final_amount": 16470.09, "interest_earned": 6470.09}

--- Turn 2 ---

✓ Conversation complete

ASSISTANT: If you invest $10,000 at 5% annual interest for 10 years with monthly compounding, you will have:

**Final Amount: $16,470.09**

This means you'll earn **$6,470.09** in interest over the 10-year period.

The monthly compounding means that interest is calculated and added to your principal every month, which allows your investment to grow faster than with annual compounding due to the effect of earning "interest on interest" more frequently.

================================================================================
```

##  Conclusion

In this cookbook, we implemented a client-side tool search system that enables Claude to work with large tool libraries efficiently. We covered:

* **Semantic tool discovery**: Using embeddings to match natural language queries to relevant tools, enabling Claude to find the right capability without seeing all available tools upfront
* **Dynamic tool loading**: Returning tool definitions in tool results using Claude's tool search feature, allowing Claude to discover and immediately use new tools mid-conversation
* **Context optimization**: Reducing initial context from thousands of tokens (19+ tool definitions) to just the single `tool_search` definition, cutting context usage by 90%+

###  Applying This to Your Projects

Consider tool search when:

* You have **>20 specialized tools** and context usage becomes a concern
* Your tool library **grows over time** and manual curation becomes impractical
* You need to support **domain-specific APIs** with hundreds of endpoints (database operations, internal microservices, third-party integrations)
* **Cost and latency optimization** are priorities for your application

###  Next Steps

To take this implementation further:

1. **Persist embeddings**: Cache embeddings to disk to avoid recomputing on every session, reducing startup time
2. **Improve search quality**: Experiment with different embedding models (e.g., larger models like `all-mpnet-base-v2`) or implement hybrid search combining semantic and keyword matching (BM25)
3. **Scale to larger libraries**: Test with hundreds or thousands of tools to see how the pattern performs at production scale
4. **Add tool metadata**: Include usage statistics, cost information, or reliability scores in your search ranking
5. **Implement caching**: Cache frequently used tool definitions to reduce repeated searches

###  Further Reading

* [Claude Tool Use Guide(opens in new tab)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - Comprehensive guide to building with tools
* [SentenceTransformers Documentation(opens in new tab)](https://www.sbert.net/) - Learn more about embedding models and semantic search
* [Tool Search Tool Documentation(opens in new tab)](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#tool-search) - Official documentation on the tool search pattern
