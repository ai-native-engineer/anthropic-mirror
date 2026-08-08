<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-01-the-chief-of-staff-agent -->



from dotenv import load\_dotenv

from utils.agent\_visualizer import (

display\_agent\_response,

print\_activity,

reset\_activity\_context,

visualize\_conversation,

)

from claude\_agent\_sdk import ClaudeAgentOptions, ClaudeSDKClient

load\_dotenv()

# Define the model to use throughout this notebook

# Using Opus 4.6 for its superior planning and reasoning capabilities

MODEL = "claude-opus-4-6"

print(f"📋 Notebook configured to use: {MODEL}")



```
📋 Notebook configured to use: claude-opus-4-6
```

#  01 - The Chief of Staff Agent

####  Introduction

In notebook 00, we built a simple research agent. In this notebook, we'll incrementally introduce key Claude Code SDK features for building comprehensive agents. For each introduced feature, we'll explain:

* **What**: what the feature is
* **Why**: what the feature can do and why you would want to use it
* **How**: a minimal implementation showing how to use it

If you are familiar with Claude Code, you'll notice how the SDK brings feature parity and enables you to leverage all of Claude Code's capabilities in a programmatic headless manner.

####  Scenario

Throughout this notebook, we'll build an **AI Chief of Staff** for a 50-person startup that just raised $10M Series A. The CEO needs data-driven insights to balance aggressive growth with financial sustainability.

Our final Chief of Staff agent will:

* **Coordinate specialized subagents** for different domains
* **Aggregate insights** from multiple sources
* **Provide executive summaries** with actionable recommendations

##  Basic Features

###  Feature 0: Memory with [CLAUDE.md(opens in new tab)](https://www.anthropic.com/engineering/claude-code-best-practices)

**What**: `CLAUDE.md` files serve as persistent memory and instructions for your agent. When present in the project directory, Claude Code automatically reads and incorporates this context when you initialize your agent.

**Why**: Instead of repeatedly providing project context, team preferences, or standards in each interaction, you can define them once in `CLAUDE.md`. This ensures consistent behavior and reduces token usage by avoiding redundant explanations.

**How**:

* Have a `CLAUDE.md` file in the working directory - in our example: `chief_of_staff_agent/CLAUDE.md`
* Set the `cwd` argument of your ClaudeSDKClient to point to directory of your CLAUDE.md file
* Use explicit prompts to guide the agent when you want it to prefer high-level context over detailed data files

**Important Behavior Note**: When both CLAUDE.md and detailed data files (like CSVs) are available, the agent may prefer to read the more granular data sources to provide precise answers. This is expected behavior - agents naturally seek authoritative data. To ensure the agent uses high-level CLAUDE.md context, use explicit prompt instructions (see example below). This teaches an important lesson: CLAUDE.md provides *context and guidance*, not hard constraints on data sources.



messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="chief\_of\_staff\_agent", # Points to subdirectory with our CLAUDE.md

setting\_sources=["project"],

)

) as agent:

await agent.query("What's our current runway?")

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)

# Display the response with HTML rendering

display\_agent\_response(messages)

# With this prompt, the agent should use CLAUDE.md values: ~$500K burn, 20 months runway



```
🤖 Thinking...

<IPython.core.display.HTML object>
```

####  Understanding Agent Data Source Preferences

**What Just Happened:**
By adding to our prompt, we guided the agent to rely on the CLAUDE.md context rather than seeking more granular data from CSV files.

**Key Insights:**

1. **CLAUDE.md as Context, Not Constraint**: When you set `cwd`, the CLAUDE.md file is loaded as background context. However, agents will naturally seek the most authoritative data sources available. If detailed CSV files exist, the agent may prefer them for precision.
2. **Prompt Engineering Matters**: The phrasing "high-level financial numbers from context" signals to the agent that you want the simplified executive summary from CLAUDE.md (500Kburn,20monthsrunway)ratherthantheprecisemonth−by−monthdatafromfinancialdata/burnrate.csv(500K burn, 20 months runway) rather than the precise month-by-month data from financial\_data/burn\_rate.csv (500Kburn,20monthsrunway)ratherthantheprecisemonth−by−monthdatafromfinanciald​ata/burnr​ate.csv(525K gross, $235K net burn).
3. **Architectural Design Choice**: This behavior is actually desirable in production systems - you want agents to find the best data source. CLAUDE.md should contain:

   * High-level context and strategy
   * Company information and standards
   * Pointers to where detailed data lives
   * Guidelines on when to use high-level vs. detailed numbers
4. **Real-World Pattern**: Think of CLAUDE.md as an "onboarding document" that orients the agent, while detailed files are "source systems" the agent can query when precision matters.

