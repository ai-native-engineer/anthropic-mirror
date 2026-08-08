<!-- source: https://platform.claude.com/cookbook/managed-agents-cma-watch-subagents-live -->

#  Multiagent: watch a curriculum team work in real time

A coordinator that delegates to subagents has an observability gap. The session-level stream previews the primary thread's text as the model generates it, but a subagent's output only becomes visible after its whole turn is buffered. If the researcher runs for two minutes, you watch nothing for two minutes.

This notebook closes that gap, using four Managed Agents API features together:

* **Per-thread delta streaming.** Each session thread's stream accepts the same `event_deltas` parameter as the session-level stream, so a subagent's text previews live on its own stream.
* **Initial events on session create.** `sessions.create` accepts `initial_events`, so a session starts working in the same call that creates it.
* **Effort on the agent's model.** `model.effort` sets how hard Claude works on each inference call, per agent. In a team, that's a per-role cost lever.
* **Optional version on agent update.** `agents.update` treats the current version as an optional concurrency key rather than a required one.

The team you'll build plans a one-week 7th-grade science unit: a coordinator delegates to a standards researcher (web search, high effort) and a lesson writer (no web access), then assembles the unit plan. If the `multiagent` coordinator pattern is new to you, start with [`CMA_coordinate_specialist_team.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_coordinate_specialist_team.ipynb). This notebook builds on those shapes.

##  1. Set up the client

These features ride the standard `managed-agents-2026-04-01` beta header. The SDK calls in this notebook (`initial_events` on `sessions.create`, `event_deltas` on thread streams, `model.effort`) need `anthropic>=0.118.0`.



%%capture

%pip install -qU "anthropic>=0.118.0" python-dotenv



import os

import anthropic

from dotenv import load\_dotenv

load\_dotenv()

BETAS = ["managed-agents-2026-04-01"]

MODEL = os.environ.get("COOKBOOK\_MODEL", "claude-sonnet-5")

client = anthropic.Anthropic()

##  2. Create the two specialists

The researcher gets web search and a `high` effort level, because standards alignment is judgment-heavy work: it has to weigh which performance expectations actually fit the unit rather than list everything it finds. `effort` goes inside the `model` object and accepts `low`, `medium`, `high`, `xhigh`, or `max` (as a bare string or `{"type": "high"}`). Not every model accepts every level, and an invalid combination is rejected at create time.

Effort is also the team's main cost lever: higher levels let Claude spend more tokens per inference call, lower levels cap that spend. Because it's set per agent, you buy depth only for the roles that need it. In a larger team, a formatting or triage role could drop to `low` without touching the researcher's budget.

Set effort on the agent, not per session: an `effort` level inside a per-session `model` override isn't applied.

The web tools' configuration also accepts allowed- and blocked-domain lists, so a production deployment can fence this researcher to the standards sites it should trust. See [Configuring the toolset(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/tools#configuring-the-toolset) for the config shape.



RESEARCHER\_SYSTEM = """You research US middle school science standards.

Given a unit topic and grade level, use web search to find:

- The two or three NGSS performance expectations the unit should target

- What students are expected to already know, and where the topic leads next

- Two or three documented student misconceptions for the topic

Return via send\_to\_parent:

{"standards": [...], "prior\_knowledge": ..., "leads\_to": ...,

"misconceptions": [...], "sources": [...]}"""

standards\_researcher = client.beta.agents.create(

name="standards\_researcher",

description="Finds the NGSS standards and documented misconceptions for a science topic.",

model={"id": MODEL, "effort": "high"},

system=RESEARCHER\_SYSTEM,

tools=[

{

"type": "agent\_toolset\_20260401",

"configs": [{"name": "web\_search"}, {"name": "web\_fetch"}],

}

],

betas=BETAS,

)

The lesson writer works only from what the coordinator hands it. Disabling the web tools keeps its lessons grounded in the researcher's vetted findings instead of whatever a fresh search returns.



WRITER\_SYSTEM = """You write middle school lesson plans.

You will be given a topic, grade level, target standards, and known misconceptions.

Draft five 45-minute lessons, one per day. For each day give:

- Objective (tied to a target standard)

- Warm-up (5 min)

- Main activity (30 min)

- Exit ticket (one question that probes a misconception where possible)

Return via send\_to\_parent: {"days": [{"day": 1, "objective": ..., "warm\_up": ...,

"main\_activity": ..., "exit\_ticket": ...}, ...]}"""

