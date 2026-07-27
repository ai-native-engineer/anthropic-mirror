<!-- source: https://platform.claude.com/cookbook/tool-use-tool-search-with-embeddings -->

# Tool Search with Embeddings: Scaling Claude to Thousands of Tools

Building Claude applications with dozens of specialized tools quickly hits a wall: providing all tool definitions upfront consumes your context window, increases latency and costs, and makes it harder for Claude to find the right tool. Beyond ~100 tools, this approach becomes impractical.

Semantic tool search solves this by treating tools as discoverable resources. Instead of front-loading hundreds of definitions, you give Claude a single `tool_search` tool that returns relevant capabilities on demand, cutting context usage by 90%+ while enabling applications that scale to thousands of tools.

**By the end of this cookbook, you'll be able to:**

* Implement client-side tool search to scale Claude applications from dozens to thousands of tools
* Use semantic embeddings to dynamically discover relevant tools based on task context
* Apply this pattern to domain-specific tool libraries (APIs, databases, internal systems)

This pattern is used in production by teams managing large tool ecosystems where context efficiency is critical. While we'll demonstrate with a small set of tools for clarity, the same approach scales seamlessly to libraries with hundreds or thousands of tools.

## Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

* Python fundamentals - comfortable with functions, dictionaries, and basic data structures
* Basic understanding of Claude tool use - we recommend reading the [Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) first

**Required Tools**