###  Feature 1: The Bash tool for Python Script Execution

**What**: The Bash tool allows your agent to (among other things) run Python scripts directly, enabling access to procedural knowledge, complex computations, data analysis and other integrations that go beyond the agent's native capabilities.

**Why**: Our Chief of Staff might need to process data files, run financial models or generate visualizations based on this data. These are all good scenarios for using the Bash tool.

**How**: Have your Python scripts set-up in a place where your agent can reach them and add some context on what they are and how they can be called. If the scripts are meant for your chief of staff agent, add this context to its CLAUDE.md file and if they are meant for one your subagents, add said context to their MD files (more details on this later). For this tutorial, we added five toy examples to `chief_of_staff_agent/scripts`:

1. `hiring_impact.py`: Calculates how new engineering hires affect burn rate, runway, and cash position. Essential for the `financial-analyst` subagent to model hiring scenarios against the $500K monthly burn and 20-month runway.
2. `talent_scorer.py`: Scores candidates on technical skills, experience, culture fit, and salary expectations using weighted criteria. Core tool for the `recruiter` subagent to rank engineering candidates against TechStart's $180-220K senior engineer benchmarks.
3. `simple_calculation.py`: Performs quick financial calculations for runway, burn rate, and quarterly metrics. Utility script for chief of staff to get instant metrics without complex modeling.
4. `financial_forecast.py`: Models ARR growth scenarios (base/optimistic/pessimistic) given the current 2.4MARRgrowingat152.4M ARR growing at 15% MoM.Critical for `financial-analyst` to project Series B readiness and validate the 2.4MARRgrowingat1530M fundraising target.
5. `decision_matrix.py`: Creates weighted decision matrices for strategic choices like the SmartDev acquisition or office expansion. Helps chief of staff systematically evaluate complex decisions with multiple stakeholders and criteria.



messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

allowed\_tools=["Bash", "Read"],

cwd="chief\_of\_staff\_agent", # Points to subdirectory where our agent is defined

)

) as agent:

await agent.query(

"Use your simple calculation script with a total runway of 2904829 and a monthly burn of 121938."

)

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)

# Display the response with HTML rendering

display\_agent\_response(messages)