lesson\_writer = client.beta.agents.create(

name="lesson\_writer",

description="Drafts a day-by-day lesson sequence from standards and misconceptions.",

model={"id": MODEL},

system=WRITER\_SYSTEM,

tools=[

{

"type": "agent\_toolset\_20260401",

"configs": [

{"name": "web\_search", "enabled": False},

{"name": "web\_fetch", "enabled": False},

],

}

],

betas=BETAS,

)

The create response echoes the resolved model configuration, including fields you omitted. The researcher shows the `high` you set, and the writer shows the model's default effort. If `effort` comes back `None`, your organization's beta header doesn't carry the feature yet: the field is dropped, not rejected, so this echo is the place to catch it.



for agent in (standards\_researcher, lesson\_writer):

effort = getattr(agent.model, "effort", None)

print(f"{agent.name}: {agent.id} v{agent.version} effort={effort and effort.type}")

##  3. Create the coordinator

The coordinator carries the `multiagent` roster. The spawn and delegation tools are injected from the roster automatically, and the roster pins each child to the version that's current right now. That pinning matters later, when you update the researcher.



COORDINATOR\_SYSTEM = """You plan one-week teaching units.

Given a topic and grade level:

1. Send the topic and grade to standards\_researcher.

2. When the researcher reports back, send the topic, grade, target standards, and

misconceptions to lesson\_writer.

3. Write /mnt/session/outputs/unit\_plan.md with sections: Overview, Standards alignment,

Day-by-day plan (from the writer), Misconceptions to watch for, Materials.

Keep it under three pages. To revise the plan, rewrite the whole file with the write

tool rather than patching it with edit. While a subagent is working, wait silently: no

status commentary until its report arrives."""

coordinator = client.beta.agents.create(

name="unit\_planner",

description="Plans one-week teaching units by delegating research and drafting.",

model={"id": MODEL},

system=COORDINATOR\_SYSTEM,

tools=[{"type": "agent\_toolset\_20260401"}],

multiagent={

"type": "coordinator",

"agents": [standards\_researcher.id, lesson\_writer.id],

},

betas=BETAS,

)

print(f"{coordinator.name}: {coordinator.id} v{coordinator.version}")

##  4. Start the session with its first message inline

Without `initial_events`, starting a session takes two calls: create it, then post a `user.message`. Seeding the first message at create time collapses that into one. The array accepts up to 50 `user.message` and `user.define_outcome` events, processed in order, and validation is all-or-nothing: if any event fails, no session is created. A non-empty list starts the agent loop in the same call, so the session comes back already moving toward `running`.