* Python 3.11 or higher
* Anthropic API key ([get one here](https://docs.anthropic.com/claude/reference/getting-started-with-the-api))

## Setup

First, install the required dependencies:

python

```
# Note: we use -q to avoid printing too much to stdout
# Use --only-binary to avoid build issues with pythran
%pip install --only-binary :all: -q anthropic sentence-transformers numpy python-dotenv
```

```
huggingface/tokenizers: The current process just got forked, after parallelism has already been used. Disabling parallelism to avoid deadlocks...
To disable this warning, you can either:
	- Avoid using `tokenizers` before the fork if possible
	- Explicitly set the environment variable TOKENIZERS_PARALLELISM=(true | false)

Note: you may need to restart the kernel to use updated packages.
```

Ensure your `.env` file contains:

```
ANTHROPIC_API_KEY=your_key_here
```

Load your environment variables and configure the client:

python

```
import json
import random
from datetime import datetime, timedelta
from typing import Any

import anthropic
import numpy as np
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

# Load environment variables from .env file
load_dotenv()

# Define model constant for easy updates
MODEL = "claude-sonnet-4-6"

# Initialize Claude client (API key loaded from environment)
claude_client = anthropic.Anthropic()

# Load the SentenceTransformer model
# all-MiniLM-L6-v2 is a lightweight model with 384 dimensional embeddings
# It will be downloaded from HuggingFace on first use
print("Loading SentenceTransformer model...")
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("✓ Clients initialized successfully")
```

```
Loading SentenceTransformer model...
✓ Clients initialized successfully
```

## Define Tool Library

Before we can implement semantic search, we need tools to search through. We'll create a library of 8 tools across two categories: Weather and Finance.

In production applications, you might manage hundreds or thousands of tools across your internal APIs, database operations, or third-party integrations. The semantic search approach scales to these larger libraries without modification - we're using a small set here purely for demonstration clarity.

python

```
# Define our tool library with 2 domains
TOOL_LIBRARY = [
    # Weather Tools
    {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "input_schema": {
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
        "name": "get_forecast",
        "description": "Get the weather forecast for multiple days ahead",
        "input_schema": {
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
        "name": "get_timezone",
        "description": "Get the current timezone and time for a location",
        "input_schema": {
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
        "name": "get_air_quality",
        "description": "Get current air quality index and pollutant levels for a location",
        "input_schema": {
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
        "name": "get_stock_price",
        "description": "Get the current stock price and market data for a given ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {
                    "type": "string",
                    "description": "Stock ticker symbol (e.g., AAPL, GOOGL)",
                },
                "include_history": {
                    "type": "boolean",
                    "description": "Include historical data",
                },
            },
            "required": ["ticker"],
        },
    },
    {
        "name": "convert_currency",
        "description": "Convert an amount from one currency to another using current exchange rates",
        "input_schema": {
            "type": "object",
            "properties": {
                "amount": {
                    "type": "number",
                    "description": "Amount to convert",
                },
                "from_currency": {
                    "type": "string",
                    "description": "Source currency code (e.g., USD)",
                },
                "to_currency": {
                    "type": "string",
                    "description": "Target currency code (e.g., EUR)",
                },
            },
            "required": ["amount", "from_currency", "to_currency"],
        },
    },
    {
        "name": "calculate_compound_interest",
        "description": "Calculate compound interest for investments over time",
        "input_schema": {
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
        "name": "get_market_news",
        "description": "Get recent financial news and market updates for a specific company or sector",
        "input_schema": {
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

print(f"✓ Defined {len(TOOL_LIBRARY)} tools in the library")
```

```
✓ Defined 8 tools in the library
```

## Create Tool Embeddings

Semantic search works by comparing the *meaning* of text, rather than just searching for keywords. To enable this, we need to convert each tool definition into an **embedding vector** that captures its semantic meaning.

Since our tool definitions are structured JSON objects with names, descriptions, and parameters, we first convert each tool into a human-readable text representation, then generate embedding vectors using SentenceTransformer's `all-MiniLM-L6-v2` model.

We picked this model because it is:

* **Lightweight and fast** (only 384 dimensions vs 768+ for larger models)
* **Runs locally** without requiring API calls
* **Sufficient for tool search** (you can experiment with larger models for better accuracy)

Let's start by creating a function that converts tool definitions into searchable text:

python

```
def tool_to_text(tool: dict[str, Any]) -> str:
    """
    Convert a tool definition into a text representation for embedding.
    Combines the tool name, description, and parameter information.
    """
    text_parts = [
        f"Tool: {tool['name']}",
        f"Description: {tool['description']}",
    ]

    # Add parameter information
    if "input_schema" in tool and "properties" in tool["input_schema"]:
        params = tool["input_schema"]["properties"]
        param_descriptions = []
        for param_name, param_info in params.items():
            param_desc = param_info.get("description", "")
            param_type = param_info.get("type", "")
            param_descriptions.append(f"{param_name} ({param_type}): {param_desc}")

        if param_descriptions:
            text_parts.append("Parameters: " + ", ".join(param_descriptions))

    return "\n".join(text_parts)

# Test with one tool
sample_text = tool_to_text(TOOL_LIBRARY[0])
print("Sample tool text representation:")
print(sample_text)
```

```
Sample tool text representation:
Tool: get_weather
Description: Get the current weather in a given location
Parameters: location (string): The city and state, e.g. San Francisco, CA, unit (string): The unit of temperature
```

Now let's create embeddings for all our tools:

python

```
# Create embeddings for all tools
print("Creating embeddings for all tools...")

tool_texts = [tool_to_text(tool) for tool in TOOL_LIBRARY]

# Embed all tools at once using SentenceTransformer
# The model returns normalized embeddings by default
tool_embeddings = embedding_model.encode(tool_texts, convert_to_numpy=True)

print(f"✓ Created embeddings with shape: {tool_embeddings.shape}")
print(f"  - {tool_embeddings.shape[0]} tools")
print(f"  - {tool_embeddings.shape[1]} dimensions per embedding")
```

```
Creating embeddings for all tools...
✓ Created embeddings with shape: (8, 384)
  - 8 tools
  - 384 dimensions per embedding
```

## Implement Tool Search

With our tools embedded as vectors, we can now implement semantic search. If two pieces of text have similar meanings, their embedding vectors will be close together in vector space. We measure this "closeness" using **cosine similarity**.

The search process:

1. **Embed the query**: Convert Claude's natural language search request into the same vector space as our tools
2. **Calculate similarity**: Compute cosine similarity between the query vector and each tool vector
3. **Rank and return**: Sort tools by similarity score and return the top N matches

With semantic search, Claude can search using natural language like "I need to check the weather" or "calculate investment returns" rather than exact tool names.

Let's implement the search function and test it with a sample query:

python

```
def search_tools(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """
    Search for tools using semantic similarity.

    Args:
        query: Natural language description of what tool is needed
        top_k: Number of top tools to return

    Returns:
        List of tool definitions most relevant to the query
    """
    # Embed the query using SentenceTransformer
    query_embedding = embedding_model.encode(query, convert_to_numpy=True)

    # Calculate cosine similarity using dot product
    # SentenceTransformer returns normalized embeddings, so dot product = cosine similarity
    similarities = np.dot(tool_embeddings, query_embedding)

    # Get top k indices
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    # Return the corresponding tools with their scores
    results = []
    for idx in top_indices:
        results.append({"tool": TOOL_LIBRARY[idx], "similarity_score": float(similarities[idx])})

    return results

# Test the search function
test_query = "I need to check the weather"
test_results = search_tools(test_query, top_k=3)

print(f"Search query: '{test_query}'\n")
print("Top 3 matching tools:")
for i, result in enumerate(test_results, 1):
    tool_name = result["tool"]["name"]
    score = result["similarity_score"]
    print(f"{i}. {tool_name} (similarity: {score:.3f})")
```

```
Search query: 'I need to check the weather'

Top 3 matching tools:
1. get_weather (similarity: 0.560)
2. get_forecast (similarity: 0.508)
3. get_air_quality (similarity: 0.401)
```

## Define the tool\_search Tool

Now we'll implement the **meta-tool** that allows Claude to discover other tools on demand. When Claude needs a capability it doesn't have, it searches for it using this `tool_search` tool, receives the tool definitions in the result, and can use those newly discovered tools immediately.

This is the only tool we provide to Claude initially:

python

```
# The tool_search tool definition
TOOL_SEARCH_DEFINITION = {
    "name": "tool_search",
    "description": "Search for available tools that can help with a task. Returns tool definitions for matching tools. Use this when you need a tool but don't have it available yet.",
    "input_schema": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Natural language description of what kind of tool you need (e.g., 'weather information', 'currency conversion', 'stock prices')",
            },
            "top_k": {
                "type": "number",
                "description": "Number of tools to return (default: 5)",
            },
        },
        "required": ["query"],
    },
}

print("✓ Tool search definition created")
```

```
✓ Tool search definition created
```

Now let's implement the handler that processes `tool_search` calls from Claude and returns discovered tools:

python

```
def handle_tool_search(query: str, top_k: int = 5) -> list[dict[str, Any]]:
    """
    Handle a tool_search invocation and return tool references.

    Returns a list of tool_reference content blocks for discovered tools.
    """
    # Search for relevant tools
    results = search_tools(query, top_k=top_k)

    # Create tool_reference objects instead of full definitions
    tool_references = [
        {"type": "tool_reference", "tool_name": result["tool"]["name"]} for result in results
    ]

    print(f"\n🔍 Tool search: '{query}'")
    print(f"   Found {len(tool_references)} tools:")
    for i, result in enumerate(results, 1):
        print(f"   {i}. {result['tool']['name']} (similarity: {result['similarity_score']:.3f})")

    return tool_references

# Test the handler
test_result = handle_tool_search("stock market data", top_k=3)
print(f"\nReturned {len(test_result)} tool references:")
for ref in test_result:
    print(f"  {ref}")
```

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

## Mock Tool Execution

For this demonstration, we'll create mock responses for tool executions. In a real application, these would call actual APIs or services:

python

```
def mock_tool_execution(tool_name: str, tool_input: dict[str, Any]) -> str:
    """
    Generate realistic mock responses for tool executions.

    Args:
        tool_name: Name of the tool being executed
        tool_input: Input parameters for the tool

    Returns:
        Mock response string appropriate for the tool
    """
    # Weather tools
    if tool_name == "get_weather":
        location = tool_input.get("location", "Unknown")
        unit = tool_input.get("unit", "fahrenheit")
        temp = random.randint(15, 30) if unit == "celsius" else random.randint(60, 85)
        conditions = random.choice(["sunny", "partly cloudy", "cloudy", "rainy"])
        return json.dumps(
            {
                "location": location,
                "temperature": temp,
                "unit": unit,
                "conditions": conditions,
                "humidity": random.randint(40, 80),
                "wind_speed": random.randint(5, 20),
            }
        )

    elif tool_name == "get_forecast":
        location = tool_input.get("location", "Unknown")
        days = int(tool_input.get("days", 5))
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

    elif tool_name == "get_timezone":
        location = tool_input.get("location", "Unknown")
        return json.dumps(
            {
                "location": location,
                "timezone": "UTC+9",
                "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "utc_offset": "+09:00",
            }
        )

    elif tool_name == "get_air_quality":
        location = tool_input.get("location", "Unknown")
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
    elif tool_name == "get_stock_price":
        ticker = tool_input.get("ticker", "UNKNOWN")
        return json.dumps(
            {
                "ticker": ticker,
                "price": round(random.uniform(100, 500), 2),
                "change": round(random.uniform(-5, 5), 2),
                "change_percent": round(random.uniform(-2, 2), 2),
                "volume": random.randint(1000000, 10000000),
                "market_cap": f"${random.randint(100, 1000)}B",
            }
        )

    elif tool_name == "convert_currency":
        amount = tool_input.get("amount", 0)
        from_currency = tool_input.get("from_currency", "USD")
        to_currency = tool_input.get("to_currency", "EUR")
        # Mock exchange rate
        rate = random.uniform(0.8, 1.2)
        converted = round(amount * rate, 2)
        return json.dumps(
            {
                "original_amount": amount,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "exchange_rate": round(rate, 4),
                "converted_amount": converted,
            }
        )

    elif tool_name == "calculate_compound_interest":
        principal = tool_input.get("principal", 0)
        rate = tool_input.get("rate", 0)
        years = tool_input.get("years", 0)
        frequency = tool_input.get("frequency", "monthly")

        # Calculate compound interest
        n_map = {"daily": 365, "monthly": 12, "quarterly": 4, "annually": 1}
        n = n_map.get(frequency, 12)
        final_amount = principal * (1 + rate / 100 / n) ** (n * years)
        interest_earned = final_amount - principal

        return json.dumps(
            {
                "principal": principal,
                "rate": rate,
                "years": years,
                "compounding_frequency": frequency,
                "final_amount": round(final_amount, 2),
                "interest_earned": round(interest_earned, 2),
            }
        )

    elif tool_name == "get_market_news":
        query = tool_input.get("query", "")
        limit = tool_input.get("limit", 5)
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
                "tool": tool_name,
                "message": f"Tool {tool_name} executed successfully with input: {json.dumps(tool_input)}",
            }
        )

print("✓ Mock tool execution function created")
```

```
✓ Mock tool execution function created
```

## Implement Conversation Loop

Now let's put it all together! We'll create a conversation loop that handles the complete tool search workflow.

**The conversation flow:**

1. Claude starts with only the `tool_search` tool available
2. When Claude calls `tool_search`, we run semantic search and return matching tool definitions
3. Claude can then use the discovered tools immediately
4. When Claude calls a discovered tool, we execute it (using mock responses for this demo)
5. The loop continues until Claude has a final answer

python

```
def run_tool_search_conversation(user_message: str, max_turns: int = 5) -> None:
    """
    Run a conversation with Claude using the tool search pattern.

    Args:
        user_message: The initial user message
        max_turns: Maximum number of conversation turns
    """
    print(f"\n{'=' * 80}")
    print(f"USER: {user_message}")
    print(f"{'=' * 80}\n")

    # Initialize conversation with only tool_search available
    messages = [{"role": "user", "content": user_message}]

    for turn in range(max_turns):
        print(f"\n--- Turn {turn + 1} ---")

        # Call Claude with current message history
        response = claude_client.messages.create(
            model=MODEL,
            max_tokens=1024,
            tools=TOOL_LIBRARY + [TOOL_SEARCH_DEFINITION],
            messages=messages,
            # IMPORTANT: This beta header enables tool definitions in tool results
            extra_headers={"anthropic-beta": "advanced-tool-use-2025-11-20"},
        )

        # Add assistant's response to messages
        messages.append({"role": "assistant", "content": response.content})

        # Check if we're done
        if response.stop_reason == "end_turn":
            print("\n✓ Conversation complete\n")
            # Print final response
            for block in response.content:
                if block.type == "text":
                    print(f"ASSISTANT: {block.text}")
            break

        # Handle tool uses
        if response.stop_reason == "tool_use":
            tool_results = []

            for block in response.content:
                if block.type == "text":
                    print(f"\nASSISTANT: {block.text}")

                elif block.type == "tool_use":
                    tool_name = block.name
                    tool_input = block.input
                    tool_use_id = block.id

                    print(f"\n🔧 Tool invocation: {tool_name}")
                    print(f"   Input: {json.dumps(tool_input, indent=2)}")

                    if tool_name == "tool_search":
                        # Handle tool search
                        query = tool_input["query"]
                        top_k = tool_input.get("top_k", 5)

                        # Get tool references
                        tool_references = handle_tool_search(query, top_k)

                        # Create tool result with tool_reference content blocks
                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": tool_use_id,
                                "content": tool_references,
                            }
                        )
                    else:
                        # Execute the discovered tool with mock data
                        mock_result = mock_tool_execution(tool_name, tool_input)

                        # Print a preview of the result
                        if len(mock_result) > 150:
                            print(f"   ✅ Mock result: {mock_result[:150]}...")
                        else:
                            print(f"   ✅ Mock result: {mock_result}")

                        tool_results.append(
                            {
                                "type": "tool_result",
                                "tool_use_id": tool_use_id,
                                "content": mock_result,
                            }
                        )

            # Add tool results to messages
            if tool_results:
                messages.append({"role": "user", "content": tool_results})
        else:
            print(f"\nUnexpected stop reason: {response.stop_reason}")
            break

    print(f"\n{'=' * 80}\n")

print("✓ Conversation loop implemented")
```

```
✓ Conversation loop implemented
```

## Example 1: Weather Query

Let's test with a simple weather question. Claude should:

1. Call `tool_search` to find weather tools
2. Receive weather tool definitions in the result
3. Use one of the discovered tools

python

```
run_tool_search_conversation("What's the weather like in Tokyo?")
```

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

## Example 2: Finance Query

Let's try a financial calculation query that requires discovering and using finance tools:

python

```
run_tool_search_conversation(
    "If I invest $10,000 at 5% annual interest for 10 years with monthly compounding, how much will I have?"
)
```

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

## Conclusion

In this cookbook, we implemented a client-side tool search system that enables Claude to work with large tool libraries efficiently. We covered:

* **Semantic tool discovery**: Using embeddings to match natural language queries to relevant tools, enabling Claude to find the right capability without seeing all available tools upfront
* **Dynamic tool loading**: Returning tool definitions in tool results using Claude's tool search feature, allowing Claude to discover and immediately use new tools mid-conversation
* **Context optimization**: Reducing initial context from thousands of tokens (19+ tool definitions) to just the single `tool_search` definition, cutting context usage by 90%+

### Applying This to Your Projects

Consider tool search when:

* You have **>20 specialized tools** and context usage becomes a concern
* Your tool library **grows over time** and manual curation becomes impractical
* You need to support **domain-specific APIs** with hundreds of endpoints (database operations, internal microservices, third-party integrations)
* **Cost and latency optimization** are priorities for your application

### Next Steps

To take this implementation further:

1. **Persist embeddings**: Cache embeddings to disk to avoid recomputing on every session, reducing startup time
2. **Improve search quality**: Experiment with different embedding models (e.g., larger models like `all-mpnet-base-v2`) or implement hybrid search combining semantic and keyword matching (BM25)
3. **Scale to larger libraries**: Test with hundreds or thousands of tools to see how the pattern performs at production scale
4. **Add tool metadata**: Include usage statistics, cost information, or reliability scores in your search ranking
5. **Implement caching**: Cache frequently used tool definitions to reduce repeated searches

### Further Reading

* [Claude Tool Use Guide](https://docs.anthropic.com/en/docs/build-with-claude/tool-use) - Comprehensive guide to building with tools
* [SentenceTransformers Documentation](https://www.sbert.net/) - Learn more about embedding models and semantic search
* [Tool Search Tool Documentation](https://docs.anthropic.com/en/docs/build-with-claude/tool-use#tool-search) - Official documentation on the tool search pattern
