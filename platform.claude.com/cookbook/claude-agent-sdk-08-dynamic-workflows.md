<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-08-dynamic-workflows -->

#  Orchestrate subagents at scale with dynamic workflows

##  Introduction

Fact-checking a draft investor update means checking many independent claims, applying real judgment to each, and making sure the verification actually runs: more items, judgment, and enforced verification than one context window comfortably holds. Dynamic workflows are a Claude Code feature for tasks like that, ones that need more agents than one conversation can coordinate. Instead of orchestrating turn by turn, Claude writes a JavaScript orchestration script for the task and passes it to the `Workflow` tool, whose runtime executes it in the background. The script spawns subagents in parallel or in stages, holds their results in variables, and applies the connecting logic (filtering, loops, verification passes) in plain code. Because the Agent SDK drives the Claude Code runtime, you can launch a workflow straight from Python.

Each of those subagents is a full Claude Code agent. It starts with a clean context, sees only the prompt the script gives it, and works in your session's working directory with the tool allowlist you configured. Every agent runs on your session's model by default, but the script can route a stage to a different one: a cheaper model for mechanical extraction and the strongest one for the hard judgment calls. You steer that from your prompt, or override every agent at once with the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable. The runtime keeps up to 16 agents running concurrently (fewer on machines with limited CPU cores) and caps a run at 1,000 agents; a workflow that plans more work than the concurrency limit queues it until a slot frees up.

Because the plan lives in code instead of a model's context window, every item gets the same treatment, verification runs because the script says so, a single run can coordinate dozens to hundreds of agents, and the script is a file you can read, edit, save, and re-run. The cost is tokens: many subagents use substantially more of them. A workflow is worth it when a task outgrows one context window, when verification has to be enforced by structure, or when the orchestration itself is worth keeping.

**By the end of this cookbook, you'll be able to:**

* Decide when a task calls for a dynamic workflow instead of a single agent or subagents
* Trigger a dynamic workflow from the Python Agent SDK and stream its progress
* Read the orchestration script Claude writes and recognize the patterns inside it (fan-out, adversarial verification)

The worked example fact-checks a draft investor update against its source documents. The same shape (many pieces, real judgment, a verification step) shows up in document audits, content migrations, research synthesis, and triage queues.

> **Note:** All company names, metrics, and customer data in this notebook are fictional and generated for demonstration purposes.

##  Prerequisites

**Required knowledge:**