```
🤖 Using: Glob()
🤖 Using: Glob()
🤖 Using: Glob()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: Read()
✓ Tool completed
🤖 Thinking...
🤖 Using: Bash()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

###  Feature 2: Output Styles

**What**: Output styles allow you to use different output styles for different audiences. Each style is defined in a markdown file.

**Why**: Your agent might be used by people of different levels of expertise or they might have different priorities. Your output style can help differentiate between these segments without having to create a separate agent.

**How**:

* Configure a markdown file per style in `chief_of_staff_agent/.claude/output-styles/`. For example, check out the Executive Ouput style in `.claude/output-styles/executive.md`. Output styles are defined with a simple frontmatter including two fields: name and description. Note: Make sure the name in the frontmatter matches exactly the file's name (case sensitive)

> **IMPORTANT**: Output styles modify the system prompt that Claude Code has underneath, leaving out the parts focused on software engineering and giving you more control for your specific use case beyond software engineering work.

> **SDK CONFIGURATION NOTE**: Similar to slash commands (covered in Feature 4), output styles are stored on the filesystem in `.claude/output-styles/`. For the SDK to load these files, you **must** include `setting_sources=["project"]` in your `ClaudeAgentOptions`. The `settings` parameter tells the SDK *which* style to use, but `setting_sources` is required to actually *load* the style definitions. This requirement was identified while debugging later sections and applies to all filesystem-based settings.



messages\_executive = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="chief\_of\_staff\_agent",

settings='{"outputStyle": "executive"}',

# IMPORTANT: setting\_sources must include "project" to load output styles from .claude/output-styles/

# Without this, the SDK does NOT load filesystem settings (output styles, slash commands, etc.)

setting\_sources=["project"],

)

) as agent:

await agent.query("Tell me in two sentences about your writing output style.")

async for msg in agent.receive\_response():

print\_activity(msg)

messages\_executive.append(msg)

messages\_technical = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="chief\_of\_staff\_agent",

settings='{"outputStyle": "technical"}',

setting\_sources=["project"],

)

) as agent:

await agent.query("Tell me in two sentences about your writing output style.")

async for msg in agent.receive\_response():

print\_activity(msg)

messages\_technical.append(msg)



```
🤖 Thinking...
🤖 Thinking...
```



# Display executive style response

display\_agent\_response(messages\_executive)



```
<IPython.core.display.HTML object>
```



# Technical output style - detailed, implementation-focused

display\_agent\_response(messages\_technical, title="Technical Style")



```
<IPython.core.display.HTML object>
```

###  Feature 3: Plan Mode - Strategic Planning Without Execution

**What**: Plan mode instructs the agent to create a detailed execution plan without performing any actions. The agent analyzes requirements, proposes solutions, and outlines steps, but doesn't modify files, execute commands, or make changes.

**Why**: Complex tasks benefit from upfront planning to reduce errors, enable review and improve coordination. After the planning phase, the agent will have a red thread to follow throughout its execution.

**How**: Just set `permission_mode="plan"`

**Plan Persistence**: Since plans are valuable artifacts for review and decision-making, we'll demonstrate how to capture and save them to persistent markdown files. This enables stakeholders to review plans before approving execution.

> Note: this feature shines in Claude Code but still needs to be fully adapted for headless applications with the SDK. Namely, the agent will try calling its `ExitPlanMode()` tool, which is only relevant in the interactive mode. In this case, you can send up a follow-up query with `continue_conversation=True` for the agent to execute its plan in context.



# =============================================================================

# Plan Mode Helper Functions

# =============================================================================

# These utilities handle the various ways an agent might output its plan.

# Since agents can output plans via direct text, Write tool, or Claude's

# internal plan directory, we need robust extraction from multiple sources.

import glob as glob\_module

import os

import re

from datetime import datetime

from pathlib import Path

from typing import Any

def extract\_plan\_from\_xml(text: str | None, min\_length: int = 200) -> str | None:

"""

Extract content between <plan> tags from text.

Args:

text: The text to search for plan content

min\_length: Minimum character count for valid plan (prevents empty matches)

Returns:

Extracted plan content, or None if not found/too short

"""

if not text:

return None

match = re.search(r"<plan>(.\*?)</plan>", text, re.DOTALL)

if match:

extracted = match.group(1).strip()

if len(extracted) > min\_length:

return extracted

return None

def extract\_plan\_from\_messages(

plan\_content: list[str], min\_fallback\_length: int = 500

) -> tuple[str | None, str | None]:

"""

Try to extract plan from captured message stream content.

Args:

plan\_content: List of text blocks captured during streaming

min\_fallback\_length: Minimum length for fallback (no XML tags)

Returns:

Tuple of (plan\_text, source\_description)

"""

combined\_text = "\n\n".join(plan\_content)

# First try: XML tags

plan = extract\_plan\_from\_xml(combined\_text)

if plan:

return plan, "message stream"

# Fallback: Use raw content if substantial

if len(combined\_text.strip()) > min\_fallback\_length:

return combined\_text.strip(), "full message content (fallback)"

return None, None

def extract\_plan\_from\_write\_tool(

write\_contents: list[str], min\_fallback\_length: int = 500

) -> tuple[str | None, str | None]:

"""

Try to extract plan from captured Write tool calls.

Args:

write\_contents: List of content strings from Write tool calls

min\_fallback\_length: Minimum length for fallback (no XML tags)

Returns:

Tuple of (plan\_text, source\_description)

"""

for content in write\_contents:

# Try XML extraction first

plan = extract\_plan\_from\_xml(content)

if plan:

return plan, "Write tool capture"

# Fallback: substantial content without tags

if content and len(content.strip()) > min\_fallback\_length:

return content.strip(), "Write tool capture (no XML tags)"

return None, None

def extract\_plan\_from\_claude\_dir(

max\_age\_seconds: int = 300, min\_fallback\_length: int = 500

) -> tuple[str | None, str | None]:

"""

Check Claude's internal plan directory for recently created plans.

Args:

max\_age\_seconds: Maximum age of plan file to consider (default: 5 minutes)

min\_fallback\_length: Minimum length for fallback (no XML tags)

Returns:

Tuple of (plan\_text, source\_description)

"""

claude\_plans\_dir = os.path.expanduser("~/.claude/plans")

if not os.path.exists(claude\_plans\_dir):

return None, None

# Find most recent plan file

plan\_files = sorted(

glob\_module.glob(os.path.join(claude\_plans\_dir, "\*.md")),

key=os.path.getmtime,

reverse=True,

)

if not plan\_files:

return None, None

most\_recent = plan\_files[0]

file\_age = datetime.now().timestamp() - os.path.getmtime(most\_recent)

if file\_age > max\_age\_seconds:

return None, None

with open(most\_recent) as f:

content = f.read()

filename = os.path.basename(most\_recent)

# Try XML extraction first

plan = extract\_plan\_from\_xml(content)

if plan:

return plan, f"Claude plan file ({filename})"

# Fallback: substantial content without tags

if len(content.strip()) > min\_fallback\_length:

return content.strip(), f"Claude plan file ({filename}, no XML tags)"

return None, None

def save\_plan\_to\_file(

plan\_content: str,

plan\_source: str,

model\_name: str,

prompt\_summary: str,

output\_dir: str = "chief\_of\_staff\_agent/plans",

title: str = "Agent Plan: Engineering Restructure for AI Focus",

) -> Path:

"""

Save extracted plan to a timestamped markdown file.

Args:

plan\_content: The plan text to save

plan\_source: Description of where plan was extracted from

model\_name: The model used to generate the plan

prompt\_summary: Brief description of the original prompt

output\_dir: Directory to save plan files

title: Title for the plan document

Returns:

Path to the saved plan file

"""

plans\_dir = Path(output\_dir)

plans\_dir.mkdir(exist\_ok=True)

timestamp = datetime.now().strftime("%Y%m%d\_%H%M%S")

plan\_file = plans\_dir / f"plan\_{timestamp}.md"

with open(plan\_file, "w") as f:

f.write(f"# {title}\n\n")

f.write(f"\*\*Created:\*\* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

f.write(f"\*\*Prompt:\*\* {prompt\_summary}\n")

f.write(f"\*\*Model:\*\* {model\_name}\n")

f.write(f"\*\*Plan Source:\*\* {plan\_source}\n\n")

f.write("---\n\n")

f.write(plan\_content)

f.write("\n\n---\n\n")

f.write("\*This plan was generated in plan mode and has not been executed.\*\n")

return plan\_file

def capture\_message\_content(

msg: Any,

plan\_content: list[str],

write\_tool\_content: list[str],

write\_tool\_paths: list[str],

) -> None:

"""

Process a streaming message and capture relevant plan content.

This function extracts content from three potential sources:

1. Text blocks in message content

2. Write tool call parameters

3. Final result attribute

Args:

msg: The message object from the agent stream

plan\_content: List to append text content to

write\_tool\_content: List to append Write tool content to

write\_tool\_paths: List to append Write tool file paths to

"""

# Source 1: Text blocks from message content

if hasattr(msg, "content"):

for block in msg.content:

if hasattr(block, "text"):

plan\_content.append(block.text)

# Source 2: Write tool calls

if hasattr(block, "type") and block.type == "tool\_use":

if hasattr(block, "name") and block.name == "Write":

if hasattr(block, "input") and isinstance(block.input, dict):

if "content" in block.input:

write\_tool\_content.append(block.input["content"])

if "file\_path" in block.input:

write\_tool\_paths.append(block.input["file\_path"])

# Source 3: Final result

if hasattr(msg, "result") and msg.result:

plan\_content.append(msg.result)

print("✅ Plan Mode helper functions loaded")



```
✅ Plan Mode helper functions loaded
```



# =============================================================================

# Plan Mode Configuration

# =============================================================================

# Note: MODEL is defined in cell-0 as "claude-opus-4-6"

# Opus excels at complex planning tasks

# The prompt is carefully crafted to:

# 1. Provide explicit context (since Opus prefers explicit information)

# 2. Request XML-tagged output for reliable extraction

# 3. Prevent file-writing so we can capture the plan programmatically

PLAN\_PROMPT = """Restructure our engineering team for AI focus.

\*\*CONTEXT (from CLAUDE.md):\*\*

You are the Chief of Staff for TechStart Inc, a 50-person B2B SaaS startup that raised $10M Series A.

- Current engineering team: 25 people (Backend: 12, Frontend: 8, DevOps: 5)

- Monthly burn rate: ~$500K, Runway: 20 months

- Senior Engineer compensation: $180K-$220K + equity

\*\*CRITICAL OUTPUT INSTRUCTIONS:\*\*

1. \*\*DO NOT use the Write tool\*\* - Output your plan directly in your response text

2. \*\*DO NOT save to any files\*\* - I will handle saving the plan myself

3. \*\*Wrap your ENTIRE plan inside `<plan> </plan>` XML tags\*\* in your response

\*\*Required Format:\*\*

<plan>

[Your complete restructuring plan here - include all sections, timelines, budgets, and recommendations]

</plan>

\*\*IMPORTANT:\*\*

- The plan content MUST appear directly in your response between the XML tags

- Do NOT use Write, Edit, or any file-saving tools

- You may research and analyze before outputting, but the final plan must be in your response text

- Include: team structure, hiring recommendations, timeline, budget impact, and success metrics

- Use the company context provided above - do NOT ask clarifying questions"""

print(f"📋 Plan Mode configured with model: {MODEL}")

print(f"📝 Prompt length: {len(PLAN\_PROMPT):,} characters")



```
📋 Plan Mode configured with model: claude-opus-4-6
📝 Prompt length: 1,180 characters
```



# =============================================================================

# Execute Plan Mode Agent

# =============================================================================

# Run the agent with plan mode enabled. The agent will create a detailed plan

# but won't execute any actions. We capture content from multiple sources

# to handle different agent behaviors.

# Initialize capture lists

messages = []

plan\_content = [] # Text from message stream

write\_tool\_content = [] # Content from Write tool calls

write\_tool\_paths = [] # Paths from Write tool calls

# Run the agent in plan mode

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

permission\_mode="plan",

cwd="chief\_of\_staff\_agent",

)

) as agent:

await agent.query(PLAN\_PROMPT)

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)

# Capture content from this message

capture\_message\_content(msg, plan\_content, write\_tool\_content, write\_tool\_paths)

print(f"\n✅ Agent completed. Captured {len(plan\_content)} content blocks.")



```
🤖 Thinking...
🤖 Using: ExitPlanMode()
✓ Tool completed
🤖 Thinking...