If you want the unit plan graded against a rubric, add a single `user.define_outcome` event here (it must include a `rubric`, and only one is allowed per create). [`CMA_verify_with_outcome_grader.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/CMA_verify_with_outcome_grader.ipynb) covers that loop.



import time

env = client.beta.environments.create(

name="curriculum-studio",

config={"type": "anthropic\_cloud", "networking": {"type": "unrestricted"}},

betas=BETAS,

)

session = client.beta.sessions.create(

agent=coordinator.id,

environment\_id=env.id,

title="Unit plan: water cycle, grade 7",

initial\_events=[

{

"type": "user.message",

"content": [

{

"type": "text",

"text": "Plan a one-week unit on the water cycle for 7th grade science. "

"Classes are 45 minutes. Write the plan to /mnt/session/outputs/unit\_plan.md.",

}

],

}

],

betas=BETAS,

)

deadline = time.monotonic() + 60

while session.status == "idle" and time.monotonic() < deadline:

time.sleep(1)

session = client.beta.sessions.retrieve(session.id, betas=BETAS)

print(f"{session.id}: {session.status}")

if session.status == "idle":

events = client.beta.sessions.events.list(session.id, limit=1, betas=BETAS)

if next(iter(events), None) is None:

raise RuntimeError(

"The session has no events: your organization's beta header does not carry "

"initial\_events yet. The field is dropped at the gateway, not rejected."

)

raise RuntimeError(

"The seeded message is in the event log but the session is still idle after 60s. "

"Re-run this cell to keep waiting."

)

##  5. Watch the whole team live

Previews are thread-scoped by design. A connection previews only the thread it reads: the session-level stream previews the primary thread, and a child's previews appear only on that child's own stream at `GET /v1/sessions/{session_id}/threads/{thread_id}/stream`. So the pattern is one stream per thread: read the session-level stream for the coordinator, and every time a `session.thread_created` event announces a child (it carries `session_thread_id` and `agent_name`), attach a watcher to that thread's stream in a background thread.

Two rules shape the code:

* **The preview is a scratch buffer, the buffered event is the record.** Deltas are best-effort and may stop under load. The buffered `agent.message` that follows carries the complete content. The SDK's `accumulate_managed_agents_event` helper folds `event_start`, `event_delta`, and the buffered event into one snapshot, replacing the preview when the record arrives. Run one accumulator per stream connection.
* **No replay.** A connection opened after a model request started receives no deltas for that in-flight request, and a reconnect never replays missed deltas. Attaching the watcher as soon as `session.thread_created` arrives catches the child's work from its first response onward.

Each watcher exits on `session.thread_status_idle`, the event emitted when the child's turn finishes.



import threading

from anthropic.lib.sessions import accumulate\_managed\_agents\_event

print\_lock = threading.Lock()

current\_speaker = None

reconciliations = []

def say(speaker, text):

"""Print streamed text, labeling it whenever the speaker changes."""

global current\_speaker

with print\_lock:

if speaker != current\_speaker:

print(f"\n\n=== {speaker} ===")

current\_speaker = speaker

print(text, end="", flush=True)

def text\_of(event):

if event is None:

return ""

return "".join(block.text for block in event.content if block.type == "text")

def fold\_preview(snapshot, ev, speaker):

"""Fold one preview event into the speaker's snapshot and return the new snapshot.

Prints delta text as it arrives. When the buffered record lands, logs a

reconciliation row comparing it against the accumulated preview. The id

check guards the case where every delta for a message was shed: the

snapshot then still holds the previous message, not a preview of this one.

"""

if ev.type == "event\_delta":

say(speaker, ev.delta.content.text)

elif ev.type == "agent.message":

preview = text\_of(snapshot) if snapshot and snapshot.id == ev.id else ""

final = text\_of(ev)

reconciliations.append((speaker, len(preview), len(final), final.startswith(preview)))

return accumulate\_managed\_agents\_event(snapshot, ev)

def watch\_child(thread\_id, agent\_name):

"""Stream one child thread, previewing its text as the model generates it."""

snapshot = None

with client.beta.sessions.threads.events.stream(

thread\_id,

session\_id=session.id,

event\_deltas=["agent.message"],

betas=BETAS,

) as thread\_stream:

for ev in thread\_stream:

if ev.type in ("event\_start", "event\_delta", "agent.message"):

snapshot = fold\_preview(snapshot, ev, agent\_name)

elif ev.type == "agent.tool\_use":

detail = ev.input.get("query", "") if ev.name == "web\_search" else ""

say(agent\_name, f"\n[{ev.name}] {detail}")

elif ev.type in ("session.thread\_status\_idle", "session.thread\_status\_terminated"):

break

The main loop feeds the same `fold_preview` for the coordinator's text, plus the coordination events that only appear on the primary thread: `session.thread_created` when a child spawns, `agent.thread_message_sent` when the coordinator hands off a task, and `agent.thread_message_received` when a child reports back. A tool call cross-posted from a child thread carries `session_thread_id`, so the loop skips those: the child's own watcher shows them.

The loop ends on any `session.status_idle`, printing the stop reason when it isn't `end_turn`: a session waiting on a tool confirmation or out of retries should end the cell, not hang it. Both loops also break on the terminated status events, so an unrecoverable session error ends the cell instead of leaving the stream open.



watchers = []

snapshot = None

with client.beta.sessions.events.stream(

session.id, event\_deltas=["agent.message"], betas=BETAS

) as stream:

for ev in stream:

if ev.type in ("event\_start", "event\_delta", "agent.message"):

snapshot = fold\_preview(snapshot, ev, "unit\_planner")

elif ev.type == "session.thread\_created":

say("unit\_planner", f"\n[spawned {ev.agent\_name}]")

watcher = threading.Thread(

target=watch\_child,

args=(ev.session\_thread\_id, ev.agent\_name),

daemon=True,

)

watcher.start()

watchers.append(watcher)

elif ev.type == "agent.thread\_message\_sent":

say("unit\_planner", f"\n[task sent to {ev.to\_agent\_name}]")

elif ev.type == "agent.thread\_message\_received":

say("unit\_planner", f"\n[{ev.from\_agent\_name} reported back]")

elif ev.type == "agent.tool\_use" and not ev.session\_thread\_id:

# session\_thread\_id marks a call cross-posted from a child thread;

# that child's watcher already shows it

say("unit\_planner", f"\n[{ev.name}]")

elif ev.type == "session.status\_terminated":

break

elif ev.type == "session.status\_idle":

if ev.stop\_reason.type != "end\_turn":

say("unit\_planner", f"\n[idle without end\_turn: {ev.stop\_reason.type}]")

break

for watcher in watchers:

watcher.join(timeout=60)

if any(watcher.is\_alive() for watcher in watchers):

print("\n[a child stream is still open after the join timeout]")

If a stream connects but only ever delivers buffered events, the `event_deltas` parameter was stripped rather than rejected: that's the signature of a beta header that doesn't carry the feature. A 404 on the thread stream URL means a wrong path or a missing managed-agents beta header (the thread endpoints are beta-gated). The path is `/threads/{thread_id}/stream`, not `/threads/{thread_id}/events/stream`.

The streaming contract in full (delta shapes, the reconciliation guarantees, and the troubleshooting table) is in [events and streaming(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/events-and-streaming#event-deltas).

##  6. Check the preview against the record

Concatenating a preview's deltas gives a prefix of the buffered event's text: a prefix, not necessarily the whole text, because deltas may be shed under load. That guarantee is what makes reconciliation a single replace. Each row below is one buffered `agent.message`, compared against the preview the accumulator had built when the record arrived.



for agent\_name, preview\_chars, final\_chars, is\_prefix in reconciliations:

print(

f"{agent\_name:22s} preview {preview\_chars:5d} chars | "

f"final {final\_chars:5d} chars | preview is prefix: {is\_prefix}"

)

##  7. Read the unit plan

The coordinator's prompt says to write the plan with whole-file `write` calls, so the full document is in the event log and the last `write` to the file is the final version. If your own agent patches files with `edit`, read the file itself instead of replaying writes.



unit\_plan = ""

for ev in client.beta.sessions.events.list(session.id, limit=1000, betas=BETAS):

if (

ev.type == "agent.tool\_use"

and ev.name == "write"

and ev.input.get("file\_path", "").endswith("unit\_plan.md")

):

unit\_plan = ev.input["content"] # keep the last write, in case of revisions

# Show the structure rather than the full plan. Print unit\_plan to read it all.

for line in unit\_plan.splitlines():

if line.startswith("#"):

print(line)

##  8. Ship a prompt change without the version round trip

Suppose review feedback says every alignment claim needs the standard's code next to it. `agents.update` treats the agent's current `version` as an optional concurrency key: omit it and the update applies unconditionally, with the server incrementing the version for you. A provisioning script doesn't have to read the agent just to write it back.

Supply `version` when concurrent writers are possible (a mismatch returns a 409, so you always update from a known state). Omit it when a single flow owns the agent, like a CI job that syncs checked-in agent definitions.



updated = client.beta.agents.update(

standards\_researcher.id,

system=RESEARCHER\_SYSTEM

+ "\nCite the performance expectation code (for example MS-ESS2-4) next to every "

"alignment claim.",

betas=BETAS,

)

print(f"standards\_researcher v{standards\_researcher.version} -> v{updated.version}")

One caveat for multiagent setups: the coordinator's roster pinned the researcher's version at coordinator create time, so existing coordinators keep delegating to the old version. Update the coordinator (its `multiagent` field, or any field) to re-resolve the roster against the latest child versions.

##  9. Clean up



from utilities import wait\_for\_idle\_status

wait\_for\_idle\_status(client, session.id)

client.beta.sessions.archive(session.id, betas=BETAS)

client.beta.environments.archive(env.id, betas=BETAS)

print("archived")
