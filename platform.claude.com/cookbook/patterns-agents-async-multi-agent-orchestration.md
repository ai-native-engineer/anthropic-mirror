<!-- source: https://platform.claude.com/cookbook/patterns-agents-async-multi-agent-orchestration -->

#  Async Multi-Agent Orchestration with Claude

This cookbook shows the **shape** of the two multi-agent orchestration patterns behind the multi-agent results in the Claude Opus 4.8 system card: a **fixed N-agent team** and **async subagents**. There is no domain task here — just the messaging and subagent mechanics, so you can see exactly which tools fire and in what order, then drop your own tools and task in.

Everything runs on the public [Anthropic Python SDK(opens in new tab)](https://github.com/anthropics/anthropic-sdk-python) + `asyncio`, with any API key, typically in under thirty seconds.

##  Setup

%pip install -qU anthropic

import asyncio

import itertools

from collections import Counter, defaultdict

import anthropic

MODEL = "claude-opus-4-8" # swap for the newest Claude model available to you

client = anthropic.AsyncAnthropic() # reads ANTHROPIC\_API\_KEY from env

##  Shared building blocks

###  The message hub

Every agent gets an inbox list and an `asyncio.Event` for blocking waits. `drain` empties an inbox and returns the structured messages; `render` formats them as text for appending to a tool result.

class Hub:

def \_\_init\_\_(self):

self.inbox: dict[str, list[dict]] = defaultdict(list)

self.event: dict[str, asyncio.Event] = defaultdict(asyncio.Event)

self.status: dict[str, str] = {}

self.\_ids = itertools.count(1)

def register(self, name: str):

self.status[name] = "active"

\_ = self.inbox[name], self.event[name]

def new\_name(self, prefix="helper") -> str:

n = f"{prefix}{next(self.\_ids)}"

self.register(n)

return n

def post(self, sender: str, recipients: list[str], content: str) -> list[str]:

delivered = []

for rid in recipients:

if rid in self.status:

self.inbox[rid].append({"from": sender, "content": content})

self.event[rid].set()

delivered.append(rid)

return delivered

def drain(self, name: str) -> list[dict]:

msgs, self.inbox[name] = self.inbox[name], []

self.event[name] = asyncio.Event()

return msgs

@staticmethod

def render(msgs: list[dict]) -> str:

if not msgs:

return ""

body = "\n".join(

f'<agent-message from="{m["from"]}">\n{m["content"]}\n</agent-message>' for m in msgs

)

return f"\n\n[Messages received while you were working:]\n{body}"

###  Messaging tools

Every agent in both patterns gets these two.

SEND\_MESSAGE = {

"name": "send\_message",

"description": (

"Send a message to one or more other agents. It will appear appended to their next tool "

"result. This is the ONLY way to reach other agents — plain text in your turn goes nowhere."

),

"input\_schema": {

"type": "object",

"properties": {

"recipient\_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1},

"content": {"type": "string"},

},

"required": ["recipient\_ids", "content"],

},

}

WAIT\_FOR\_MESSAGE = {

"name": "wait\_for\_message",

"description": (

"Block until another agent messages you. Note: messages also arrive automatically appended "

"to the result of ANY other tool call, so only use this when you have nothing else to do."

),

"input\_schema": {"type": "object", "properties": {}},

}

BASE\_TOOLS = [SEND\_MESSAGE, WAIT\_FOR\_MESSAGE]

###  The base agent loop

One function runs any agent: a standard tool-use loop that dispatches `send_message` / `wait_for_message` against the hub, routes any extra tools through `extra_dispatch`, and **appends the drained inbox to the last tool result** — so agents never poll; messages arrive inline. Each tool call and inbox delivery is printed live so you can watch the orchestration unfold; a summary trace prints at the end.

TRACE: dict[str, list[str]] = defaultdict(list)

def \_snip(s, n=60):

s = str(s).replace("\n", " ")

return s if len(s) <= n else s[:n] + "…"

async def run\_agent(

hub: Hub,

name: str,

system: str,

first\_user\_turn: str,

tools: list = None,

extra\_dispatch=None,

max\_turns: int = 20,

) -> str:

tools = tools or BASE\_TOOLS

extra\_dispatch = extra\_dispatch or {}

messages = [{"role": "user", "content": first\_user\_turn}]

try:

for \_ in range(max\_turns):

resp = await client.messages.create(

model=MODEL,

max\_tokens=2048,

system=system,

tools=tools,

messages=messages,

)

messages.append({"role": "assistant", "content": resp.content})

if resp.stop\_reason == "end\_turn":

hub.status[name] = "done"

return "".join(getattr(b, "text", "") for b in resp.content)

if resp.stop\_reason != "tool\_use":

raise RuntimeError(f"unexpected stop\_reason: {resp.stop\_reason}")

results = []

for block in resp.content:

if block.type != "tool\_use":

continue

TRACE[name].append(block.name)

if block.name == "send\_message":

rids = block.input["recipient\_ids"]

delivered = hub.post(name, rids, block.input["content"])

unknown = [r for r in rids if r not in delivered]

out = f"delivered to {delivered}" + (f"; unknown: {unknown}" if unknown else "")

elif block.name == "wait\_for\_message":

hub.status[name] = "idling"

try:

await asyncio.wait\_for(hub.event[name].wait(), timeout=60)

out = "woke: new messages"

except TimeoutError:

out = "woke: 60s timeout"

hub.status[name] = "active"

elif block.name in extra\_dispatch:

out = await extra\_dispatch[block.name](block)

else:

out = f"error: no dispatch for {block.name}"

print(f" [{name}] {block.name}({\_snip(block.input)}) → {\_snip(out)}")

results.append({"type": "tool\_result", "tool\_use\_id": block.id, "content": out})

inbox = hub.drain(name)

for m in inbox:

print(f" [{name}] ← received from {m['from']}: {\_snip(m['content'])}")

if results:

results[-1]["content"] += hub.render(inbox) # ← the key line

messages.append({"role": "user", "content": results})

hub.status[name] = "done"

return f"[{name} hit max\_turns={max\_turns}]"

except Exception:

hub.status[name] = "crashed"

raise

def print\_trace():

for agent in sorted(TRACE):

counts = Counter(TRACE[agent])

print(f" {agent}: " + ", ".join(f"{n}×{t}" for t, n in counts.most\_common()))

TRACE.clear()

---

##  Part 1 · Fixed N-Agent Team

Three agents — one **lead** and two **helpers** — each given a one-line persona. All they do is introduce themselves to each other via `send_message`; the lead writes a one-sentence summary and ends the run. No domain tool: this is purely the messaging path.

TEAM\_SYSTEM = "You are {name}, one of 3 agents working together (peers: {peers})."

TASKS = {

"lead": "You are the lead. Introduce yourself to the others. Once everyone has introduced "

"themselves, finish with a one-sentence summary of the team.",

"helper1": "You are a backend engineer named Ada. Introduce yourself to the others, then wait "

"for their replies.",

"helper2": "You are a designer named Bo. Introduce yourself to the others, then wait for their "

"replies.",

}

async def run\_team() -> str:

hub = Hub()

names = list(TASKS)

for n in names:

hub.register(n)

helper\_tasks = [

asyncio.create\_task(

run\_agent(

hub,

n,

system=TEAM\_SYSTEM.format(name=n, peers=[p for p in names if p != n]),

first\_user\_turn=TASKS[n],

)

)

for n in names[1:]

]

try:

return await run\_agent(

hub,

"lead",

system=TEAM\_SYSTEM.format(name="lead", peers=names[1:]),

first\_user\_turn=TASKS["lead"],

)

finally:

for t in helper\_tasks:

t.cancel()

await asyncio.gather(\*helper\_tasks, return\_exceptions=True)

answer = await run\_team()

print(f"\n[lead final answer]\n{answer}\n\nTool-call summary:")

print\_trace()

```
[helper1] send_message({'recipient_ids': ['lead', 'helper2'], 'content': "Hi all, I…) → delivered to ['lead', 'helper2']
  [helper2] send_message({'recipient_ids': ['lead', 'helper1'], 'content': "Hi everyo…) → delivered to ['lead', 'helper1']
  [helper2] ← received from helper1: Hi all, I'm Ada, a backend engineer on the team. I focus on …
  [lead] send_message({'recipient_ids': ['helper1', 'helper2'], 'content': "Hi tea…) → delivered to ['helper1', 'helper2']
  [lead] ← received from helper1: Hi all, I'm Ada, a backend engineer on the team. I focus on …
  [lead] ← received from helper2: Hi everyone! I'm Bo, the designer on the team. Looking forwa…
  [helper1] wait_for_message({}) → woke: new messages
  [helper1] ← received from helper2: Hi everyone! I'm Bo, the designer on the team. Looking forwa…
  [helper1] ← received from lead: Hi team, I'm lead, the coordinator for our group. Looking fo…
  [helper2] wait_for_message({}) → woke: new messages
  [helper2] ← received from lead: Hi team, I'm lead, the coordinator for our group. Looking fo…
  [lead] send_message({'recipient_ids': ['helper1', 'helper2'], 'content': "Thanks…) → delivered to ['helper1', 'helper2']

[lead final answer]
Everyone has introduced themselves, and I've shared the summary.

**Team summary:** We're a three-person team with me (lead) coordinating, Ada handling backend engineering (APIs, databases, architecture), and Bo driving design — a well-rounded crew ready to build great things together.

Tool-call summary:
  helper1: 1×send_message, 1×wait_for_message
  helper2: 1×send_message, 1×wait_for_message
  lead: 2×send_message
```

---

##  Part 2 · Async Subagents (dynamic spawn)

Now give the lead **subagent tools** and a trivial client-side `sleep(seconds)` tool. The lead spawns three helpers; each sleeps *N* seconds, `send_message`s "done" to the lead, then `wait_for_message`s for further instructions. The spawn call returns immediately; the lead checks `get_status` while they run, collects their reports via `wait_for_message`, then `kill_subagents` all three to dismiss them. No domain logic — just the full spawn / status / collect / kill path.

SLEEP = {

"name": "sleep",

"description": "Sleep for the given number of seconds, then return.",

"input\_schema": {

"type": "object",

"properties": {"seconds": {"type": "integer", "minimum": 0, "maximum": 10}},

"required": ["seconds"],

},

}

SUBAGENT\_TOOLS = [

{

"name": "create\_subagents",

"description": "Spawn helper subagents. Returns immediately — helpers run concurrently in the "

"background in parallel with you. Each gets base\_instruction, optionally + "

"per\_subagent\_instructions[i].",

"input\_schema": {

"type": "object",

"properties": {

"base\_instruction": {"type": "string"},

"per\_subagent\_instructions": {

"type": "array",

"items": {"type": "string"},

"maxItems": 10,

},

},

"required": ["base\_instruction"],

},

},

{

"name": "get\_status",

"description": "Status of every helper (active / idling / done / crashed).",

"input\_schema": {"type": "object", "properties": {}},

},

{

"name": "kill\_subagents",

"description": "Cancel running helpers you no longer need.",

"input\_schema": {

"type": "object",

"properties": {

"subagent\_ids": {"type": "array", "items": {"type": "string"}, "minItems": 1}

},

"required": ["subagent\_ids"],

},

},

]

async def dispatch\_sleep(block) -> str:

s = int(block.input["seconds"])

await asyncio.sleep(s)

return f"slept {s}s"

async def run\_spawn\_lead() -> str:

hub = Hub()

hub.register("lead")

helpers: dict[str, asyncio.Task] = {}

async def \_create(block):

base = block.input["base\_instruction"]

per = block.input.get("per\_subagent\_instructions") or [""]

spawned = []

for suffix in per:

h = hub.new\_name()

helpers[h] = asyncio.create\_task(

run\_agent(

hub,

h,

system=f"You are {h}, a helper.",

first\_user\_turn=f"{base}\n\n{suffix}".strip(),

tools=[SLEEP, \*BASE\_TOOLS],

extra\_dispatch={"sleep": dispatch\_sleep},

)

)

spawned.append(h)

return f"spawned: {', '.join(spawned)}"

async def \_status(block):

return "\n".join(f"{n}: {s}" for n, s in hub.status.items() if n != "lead") or "(none)"

async def \_kill(block):

killed\_ids, to\_await = [], []

for sid in block.input["subagent\_ids"]:

if sid in helpers and not helpers[sid].done():

helpers[sid].cancel()

hub.status[sid] = "done"

to\_await.append(helpers.pop(sid))

killed\_ids.append(sid)

await asyncio.gather(\*to\_await, return\_exceptions=True)

return f"cancelled: {', '.join(killed\_ids)}" if killed\_ids else "no matching active helpers"

try:

return await run\_agent(

hub,

"lead",

system="You are the lead.",

first\_user\_turn=(

"Spawn three helper agents. Instruct each to sleep a different number of seconds "

"(1, 2, 3), report back to you 'done, slept Ns', then wait for your further "

"instructions. After that, check that they're running, collect all three reports, "

"then dismiss all three helpers. Finish with a one-line summary."

),

tools=[\*SUBAGENT\_TOOLS, \*BASE\_TOOLS],

extra\_dispatch={

"create\_subagents": \_create,

"get\_status": \_status,

"kill\_subagents": \_kill,

},

)

finally:

for t in helpers.values():

t.cancel()

await asyncio.gather(\*helpers.values(), return\_exceptions=True)

answer = await run\_spawn\_lead()

print(f"\n[lead final answer]\n{answer}\n\nTool-call summary:")

print\_trace()

```
[lead] create_subagents({'base_instruction': 'You are a helper agent. Follow your sp…) → spawned: helper1, helper2, helper3
  [lead] get_status({}) → helper1: active helper2: active helper3: active
  [helper1] sleep({'seconds': 1}) → slept 1s
  [helper2] sleep({'seconds': 2}) → slept 2s
  [helper1] send_message({'recipient_ids': ['lead'], 'content': 'done, slept 1s'}) → delivered to ['lead']
  [lead] wait_for_message({}) → woke: new messages
  [lead] ← received from helper1: done, slept 1s
  [helper3] sleep({'seconds': 3}) → slept 3s
  [helper2] send_message({'recipient_ids': ['lead'], 'content': 'done, slept 2s'}) → delivered to ['lead']
  [lead] wait_for_message({}) → woke: new messages
  [lead] ← received from helper2: done, slept 2s
  [helper3] send_message({'recipient_ids': ['lead'], 'content': 'done, slept 3s'}) → delivered to ['lead']
  [lead] wait_for_message({}) → woke: new messages
  [lead] ← received from helper3: done, slept 3s
  [lead] kill_subagents({'subagent_ids': ['helper1', 'helper2', 'helper3']}) → cancelled: helper1, helper2, helper3

[lead final answer]
Summary: All 3 helpers were spawned and confirmed active, each reported back successfully ("done, slept 1s/2s/3s"), and all three were then dismissed.

Tool-call summary:
  helper1: 1×sleep, 1×send_message, 1×wait_for_message
  helper2: 1×sleep, 1×send_message, 1×wait_for_message
  helper3: 1×sleep, 1×send_message, 1×wait_for_message
  lead: 3×wait_for_message, 1×create_subagents, 1×get_status, 1×kill_subagents
```

---

##  Next steps

Swap in your own domain tools — add them to `tools` and a handler to `extra_dispatch`. The `Hub`, `run_agent`, and the two team runners above are all you need; the rest is your task and your tools.

See the [tool use guide(opens in new tab)](https://docs.claude.com/en/docs/tool-use) for the full tool-definition reference.