✅ Agent completed. Captured 3 content blocks.
```



# =============================================================================

# Extract and Save the Plan

# =============================================================================

# Try multiple sources in priority order to find the plan content.

# This handles different agent behaviors robustly.

final\_plan = None

plan\_source = None

# Priority 1: Message stream (preferred - direct from agent response)

final\_plan, plan\_source = extract\_plan\_from\_messages(plan\_content)

# Priority 2: Write tool captures (if agent saved despite instructions)

if not final\_plan and write\_tool\_content:

final\_plan, plan\_source = extract\_plan\_from\_write\_tool(write\_tool\_content)

# Priority 3: Claude's internal plan directory (safety net)

if not final\_plan:

final\_plan, plan\_source = extract\_plan\_from\_claude\_dir()

# Report results

if final\_plan:

print(f"✅ Plan extracted from: {plan\_source}")

print(f" Plan length: {len(final\_plan):,} characters")

# Save to file

plan\_file = save\_plan\_to\_file(

plan\_content=final\_plan,

plan\_source=plan\_source,

model\_name=MODEL,

prompt\_summary="Restructure our engineering team for AI focus.",

)

print(f"\n📁 Plan saved to: {plan\_file}")

else:

error\_msg = "Could not extract plan content from any source!\n"

error\_msg += " Sources checked: message stream, Write tool, ~/.claude/plans/"

if write\_tool\_paths:

error\_msg += f"\n Write tool attempted to save to: {write\_tool\_paths}"

print(f"❌ ERROR: {error\_msg}")

raise RuntimeError(f"Plan extraction failed: {error\_msg}")



```
✅ Plan extracted from: message stream
   Plan length: 6,783 characters

