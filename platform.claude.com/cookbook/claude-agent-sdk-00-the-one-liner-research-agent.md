<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-00-the-one-liner-research-agent -->

#  Building a One-Liner Research Agent

Research tasks consume hours of expert time: market analysts manually gathering competitive intelligence, legal teams tracking regulatory changes, engineers investigating bug reports across documentation. The core challenge isn't finding information but knowing what to search for next based on what you just discovered.

The Claude Agent SDK makes it possible to build agents that autonomously explore external systems without a predefined workflow. Unlike traditional workflow automations that follow fixed steps, research agents adapt their strategy based on what they find--following promising leads, synthesizing conflicting sources, and knowing when they have enough information to answer the question.

##  By the end of this cookbook, you'll be able to:

* Build a research agent that autonomously searches and synthesizes information with a few lines of code

This foundation applies to any task where the information needed isn't available upfront: competitive analysis, technical troubleshooting, investment research, or literature reviews.

#  Why Research Agents?

Research is an ideal agentic use case for two reasons:

1. **Information isn't self-contained**. The input question alone doesn't contain the answer. The agent must interact with external systems (search engines, databases, APIs) to gather what it needs.
2. **The path emerges during exploration**. You can't predetermine the workflow. Whether an agent should search for company financials or regulatory filings depends on what it discovers about the business model. The optimal strategy reveals itself through investigation.

In its simplest form, a research agent searches the web and synthesizes findings. Below, we'll build exactly that with the Claude Agent SDK's built-in web search tool in just a few lines of code.

