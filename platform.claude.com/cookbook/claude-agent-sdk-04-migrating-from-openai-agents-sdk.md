<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk -->

# Migrating from the OpenAI Agents SDK

If you have an app on the OpenAI Agents SDK and want to port it to the Claude Agent SDK, this notebook maps each primitive using a single example: an expense approval agent.

**What you get after migrating.** The Claude Agent SDK runs on the same runtime as Claude Code — you inherit its built-in `Read`, `Edit`, `Bash`, and `Grep` tools, a layered permission system for gating what the agent can touch, automatic prompt caching, and direct access to the event stream for progress streaming or mid-run interception. Tool definitions are explicit (you declare schemas rather than relying on type-hint introspection), and the loop is yours to drive. Most ports involve more boilerplate per tool and less boilerplate everywhere else.

## By the end of this notebook, you'll be able to:

* Replace `@function_tool`, guardrails, and `Runner.run` with their Claude equivalents without rewriting your business logic
* Port a single-agent app: custom tool, input/output guardrails, multi-turn sessions, and durable resume
* Know when to reach for `ClaudeSDKClient` vs the stateless `query()` function
* Wire the SDK's OpenTelemetry export to your existing observability stack

Both SDKs run live. You'll need `OPENAI_API_KEY` and `ANTHROPIC_API_KEY` in your `.env`.

| OpenAI Agents SDK | Claude Agent SDK |
| --- | --- |
| `Agent(name, instructions, tools)` | `ClaudeAgentOptions` + system prompt |
| `@function_tool` | `@tool` + `create_sdk_mcp_server` |
| `@input_guardrail` | Plain function before the loop (or `UserPromptSubmit` hook) |
| `@output_guardrail` | Plain function on `ResultMessage.result` |
| `Runner.run(agent, msg)` | `ClaudeSDKClient` context manager |
| `Sessions` (client-managed) | Reuse the same `ClaudeSDKClient` |
| `conversation_id` (server-managed) | `resume=session_id` (disk-backed) |
| Built-in tracing dashboard | OTel-native — plugs into your existing Grafana/Datadog/Honeycomb |
| `handoffs=[...]` | `AgentDefinition` + Agent tool — see appendix |

## The example: expense approval

A single agent that approves or flags expense submissions. One tool (`check_policy`), one input guardrail (reject if no dollar amount), the loop.

We build it once in the OpenAI Agents SDK, then port each primitive.

## Prerequisites

**Required Knowledge**

* Comfortable with `async`/`await` in Python
* Familiarity with the OpenAI Agents SDK primitives you're migrating from

**Required Tools**