📁 Plan saved to: chief_of_staff_agent/plans/plan_20251204_152737.md
```



# Display the plan result with styled HTML

display\_agent\_response(messages, title="Engineering Restructure Plan")



```
<IPython.core.display.HTML object>
```

####  Executing the Saved Plan

As mentioned above, the agent will stop after creating its plan. The saved plan file serves as a review artifact for stakeholders.

**To execute the plan after review:**

1. Review the saved plan in `chief_of_staff_agent/plans/plan_*.md`
2. If approved, send a new query with `continue_conversation=True` and remove `permission_mode="plan"` to execute

This workflow enables a "plan → review → approve → execute" cycle, perfect for high-stakes decisions like organizational restructuring or major infrastructure changes.

####  How Plan Persistence Works

In the code above, we implemented a **robust multi-source plan capture mechanism** that handles the various ways Plan Mode agents may output their plans:

**The Challenge:**
When using `permission_mode="plan"`, the agent may output the plan in different ways:

1. **Direct text output** in the message stream (ideal case)
2. **Write tool** to save to `~/.claude/plans/` (Claude's internal plan system)
3. **Write tool** to save to a custom path

Our capture mechanism handles all three scenarios with a **priority-based fallback system**:

**Source Priority (in order):**

1. **Message Stream** (Preferred)

   * Capture text blocks from `msg.content` during streaming
   * Extract content between `<plan></plan>` XML tags
   * This is the cleanest approach as content comes directly from the response
2. **Write Tool Capture**

   * Monitor for Write tool calls in the message stream
   * Extract the `content` parameter being written
   * Useful when the agent decides to save despite prompt instructions
3. **Claude's Internal Plan Directory**

   * Check `~/.claude/plans/` for recently created plan files (within 5 minutes)
   * Read and extract content from the most recent file
   * Acts as a safety net when other methods fail
4. **Full Content Fallback**

   * If no XML tags found but substantial content exists (>500 chars), use it directly
   * Prevents empty plan files while preserving partial information

**Key Implementation Details:**



def extract\_plan\_from\_text(text):

"""Extract content between <plan> tags, return None if not found or empty."""

match = re.search(r'<plan>(.\*?)</plan>', text, re.DOTALL)

if match:

extracted = match.group(1).strip()

# Validate minimum content length (a real plan should be substantial)

if len(extracted) > 200:

return extracted

return None

**Why Content Validation Matters:**

* Previous versions could produce empty plan files if extraction "succeeded" with no content
* We now require a minimum of 200 characters for XML-tagged content
* This prevents false positives where regex matches empty or trivial content

**Prompt Engineering for Direct Output:**
The prompt explicitly instructs the agent:

* **DO NOT use the Write tool** - prevents file-system detours
* **Output directly in response** - ensures content flows through message stream
* **Use XML tags** - enables clean extraction from potentially verbose responses

This approach gives you:

* **Reliability**: Plans are captured regardless of agent behavior
* **Transparency**: The saved file indicates which source was used
* **Audit Trail**: History of all plans with timestamps and source metadata
* **Debugging**: Clear error messages when extraction fails

Let's view the saved plan:



# Display the saved plan with markdown rendering

from IPython.display import Markdown, display

# Show the plan with proper markdown formatting

display(Markdown(f"## 📋 Saved Plan Preview\n\n{final\_plan}"))

print(f"\n📁 Full plan with metadata saved to: {plan\_file}")



```
<IPython.core.display.Markdown object>

