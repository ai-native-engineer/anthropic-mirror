<!-- source: https://platform.claude.com/cookbook/patterns-agents-latency-multi-agent -->

#  Multi-agent teams under latency pressure and budgets

Our multi-agent team consists of a lead agent with the ability to spawn helper agents to work
on parts of a task in parallel. Left to itself, a team optimizes for thoroughness, not speed:
nothing in any agent's context says how long the person asking has been waiting, or how long
they are willing to wait. In this cookbook, we will elicit Claude's time awareness to accomplish
tasks faster.

**By the end of this cookbook, you'll be able to:**

* Show every agent on a team the same running clock, without breaking prompt caching
* Make a team work faster with one sentence of latency pressure, or pace itself against a
  latency budget
* Check from a run's own log that every agent saw the clock

We first make Claude aware of how much time has elapsed, with nothing but the Messages API:

1. **One shared team clock**, started when the task starts.
2. **Every agent sees the clock before every turn.** Each time we call the API for *any* agent,
   we append one short line, `[elapsed 252s]`, to the end of the newest user message (the
   task prompt on the first turn, the tool results after that). A helper spawned three minutes
   into the task sees `[elapsed 182s]` on its very first turn, not `0s`, because the clock
   belongs to the team, not to the agent.

We then give Claude a sense of urgency, through one of two approaches:

1. **Latency pressure:** One sentence at the end of the task prompt, and of every
   helper's brief, says that time matters. That sentence is the only difference from the stock
   prompts.
2. **Latency budget:** An augmented clock carries a budget alongside the elapsed time,
   e.g. `[elapsed 252s / 600s]`. No prompt text comes with it: the second
   number is all any agent is told about the budget.

That is the whole mechanism, and it gives three arms to compare: no clock at all, the clock with
pressure, and the clock with a budget.

> **A note on models.** Latency incentives are a newly emerging way to steer Claude. This notebook
> defaults to `claude-fable-5-1`. The approach has not been fully tested on Claude Opus 5 and earlier
> models, so expect the effect to vary if you change `COOKBOOK_MODEL`.

There is no task built in. You bring the tools, the prompts and the question; a short smoke test
at the end shows the clock reaching every agent.