* Python 3.11 or 3.12
* `ANTHROPIC_API_KEY` ([get one](https://console.anthropic.com)) and `OPENAI_API_KEY` ([get one](https://platform.openai.com/api-keys)) — both SDKs run live

**Recommended:**

* Skim [notebook 00](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./00_The_one_liner_research_agent.ipynb) for `query()` and `ClaudeSDKClient` basics

> `openai-agents` is pinned to `0.9.3` — it's pre-1.0 and its API changes frequently. If you bump the version, re-verify the `Agent`/`Runner`/`@function_tool` signatures.

python

```
%%capture
# openai-agents pinned to 0.9.3 — see prereqs note before bumping
%pip install "openai-agents==0.9.3" claude-agent-sdk python-dotenv
```

python

```
import os
import re
from dataclasses import replace

from dotenv import load_dotenv

load_dotenv()

assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY missing from .env"
assert os.getenv("ANTHROPIC_API_KEY"), "ANTHROPIC_API_KEY missing from .env"

OAI_MODEL = "gpt-4.1"
CLAUDE_MODEL = "claude-sonnet-4-6"
```

python

```
# ===== OpenAI Agents SDK — full implementation =====
from agents import Agent, GuardrailFunctionOutput, Runner, function_tool, input_guardrail

@function_tool
def check_policy(category: str, amount: float) -> dict:
    """Look up the expense policy for a category. Returns the approval limit. Valid categories: meals, travel, software, other."""
    limits = {"meals": 75.0, "travel": 500.0, "software": 200.0, "other": 50.0}
    return {
        "category": category,
        "limit": limits.get(category.lower(), 50.0),
        "requires_receipt": amount > 25.0,
    }

@input_guardrail
def has_dollar_amount(ctx, agent, user_input: str) -> GuardrailFunctionOutput:
    has_amount = bool(re.search(r"\$\d+", user_input))
    return GuardrailFunctionOutput(
        output_info={"has_amount": has_amount},
        tripwire_triggered=not has_amount,
    )

expense_agent = Agent(
    name="Expense Approver",
    instructions=(
        "You approve or flag expense submissions. "
        "Always call check_policy first to get the limit for the expense category. "
        "Approve if the amount is under the limit; otherwise flag for manager review."
    ),
    tools=[check_policy],
    input_guardrails=[has_dollar_amount],
    model=OAI_MODEL,
)

async def run_oai(msg: str) -> str:
    result = await Runner.run(expense_agent, msg)
    return result.final_output

print(await run_oai("Lunch with Acme, $47"))
```

```
This lunch expense of $47 falls under the "meals" category, which has an approval limit of $75. Since the amount is below the limit, I approve the expense (assuming a receipt is provided, as required by policy).
```

## Porting primitive by primitive

### `@function_tool` → `@tool` + `create_sdk_mcp_server`

**OpenAI:** `@function_tool` derives the tool schema from type hints and the docstring. The decorated function goes straight into `tools=[...]`.

**Claude:** `@tool` takes name, description, and schema as explicit arguments — what you write is what the model sees. The handler is `async`, receives a single `args` dict, and returns `{"content": [{"type": "text", "text": ...}]}`. Tools are bundled into an in-process MCP server (no subprocess or network transport despite the name), which is the unit you pass to the agent.

The logic inside your function doesn't change. Only the wrapper does.

python

```
import json

from claude_agent_sdk import create_sdk_mcp_server, tool

@tool(
    "check_policy",
    "Look up the expense policy for a category. Returns the approval limit. Valid categories: meals, travel, software, other.",
    {"category": str, "amount": float},
)
async def check_policy_claude(args):
    limits = {"meals": 75.0, "travel": 500.0, "software": 200.0, "other": 50.0}
    category, amount = args["category"], args["amount"]
    result = {
        "category": category,
        "limit": limits.get(category.lower(), 50.0),
        "requires_receipt": amount > 25.0,
    }
    return {"content": [{"type": "text", "text": json.dumps(result)}]}

policy_server = create_sdk_mcp_server(name="expense", tools=[check_policy_claude])
```

### `Agent(...)` → `ClaudeAgentOptions`

`ClaudeAgentOptions` carries model, tools, and system prompt — the config that actually gets sent to Claude. Your guardrail logic stays in application code instead of being registered on a framework object. OpenAI's `Agent` bundles all of these together.

| `Agent(...)` field | `ClaudeAgentOptions` equivalent |
| --- | --- |
| `instructions=...` | `system_prompt=...` |
| `tools=[fn]` | `mcp_servers={...}` + `allowed_tools=[...]` |
| `model=...` | `model=...` |
| `name=...` | Not needed — options are a config value, not a named entity. Subagent names go on `AgentDefinition` (see appendix). |
| `input_guardrails=[...]` | Called in your run function — see next section |

Tool names in `allowed_tools` follow the pattern `mcp__{server_name}__{tool_name}`.

> **A note on permissions:** `allowed_tools` is an allow-rule — it makes the tool *available* to the agent. Whether the agent can call it without user approval depends on `permission_mode`. Read-only custom tools like `check_policy` run freely by default; tools that write files or run shell commands will prompt unless you set `permission_mode="acceptEdits"` or `"bypassPermissions"`. See the [permissions guide](https://platform.claude.com/docs/en/agent-sdk/permissions) if your tool does more than read.

python

```
from claude_agent_sdk import ClaudeAgentOptions

expense_system_prompt = (
    "You approve or flag expense submissions. "
    "Always call check_policy first to get the limit for the expense category. "
    "Approve if the amount is under the limit; otherwise flag for manager review."
)

expense_options = ClaudeAgentOptions(
    model=CLAUDE_MODEL,
    system_prompt=expense_system_prompt,
    mcp_servers={"expense": policy_server},
    allowed_tools=["mcp__expense__check_policy"],
)
```

> **Built-in tools.** The expense agent only uses a custom tool, but the SDK ships `Read`, `Edit`, `Bash`, `Grep`, and more — add them to `allowed_tools` by name (e.g., `allowed_tools=["Read", "Grep", "mcp__expense__check_policy"]`). See [notebook 00](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./00_The_one_liner_research_agent.ipynb) for filesystem patterns.

### `@input_guardrail` / `@output_guardrail` → pre/post-call checks

**OpenAI:** `@input_guardrail` validates the user's message; `@output_guardrail` validates the agent's final answer. Both return `GuardrailFunctionOutput(tripwire_triggered=True)` to block, which raises `InputGuardrailTripwireTriggered` (or the output variant). Input guardrails run concurrently with the agent.

**Claude:** Your checks are plain functions. Call the input check before you start the client, call the output check on `ResultMessage.result` after the loop finishes.

| OAI | Claude |
| --- | --- |
| `@input_guardrail` decorator | Plain function called before the loop |
| `@output_guardrail` decorator | Plain function called on `result.result` after the loop |
| `tripwire_triggered=True` raises | Return early (input) or override result (output) |
| Registered on `Agent(input_guardrails=[...])` | Called in your run function |

#### The `UserPromptSubmit` hook alternative

The SDK's `UserPromptSubmit` hook fires before the prompt reaches Claude and can block it — the closest structural match to `@input_guardrail`. We show both below but demonstrate with plain functions for two reasons: the rejection message stays in your control (when a hook blocks, `ResultMessage.result` comes back empty — the reason isn't surfaced to the caller), and the guardrail logic stays visible in your run function rather than registered on the options object. `@output_guardrail` has no clean hook equivalent — `Stop` fires after the response completes but doesn't rewrite output. See [notebook 03](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./03_The_site_reliability_agent.ipynb) for `PreToolUse` hooks gating tool calls, which is a different use case.

python

```
def has_dollar_amount_check(user_input: str) -> tuple[bool, str | None]:
    """Input check — returns (allowed, rejection_message)."""
    if re.search(r"\$\d+", user_input):
        return True, None
    return False, "I need a dollar amount to process this. Please include one (e.g., '$47')."

def has_decision_check(result: str) -> tuple[bool, str | None]:
    """Output check — returns (allowed, override_message)."""
    # Stem match is intentionally permissive for a demo; tighten for production.
    if re.search(r"\b(approv|flag|review)", result, re.IGNORECASE):
        return True, None
    return False, "I couldn't reach a clear approve/flag decision. Please resubmit."
```

For comparison, here's the same check wired as a `UserPromptSubmit` hook. The callback receives `input_data["prompt"]`, returns `{}` to allow or `{"decision": "block", "reason": "..."}` to block. `HookMatcher` takes no `matcher` argument here because `UserPromptSubmit` fires on every prompt — there's no tool name to filter on.

To try it, replace `options=expense_options` with `options=hooked_options` in the `ClaudeSDKClient(...)` call in the next section. One caveat: when a `UserPromptSubmit` hook blocks, the block reason doesn't currently surface in `ResultMessage.result` — you'll get an empty string back rather than the rejection text. That's why the demo loop uses the plain function, which controls its own return.

For tool-level guardrails — guarding what the agent *does* rather than what the user *sends* — see the `PreToolUse` hook pattern in [notebook 03](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./03_The_site_reliability_agent.ipynb).

python

```
from claude_agent_sdk import HookMatcher

async def has_dollar_amount_hook(input_data, tool_use_id, context):
    # tool_use_id is None for UserPromptSubmit — it's a uniform signature across all hook types.
    if re.search(r"\$\d+", input_data["prompt"]):
        return {}
    return {"decision": "block", "reason": "I need a dollar amount to process this."}

hooked_options = ClaudeAgentOptions(
    model=CLAUDE_MODEL,
    system_prompt=expense_system_prompt,
    mcp_servers={"expense": policy_server},
    allowed_tools=["mcp__expense__check_policy"],
    hooks={"UserPromptSubmit": [HookMatcher(hooks=[has_dollar_amount_hook])]},
)
```

### `Runner.run()` → `ClaudeSDKClient`

**OpenAI:** `result = await Runner.run(agent, msg)` runs the loop and returns a result object. Read `result.final_output` for the text.

**Claude:** `ClaudeSDKClient` is an async context manager. Call `.query(msg)` to send, then iterate `.receive_response()` for events as they arrive — you see every tool call, every text block, and the final result in order. The event types:

| Event | Contains |
| --- | --- |
| `SystemMessage` | Session init metadata |
| `AssistantMessage` | Text blocks or tool-use blocks |
| `UserMessage` | Tool-result blocks |
| `ResultMessage` | Always last: `.result`, `.usage`, `.total_cost_usd` |

The final answer is `messages[-1].result`.

> The SDK also exposes a stateless `query()` function (see [notebook 00](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./00_The_one_liner_research_agent.ipynb)) for one-off calls using built-in tools. `ClaudeSDKClient` is the right choice when you're bringing custom tools via `create_sdk_mcp_server`, since its persistent transport handles the in-process MCP handshake.

python

```
from utils.agent_visualizer import display_agent_response, print_activity, reset_activity_context

from claude_agent_sdk import ClaudeSDKClient

async def run_claude(msg: str) -> None:
    # Input guardrail — short-circuit before the agent runs
    allowed, rejection = has_dollar_amount_check(msg)
    if not allowed:
        print(rejection)
        return

    reset_activity_context()
    messages = []
    async with ClaudeSDKClient(options=expense_options) as client:
        await client.query(msg)
        async for event in client.receive_response():
            print_activity(event)
            messages.append(event)

    # receive_response() guarantees ResultMessage is the last event yielded
    final = messages[-1].result
    ok, override = has_decision_check(final or "")
    if not ok:
        print(override)
        return

    display_agent_response(messages)

await run_claude("Lunch with Acme, $47")
```

```
🤖 Thinking...
🤖 Thinking...
🤖 Using: mcp__expense__check_policy()
✓ Tool completed
🤖 Thinking...

<IPython.core.display.HTML object>
```

### Sessions → `ClaudeSDKClient` (in-memory) or `resume=` (disk-backed)

OpenAI offers two session modes:

| OAI mode | Durability | Claude equivalent |
| --- | --- | --- |
| `result.to_input_list()` + re-send | Client holds history in memory | Reuse one `ClaudeSDKClient` — call `.query()` again on the same open context |
| `conversation_id` | Server-side, survives process restarts | `resume=session_id` — conversation transcript is written to disk locally, survives restarts |

**In-memory (below):** Keep the `ClaudeSDKClient` context open and call `.query()` again. No history re-sending. Dies when your process does.

**Disk-backed:** Every run produces a `session_id` (on `ResultMessage.session_id`). Store it, then pass `ClaudeAgentOptions(resume=session_id, ...)` on the next run. The transcript lives on the local filesystem, not on Anthropic's servers — it's durable across restarts but not across machines.

For conversations that outgrow the context window in either mode, see [`../misc/session_memory_compaction.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/../misc/session_memory_compaction.ipynb).

python

```
# --- In-memory: reuse the same client ---
async def run_claude_multiturn():
    async with ClaudeSDKClient(options=expense_options) as client:
        await client.query("Lunch with Acme, $47")
        async for _ in client.receive_response():
            pass  # consume the stream

        # Same client — remembers turn 1
        await client.query("What about $90?")
        turn2 = [m async for m in client.receive_response()]
        # receive_response() guarantees ResultMessage is the last event yielded
        return turn2[-1].result

print(await run_claude_multiturn())
```

```
🚩 **Flagged for Manager Review**

| Detail | Info |
|---|---|
| **Description** | Lunch with Acme |
| **Category** | Meals |
| **Amount** | $90.00 |
| **Policy Limit** | $75.00 |
| **Over Limit By** | $15.00 |
| **Status** | **Flagged** |

The $90 lunch exceeds the $75 meals limit by **$15.00**, so it requires manager approval before it can be reimbursed.
```

python

```
# --- Disk-backed: capture session_id, resume later ---

# Turn 1: capture the session_id from the ResultMessage (always the last event)
async with ClaudeSDKClient(options=expense_options) as client:
    await client.query("Lunch with Acme, $47")
    turn1 = [m async for m in client.receive_response()]
session_id = turn1[-1].session_id

# Turn 2: new client, new process — resume from disk
resume_opts = replace(expense_options, resume=session_id)
async with ClaudeSDKClient(options=resume_opts) as client:
    await client.query("What about $90?")
    turn2 = [m async for m in client.receive_response()]
print(f"[resumed {session_id[:8]}...] {turn2[-1].result}")
```

```
[resumed 4fc6dc1e...] Here's the rundown for both expenses:

| Expense | Amount | Limit | Status |
|---|---|---|---|
| Lunch with Acme | $47 | $75 | ✅ **Approved** |
| Lunch with Acme | $90 | $75 | 🚩 **Flagged for Manager Review** |

- **$47** – Under the $75 meals limit, so it's **approved**. (Receipt required.)
- **$90** – Exceeds the $75 meals limit by $15, so it's **flagged for manager review**.
```

## Side-by-side comparison

Run all three test inputs through both SDKs. We expect both to approve the 47lunch,flagthe47 lunch, flag the 47lunch,flagthe650 flight, and reject the input with no dollar amount.

python

```
from agents.exceptions import InputGuardrailTripwireTriggered

async def run_claude_quiet(msg: str) -> str:
    # Same guardrail as run_claude — duplicated here for a minimal comparison helper
    allowed, rejection = has_dollar_amount_check(msg)
    if not allowed:
        return rejection
    async with ClaudeSDKClient(options=expense_options) as client:
        await client.query(msg)
        messages = [m async for m in client.receive_response()]
        # receive_response() guarantees ResultMessage is the last event yielded
        return messages[-1].result or ""

test_inputs = [
    ("Lunch with Acme, $47", "approve"),
    ("Flight to NYC, $650", "flag"),
    ("Need approval for the thing", "guardrail"),
]

for msg, expected in test_inputs:
    print(f"\n{'=' * 60}\nINPUT: {msg}  (expect: {expected})\n{'=' * 60}")

    try:
        oai_out = await run_oai(msg)
    except InputGuardrailTripwireTriggered:
        oai_out = "[guardrail: InputGuardrailTripwireTriggered]"

    claude_out = await run_claude_quiet(msg)

    print(f"OAI:    {str(oai_out)[:200]}")
    print(f"Claude: {str(claude_out)[:200]}")
```

```
============================================================
INPUT: Lunch with Acme, $47  (expect: approve)
============================================================
OAI:    The expense for lunch ($47) is under the meals category limit of $75. This expense is approved.
Claude: ✅ **Expense Approved**

| Detail | Info |
|---|---|
| **Description** | Lunch with Acme |
| **Category** | Meals |
| **Amount** | $47.00 |
| **Meal Limit** | $75.00 |
| **Status** | **Approved** |

Yo

============================================================
INPUT: Flight to NYC, $650  (expect: flag)
============================================================
OAI:    The approval limit for travel expenses is $500. Since your flight to NYC costs $650, this expense exceeds the limit and will be flagged for manager review.
Claude: 🚩 **Expense Flagged for Manager Review**

| Detail | Info |
|---|---|
| **Description** | Flight to NYC |
| **Category** | Travel |
| **Amount** | $650.00 |
| **Policy Limit** | $500.00 |
| **Over Lim

============================================================
INPUT: Need approval for the thing  (expect: guardrail)
============================================================
OAI:    [guardrail: InputGuardrailTripwireTriggered]
Claude: I need a dollar amount to process this. Please include one (e.g., '$47').
```

## Tracing

Claude emits to the standard your team already runs.

**Per-run metrics are already in your hands.** Every `ResultMessage` carries `.total_cost_usd` and `.usage` — input/output tokens, cache reads, cache writes, turn count. You'll see this in the caching cell below. For programmatic cost tracking, see [`../observability/usage_cost_api.ipynb`](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/../observability/usage_cost_api.ipynb).

**OpenTelemetry is native.** The SDK shares the Claude Code runtime, which exports OTel metrics and events when enabled:

```
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp
export OTEL_LOGS_EXPORTER=otlp
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://your-collector:4317
```

None of this is required for the port — your agent runs identically whether telemetry is on or off.

Every tool call and API request emits an event tagged with a `prompt.id`, so you can correlate all activity back to the originating prompt. Point it at your existing Grafana / Datadog / Honeycomb / Langfuse stack. See the [monitoring docs](https://code.claude.com/docs/en/monitoring-usage) for the full event schema.

## Claude-only: prompt caching

The system prompt and tool schemas are cached automatically after the first call — no configuration needed. Subsequent calls with the same prefix pay roughly 10% of the input token cost for that prefix.

> Since earlier cells already ran with `expense_options`, the cache is warm by the time we get here — so even Run 1 shows substantial `cache_read_input_tokens`. In a cold notebook, Run 1 would be mostly `cache_creation`, Run 2 mostly `cache_read`. The tool-calling loop makes multiple API requests per query, each extending the cached prefix — so cache\_creation won't hit zero even on repeat runs, but it should shrink while cache\_read grows.

python

```
for i in range(2):
    async with ClaudeSDKClient(options=expense_options) as client:
        await client.query("Coffee, $6")
        messages = [m async for m in client.receive_response()]
    # receive_response() guarantees ResultMessage is the last event yielded
    usage = messages[-1].usage or {}
    print(
        f"Run {i + 1}: cache_creation={usage.get('cache_creation_input_tokens', 0):>5}  "
        f"cache_read={usage.get('cache_read_input_tokens', 0):>5}  "
        f"input={usage.get('input_tokens', 0):>5}"
    )
```

```
Run 1: cache_creation=38728  cache_read=66272  input=    4
Run 2: cache_creation=  659  cache_read=95025  input=    4
```

---

## Appendix: Migrating `handoffs`

If your OpenAI Agents SDK app uses `handoffs=[...]`, this is where the mental model shifts.

**OpenAI:** `handoffs=[specialist]` exposes a `transfer_to_specialist` tool. When called, the specialist **takes over** the conversation. The first agent is done.

**Claude:** Subagents are defined programmatically via `AgentDefinition` and passed in `ClaudeAgentOptions(agents={...})`. The orchestrator **delegates** via the Agent tool, gets results back, and stays in control.

For pure routers (triage → specialist) the difference is small. For apps where "agent B takes over and A never runs again" is load-bearing, consider a thin Python dispatcher instead of LLM-decided routing.

> You may also see subagents defined as `.claude/agents/*.md` files in Claude Code CLI workflows (e.g., [notebook 01](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./01_The_chief_of_staff_agent.ipynb)). That's the filesystem-based path for interactive use. For an SDK application that ships as code, the programmatic `agents=` parameter below is the natural fit — no filesystem dependency.

python

```
from claude_agent_sdk import AgentDefinition

approver = AgentDefinition(
    description="Approves expenses under policy limits. Use for any submission where the amount is at or under the limit returned by check_policy.",
    prompt="You approve expense submissions that are within policy. Confirm the amount and category, and remind the submitter if a receipt is required.",
    tools=["mcp__expense__check_policy"],
)

escalator = AgentDefinition(
    description="Escalates over-limit expenses to a manager. Use when the submitted amount exceeds the policy limit for its category.",
    prompt="You escalate over-limit expenses. Draft a one-line note to the manager: include the amount, the category, and how far over the limit it is.",
    tools=["mcp__expense__check_policy"],
)

triage_options = ClaudeAgentOptions(
    model=CLAUDE_MODEL,
    system_prompt="Route each expense to the appropriate subagent. Delegate to approver if under limit, escalator if over.",
    mcp_servers={"expense": policy_server},
    allowed_tools=["Agent", "mcp__expense__check_policy"],
    agents={"approver": approver, "escalator": escalator},
)

print(f"Orchestrator configured with subagents: {list(triage_options.agents)}")

# Config only — not executed here. For a full end-to-end multi-agent run,
# see ./01_The_chief_of_staff_agent.ipynb
```

```
Orchestrator configured with subagents: ['approver', 'escalator']
```

## Conclusion

### What you built

One expense-approval agent, ported primitive by primitive: `@function_tool` → `@tool`, `Agent` → `ClaudeAgentOptions`, `@input_guardrail`/`@output_guardrail` → plain pre/post checks, `Runner.run` → `ClaudeSDKClient`, sessions in-memory and disk-backed.

### Key takeaways

* **Tools:** Explicit schemas mean what you write is what the model sees — no introspection surprises. Bundle as an in-process MCP server and pass via `ClaudeSDKClient`.
* **Guardrails:** Plain functions put the rejection flow in your code, not a framework's. The `UserPromptSubmit` hook is there when you want it registered on options.
* **Sessions:** One `ClaudeSDKClient` for in-memory multi-turn. `resume=session_id` for disk-backed conversations that survive restarts.
* **Tracing:** OpenTelemetry-native, so it plugs into the stack you already run. Per-turn cost and token usage are on every `ResultMessage` — no extra wiring.

### Next steps

* Multi-agent orchestration: [01\_The\_chief\_of\_staff\_agent.ipynb](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./01_The_chief_of_staff_agent.ipynb)
* Tool-lifecycle hooks (`PreToolUse`/`PostToolUse`): [03\_The\_site\_reliability\_agent.ipynb](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./03_The_site_reliability_agent.ipynb)
* Cost and usage tracking patterns: [../observability/usage\_cost\_api.ipynb](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/../observability/usage_cost_api.ipynb)