📁 Full plan with metadata saved to: chief_of_staff_agent/plans/plan_20251204_152737.md
```

##  Advanced Features

###  Feature 4: Custom Slash Commands

> Note: slash commands are syntactic sugar for users, not new agent capabilities

**What**: Custom slash commands are predefined prompt templates that users can trigger with shorthand syntax (e.g., `/budget-impact`). These are **user-facing shortcuts**, not agent capabilities. Think of them as keyboard shortcuts that expand into full, well-crafted prompts.

**Why**: Your Chief of Staff will handle recurring executive questions. Instead of users typing complex prompts repeatedly, they can use already vetted prompts. This improves consistency and standardization.

**How**:

* Define a markdown file in `.claude/commands/`. For example, we defined one in `.claude/commands/slash-command-test.md`. Notice how the command is defined: frontmatter with two fields (name, description) and the expanded prompt with an option to include arguments passed on in the query.
* You can add parameters to your prompt using `$ARGUMENTS` (for full argument string) or `$1`, `$2`, etc. (for positional arguments)
* The user uses the slash command in their prompt

> **CRITICAL SDK CONFIGURATION**: When using the SDK, you **must** set `setting_sources=["project"]` in your `ClaudeAgentOptions` for slash commands to work. By default, the SDK operates in isolation mode and does NOT load filesystem settings (slash commands, CLAUDE.md, subagents, hooks, etc.). This is different from using Claude Code interactively where these are loaded automatically.



# User types: "/slash-command-test this is a test"

# -> behind the scenes EXPANDS to the prompt in .claude/commands/slash-command-test.md

# In this case the expanded prompt says to simply reverse the sentence word wise

messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="chief\_of\_staff\_agent",

# IMPORTANT: setting\_sources must include "project" to load slash commands from .claude/commands/

# Without this, the SDK does NOT load filesystem settings (slash commands, CLAUDE.md, etc.)

setting\_sources=["project"],

)

) as agent:

await agent.query("/slash-command-test this is a test")

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)



```
🤖 Thinking...
```



display\_agent\_response(messages, title="Slash Command Result")



```
<IPython.core.display.HTML object>
```

###  Feature 5: Hooks - Automated Deterministic Actions

**What**: Hooks are Python scripts that you can set to execute automatically, among other events, before (pre) or after (post) specific tool calls. Hooks run **deterministically**, making them perfect for validation and audit trails.

**Why**: Imagine scenarios where you want to make sure that your agent has some guardrails (e.g., prevent dangerous operations) or when you want to have an audit trail. Hooks are ideal in combination with agents to allow them enough freedom to achieve their task, while still making sure that the agents behave in a safe way.

**How**:

* Define hook scripts in `.claude/hooks/` -> *what* is the behaviour that should be executed when a hook is triggered
* Define hook configuration in `.claude/settings.local.json` -> *when* should a hook be triggered
* In this case, our hooks are configured to watch specific tool calls (Bash, Write, Edit)
* When those tools are called, the hook script runs after the tool completes (PostToolUse)

> **SDK CONFIGURATION NOTE**: Hooks configured in `.claude/settings.local.json` require `setting_sources=["project", "local"]`. The SDK distinguishes between three setting sources:
>
> * `"project"` → `.claude/settings.json` (version-controlled, team-shared)
> * `"local"` → `.claude/settings.local.json` (gitignored, local settings like hooks)
> * `"user"` → `~/.claude/settings.json` (global user settings)
>
> Since our hooks are in `settings.local.json`, we must include `"local"` in `setting_sources`.

**Example: Report Tracking for Compliance**

A hook to log Write/Edit operations on financial reports for audit and compliance purposes.
The hook is defined in `chief_of_staff_agent/.claude/hooks/report-tracker.py` and the logic that enforces it is in `chief_of_staff_agent/.claude/settings.local.json`:



"hooks": {

"PostToolUse": [

{

"matcher": "Write",

"hooks": [

{

"type": "command",

"command": "$CLAUDE\_PROJECT\_DIR/.claude/hooks/report-tracker.py"

}

]

},

{

"matcher": "Edit",

"hooks": [

{

"type": "command",

"command": "$CLAUDE\_PROJECT\_DIR/.claude/hooks/report-tracker.py"

}

]

}

]

}



messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

cwd="chief\_of\_staff\_agent",

allowed\_tools=["Bash", "Write", "Edit", "MultiEdit"],

# IMPORTANT: setting\_sources must include BOTH "project" AND "local" to load hooks

# - "project" loads .claude/settings.json (shared settings, CLAUDE.md, slash commands)

# - "local" loads .claude/settings.local.json (where hooks are configured)

setting\_sources=["project", "local"],

)

) as agent:

await agent.query(

"Create a quick Q2 financial forecast report with our current burn rate and runway projections. Save it to our /output\_reports folder."

)

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)

# The hook will track this in audit/report\_history.json

display\_agent\_response(messages, title="Q2 Financial Forecast")



```
🤖 Using: Bash()
🤖 Using: Bash()
🤖 Using: Bash()
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Using: Read()
🤖 Using: Read()
🤖 Using: Read()
🤖 Using: Bash()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: Write()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