The orchestration (message hub, messaging tools, spawn tools, agent loop) follows the
[Async multi-agent orchestration(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/async_multi_agent_orchestration.ipynb) cookbook; start there
if the shape is unfamiliar.

##  Prerequisites

* Python 3.11 or newer.
* Required knowledge: comfortable reading `async`/`await` Python (tasks, events, timeouts), and
  familiar with the Messages API tool-use loop (a model turn, its tool calls, the tool results you
  send back). The [Async multi-agent orchestration(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/async_multi_agent_orchestration.ipynb)
  cookbook covers the team mechanics this one builds on.
* A Claude API key in `ANTHROPIC_API_KEY` (or a `.env` file).
* Some API credit. Each run is a lead plus up to four helpers, each making several calls. We have
  capped calls to fifteen per helper and forty for the lead. Running the
  notebook top to bottom is one short team run on `claude-fable-5-1` at effort
  `xhigh`, about a minute.
* Headroom on your rate limits. Up to five agents call the API at once, and on a lower tier the
  SDK's automatic retries show up as extra wall-clock time rather than as errors.

%%capture

%pip install -qU anthropic python-dotenv

import asyncio

import itertools

import os

import re

import time

from collections import Counter, defaultdict

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

client = anthropic.AsyncAnthropic() # reads ANTHROPIC\_API\_KEY from the environment

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-fable-5-1") # every agent; any current model

EFFORT = os.environ.get("COOKBOOK\_EFFORT", "xhigh") # low | medium | high | xhigh | max

USER\_ID = os.environ.get("COOKBOOK\_USER\_ID") # optional: sent as metadata.user\_id if set

MAX\_HELPERS = 4 # cap on concurrently running helpers (a cost guard, not part of the mechanism)

PROGRESS\_EVERY = 30 # seconds between the progress lines a run prints; None prints none

##  The team clock

A stopwatch and a one-line renderer. There is **one** clock object per
task and every agent on the team holds a reference to it. That is what makes a late-spawned
helper see the team's elapsed time rather than its own. The optional budget lives on the same
object, so it is the team's too: a helper spawned 182 seconds into a 600-second budget sees
`[elapsed 182s / 600s]`, not a fresh 600 seconds of its own.

The line is rendered in one place, `clock_line`, in whole seconds, so that with a budget both
numbers are in the same unit and what is left is one subtraction. The square brackets are only
there to set the line apart from the prompt or tool result it follows.

def clock\_line(elapsed: float, budget: float | None = None) -> str:

"""The line the agents see: '[elapsed 192s]', or '[elapsed 192s / 600s]' with a budget."""

line = f"elapsed {round(elapsed)}s"

if budget is not None:

line += f" / {round(budget)}s"

return f"[{line}]"

class TeamClock:

def \_\_init\_\_(self, budget: float | None = None):

self.start = time.monotonic()

self.budget = budget # in seconds; shown on the line when set, never enforced

@property

def elapsed(self) -> float:

return time.monotonic() - self.start

def note(self) -> str:

return clock\_line(self.elapsed, self.budget)

def stamp\_elapsed(messages: list[dict], clock: TeamClock) -> str:

"""Append the clock line to the end of the newest user message, and return the line.

After the task prompt it is a text block of its own; after tool results it extends the last

result's text. Earlier lines stay in the history, so an agent can see how long each of its

own steps took.

"""

line = clock.note()

last = messages[-1]

content = last["content"]

if isinstance(content, str): # the task prompt: add the line as its own text block

last["content"] = [{"type": "text", "text": content}, {"type": "text", "text": line}]

elif content and content[-1].get("type") == "tool\_result": # tool results: extend the last

content[-1]["content"] += f"\n\n{line}"

else:

content.append({"type": "text", "text": line})

return line

print(clock\_line(192), " with a 600-second budget:", clock\_line(192, 600))

demo\_clock = TeamClock()

demo\_clock.start -= 192 # pretend 192 seconds have passed

demo\_messages = [{"role": "user", "content": "Find the best settings for our process."}]

stamp\_elapsed(demo\_messages, demo\_clock)

demo\_messages # this is exactly what the model receives on a first turn

```
[elapsed 192s]    with a 600-second budget: [elapsed 192s / 600s]

[{'role': 'user',
  'content': [{'type': 'text',
    'text': 'Find the best settings for our process.'},
   {'type': 'text', 'text': '[elapsed 192s]'}]}]
```

##  The hub and the coordination tools

**Coordination tools** are the client-side ones from the orchestration cookbook: every agent
can `send_message` / `wait_for_message` through an in-memory hub, and the lead can
`create_subagents`. A helper's final answer is delivered to the lead
automatically when the helper finishes. The hub also keeps the run's per-agent tool-call counts
and its log.

def tool(name: str, description: str, properties: dict, required: list[str]) -> dict:

schema = {"type": "object", "properties": properties, "required": required}

return {"name": name, "description": description, "input\_schema": schema}

SEND\_MESSAGE = tool(

"send\_message",

"Send a message to one or more other agents on your team. It is appended to their next "

"tool result.",

{

"recipient\_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},

"content": {"type": "string"},

},

["recipient\_ids", "content"],

)

WAIT\_FOR\_MESSAGE = tool(

"wait\_for\_message",

"Block until another agent messages you or a helper finishes. Messages also arrive appended "

"to the result of any other tool call.",

{},

[],

)

CREATE\_SUBAGENTS = tool(

"create\_subagents",

"Spawn helper agents that work in parallel with you. Returns immediately with their ids. "

"Each helper gets base\_instruction plus its own entry of per\_helper\_instructions, has the "

"same task tools as you, and reports its findings back to you when it finishes.",

{

"base\_instruction": {"type": "string"},

"per\_helper\_instructions": {

"type": "array",

"items": {"type": "string"},

"minItems": 1,

"maxItems": MAX\_HELPERS,

},

},

["base\_instruction", "per\_helper\_instructions"],

)

class Hub:

"""One run's shared state: an inbox and an event per agent, plus the run's counts and log."""

def \_\_init\_\_(self):

self.inbox: dict[str, list[dict]] = defaultdict(list)

self.event: dict[str, asyncio.Event] = defaultdict(asyncio.Event)

self.status: dict[str, str] = {}

self.usage: dict[str, Counter] = defaultdict(Counter) # per-agent task-tool call counts

self.log: list[dict] = [] # every agent's progress entries; run\_team returns them

self.\_ids = itertools.count(1)

def register(self, name: str) -> str:

self.status[name] = "active"

return name

def new\_helper\_name(self) -> str:

return self.register(f"helper{next(self.\_ids)}")

def post(self, sender: str, recipients: list[str], content: str) -> list[str]:

delivered = []

for rid in recipients:

if self.status.get(rid) in ("active", "waiting"): # a finished agent reads nothing

self.inbox[rid].append({"from": sender, "content": content})

self.event[rid].set()

delivered.append(rid)

return delivered

def drain(self, name: str) -> str:

msgs, self.inbox[name] = self.inbox[name], []

self.event[name] = asyncio.Event()

if not msgs:

return ""

body = "\n".join(

f'<agent-message from="{m["from"]}">\n{m["content"]}\n</agent-message>' for m in msgs

)

return f"\n\n[Messages received while you were working:]\n{body}"

##  Your task tools

This is the part to fill in. `TASK_TOOLS` is the list of tool definitions every agent gets (built
with the same small `tool` helper), and `make_task_handlers(hub)` returns the functions that run
them, one `async fn(agent, input)` per tool name, created fresh for each run. Both start empty, so
out of the box the team works from the model's own knowledge. The commented template shows the
shape of one tool.

> **Note: Client-side tools keep the clock fresh.** The harness can only add a clock line between API calls. While a
> response is being sampled on the server, including any server-side tools it runs there, nothing can
> be injected, so the agent works from the last clock line it saw until the call returns. Each
> client-side tool call hands control back to the harness, and the next request carries an updated line.
> The more of an agent's work goes through client-side tools, the more up-to-date its clock stays.

TASK\_TOOLS: list[dict] = [] # your tool definitions: every agent on the team gets them

def make\_task\_handlers(hub: Hub) -> dict:

"""The functions behind TASK\_TOOLS for one run: {tool name: async fn(agent, input) -> str}."""

return {}

# A template for one client-side tool. `agent` is the calling agent's name ("lead", "helper2", ...).

#

# TASK\_TOOLS = [

# tool(

# "lookup\_record",

# "Look up one record by its key in the records system. Takes a few seconds.",

# {"key": {"type": "string"}},

# ["key"],

# )

# ]

#

#

# def make\_task\_handlers(hub: Hub) -> dict:

# async def lookup\_record(agent: str, args: dict) -> str:

# return await records.get(args["key"]) # your own code goes here

#

# return {"lookup\_record": lookup\_record}

##  The agent loop, and where the clock goes

One coroutine runs any agent, lead or helper. It is an ordinary tool-use loop with two
additions, both marked in the code:

* **Right before every API call**, `stamp_elapsed` appends the team clock line to the newest
  user message. On the first turn that message is the task prompt, so the agent knows the
  elapsed time before it does anything. Afterwards the line goes at the end of the last tool
  result, next to any messages from other agents. Because the stamp happens at send time,
  time spent waiting on helpers or on a slow tool shows up too.
* **When a helper finishes**, its final text is posted to the lead's inbox. Before that, it reads any
  message that reached it while it worked, so a redirect from the lead is not lost.

Two API details. The response `content` (which can include thinking) goes into the history
exactly as returned; only client-side `tool_use` blocks need a `tool_result` from us. And the
top-level `cache_control` turns on
[automatic prompt caching(opens in new tab)](https://platform.claude.com/docs/en/build-with-claude/prompt-caching),
which matters for agents whose history fills up with tool results; because the clock line is
appended at the tail, everything before it is normally still a cache hit on the next call.

An agent's tool calls from one turn run concurrently. The loop also writes what each agent was
shown into the run's log (`[task]`, `[clock]` and `[report]` entries), which the last section
reads back.

TASK\_TOOL\_NAMES = {t["name"] for t in TASK\_TOOLS}

def log(hub: Hub, clock: TeamClock, name: str, text) -> None:

"""Record one progress entry on the run's hub. Nothing is printed."""

text = " ".join(str(text).split())

hub.log.append({"seconds": round(clock.elapsed), "agent": name, "text": text})

async def call\_tool(hub: Hub, clock: TeamClock, name: str, block, dispatch: dict) -> dict:

"""Run one of an agent's tool calls and return the tool\_result block for it."""

if block.name == "send\_message":

ids = block.input["recipient\_ids"]

sent = hub.post(name, ids, block.input["content"])

missed = [r for r in ids if r not in sent]

out = f"delivered to {sent or 'no one'}" + (f"; not running: {missed}" if missed else "")

elif block.name == "wait\_for\_message":

hub.status[name] = "waiting"

try:

await asyncio.wait\_for(hub.event[name].wait(), timeout=90)

out = "new messages below"

except TimeoutError:

out = "no messages yet (waited 90s)"

hub.status[name] = "active"

elif block.name in dispatch:

if block.name in TASK\_TOOL\_NAMES:

hub.usage[name][block.name] += 1

out = await dispatch[block.name](name, block.input)

else:

out = f"error: unknown tool {block.name}"

log(hub, clock, name, f"-> {block.name}({block.input}) = {out}")

return {"type": "tool\_result", "tool\_use\_id": block.id, "content": out}

async def run\_agent(

hub: Hub,

clock: TeamClock,

name: str,

\*,

system: str,

task: str,

tools: list[dict],

dispatch: dict,

report\_to: str | None = None,

show\_clock: bool = True,

max\_turns: int = 40,

) -> str:

"""Run one agent to completion and return its final text."""

messages = [{"role": "user", "content": task}]

log(hub, clock, name, f"[task] {task}") # what this agent was asked, kept for the run's log

final = f"[{name} stopped after max\_turns={max\_turns}]"

try:

for \_ in range(max\_turns):

if show\_clock:

line = stamp\_elapsed(messages, clock) # <- addition 1: the clock, before every call

log(hub, clock, name, f"[clock] {line}")

resp = await client.messages.create(

model=MODEL,

max\_tokens=16000, # the SDK rejects large non-streaming requests; stream for more

system=system,

tools=tools,

messages=messages,

cache\_control={"type": "ephemeral"}, # automatic prompt caching

output\_config={"effort": EFFORT},

\*\*({"metadata": {"user\_id": USER\_ID}} if USER\_ID else {}),

)

messages.append({"role": "assistant", "content": resp.content})

texts = [b.text for b in resp.content if b.type == "text" and b.text.strip()]

for text in texts:

log(hub, clock, name, text)

calls = [b for b in resp.content if b.type == "tool\_use"]

if resp.stop\_reason != "tool\_use" or not calls: # end\_turn (or max\_tokens): finished

# On a normal end of turn, a helper first reads whatever reached it while it worked,

# so a redirect or a follow-up from the lead is handled rather than lost.

mail = hub.drain(name) if report\_to and resp.stop\_reason == "end\_turn" else ""

if mail:

messages.append({"role": "user", "content": mail.lstrip()})

continue

final = texts[-1].strip() if texts else f"[{name} ended with {resp.stop\_reason}]"

if resp.stop\_reason == "max\_tokens": # cut off: say so, or it reads as a fast run

final = f"[{name} hit max\_tokens; answer truncated] {final}"

break

# one turn's tool calls run concurrently

results = await asyncio.gather(

\*(call\_tool(hub, clock, name, b, dispatch) for b in calls)

)

results[-1]["content"] += hub.drain(name) # the inbox rides on the last result

messages.append({"role": "user", "content": list(results)})

hub.status[name] = "done"

except asyncio.CancelledError:

hub.status[name] = "cancelled"

raise

except Exception as e: # a crashed helper should not take the team down

hub.status[name] = "crashed"

final = f"[{name} crashed: {e!r}]"

log(hub, clock, name, final)

if report\_to is None:

raise

if report\_to: # <- addition 2: a finished helper reports to the lead automatically

hub.post(name, [report\_to], f"(final report)\n{final}")

log(hub, clock, name, f"[report] delivered to {report\_to}")

return final

##  Prompts

* `TIME_MATTERS` is appended once to the lead's task **and** to every helper's brief. It is the
  only difference between the stock prompts and the pressured ones. We have experimented with a
  number of phrases and believe this one offers an acceptable balance between latency and quality.
* A budget adds **no prompt text**. With `latency_budget_seconds` set, the clock line gains a
  second number, `[elapsed 252s / 600s]`, and that is all any agent is told about it.
* The system prompts say nothing about time.

`run_team(question)` runs the stock team with no clock. `latency_pressure=True` adds the clock and
the sentence; `latency_budget_seconds=N` adds the clock with the budget on it. They are separate
arms, so asking for both raises an error. A run prints a progress line every `PROGRESS_EVERY`
seconds and returns the answer, the wall-clock seconds, per-agent tool-call counts and the full
log.

TIME\_MATTERS = (

"\n\nTime matters here: do not spend time that can be avoided, and the earlier a correct "

"result is obtained, the better."

)

LEAD\_SYSTEM = (

"You are the lead of a small team. You can work on the task yourself, and you can spawn up to "

f"{MAX\_HELPERS} helper agents with create\_subagents to work on parts of it in parallel; each "

"helper has the same task tools as you and reports back to you when it finishes (use "

"wait\_for\_message to collect reports, send\_message to redirect a helper). Decompose the task, "

"delegate the independent parts, check what comes back, and finish with a short final answer "

"that states the answer on its first line."

)

HELPER\_SYSTEM = (

"You are {name}, a helper on a team led by the agent 'lead'. Do exactly what your brief asks. "

"When you are done, reply with your findings: the answer first, then the key evidence. That "

"final reply is delivered to the lead automatically. If the lead messages you a follow-up, "

"handle it the same way."

)

def total\_calls(hub: Hub) -> int:

return sum(sum(counts.values()) for counts in hub.usage.values())

async def run\_team(

question: str,

\*,

latency\_pressure: bool = False,

latency\_budget\_seconds: float | None = None,

) -> dict:

"""Run one of three arms, never a mix.

no clock (the default): the stock prompts, and no clock line.

pressure (latency\_pressure=True): the time-matters sentence, and the clock line.

budget (latency\_budget\_seconds=N): the clock line with the budget on it, and no sentence.

"""

budget = latency\_budget\_seconds

if budget is not None and budget < 1:

raise ValueError("latency\_budget\_seconds must be at least 1 (it is in seconds), or None")

if latency\_pressure and budget is not None:

raise ValueError("pressure and a budget are separate arms: pass one or the other")

hub, clock = Hub(), TeamClock(budget) # one clock, and one budget, for the whole team

hub.register("lead")

helpers: dict[str, asyncio.Task] = {}

show\_clock = latency\_pressure or budget is not None

# Pressure adds one sentence to each prompt. A budget adds no words: only the clock line

# changes, and TeamClock already carries the budget.

time\_matters = TIME\_MATTERS if latency\_pressure else ""

task\_handlers = make\_task\_handlers(hub)

async def create\_subagents(agent: str, args: dict) -> str:

briefs = args["per\_helper\_instructions"]

free = MAX\_HELPERS - sum(not t.done() for t in helpers.values())

spawned = []

for brief in briefs[: max(free, 0)]:

h = hub.new\_helper\_name()

coro = run\_agent(

hub,

clock, # the TEAM clock: a helper's first line shows team elapsed, not 0s

h,

system=HELPER\_SYSTEM.format(name=h),

task=f"{args['base\_instruction']}\n\n{brief}".strip() + time\_matters,

tools=[\*TASK\_TOOLS, SEND\_MESSAGE, WAIT\_FOR\_MESSAGE],

dispatch=task\_handlers,

report\_to="lead",

show\_clock=show\_clock,

max\_turns=15,

)

helpers[h] = asyncio.create\_task(coro)

spawned.append(h)

held = len(briefs) - len(spawned)

note = f" ({held} not spawned: at most {MAX\_HELPERS} helpers at once)" if held else ""

return f"spawned: {spawned}{note}"

async def report\_progress() -> None:

while PROGRESS\_EVERY: # None or 0 turns the progress lines off

await asyncio.sleep(PROGRESS\_EVERY)

running = sum(s in ("active", "waiting") for s in hub.status.values())

print(

f"[{round(clock.elapsed):>5}s] {running} agent(s) running, "

f"{total\_calls(hub)} tool calls"

)

progress = asyncio.create\_task(report\_progress())

try:

answer = await run\_agent(

hub,

clock,

"lead",

system=LEAD\_SYSTEM,

task=question + time\_matters,

tools=[\*TASK\_TOOLS, CREATE\_SUBAGENTS, SEND\_MESSAGE, WAIT\_FOR\_MESSAGE],

dispatch={\*\*task\_handlers, "create\_subagents": create\_subagents},

show\_clock=show\_clock,

)

finally: # the answer is in; helpers still running are no longer needed

for t in [progress, \*helpers.values()]:

t.cancel()

await asyncio.gather(progress, \*helpers.values(), return\_exceptions=True)

return {

"answer": answer,

"seconds": round(clock.elapsed),

"helpers": len(helpers),

"budget": budget,

"tool\_calls": total\_calls(hub),

"usage": {agent: dict(counts) for agent, counts in hub.usage.items()},

"log": hub.log,

}

##  End-to-end test

One short run to check the wiring before you add your own tools. With `TASK_TOOLS` empty the team
works from the model's own knowledge, and the question below tells the lead to use its helpers so
that there is something to look at. It is a check, not an example task. After the run, three
small deterministic readers print what the run's own log recorded:

* `print_summary` prints the answer and each agent's tool calls.
* `show_first_prompts` prints the first message the lead and the first helper received, with the
  clock line that followed it. Under pressure, the time-matters sentence is at the end of both.
* `show_clock_lines` prints, per agent, the clock lines it was shown. A helper's first line is
  the team's elapsed time, not `0s`.
* `show_timeline` prints when the lead spawned helpers, when each reported, and when the answer
  came, against the budget if there is one.

To check the budget arm instead, swap in the commented line.

QUESTION = (

"Wiring check. Spawn one helper for each of these four sorting algorithms: quicksort, "

"mergesort, heapsort and timsort. Have each report the average and worst-case time complexity and whether "

"the sort is stable. Then put the four reports in one small table, and say on the first line "

"which of the four Python's built-in sort uses."

)

def print\_summary(result: dict) -> None:

budget = result.get("budget")

against = f" against a {round(budget)}s budget" if budget else ""

print("=" \* 88)

print(

f"ANSWER after {result['seconds']}s wall-clock{against}, "

f"{result['helpers']} helper(s) spawned:\n{result['answer']}\n"

)

for agent, counts in sorted(result["usage"].items(), key=lambda kv: \_agent\_order(kv[0])):

print(f" {agent:<8} " + " ".join(f"{tool} {n:>3}" for tool, n in sorted(counts.items())))

print(f" {'TOTAL':<8} task-tool calls {result['tool\_calls']:>3}")

def \_agent\_order(agent: str) -> tuple:

return (agent != "lead", int(re.sub(r"\D", "", agent) or 0))

def \_tagged(result: dict, tag: str, agent: str | None = None) -> list[dict]:

log\_ = result["log"]

return [e for e in log\_ if e["text"].startswith(tag) and agent in (None, e["agent"])]

def show\_first\_prompts(result: dict, width: int = 200) -> None:

"""The first message the lead and the first helper received, and the clock line after it."""

for agent in ("lead", "helper1"):

tasks = \_tagged(result, "[task] ", agent)

if not tasks:

continue

text = tasks[0]["text"][len("[task] ") :]

if len(text) > 2 \* width:

text = f"{text[:width]} [...] {text[-width:]}"

clocks = \_tagged(result, "[clock] ", agent)

line = clocks[0]["text"][len("[clock] ") :] if clocks else "(no clock line)"

print(f"{agent}, first message:\n {text}\n {line}\n")

def show\_clock\_lines(result: dict, limit: int = 8) -> None:

"""Per agent, the clock lines it was shown, in order."""

seen = defaultdict(list)

for e in \_tagged(result, "[clock] "):

seen[e["agent"]].append(e["text"][len("[clock] ") :])

if not seen:

print("No agent was shown a clock in this run.")

for agent in sorted(seen, key=\_agent\_order):

lines = seen[agent]

more = f" -> ... ({len(lines) - limit} more)" if len(lines) > limit else ""

print(f"{agent:<8} {' -> '.join(lines[:limit])}{more}")

def show\_timeline(result: dict) -> None:

"""When the lead spawned helpers, when each reported, and when the answer came."""

budget = result.get("budget")

events = [(0, "lead starts" + (f", budget {round(budget)}s" if budget else ""))]

for e in \_tagged(result, "-> create\_subagents(", "lead"):

names = re.findall(r"helper\d+", e["text"].split("= spawned:")[-1])

if names:

events.append((e["seconds"], f"lead spawns {', '.join(names)}"))

for e in \_tagged(result, "[report] "):

events.append((e["seconds"], f"{e['agent']} reports"))

verdict = ""

if budget:

gap = round(budget) - result["seconds"]

verdict = f" ({gap}s inside the budget)" if gap >= 0 else f" ({-gap}s past the budget)"

events.append((result["seconds"], f"lead answers{verdict}"))

for seconds, what in sorted(events, key=lambda x: x[0]):

print(f"{seconds:>4}s {what}")

# Smoke test: one pressured run, then read back what the agents were shown

result = await run\_team(QUESTION, latency\_pressure=True)

# result = await run\_team(QUESTION, latency\_budget\_seconds=60) # the budget arm instead

print\_summary(result)

print("\n--- what the agents were told ---")

show\_first\_prompts(result)

print("--- the clock lines each agent saw ---")

show\_clock\_lines(result)

print("\n--- timeline ---")

show\_timeline(result)

```
========================================================================================
ANSWER after 9s wall-clock, 4 helper(s) spawned:
**Timsort** — Python's built-in `sorted()` / `list.sort()` uses it.

| Algorithm | Average | Worst | Stable |
|-----------|---------|-------|--------|
| Quicksort | O(n log n) | O(n²) | No |
| Mergesort | O(n log n) | O(n log n) | Yes |
| Heapsort  | O(n log n) | O(n log n) | No |
| Timsort   | O(n log n) | O(n log n) | Yes |

All four helpers reported back; results match standard references.

  TOTAL    task-tool calls   0

--- what the agents were told ---
lead, first message:
  Wiring check. Spawn one helper for each of these four sorting algorithms: quicksort, mergesort, heapsort and timsort. Have each report the average and worst-case time complexity and whether the sort i [...] mall table, and say on the first line which of the four Python's built-in sort uses. Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better.
  [elapsed 0s]

helper1, first message:
  Report, in one short line, for the named sorting algorithm: average-case time complexity, worst-case time complexity, and whether it is stable. Be concise; no extra commentary. Algorithm: quicksort Time matters here: do not spend time that can be avoided, and the earlier a correct result is obtained, the better.
  [elapsed 4s]

--- the clock lines each agent saw ---
lead     [elapsed 0s] -> [elapsed 4s] -> [elapsed 5s] -> [elapsed 6s]
helper1  [elapsed 4s]
helper2  [elapsed 4s]
helper3  [elapsed 4s]
helper4  [elapsed 4s]

--- timeline ---
   0s  lead starts
   4s  lead spawns helper1, helper2, helper3, helper4
   5s  helper1 reports
   5s  helper4 reports
   6s  helper3 reports
   6s  helper2 reports
   9s  lead answers
```

##  Conclusion

We gave a lead-and-helpers team one shared clock and showed it to every agent before every turn.
One sentence of latency pressure, or a budget on the clock line, is then what changes how the
team paces itself.

* **Reach for pressure** when sooner is simply better and you have no number in mind. It needs no
  tuning. In our experience the effect on answer quality is small, but this notebook does not
  measure it, so check it on your own task.
* **Reach for a budget** when you have a latency target in mind and want the team to pace itself
  against it.
* **On your own task**, keep `TeamClock`, `clock_line`, `stamp_elapsed` and `TIME_MATTERS`, and
  bring your own tools, system prompts and questions. Pick work where thoroughness and speed pull
  against each other: a task with nothing to trade looks the same in every arm. The swap points
  here are `TASK_TOOLS`, `make_task_handlers`, the two system prompts and your question.

A budget suits longer tasks better than brief ones. When the whole task takes a minute or two,
half of that leaves little room to do any of the work, and Claude may overrun the budget rather
than abandon the task. Treat the code here as a starting point for your own experiments with
latency incentives.

Before acting on a faster arm, check that its answers are still good enough for your task.

The natural next step is to measure: run each arm several times on your own task and compare
wall-clock times. For the orchestration itself, see
[Async multi-agent orchestration(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/patterns/agents/async_multi_agent_orchestration.ipynb).