Note: You can also view the full list of [Claude Code's built-in tools(opens in new tab)](https://docs.claude.com/en/docs/claude-code/settings#tools-available-to-claude)

#  Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

* Python fundamentals - comfortable with async/await, functions, and basic data structures
* Basic understanding of agentic patterns - we recommend reading [Building effective agents(opens in new tab)](https://www.anthropic.com/engineering/building-effective-agents) first if you're new to agents

**Required Tools**

* Python 3.11 or higher
* Anthropic API key [(get one here)(opens in new tab)](https://console.anthropic.com)

**Recommended:**

* Familiarity with the Claude Agent SDK concepts
* Understanding of tool use patterns in LLMs

##  Setup

First, install the required dependencies:

%%capture

%pip install -U claude-agent-sdk python-dotenv

Note: Ensure your .env file contains:

ANTHROPIC\_API\_KEY=your\_key\_here

Load your environment variables and configure the client:

from dotenv import load\_dotenv

load\_dotenv()

MODEL = "claude-opus-4-6"

##  Building Your First Research Agent

Let's start with the simplest possible implementation: a research agent that can search the web and synthesize findings. With the Claude Agent SDK, this takes just a few lines of code.

The key is the query() function, which creates a stateless agent interaction. We'll provide Claude with a single tool, WebSearch, and let it autonomously decide when and how to use it based on our research question.

from utils.agent\_visualizer import (

display\_agent\_response,

print\_activity,

)

from claude\_agent\_sdk import ClaudeAgentOptions, query

messages = []

async for msg in query(

prompt="Research the latest trends in AI agents and give me a brief summary and relevant citiations links.",

options=ClaudeAgentOptions(model=MODEL, allowed\_tools=["WebSearch"]),

):

print\_activity(msg)

messages.append(msg)

```
🤖 Using: WebSearch()
🤖 Using: WebSearch()
🤖 Using: WebSearch()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
```

display\_agent\_response(messages)

```
<IPython.core.display.HTML object>
```

##  What's happening here:

* `query()` creates a single-turn agent interaction (no conversation memory)
* `allowed_tools=["WebSearch"]` gives Claude permission to search the web without asking for approval
* The agent autonomously decides when to search, what queries to run, and how to synthesize results

**Visualization utilities from `utils.agent_visualizer`:**

* `print_activity()` - Shows the agent's actions in real-time (tool calls, thinking)
* `display_agent_response()` - Renders the final response as a styled HTML card
* `visualize_conversation()` - Creates a timeline view of the full conversation

That's it! A functional research agent in just a few lines of code. The agent will search for relevant information, follow up on promising leads, and provide a synthesized summary with citations.

The query() function creates a stateless agent interaction. Each call is independent—no conversation memory, no context from previous queries. This makes it perfect for one-off research tasks where you need a quick answer without maintaining state.

**How tool permissions work:**

The `allowed_tools=["WebSearch"]` parameter gives Claude permission to search without asking for approval. This is critical for autonomous operation:

* `Allowed tools` - Claude can use these freely (in this case, WebSearch)
* `Other tools` - Available but require approval before use
* `Read-only tools` - Tools like Read are always allowed by default
* `Disallowed tools` - Add tools to disallowed\_tools to remove them entirely from Claude's context

**When to use stateless queries:**

* One-off research questions where context doesn't matter
* Parallel processing of independent research tasks
* Scenarios where you want fresh context for each query

**When not to use stateless queries:**

* Multi-turn investigations that build on previous findings
* Iterative refinement of research based on initial results
* Complex analysis requiring sustained context

Let's inspect what the agent actually did using the visualize\_conversation helper:

from utils.agent\_visualizer import visualize\_conversation

visualize\_conversation(messages)

```
<IPython.core.display.HTML object>
```

##  From Prototype to Production: Three Key Improvements

Our one-line research agent works, but it's limited. Single queries without memory can't handle iterative research ("find X, then analyze Y based on what you found"). Let's explore three ways we can further improve our implementation.

**1. Conversation Memory with ClaudeSDKClient**: Stateless queries can't build on previous findings. If you ask "What are the top AI startups?" then "How are they funded?", the second query has no context about which startups you mean. We can use `ClaudeSDKClient` to maintain conversation history across multiple queries.

**2. System Prompts for Specialized Behavior**: Research domains often have specific requirements. Financial analysis needs different rigor than tech news summaries. Use the system prompt to encode your research standards, preferred sources, citation format, or output structure. See our [agent prompting guide(opens in new tab)](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents/prompts) for research-specific examples.

**3. Multimodal Research with the Read Tool**: Real research isn't just text. Market reports have charts, technical docs have diagrams, competitive analysis requires screenshot comparison. Enable the `Read` tool so Claude can analyze images, PDFs, and other visual content.

Let's implement these three changes for our research agent.

from claude\_agent\_sdk import ClaudeSDKClient

# System prompt with citation requirements for research quality

RESEARCH\_SYSTEM\_PROMPT = """You are a research agent specialized in AI.

When providing research findings:

- Always include source URLs as citations

- Format citations as markdown links: [Source Title](URL)

- Group sources in a "Sources:" section at the end of your response"""

messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="research\_agent",

system\_prompt=RESEARCH\_SYSTEM\_PROMPT,

allowed\_tools=["WebSearch", "Read"],

max\_buffer\_size=10 \* 1024 \* 1024, # Increase to 10MB for image handling

)

) as research\_agent:

# First query: Analyze the chart image

await research\_agent.query("Analyze the chart in research\_agent/projects\_claude.png")

async for msg in research\_agent.receive\_response():

print\_activity(msg)

messages.append(msg)

# Second query: Use web search to validate/contextualize the chart findings

await research\_agent.query(

"Based on the chart analysis, search for recent news or data that validates or provides context for these findings. Include source URLs."

)

async for msg in research\_agent.receive\_response():

print\_activity(msg)

messages.append(msg)

```
🤖 Using: Read()
✓ Tool completed
🤖 Thinking...
🤖 Using: Glob()
✓ Tool completed
🤖 Thinking...
🤖 Using: Read()
✓ Tool completed
🤖 Thinking...
🤖 Using: WebSearch()
🤖 Using: WebSearch()
🤖 Using: WebSearch()
🤖 Using: WebSearch()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
```

###  🔧 Handling Large Responses and Buffer Limits

When working with images or large data, you may encounter buffer overflow errors:

Fatal error in message reader: Failed to decode JSON: JSON message exceeded maximum buffer size of 1048576 bytes

**Why this happens:**

* The default `max_buffer_size` is 1MB (1,048,576 bytes)
* Images are base64-encoded in messages, significantly increasing size
* The chart image (~200KB on disk) becomes ~270KB+ when base64-encoded, plus message overhead

**Solution:**
Set `max_buffer_size` in `ClaudeAgentOptions` to a higher value (e.g., 10MB) when working with images or large tool outputs.

**Best practices:**

* Set buffer size based on your use case: 10MB for typical multimodal work, higher for large document processing
* Consider if you really need to pass full images - sometimes descriptions or smaller thumbnails suffice
* Monitor for buffer errors and adjust accordingly
* Include citation requirements in your system prompt to ensure verifiable research outputs

##  What's happening here:

This example combines all three improvements: conversation memory, citation-aware system prompt, and multimodal analysis.

**Key components:**

| Component | Purpose |
| --- | --- |
| `ClaudeSDKClient` | Maintains conversation state across multiple queries |
| `RESEARCH_SYSTEM_PROMPT` | Enforces citation formatting and source URLs |
| `allowed_tools=["WebSearch", "Read"]` | Enables web search and image/document analysis |
| `max_buffer_size=10MB` | Handles base64-encoded images without overflow |

**Execution flow:**

1. **First query** - Analyzes the chart image using the `Read` tool
2. **First response loop** - Collects all messages until the agent completes
3. **Second query** - Searches the web to validate/contextualize the chart findings
4. **Context inheritance** - The second query remembers the chart analysis from the first

**Why `ClaudeSDKClient` vs `query()`:**

The `async with ClaudeSDKClient()` context manager maintains conversation state. Each `receive_response()` call builds on previous context. This differs from `query()` which creates independent, stateless sessions.

visualize\_conversation(messages)

```
<IPython.core.display.HTML object>
```

##  Building for Production

Jupyter notebooks are great for learning, but production systems need reusable modules. We've packaged the research agent into `research_agent/agent.py` with a clean interface:

###  Core functions:

* `print_activity()` - Shows what the agent is doing in real-time (imported from shared utilities)
* `get_activity_text()` - Extract activity text for custom handlers, such as logging or monitoring
* `send_query()` - Main entry point for research queries with built-in activity display

###  Built-in best practices:

The module includes the `RESEARCH_SYSTEM_PROMPT` which ensures:

* Source URLs are always included as citations
* Citations are formatted as markdown links for clean rendering
* A "Sources:" section groups all references

###  Display control:

The `send_query()` function has a `display_result` parameter (default: `True`):

* `display_result=True` - Renders a styled HTML card in Jupyter notebooks
* `display_result=False` - Returns only the text result for programmatic use

This agent can now be used in any Python script!

For independent questions where conversation context doesn't matter.

The module automatically handles:

* Activity display during execution
* Context reset for new conversations
* Styled HTML rendering of the final response

from research\_agent.agent import send\_query

# The module handles activity display, context reset, and result visualization internally

result = await send\_query("What is the Claude Code SDK? Only do one websearch and be concise")

```
🤖 Using: WebSearch()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

Now we test out a multi-turn conversation that reuses the same conversation.

Multi-turn conversations work seamlessly—just pass `continue_conversation=True`:

result1 = await send\_query("What is Anthropic? Only do one websearch and be concise")

```
🤖 Using: WebSearch()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

# Continue the conversation to dig deeper by setting continue\_conversation=True

result2 = await send\_query(

"What are some of their products?",

continue\_conversation=True,

)

```
🤖 Thinking...

<IPython.core.display.HTML object>
```

##  Conclusion

###  What You Built

In this cookbook, you built three progressively sophisticated research agents:

* Stateless research agent - One-line queries for independent research tasks
* Stateful agent with memory - Multi-turn investigations that build on previous findings
* Production module - Reusable research functions for integration into applications

###  Key Takeaways

**When to use stateless queries (query()):**

* Independent research questions
* Parallel processing of unrelated tasks
* Scenarios requiring fresh context each time

**When to use stateful agents (ClaudeSDKClient):**

* Multi-turn investigations building on previous findings
* Iterative refinement of research
* Complex analysis requiring sustained context

Research agents excel when information isn't self-contained and the optimal workflow emerges during exploration—competitive analysis, technical troubleshooting, literature reviews, and investigative journalism all fit this pattern.

###  Next Steps

This foundation in autonomous research prepares you for enterprise-grade multi-agent systems. In the next notebook, you'll learn to:

Orchestrate specialized subagents under a coordinating agent
Implement governance through hooks and custom commands
Adapt output styles for different stakeholders (executives vs. technical teams)

Next: [01\_The\_chief\_of\_staff\_agent.ipynb(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb) - From single agents to multi-agent orchestration.