* Python fundamentals, including `async`/`await`
* Familiarity with the Claude Agent SDK basics (`query()` and `ClaudeAgentOptions`). See [notebook 00(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/00_The_one_liner_research_agent.ipynb) if you're new to it.

**Required tools:**

* Python 3.11 or higher
* An Anthropic API key ([get one here(opens in new tab)](https://platform.claude.com/)) in a `.env` file as `ANTHROPIC_API_KEY`

The Agent SDK bundles the Claude Code CLI it drives, and dynamic workflows live in that runtime. They require CLI **v2.1.154 or later**, which `claude-agent-sdk` 0.2.90 and up bundle. The install cell below sets that minimum version, so there is nothing else to set up.

Dynamic workflows are available on all paid plans, with Anthropic API access, and on Amazon Bedrock, Google Cloud's Agent Platform, and Microsoft Foundry; see the [dynamic workflows documentation(opens in new tab)](https://code.claude.com/docs/en/workflows) for the current details.

> **Cost note:** workflows spawn many subagents, so they use meaningfully more tokens than a single-agent session. Running this notebook end to end costs roughly 2to2 to 2to4 in API usage, and more if a stage fails and the run retries. The workflow run prints its cost when it finishes.

##  Setup

Install the SDK and load your API key. The version floor below guarantees an SDK release whose bundled Claude Code CLI supports dynamic workflows, and the next cell checks it. If you upgraded the SDK in a kernel that had already imported an older version, restart the kernel so Python picks up the new one.

%%capture

%pip install -U "claude-agent-sdk>=0.2.90" python-dotenv

import re

import shutil

import time

from pathlib import Path

from dotenv import load\_dotenv

from IPython.display import Markdown, display

import claude\_agent\_sdk

from claude\_agent\_sdk import (

AssistantMessage,

ClaudeAgentOptions,

ResultMessage,

TaskNotificationMessage,

TaskProgressMessage,

TextBlock,

ToolResultBlock,

ToolUseBlock,

UserMessage,

query,

)

load\_dotenv()

MODEL = "claude-sonnet-5"

# Dynamic workflows require Claude Code v2.1.154+; SDK 0.2.90 and later bundle a compatible CLI.

version\_match = re.match(r"(\d+)\.(\d+)\.(\d+)", claude\_agent\_sdk.\_\_version\_\_)

sdk\_version = tuple(int(g) for g in version\_match.groups()) if version\_match else (0, 0, 0)

assert sdk\_version >= (0, 2, 90), (

f"claude-agent-sdk {claude\_agent\_sdk.\_\_version\_\_} is too old for dynamic workflows - "

"re-run the install cell, then restart the kernel"

)

print(f"claude-agent-sdk {claude\_agent\_sdk.\_\_version\_\_}")

```
claude-agent-sdk 0.2.125
```

###  Create the OrbitCart workspace

Our fictional company is **OrbitCart**, an online cycling-gear store. The next cell writes a small workspace to disk: `investor_update.md`, a draft investor update that makes 10 factual claims, and a `sources/` directory holding the ground truth those claims should trace back to (a monthly sales CSV, customer survey results, an uptime report, and a file of press mentions).

The draft has problems planted in it so the workflow has something real to catch:

* **Claims 1, 4, 5, and 6 contradict the sources.** The sales CSV puts Q2 revenue at 4.61M,whichis284.61M, which is 28% above Q1, while the draft claims 4.61M,whichis284.8M and 42%. The survey puts NPS at 62, not 71. The uptime report averages 99.71% for the quarter (including a six-hour May incident), not 99.99%. TechPedal called OrbitCart "one of the fastest-growing online cycling retailers", not "the fastest-growing cycling retailer".
* **Claims 7 and 8 are unverifiable.** No source mentions the June flash sale or support resolution times.
* **Claims 2, 3, 9, and 10 are supported** by at least one source.

Agents work on files, so the data lives on disk, but we create it in the notebook so you can see exactly what the agents will see. After the run we'll compare the workflow's verdicts against this answer key.

WORKSPACE = Path("orbitcart\_data").resolve()

SOURCES = WORKSPACE / "sources"

SOURCES.mkdir(parents=True, exist\_ok=True)

# --- The draft investor update: 10 claims for the fact-check workflow ---

(WORKSPACE / "investor\_update.md").write\_text("""\

# OrbitCart - Q2 2026 Investor Update (DRAFT)

\*Prepared by the founding team. Not yet reviewed.\*

Dear investors,

Q2 was OrbitCart's strongest quarter yet. Highlights:

1. \*\*Revenue:\*\* Q2 revenue reached \*\*$4.8M, up 42% from Q1\*\*.

2. \*\*Order volume:\*\* We processed \*\*over 38,000 orders\*\* in the quarter.

3. \*\*Customers:\*\* Our active customer base grew to \*\*12,400\*\*.

4. \*\*Customer love:\*\* We earned a \*\*Net Promoter Score of 71\*\*.

5. \*\*Reliability:\*\* The platform maintained \*\*99.99% uptime\*\* across the quarter.

6. \*\*Press:\*\* TechPedal called us \*\*"the fastest-growing cycling retailer in North America."\*\*

7. \*\*Growth:\*\* Our June flash sale was \*\*the biggest single sales day in company history\*\*.

8. \*\*Support:\*\* Customer support resolution time improved to \*\*under 4 hours\*\*.

9. \*\*Catalog:\*\* We launched \*\*3 new product categories\*\* this quarter.

10. \*\*Trust:\*\* \*\*Zero customer data was lost\*\* during the brief May service interruption.

We look forward to discussing these results at the board meeting.

- The OrbitCart team

""")

# --- Source documents: the ground truth the claims should trace back to ---

(SOURCES / "monthly\_sales.csv").write\_text("""\

month,revenue\_usd,orders,new\_customers

2026-01,1150000,9800,1020

2026-02,1180000,10100,990

2026-03,1270000,9900,1100

2026-04,1480000,12800,1410

2026-05,1520000,12400,1380

2026-06,1610000,13200,1640

""")

(SOURCES / "customer\_survey.txt").write\_text("""\

OrbitCart Customer Survey - Q2 2026 Results

Survey window: June 10-17, 2026 | Responses: 2,140

Net Promoter Score (NPS): 62 (Q1: 58)

Active customers at end of Q2: 12,400

Support satisfaction (CSAT): 4.4 / 5

Selected verbatim feedback:

- "Ordering was painless and the bike arrived two days early." (Pro customer, Denver)

- "Great selection, but I wish there were more filter options." (Free customer, Toronto)

- "The team plan made it easy to outfit our whole shop." (Team customer, Portland)

""")

(SOURCES / "uptime\_report.txt").write\_text("""\

OrbitCart Platform Reliability Report - Q2 2026

April 2026: 99.97% uptime, no incidents

May 2026: 99.18% uptime

- May 14: checkout degraded for 5h 58m during a database failover.

No customer data was lost. Root cause: connection pool exhaustion.

June 2026: 99.98% uptime, no incidents

Quarter average: 99.71%

""")

(SOURCES / "press\_coverage.md").write\_text("""\

# Press mentions - Q2 2026

## TechPedal, May 3, 2026

"OrbitCart has quietly become one of the fastest-growing online cycling retailers

in North America, on the strength of a no-friction checkout and a generous

returns window."

## Gear & Grease Weekly, June 21, 2026

"The Portland-based startup recently expanded into bike maintenance tools, indoor

training equipment, and cycling apparel - three categories that traditional bike

shops have struggled to move online."

""")

print(f"Workspace: {WORKSPACE.name}/")

print(f"Investor update claims: 10 | Source documents: {len(list(SOURCES.iterdir()))}")

```
Workspace: orbitcart_data/
Investor update claims: 10 | Source documents: 4
```

##  Subagents vs. workflows

The Agent SDK already gives you two ways to run a multi-step task, and dynamic workflows add a third. The difference between them comes down to one question: **who holds the plan?**

|  | Single agent | Subagents | Dynamic workflow |
| --- | --- | --- | --- |
| **What it is** | One agent works step by step | Workers the lead agent spawns | A script the runtime executes |
| **Who decides what runs next** | Claude, turn by turn | Claude, turn by turn | The script |
| **Where intermediate results live** | Claude's context window | The lead agent's context window | Script variables |
| **What's repeatable** | The prompt | The worker definitions | The orchestration itself |
| **Scale** | One context window | A few delegated tasks per turn | Dozens to hundreds of agents per run |
| **Interruption** | Restarts the turn | Restarts the turn | Resumable within the same session |

With **subagents** (the pattern from [notebook 01(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb)), Claude is the orchestrator. It decides turn by turn what to delegate, and nothing guarantees that it delegates every piece, combines the results at the end, or verifies anything. Every worker's result lands back in the lead agent's context, which is fine for four delegations but not for four hundred. The plan also lives only in Claude's context: interrupt the run and the work restarts from scratch.

A **dynamic workflow** flips each of those properties. A script decides what runs, intermediate results live in script variables, and the script itself is an artifact you can read, save, edit, and re-run. The price is tokens, since a workflow spawns many subagents. Reach for one when the task is **bigger than one context window**, when you want **verification enforced by structure**, or when **the orchestration itself is worth keeping**.

##  Anatomy of a dynamic workflow

Triggering a workflow from the Agent SDK takes two things:

1. **Allow the `Workflow` tool** in `allowed_tools`. This is the tool Claude calls to launch a workflow; the SDK auto-approves tools on this list.
2. **Ask for a workflow in your prompt** in plain words: "use a workflow to…". Claude treats a direct request like that as an opt-in to orchestration-as-a-script instead of turn-by-turn work. (The interactive CLI adds a keyword trigger and an `/effort ultracode` mode; from the SDK, a plainly worded request is all you need.)

When Claude calls the `Workflow` tool, it passes a complete JavaScript orchestration script it wrote for your task. The runtime executes that script **in the background**: your `query()` stream stays live and progress events flow back while agents run. Because the launch is one turn and the completion is another, the stream yields a `ResultMessage` for each turn. The last one carries the final result, and the `run_agent()` helper below keeps that one. In the SDK there are no interactive permission prompts. Tool calls follow the permission rules you configure, which is why we set an explicit `allowed_tools` list. (You may still see a read-only call such as `Bash` succeed outside the allowlist: non-interactive runs auto-allow read-only commands and deny the rest.) The subagents the workflow spawns run in `acceptEdits` mode and inherit that allowlist.

Three things are worth knowing before the first run:

* **The script is a real artifact.** The runtime writes it to a file under your session's directory in `~/.claude/projects/` and includes the path in the tool result, so `run_agent()` below can capture it. We read the script after the run.
* **Findings return to the script instead of landing in report files.** Workflow agents hand back what they find as their return value, which is how the results reach script variables. In our runs, an agent that tried to write a report-style file such as `SUMMARY.md` was told to return the content instead. Real work products (converted documents, code, data files) write to disk normally.
* **Runs can fail and resume.** If a stage fails mid-run (for example an agent exhausting its structured-output retries), you'll see a `[Failed]` notification in the log and Claude typically relaunches the workflow. Agents that already completed return cached results, so the retry mostly redoes the failed stage; expect the cost to rise accordingly. That is the resumability at work, not a broken notebook.
* **Behavior and limits.** A workflow runs up to 16 agents concurrently (fewer on machines with limited CPU cores) and at most 1,000 agents per run. The orchestration script itself can't touch your filesystem or shell; only the agents it spawns can. A stopped run is resumable within the same session; a new session starts it fresh.

We hand-roll a small logger here instead of reusing the folder's `agent_visualizer` helpers, because workflows emit `TaskProgressMessage` and `TaskNotificationMessage` events those helpers don't cover. The next cell defines the helpers we'll use for the run: `run_agent()` streams a query and prints a compact activity log, `workflow_options()` builds the `ClaudeAgentOptions`, and `show_script()` displays the orchestration script Claude generated.

# The Workflow tool result mentions the persisted script path and task ID in plain

# text; these regexes scrape it. A convenience for this demo, not a stable API.

SCRIPT\_PATH\_RE = re.compile(r"Script file: (.+?\.js)")

TASK\_ID\_RE = re.compile(r"Task ID: (\S+)")

async def run\_agent(prompt: str, options: ClaudeAgentOptions) -> dict:

"""Stream a query through the Agent SDK and print a compact activity log.

Returns a dict with the final result text, the total cost, and - when a

workflow ran - the path of the orchestration script Claude generated.

"""

info = {"result": None, "cost\_usd": None, "script\_path": None}

last\_tool\_count = 0 # throttle progress lines

started = time.monotonic()

async for msg in query(prompt=prompt, options=options):

if isinstance(msg, AssistantMessage):

for block in msg.content:

if isinstance(block, TextBlock):

# Show the first line of Claude's narration

if narration := block.text.strip():

print(f"\nClaude: {narration.splitlines()[0]}")

elif isinstance(block, ToolUseBlock):

if block.name == "Workflow":

script = block.input.get("script", "")

n\_lines = len(script.splitlines())

print(

f"\n[Workflow tool] Claude wrote a {n\_lines}-line orchestration script"

)

else:

print(f" -> {block.name}")

elif isinstance(msg, UserMessage):

blocks = msg.content if isinstance(msg.content, list) else []

for block in blocks:

if not isinstance(block, ToolResultBlock):

continue

text = block.content if isinstance(block.content, str) else str(block.content)

if match := SCRIPT\_PATH\_RE.search(text):

info["script\_path"] = match.group(1)

task = TASK\_ID\_RE.search(text)

task\_id = task.group(1) if task else "?"

print(f"[Launched] Workflow running in the background (task {task\_id})")

elif isinstance(msg, TaskProgressMessage):

# Progress arrives every few seconds; print a line every ~8 new agent tool calls

tools = msg.usage.get("tool\_uses", 0)

if tools - last\_tool\_count >= 8:

last\_tool\_count = tools

tokens = msg.usage.get("total\_tokens", 0)

seconds = msg.usage.get("duration\_ms", 0) / 1000

print(

f" ... {tools:>3} agent tool calls | {tokens:>9,} tokens | {seconds:>4.0f}s"

)

elif isinstance(msg, TaskNotificationMessage):

print(f"[{msg.status.capitalize()}] {msg.summary}")

elif isinstance(msg, ResultMessage):

# A background workflow yields one result per turn: the launch turn, then the

# final turn after the workflow completes. Keep the latest and report once.

info["result"] = msg.result

info["cost\_usd"] = msg.total\_cost\_usd

cost = f" | ${info['cost\_usd']:.2f}" if info["cost\_usd"] is not None else ""

minutes = (time.monotonic() - started) / 60

print(f"\n=== Run complete in {minutes:.1f} min{cost} ===")

return info

def show\_script(info: dict) -> None:

"""Render the orchestration script Claude generated during a run."""

path = info.get("script\_path")

if not path or not Path(path).exists():

print("No workflow script was generated in this run.")

return

display(Markdown(f"```javascript\n{Path(path).read\_text()}\n```"))

def workflow\_options() -> ClaudeAgentOptions:

"""ClaudeAgentOptions for a workflow-enabled agent working in the OrbitCart workspace."""

return ClaudeAgentOptions(

cwd=str(WORKSPACE),

model=MODEL,

allowed\_tools=["Read", "Write", "Edit", "Glob", "Grep", "Workflow"],

permission\_mode="acceptEdits",

max\_turns=40,

)

##  Example: fact-check the investor update

**The job:** legal won't sign off on `investor_update.md` until every claim is traced to a source document. There are 10 claims and four source files.

**Why a workflow:** a single agent checking 10 claims accumulates every source document in its context and starts skimming by claim 7. "Double-check your findings" is also just an instruction, and under context pressure it gets skipped. The workflow below makes verification *structural*:

1. **Extract:** one agent reads the draft and pulls out every factual claim
2. **Verify:** one agent *per claim*, each reading the sources fresh in its own clean context
3. **Adversarial check:** a skeptic agent challenges every verdict before it's accepted
4. **Report:** one agent compiles the verdicts into a go/no-go report

This is the **fan-out + adversarial verification** pattern. Notice how much of the prompt below describes the *shape* of the work rather than the task itself. With workflows, the prompt describes the harness you want.

FACT\_CHECK\_PROMPT = """\

Use a workflow to fact-check the draft investor update at investor\_update.md against

the source documents in sources/.

Structure the workflow exactly like this:

1. EXTRACT: one agent reads investor\_update.md and extracts its ten numbered

highlights as structured output (claim number, claim text). Keep the draft's own

numbering 1-10 and treat each numbered highlight as exactly one claim, even when it

bundles two figures.

2. VERIFY: one agent per claim, running in parallel. Each verifier reads the source

documents in sources/ and returns a verdict as structured output:

- "confirmed" if a source directly supports the claim (quote the supporting line)

- "contradicted" if a source conflicts with it (quote the conflicting line and

state the correct figure)

- "unverifiable" if no source covers it

Verifiers must quote the exact lines they relied on. Pay attention to subtle

differences between what a source says and what the draft claims it says.

3. SKEPTIC: for every "confirmed" verdict, one skeptic agent re-reads the cited

source and tries to refute the confirmation. If the skeptic finds the citation

does not actually support the claim, the verdict changes to "contradicted".

4. REPORT: one final agent compiles a markdown fact-check report: a table of every

claim with its verdict and evidence, then a summary of what must be fixed before

the update can be sent. Return this report as the workflow result.

The working directory is already set to the folder containing these files. Refer to

every file by relative path (e.g. investor\_update.md, sources/monthly\_sales.csv) in

the script and in agent prompts; do not embed absolute paths.

"""

factcheck\_info = await run\_agent(FACT\_CHECK\_PROMPT, workflow\_options())

```
-> Bash

  -> Read

  -> Read

  -> Read

  -> Read

[Workflow tool] Claude wrote a 152-line orchestration script
[Launched] Workflow running in the background (task wr1292rh8)

Claude: The fact-check workflow is running in the background (task `wr1292rh8`, run `wf_1072dc96-6a2`). It's fanning out: extract the 10 claims → verify each in parallel against `sources/` → adversarially re-check every "confirmed" verdict → compile the final markdown report. I'll let you know as soon as it completes.

    ...   8 agent tool calls |   304,709 tokens |   13s

    ...  16 agent tool calls |   371,890 tokens |   13s

    ...  24 agent tool calls |   371,890 tokens |   14s

    ...  32 agent tool calls |   384,996 tokens |   17s

    ...  40 agent tool calls |   469,806 tokens |   23s

    ...  48 agent tool calls |   543,126 tokens |   30s

    ...  56 agent tool calls |   549,412 tokens |   42s

[Completed] Dynamic workflow "Fact-check the OrbitCart investor update against source documents" completed

Claude: The fact-check workflow finished. Here's the report:

=== Run complete in 2.5 min | $3.29 ===
```

display(Markdown(factcheck\_info["result"] or "\_(no result returned)\_"))

```
<IPython.core.display.Markdown object>
```

Check the verdicts against the answer key, the wrinkles we planted in the data:

| Claim | Planted truth |
| --- | --- |
| 1. "$4.8M, up 42%" | **Contradicted.** The CSV totals 4.61MforQ2,up284.61M for Q2, up 28% from Q1's 4.61MforQ2,up283.6M |
| 4. "NPS of 71" | **Contradicted.** The survey says 62 |
| 5. "99.99% uptime" | **Contradicted.** The reliability report says 99.71%, with a 6-hour May incident |
| 6. TechPedal quote | **Contradicted.** The article says "*one of* the fastest-growing *online* cycling retailers", not "the fastest-growing" |
| 7. Flash sale, 8. Support times | **Unverifiable.** No source covers either |
| 2, 3, 9, 10 | **Supported by a source** |

Claim 6 is the one worth dwelling on. A single rushed agent often glosses over the difference between "the fastest-growing" and "one of the fastest-growing." A dedicated verifier with nothing else in its context, then challenged by a skeptic, is much harder to slip past. That precision comes from the structure of the workflow rather than from a smarter model.

Don't be surprised if the workflow comes back *stricter* than our answer key on the supported claims. Claims 3, 9, and 10 are the kind a skeptic pass tends to challenge: the survey confirms the 12,400 figure but no source establishes a prior baseline for "grew" (claim 3); the press article says the company "recently expanded" into three categories without confirming the launches happened *within Q2* (claim 9); and while no data was lost in May, a skeptic may object to calling a six-hour outage a "brief" interruption (claim 10). Whether your run confirms them or flags them, that's the adversarial check doing its job. An over-strict flag costs a minute of human review; an under-strict pass costs credibility with investors.

###  Reading the script Claude wrote

The most instructive artifact is the script itself, because it shows how the work was organized. The `Workflow` tool result included a path to the persisted script, and `run_agent()` captured it. As you read the script, note the `schema` option that forces verifiers to return structured verdicts, and the plain-JavaScript logic between phases: routing only the confirmed verdicts to skeptics costs zero tokens.

show\_script(factcheck\_info)

```
<IPython.core.display.Markdown object>
```

###  How to read a workflow script

Every workflow script uses the same building blocks. The full option set is documented in the Workflow tool entry of the [Agent SDK reference(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/typescript), but you can learn most of it by mapping the common primitives to what you see above:

| Primitive | What it does |
| --- | --- |
| `export const meta = {name, description, phases}` | Declares the workflow's name and phases; the progress UI groups agents under these phases |
| `agent(prompt, options)` | Spawns one subagent with a **clean context**: it sees only the prompt string it's given, nothing else. Options can set a `label`, a `phase`, a JSON `schema` for structured output, and a `model` |
| `parallel([...])` | Runs a batch of agents concurrently and **waits for all of them** (a barrier) before continuing |
| `pipeline(items, stage1, stage2, ...)` | Runs each item through a sequence of stages **independently**, so item A can be in stage 2 while item B is still in stage 1 |
| `phase("...")` | Marks which phase the following agents belong to |
| Plain JavaScript between calls | Filtering, deduplication, merging, and loops, all exact, instant, and free of token cost |
| `return {...}` | Whatever the script returns is what comes back to your session |

Three properties fall out of this design:

1. **The plan is enforced by code.** The skeptic pass runs after the verifiers because the script's control flow sequences it that way. Nothing depends on Claude remembering an instruction.
2. **Claude's context stays clean.** Every verdict and quoted source line lived in script variables. Only the final compiled report reached the session that launched the workflow.
3. **The script is yours.** It's a file on disk. You can read it (we just did), edit it, save it into a project's `.claude/workflows/` directory, and re-run it by name. The orchestration becomes a reusable asset for your team.

##  When to reach for a workflow

Dynamic workflows sit at the top of the difficulty curve; single agents and subagents remain the right tools below it. A reasonable decision guide:

| Reach for... | When... |
| --- | --- |
| **A single agent** | The task fits in one context window and doesn't need independent verification. Most tasks live here. |
| **Subagents** | You need a few specialized workers (a researcher, a reviewer) and the lead agent should adapt the plan as results come in |
| **A dynamic workflow** | The task outgrows one context window (many items, many sources), needs verification you can't afford to skip, or is a process you'll repeat |

Three cost-control habits worth keeping from this notebook:

1. **Be explicit about structure in the prompt.** The harness you describe is the harness you get, including how much verification runs and which stages could use a cheaper model.
2. **Watch the per-run cost.** The run above printed one. Workflows that verify everything cost more than workflows that verify nothing, and that dial is set in the prompt.
3. **Keep the data scale honest.** We used 10 claims and four sources so this notebook runs in minutes. The same structure scales to hundreds of items. The script doesn't mind the size; your token budget does.

##  Cleanup

Remove the workspace this notebook created. Skip this cell if you want to poke around the files and the fact-check evidence first, and re-run the workspace-creation cell before running the fact-check again.

shutil.rmtree(WORKSPACE, ignore\_errors=True)

print("Workspace removed.")

```
Workspace removed.
```

##  What you learned

Mapping back to the objectives from the introduction:

* **When to use a workflow:** when the task outgrows one context window, when verification must be structural instead of optional, or when the orchestration is worth keeping. Single agents and subagents remain the right tool below that line.
* **How to trigger one from the Agent SDK:** allow the `Workflow` tool in `allowed_tools`, ask for a workflow in the prompt, and stream the run (launch, progress events, completion) through `query()`.
* **How to read the scripts Claude writes:** `meta` declares phases, `agent()` spawns clean-context workers, `parallel()` is a barrier, `pipeline()` streams items through stages, and plain JavaScript handles the logic in between for free. The fact-check used **fan-out + adversarial verification**; the same primitives compose into pipelines, tournaments, and triage queues.
* **How to make a workflow reusable:** the script is a file. Save it into a project's `.claude/workflows/` directory, commit it, and anyone (or any agent) working in that project can re-run the same orchestration by name.

##  Next steps

* **Point the pattern at your own data.** The fact-check workflow works on any claims-vs-sources problem: reports, marketing copy, documentation. The same structure (extract, verify in parallel, challenge, compile) carries to content migrations, triage queues, and "rank many things by judgment" problems.
* **Try a workflow in the Claude Code CLI**, where you can watch runs interactively with `/workflows` and save them with a keystroke. See the [dynamic workflows documentation(opens in new tab)](https://code.claude.com/docs/en/workflows).
* **Compare with the other orchestration approaches in this series:** [notebook 01(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/01_The_chief_of_staff_agent.ipynb) covers subagents in depth, and the [Building Effective Agents patterns(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/../patterns/agents/README.md) show the same orchestration ideas implemented directly against the Messages API.
* **Read the Anthropic engineering blog on multi-agent systems**, [How we built our multi-agent research system(opens in new tab)](https://www.anthropic.com/engineering/multi-agent-research-system), for the research behind when multi-agent setups beat single agents and what they cost.