If you now navigate to `./chief_of_staff_agent/audit/report_history.json`, you will find that it has logged that the agent has created and/or made changes to your report. The generated report itself you can find at `./chief_of_staff_agent/output_reports/`.

###  Feature 6: Subagents via Task Tool

**What**: The Task tool enables your agent to delegate specialized work to other subagents. These subagents each have their own instructions, tools, and expertise.

**Why**: Adding subagents opens up a lot of possibilities:

1. Specialization: each subagent is an expert in their domain
2. Separate context: subagents have their own conversation history and tools
3. Parallellization: multiple subagents can work simultaneously on different aspects.

**How**:

* Add `"Task"` to allowed\_tools
* Use a system prompt to instruct your agent how to delegate tasks (you can also define this its CLAUDE.md more generally)
* Create a markdown file for each agent in `.claude/agents/`. For example, check the one for `.claude/agents/financial-analyst.md` and notice how a (sub)agent can be defined with such an easy and intuitive markdown file: frontmatter with three fields (name, description, and tools) and its system prompt. The description is useful for the main chief of staff agent to know when to invoke each subagent.

**Visualization Enhancements**: Our `print_activity()` and `visualize_conversation()` utilities have been enhanced to clearly show subagent operations:

* 🚀 indicates when a subagent is being delegated to (with the subagent name)
* 📎 indicates tools being used BY the subagent (indented for visual hierarchy)
* Visual separators clearly mark subagent delegation and completion boundaries
* Task descriptions and prompts are shown in the conversation timeline



# Reset the subagent tracking context before starting a new query

# This ensures clean state for activity display

reset\_activity\_context()

messages = []

async with ClaudeSDKClient(

options=ClaudeAgentOptions(

model=MODEL,

allowed\_tools=["Task"], # this enables our Chief agent to invoke subagents

system\_prompt="Delegate financial questions to the financial-analyst subagent. Do not try to answer these questions yourself.",

cwd="chief\_of\_staff\_agent",

setting\_sources=["project", "local"],

)

) as agent:

await agent.query("Should we hire 5 engineers? Analyze the financial impact.")

async for msg in agent.receive\_response():

print\_activity(msg)

messages.append(msg)

display\_agent\_response(messages, title="Hiring Impact Analysis")



```
🤖 Thinking...
🚀 Delegating to subagent: financial-analyst
   └─ Task: Analyze 5 engineer hiring impact
   ✓ Tool completed
   📎 [financial-analyst] Using: Bash()
   📎 [financial-analyst] Using: Read()
   📎 [financial-analyst] Using: Read()
   ✓ Tool completed
   ✓ Tool completed
   ✓ Tool completed
   📎 [financial-analyst] Using: Read()
   📎 [financial-analyst] Using: Bash()
   ✓ Tool completed
   ✓ Tool completed
   📎 [financial-analyst] Using: Bash()
   ✓ Tool completed
   📎 [financial-analyst] Using: Bash()
   ✓ Tool completed
   📎 [financial-analyst] Using: Bash()
   ✓ Tool completed
   📎 [financial-analyst] Using: Bash()
   ✓ Tool completed
   ✓ Tool completed
   📎 [financial-analyst] Thinking...

<IPython.core.display.HTML object>
```



visualize\_conversation(messages)



```
<IPython.core.display.HTML object>
```

Here, when our main agent decides to use a subagent, it will:

1. Call the Task tool with parameters like:



{

"description": "Analyze hiring impact",

"prompt": "Analyze the financial impact of hiring 5 engineers...",

"subagent\_type": "financial-analyst"

}

1. The Task tool executes the subagent in a separate context
2. Return results to main Chief of Staff agent to continue processing

##  Putting It All Together

Let's now put everything we've seen together. We will ask our agent to determine the financial impact of hiring 3 senior engineers and write their insights to `output_reports/hiring_decision.md`. This demonstrates all the features seen above:

* **Bash Tool**: Used to execute the `hiring_impact.py` script to determine the impact of hiring new engineers
* **Memory**: Reads `CLAUDE.md` in directory as context to understand the current budgets, runway, revenue and other relevant information
* **Output style**: Different output styles, defined in `chief_of_staff_agent/.claude/output-styles`
* **Custom Slash Commands**: Uses the shortcut `/budget-impact` that expands to full prompt defined in `chief_of_staff_agent/.claude/commands`
* **Subagents**: Our `/budget_impact` command guides the chief of staff agent to invoke the financial-analyst subagent defined in `chief_of_staff_agent/.claude/agents`
* **Hooks**: Hooks are defined in `chief_of_staff_agent/.claude/hooks` and configured in `chief_of_staff_agent/.claude/settings.local.json`

  + If one of our agents is updating the financial report, the hook should log this edit/write activity in the `chief_of_staff_agent/audit/report_history.json` logfile
  + If the financial analyst subagent will invoke the `hiring_impact.py` script, this will be logged in `chief_of_staff_agent/audit/tool_usage_log.json` logfile
* **Plan Mode**: If you want the chief of staff to come up with a plan for you to approve before taking any action, uncomment the commented line below

To have this ready to go, we have encapsulated the agent loop in a python file, similar to what we did in the previous notebook. Check out the agent.py file in the `chief_of_staff_agent` subdirectory.

All in all, our `send_query()` function takes in 4 parameters (prompt, continue\_conversation, permission\_mode, and output\_style), everything else is set up in the agent file, namely: system prompt, max turns, allowed tools, and the working directory.

To better visualize how this all comes together, check out these [flow and architecture diagrams that Claude made for us :)(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./chief_of_staff_agent/flow_diagram.md)



from chief\_of\_staff\_agent.agent import send\_query

reset\_activity\_context()

result, messages = await send\_query(

"/budget-impact hiring 3 senior engineers. Save your insights by updating the 'hiring\_decision.md' file in /output\_reports or creating a new file there",

# permission\_mode="plan", # Enable this to use planning mode

output\_style="executive",

)



```
🤖 Thinking...
🤖 Using: Glob()
🤖 Using: Glob()
✓ Tool completed
✓ Tool completed
🤖 Using: Read()
🤖 Using: Read()
🤖 Using: Read()
🤖 Using: Read()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: Task()
✓ Tool completed
🤖 Using: Bash()
🤖 Using: Read()
🤖 Using: Read()
🤖 Using: Read()
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
✓ Tool completed
🤖 Thinking...
🤖 Using: Write()
✓ Tool completed
🤖 Thinking...
```



visualize\_conversation(messages)



```
<IPython.core.display.HTML object>
```

##  Conclusion

We've demonstrated how the Claude Code SDK enables you to build sophisticated multi-agent systems with enterprise-grade features. Starting from basic script execution with the Bash tool, we progressively introduced advanced capabilities including persistent memory with CLAUDE.md, custom output styles for different audiences, strategic planning mode, slash commands for user convenience, compliance hooks for guardrailing, and subagent coordination for specialized tasks.

By combining these features, we created an AI Chief of Staff capable of handling complex executive decision-making workflows. The system delegates financial analysis to specialized subagents, maintains audit trails through hooks, adapts communication styles for different stakeholders, and provides actionable insights backed by data-driven analysis.

This foundation in advanced agentic patterns and multi-agent orchestration prepares you for building production-ready enterprise systems. In the next notebook, we'll explore how to connect our agents to external services through Model Context Protocol (MCP) servers, dramatically expanding their capabilities beyond the built-in tools.

Next: [02\_The\_observability\_agent.ipynb(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/02_The_observability_agent.ipynb) - Learn how to extend your agents with custom integrations and external data sources through MCP.
