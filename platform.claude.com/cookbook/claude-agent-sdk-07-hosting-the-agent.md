<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-07-hosting-the-agent -->

#  Hosting your agent

You've built a research agent in [notebook 00(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./00_The_one_liner_research_agent.ipynb). It runs on your laptop. Now someone else needs to use it: a teammate, a cron job, a web app, a customer. That means it has to run *somewhere other than your terminal*, stay up, keep conversations alive across restarts, and not leak your API key.

This notebook takes the exact same agent and deploys it through three tiers:

| Tier | Where it runs | When to use it |
| --- | --- | --- |
| **1. Docker** | Your machine / a single VM | Dev loop, internal tools, single-tenant |
| **2. Modal** | Managed serverless | You want a URL and scale-to-zero without managing infra |
| **3. Kubernetes** | Your own cluster | Multi-tenant, regulated environments, full control |

The agent code, the container image, and the HTTP interface are **identical** across all three. Only the operational machinery around the container changes. Once the agent is containerized behind a stable interface, choosing a host is a deployment decision rather than a rewrite.

> **Cost to run this notebook end-to-end:** roughly **$1–2** in Anthropic API calls plus **a few cents** in Modal compute. Every tier has a teardown step.

All the deployment code lives in [`hosting/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/) next to this notebook.

##  Before you start: should you be using the Agent SDK?

If you're building a **customer-facing chat product**, look at [Claude Managed Agents(opens in new tab)](https://platform.claude.com/docs/en/managed-agents/overview) first. You get hosting, sessions, and a UI out of the box, and you can skip most of this notebook.

The Agent SDK is the right choice when you need **programmatic control**: batch and job-shaped agents, internal tools, agents embedded in your own backend, or regulated environments where you have to own the infrastructure. If that's you, read on.

##  The mental model

Three nouns to keep straight:

* A **process** is one running Python interpreter with the SDK loaded. It talks to the Anthropic API.
* A **session** is one conversation: the prompt history, tool calls, and results that the SDK writes to disk so you can `resume=` it later.
* A **container** is a packaged process plus its filesystem: your agent code, the SDK, Node, and a place for sessions to live.

Unlike in-process SDKs (OpenAI Agents SDK, Google ADK) where an "agent" is an object you instantiate inside your web server, a Claude Agent SDK agent **is** a process. That makes isolation trivial (one container = one blast radius) but means hosting is a distributed-systems problem, not a `pip install` problem.

Every deployment, at any tier, has to do the same four jobs:



┌────────────────────────────────────────────────────────────────────┐

│ caller ──► gateway ──► [ spawn | route ] ──► agent container ──► API

│ │ │

│ └── auth (not the agent's job) └── /data (persist)

│ │

│ orchestrator ──────────────── lifecycle ────────────────────────────┘

└────────────────────────────────────────────────────────────────────┘

1. **Spawn** a container when work arrives
2. **Route** each request to the container that owns that session
3. **Lifecycle**: kill idle containers, restart crashed ones
4. **Persist** session transcripts so a restart doesn't lose the conversation

Tier 1 does all four by hand. Tier 2 delegates spawn+lifecycle to Modal. Tier 3 delegates all four to Kubernetes plus a small gateway. The agent container never changes.

##  The agent we're deploying

We're reusing [`research_agent/agent.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./research_agent/agent.py) from notebook 00, the one-liner research agent with `WebSearch` and `Read`. If you haven't done notebook 00, do it first; this notebook assumes the agent already works.

The only thing `hosting/` adds is a thin HTTP server and a Dockerfile. The system prompt comes straight from `research_agent.agent`; we import it rather than copy it. One deliberate difference: the hosted server narrows the tool list to `WebSearch` only. There is no upload path on a server, so the only files `Read` could reach are other sessions' transcripts and the container's own environment, and a prompt-injected web result could walk the agent into leaking them. The comment in `server.py` spells out the reasoning.



from research\_agent.agent import DEFAULT\_MODEL, RESEARCH\_SYSTEM\_PROMPT

print(f"model: {DEFAULT\_MODEL}")

print(RESEARCH\_SYSTEM\_PROMPT)



```
model: claude-opus-4-6
You are a research agent specialized in AI.

When providing research findings:
- Always include source URLs as citations
- Format citations as markdown links: [Source Title](URL)
- Group sources in a "Sources:" section at the end of your response
```

###  Setup

Create `hosting/.env` with your API key. This file is gitignored.



%%bash

test -f hosting/.env || cp hosting/.env.example hosting/.env

echo 'Edit hosting/.env and set ANTHROPIC\_API\_KEY, then re-run this cell.'

grep -q '^ANTHROPIC\_API\_KEY=sk-ant-' hosting/.env \

&& ! grep -q 'your-key-here' hosting/.env \

&& echo '✅ key looks set'



```
Edit hosting/.env and set ANTHROPIC_API_KEY, then re-run this cell.

✅ key looks set
```

---

##  Tier 1a — Ephemeral: one prompt, one container, done

The simplest possible deployment: a container that runs the agent **once** on a prompt from an env var, prints the result, and exits. No server, no sessions, no state.

> **Model note:** the hosting layer defaults to `claude-sonnet-4-6` so your test requests stay cheap while you work through this notebook. Set `MODEL=claude-opus-4-6` in `hosting/.env` to match notebook 00's config exactly.

This is enough for a lot of real work: invoice processing, nightly report generation, batch translation, one-off analysis. If your agent's job is "take input, produce output, stop," you don't need anything past this section.

The [`Dockerfile`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/Dockerfile) packages the agent, the SDK, and the Claude Code CLI the SDK drives under the hood. The build context is `claude_agent_sdk/` (this directory), not `hosting/`, because the image needs `research_agent/` and `utils/` too:



%%bash

docker build -f hosting/Dockerfile -t research-agent . | tail -n 3



```
#0 building with "orbstack" instance using docker driver

#1 [internal] load build definition from D
ockerfile
#1 transferring dockerfile: 2.30kB done
#1 DONE 0.0s

#2 resolve image config for docker-i
mage://docker.io/docker/dockerfile:1

#2 DONE 0.6s

#3 docker-image://docker.io/docker/dockerfile:1@sha256:87999aa3d42bdc6bea60565083ee17e86d1f3339802f
543c0d03998580f9cb89
#3 CACHED

#4 [internal] load metadata for docker.io/library/python:3.11-slim

#4 DONE 0.5s

#5 [1/9] FROM docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a
9fc0e6e38295747e49ac0
#5 DONE 0.0s

#6 [internal] load build context
#6 transferring context: 814.53
kB 0.0s done
#6 DONE 0.0s

#7 [3/9] WORKDIR /app
#7 CACHED

#8 [6/9] COPY research_agent/ ./research
_agent/
#8 CACHED

#9 [7/9] COPY utils/ ./utils/
#9 CACHED

#10 [2/9] RUN apt-get update  && apt-get
 install -y --no-install-recommends curl ca-certificates  && curl -fsSL https://deb.nodesource.com/s
etup_20.x | bash -  && apt-get install -y --no-install-recommends nodejs  && npm install -g @anthrop
ic-ai/claude-code@2.1.140  && apt-get purge -y curl  && apt-get autoremove -y  && rm -rf /var/lib/ap
t/lists/*
#10 CACHED

#11 [4/9] COPY hosting/requirements.txt ./hosting/requirements.txt
#11 CACHED

#12 [5/9] RUN pip install --no-cache-dir -r hosting/requirements.txt
#12 CACHED

#13 [8/9] COPY hos
ting/server.py hosting/run_once.py hosting/entrypoint.sh ./hosting/
#13 CACHED

#14 [9/9] RUN chmod
+x hosting/entrypoint.sh  && touch hosting/__init__.py
#14 CACHED

#15 exporting to image
#15 export
ing layers done
#15 writing image sha256:b77b20f557cef5e4b9ef01212f3ba3a0895ee97ff8e31f79d9e1dc0cfb7
414f5 done
#15 naming to docker.io/library/research-agent done
#15 DONE 0.0s
```



%%bash

docker run --rm --env-file hosting/.env \

-e PROMPT='What is the Claude Agent SDK, in one paragraph?' \

research-agent



```
🤖 Thinking...

🤖 Using: ToolSearch()

✓ Tool completed

🤖 Thinking...

🤖 Using: WebSearch()

✓ Tool completed

🤖 Using: WebSearch()

✓ Tool completed

🤖 Thinking...

The **Claude Agent SDK** is a developer toolkit from Anthropic — available in Python and TypeScrip
t — that gives developers access to the same tools, agent loop, and context management that power
Claude Code, enabling them to build fully autonomous AI agents that can read files, run terminal com
mands, search the web, edit code, and interact with external APIs without requiring developers to ma
nually implement a tool execution loop. Unlike the standard Claude API (where the developer must han
dle tool-use loops themselves), the Agent SDK lets Claude manage the agentic loop autonomously, maki
ng it straightforward to build sophisticated agents such as finance assistants, personal assistants,
 customer support bots, and deep research agents that can operate with minimal human intervention.

---

**Sources:**
- [Agent SDK Overview – Claude Code Docs](https://code.claude.com/docs/en/agent-
sdk/overview)
- [Building Agents with the Claude Agent SDK – Anthropic Engineering](https://www.an
thropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- [Agent SDK Overview – Anthrop
ic API Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-overview)
- [claude-agent-sdk-py
thon – GitHub](https://github.com/anthropics/claude-agent-sdk-python)
- [claude-agent-sdk-typescri
pt – GitHub](https://github.com/anthropics/claude-agent-sdk-typescript)
```

That's it. `entrypoint.sh` sees no `serve` argument, so [`run_once.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/run_once.py) calls `research_agent.agent.send_query()` with `$PROMPT` and exits 0.

**When this is enough:** job-shaped tasks where each invocation is independent. Run it from a cron, a queue worker, a CI step, or anywhere else you'd run a CLI.

---

##  Tier 1b — Hybrid: add a server so conversations can continue

Ephemeral mode can't hold a conversation; every `docker run` starts a fresh session. For a chat-shaped agent you need a long-lived process that accepts follow-ups and resumes the right session each time.

[`hosting/server.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/server.py) is a ~100-line FastAPI app that does exactly that and nothing more. The interface is the contract every tier conforms to:



GET /health → 200 {"status": "ok"}

POST /sessions/{session\_id}/messages → 200 text/event-stream of SDK messages

Two things worth noticing in `server.py`:

* **The server has no auth.** The docstring says so loudly. Auth is the gateway's job (tier 3 shows where it goes). The server validates `session_id` format and trusts the caller.
* **It keeps a small map from your `session_id` to the SDK's internal one.** The SDK generates its own session IDs; you can't choose them. The server learns the SDK's ID from the first turn's `ResultMessage` and passes it to `resume=` on follow-ups. The map is persisted next to the transcripts under `/data`.

Start it with docker-compose, which also mounts `./sessions` at `/data` so transcripts survive restarts:



%%bash

cd hosting/docker && docker compose up --build -d

sleep 3

curl -s http://localhost:8000/health



```
Image research-agent Building

#1 [internal] load local bake definitions

#1 reading from stdin 579B done
#1 DONE 0.0s

#2 [internal] load build definition from Dockerfile
#2 transferring dockerfile: 2.30kB done

#2 DONE 0.0s

#3 resolve image config for docker-image://docker.io/docker/dockerfile:1

#3 DONE 0.2s

#4 docker-image://docker.io/docker/dockerfile:1@sha256:87999aa3d42bdc6bea60565083ee17e86d1f3339802f
543c0d03998580f9cb89
#4 CACHED

#5 [internal] load metadata for docker.io/library/python:3.11-slim

#5 DONE 0.2s

#6 [1/9] FROM docker.io/library/python:3.11-slim@sha256:a3ab0b966bc4e91546a033e22093cb840908979487a
9fc0e6e38295747e49ac0
#6 DONE 0.0s

#7 [internal] load build context
#7 transferring context: 494B d
one
#7 DONE 0.0s

#8 [2/9] RUN apt-get update  && apt-get install -y --no-install-recommends curl ca
-certificates  && curl -fsSL https://deb.nodesource.com/setup_20.x | bash -  && apt-get install -y -
-no-install-recommends nodejs  && npm install -g @anthropic-ai/claude-code@2.1.140  && apt-get purge
 -y curl  && apt-get autoremove -y  && rm -rf /var/lib/apt/lists/*
#8 CACHED

#9 [3/9] WORKDIR /app

#9 CACHED

#10 [4/9] COPY hosting/requirements.txt ./hosting/requirements.txt
#10 CACHED

#11 [7/9]
COPY utils/ ./utils/
#11 CACHED

#12 [5/9] RUN pip install --no-cache-dir -r hosting/requirements.tx
t
#12 CACHED

#13 [6/9] COPY research_agent/ ./research_agent/
#13 CACHED

#14 [8/9] COPY hosting/se
rver.py hosting/run_once.py hosting/entrypoint.sh ./hosting/
#14 CACHED

#15 [9/9] RUN chmod +x host
ing/entrypoint.sh  && touch hosting/__init__.py
#15 CACHED

#16 exporting to image
#16 exporting layers done
#16 writing image sha256:feb4e050b95b69f43fa027a2b5
a8c87974fba11cd890ba7c669db4aaa459fca0 done
#16 naming to docker.io/library/research-agent done
#16
DONE 0.0s

#17 resolving provenance for metadata file

#17 DONE 0.0s

 Image research-agent Built

 Network docker_default Creating

 Network docker_default Created

 Container docker-research-agent-1 Creating

 Container docker-research-agent-1 Created

 Container docker-research-agent-1 Starting

 Container docker-research-agent-1 Started

{"status":"ok"}
```

Send a prompt and stream the response (`-N` disables curl's buffering so you see events as they arrive):



%%bash

curl -N -s -X POST http://localhost:8000/sessions/demo-1/messages \

-H 'Content-Type: application/json' \

-d '{"prompt":"What are the three most interesting AI agent trends right now?"}'



```
event: message
data: {"subtype": "init", "data": {"type": "system", "subtype": "init", "cwd": "/app", "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "tools": ["Task", "TaskOutput", "Bash", "Glob", "Grep", "ExitPlanMode", "Read", "Edit", "Write", "N … [truncated]

event: message
data: {"content": [{"id": "toolu_01LpCYD1mQgNAmiDYq55RHyC", "name": "WebSearch", "input": {"query": "AI agent trends 2026"}}], "model": "claude-sonnet-4-6", "parent_tool_use_id": null, "error": null, "usage": {"input_tokens": 685, "cache_cr … [truncated]

[... 6 events omitted — thinking blocks, tool loading, and web-search result payloads ...]

event: message
data: {"content": [{"text": "Great question! Based on the latest research and reports, here are the **three most interesting AI agent trends** right now in 2026:\n\n---\n\n## \ud83e\udd1d 1. Multi-Agent Systems & Orchestration\nThe era of the single, all-purpose AI agent is giving way to **coordinat … [truncated]

event: message
data: {"subtype": "success", "duration_ms": 20980, "duration_api_ms": 20812, "is_error": false, "num_turns": 3, "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "stop_reason": "end_turn", "total_cost_usd": 0.0502906, "usage": {"input_t … [truncated]

event: done
data:
```

Now a follow-up to the **same** `session_id`. The agent remembers the first turn because the server resumed the session:



%%bash

curl -N -s -X POST http://localhost:8000/sessions/demo-1/messages \

-H 'Content-Type: application/json' \

-d '{"prompt":"Tell me more about the second one."}'



```
event: message
data: {"subtype": "init", "data": {"type": "system", "subtype": "init", "cwd": "/app", "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "tools": ["Task", "TaskOutput", "Bash", "Glob", "Grep", "ExitPlanMode", "Read", "Edit", "Write", "N … [truncated]

event: message
data: {"content": [{"id": "toolu_01YU5m6b66Kh6GcSN1Kbv7zq", "name": "WebSearch", "input": {"query": "context engineering AI agents 2026 techniques best practices"}}], "model": "claude-sonnet-4-6", "parent_tool_use_id": null, "error": null, … [truncated]

[... 5 events omitted — thinking blocks, tool loading, and web-search result payloads ...]

event: message
data: {"content": [{"text": "## \ud83e\uddf1 Deep Dive: Context Engineering\n\nContext engineering has quickly become **the defining AI skill of 2026**. Here's a thorough breakdown:\n\n---\n\n### What Is It, Exactly?\n\nContext engineering is the discipline of **designing what information an AI mode … [truncated]

event: message
data: {"subtype": "success", "duration_ms": 26895, "duration_api_ms": 26791, "is_error": false, "num_turns": 3, "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "stop_reason": "end_turn", "total_cost_usd": 0.08444499999999999, "usage": … [truncated]

event: done
data:
```

Restart the container and send *another* follow-up. The volume mount kept `/data`, so the conversation survives:



%%bash

cd hosting/docker && docker compose restart && sleep 3

curl -N -s -X POST http://localhost:8000/sessions/demo-1/messages \

-H 'Content-Type: application/json' \

-d '{"prompt":"Summarize what we have discussed so far."}'



```
Container docker-research-agent-1 Restarting

 Container docker-research-agent-1 Started

event: message
data: {"subtype": "init", "data": {"type": "system", "subtype": "init", "cwd": "/app
", "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "tools": ["Task", "TaskOutput", "Bash", "Gl
ob", "Grep", "ExitPlanMode", "Read", "Edit", "Write", "NotebookEdit", "WebFetch", "TodoWrite", "WebS
earch", "TaskStop", "AskUserQuestion", "Skill", "EnterPlanMode", "EnterWorktree", "ExitWorktree", "C
ronCreate", "CronDelete", "CronList", "RemoteTrigger", "ToolSearch"], "mcp_servers": [], "model": "c
laude-sonnet-4-6", "permissionMode": "default", "slash_commands": ["update-config", "debug", "simpli
fy", "batch", "loop", "schedule", "claude-api", "compact", "context", "cost", "heapdump", "init", "p
r-comments", "release-notes", "review", "security-review", "insights"], "apiKeySource": "ANTHROPIC_A
PI_KEY", "claude_code_version": "2.1.81", "output_style": "default", "agents": ["general-purpose", "
statusline-setup", "Explore", "Plan"], "skills": ["update-config", "debug", "simplify", "batch", "lo
op", "schedule", "claude-api"], "plugins": [], "uuid": "753db5ec-c432-4634-abb4-048eda1e6acd", "fast
_mode_state": "off"}, "type": "SystemMessage"}

event: message
data: {"content": [{"thinking": "The user wants a summary of our conversation so far
. No tools needed for this.", "signature": "EtYBCmcIDRgCIkBg3e+9ruTNyro9yQA8kMewU6BzRzlQR/MAvKWUy2kk
CH0rl6bddOJ1gJBmcF4L3GPf/pgLkImzUqg1JV4RfUNgKAEyEWNsYXVkZS1zb25uZXQtNC02OABCCHRoaW5raW5nEgxfs2ACXCyv
Me8OUvQaDA4MA9sG7f/fI1we2yIwQvNMoFyTGl2/Ps+arqqgLoLYtySrkCOrgNmwcZFIbzQOFWiSJIcsqA7inm8T8n90Kh0wlw1t
FbJw0suOLM6okhU+eNc0gCr59ENLuBeZhBgC"}], "model": "claude-sonnet-4-6", "parent_tool_use_id": null, "
error": null, "usage": {"input_tokens": 7108, "cache_creation_input_tokens": 0, "cache_read_input_to
kens": 0, "cache_creation": {"ephemeral_5m_input_tokens": 0, "ephemeral_1h_input_tokens": 0}, "outpu
t_tokens": 0, "service_tier": "standard", "inference_geo": "global"}, "type": "AssistantMessage"}

event: message
data: {"content": [{"text": "Sure! Here's a summary of our conversation so far:\n\n-
--\n\n### \ud83d\uddc2\ufe0f Conversation Summary\n\n**1. Top 3 AI Agent Trends (May 2026)**\nYou as
ked about the most interesting AI agent trends right now. Based on web research, the three highlight
ed were:\n\n- \ud83e\udd1d **Multi-Agent Systems & Orchestration** \u2014 Specialized agents working
 in coordinated teams, replacing single all-purpose agents. Gartner reported a 1,445% surge in multi
-agent system inquiries.\n- \ud83e\uddf1 **Context Engineering** \u2014 Designing the full informati
on architecture around an agent (memory, retrieval, data sources, token budgets) to ensure reliable,
 high-quality outputs at scale.\n- \ud83d\udee1\ufe0f **Governance & Deterministic Guardrails** \u20
14 Shifting from viewing governance as a compliance burden to an enabler, combining dynamic AI with
human oversight to safely deploy agents in high-stakes scenarios.\n\n---\n\n**2. Deep Dive into Cont
ext Engineering**\nYou asked for more detail on the second trend. Key takeaways included:\n\n- **Con
text Engineering \u2260 Prompt Engineering** \u2014 It's a broader discipline covering the entire in
formation lifecycle of an agent.\n- **Core techniques** include RAG, memory management, context comp
ression, context offloading, state persistence, and tool output structuring.\n- **Why it matters for
 agents** \u2014 Unlike chatbots, agents accumulate context over many steps, making careful informat
ion design critical to avoid context rot and token blowouts.\n- **RAG alone isn't enough** \u2014 77
% of IT leaders agree RAG is insufficient for production AI on its own.\n- Proper context engineerin
g can improve agent task completion rates dramatically (e.g., **83% \u2192 96%**).\n\n---\n\nWould y
ou like to explore any of these topics further?"}], "model": "claude-sonnet-4-6", "parent_tool_use_i
d": null, "error": null, "usage": {"input_tokens": 7108, "cache_creation_input_tokens": 0, "cache_re
ad_input_tokens": 0, "cache_creation": {"ephemeral_5m_input_tokens": 0, "ephemeral_1h_input_tokens":
 0}, "output_tokens": 0, "service_tier": "standard", "inference_geo": "global"}, "type": "AssistantM
essage"}

event: message
data: {"subtype": "success", "duration_ms": 8163, "duration_api_ms": 8025, "is_error
": false, "num_turns": 1, "session_id": "77597263-a169-4236-b3d4-8ec14f90fd2b", "stop_reason": "end_
turn", "total_cost_usd": 0.028029, "usage": {"input_tokens": 7108, "cache_creation_input_tokens": 0,
 "cache_read_input_tokens": 0, "output_tokens": 447, "server_tool_use": {"web_search_requests": 0, "
web_fetch_requests": 0}, "service_tier": "standard", "cache_creation": {"ephemeral_1h_input_tokens":
 0, "ephemeral_5m_input_tokens": 0}, "inference_geo": "", "iterations": [{"input_tokens": 7108, "out
put_tokens": 447, "cache_read_input_tokens": 0, "cache_creation_input_tokens": 0, "cache_creation":
{"ephemeral_5m_input_tokens": 0, "ephemeral_1h_input_tokens": 0}, "type": "message"}], "speed": "sta
ndard"}, "result": "Sure! Here's a summary of our conversation so far:\n\n---\n\n### \ud83d\uddc2\uf
e0f Conversation Summary\n\n**1. Top 3 AI Agent Trends (May 2026)**\nYou asked about the most intere
sting AI agent trends right now. Based on web research, the three highlighted were:\n\n- \ud83e\udd1
d **Multi-Agent Systems & Orchestration** \u2014 Specialized agents working in coordinated teams, re
placing single all-purpose agents. Gartner reported a 1,445% surge in multi-agent system inquiries.\
n- \ud83e\uddf1 **Context Engineering** \u2014 Designing the full information architecture around an
 agent (memory, retrieval, data sources, token budgets) to ensure reliable, high-quality outputs at
scale.\n- \ud83d\udee1\ufe0f **Governance & Deterministic Guardrails** \u2014 Shifting from viewing
governance as a compliance burden to an enabler, combining dynamic AI with human oversight to safely
 deploy agents in high-stakes scenarios.\n\n---\n\n**2. Deep Dive into Context Engineering**\nYou as
ked for more detail on the second trend. Key takeaways included:\n\n- **Context Engineering \u2260 P
rompt Engineering** \u2014 It's a broader discipline covering the entire information lifecycle of an
 agent.\n- **Core techniques** include RAG, memory management, context compression, context offloadi
ng, state persistence, and tool output structuring.\n- **Why it matters for agents** \u2014 Unlike c
hatbots, agents accumulate context over many steps, making careful information design critical to av
oid context rot and token blowouts.\n- **RAG alone isn't enough** \u2014 77% of IT leaders agree RAG
 is insufficient for production AI on its own.\n- Proper context engineering can improve agent task
completion rates dramatically (e.g., **83% \u2192 96%**).\n\n---\n\nWould you like to explore any of
 these topics further?", "structured_output": null, "type": "ResultMessage"}

event: done
data:
```



%%bash

# Teardown tier 1

cd hosting/docker && docker compose down



```
Container docker-research-agent-1 Stopping

 Container docker-research-agent-1 Stopped
 Container docker-research-agent-1 Removing

 Container docker-research-agent-1 Removed

 Network docker_default Removing

 Network docker_default Removed
```

---

##  Tier 2 — Modal: same image, now it's a URL

Tier 1 runs on your machine. Tier 2 runs the **same Dockerfile** on [Modal(opens in new tab)](https://modal.com) via `modal.Sandbox`, which gives you a public HTTPS URL, scale-to-zero, and no servers to manage.

That URL is *public*: anyone who has it can spend your API budget. Tiers 1 and 3 assume an authenticating gateway in front; tier 2 has no gateway, so `modal_app.py` generates a per-deploy bearer token and passes it as `AGENT_AUTH_TOKEN`. `server.py` only enforces the token when that env var is set, so the other tiers are unaffected.

[`hosting/modal/modal_app.py`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/modal/modal_app.py) is short because nothing about the agent changes:



app = modal.App.lookup("research-agent-hosting", create\_if\_missing=True)

image = modal.Image.from\_dockerfile("hosting/Dockerfile", context\_dir=".")

auth\_token = secrets.token\_urlsafe(32)

sandbox = modal.Sandbox.create(

"serve", # appended to the image's ENTRYPOINT, like compose's `command:`

app=app,

image=image,

secrets=[

modal.Secret.from\_name("anthropic"),

modal.Secret.from\_dict({"AGENT\_AUTH\_TOKEN": auth\_token}),

],

volumes={"/data": sessions\_volume},

encrypted\_ports=[8000],

)

print(sandbox.tunnels()[8000].url)

Persistence uses a `modal.Volume` mounted at `/data`, the same `CLAUDE_CONFIG_DIR` trick as tier 1. (If your workload has many sandboxes writing concurrently and you hit Volume commit-semantics issues, swap in a [`SessionStore`(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/session-storage); that's also what tier 3 and production deployments use.)

One-time setup, **in your terminal** (`modal setup` opens a browser, so it can't run from a notebook cell):



pip install modal

modal setup

Then create the secret Modal will inject as `ANTHROPIC_API_KEY`:



%%bash

modal secret create anthropic ANTHROPIC\_API\_KEY="$(grep ANTHROPIC\_API\_KEY hosting/.env | cut -d= -f2)"



```
Created a new secret 'anthropic' with the key 'ANTHROPIC_API_KEY'

Use it in your Modal app:

@app.38;2;248;248;242;48;
2;39;40;34mfunction(secret
s=[38;2;248;248;242;4
8;2;39;40;34mmodal.Secret
0m.from_name38;2;248;248;
242;48;2;39;40;34m("anthro
pic")38;2;248;248;24
2;48;2;39;40;34m])

def 38;2;166;226;46;48;2
;39;40;34msome_function()
[0m:

    os
0m.getenv38;2;248;248;242
;48;2;39;40;34m("ANTHROPIC
_API_KEY")48;2;39;40
;34m
```



%%bash

python hosting/modal/modal\_app.py | tee /tmp/modal\_deploy.out

MODAL\_URL=$(awk '/^url:/ {print $2}' /tmp/modal\_deploy.out)

MODAL\_TOKEN=$(awk '/^token:/ {print $2}' /tmp/modal\_deploy.out)

{ echo "MODAL\_URL=$MODAL\_URL"; echo "MODAL\_TOKEN=$MODAL\_TOKEN"; } > /tmp/modal\_url.env



```
sandbox: sb-7R7zQ7TtX0h9eKZ8qslvwo
url:     https://ta-01ks91e217n9fymaxjtdc9k5bh-8000-kn9n102ljd7y4
majwav00kwg0.w.modal.host
token:   sb-…redacted…

⚠️  The URL is p
ublic. The token is the only thing gating it — don't share both.

Try it:
  curl -N -X POST https:
//ta-01ks91e217n9fymaxjtdc9k5bh-8000-kn9n102ljd7y4majwav00kwg0.w.modal.host/sessions/demo-1/messages
 \
    -H 'Authorization: Bearer sb-…redacted…' \
    -H 'Content-Type
: application/json' \
    -d '{"prompt":"What are the latest AI agent trends?"}'
```



%%bash

source /tmp/modal\_url.env

curl -N -s -X POST "$MODAL\_URL/sessions/demo-1/messages" \

-H "Authorization: Bearer $MODAL\_TOKEN" \

-H 'Content-Type: application/json' \

-d '{"prompt":"Give me a one-sentence summary of the Claude Agent SDK."}'



```
event: message
data: {"subtype": "init", "data": {"type": "system", "subtype": "init", "cwd": "/app", "session_id": "1566ffe4-2b20-4a68-82ff-283984b64451", "tools": ["Task", "TaskOutput", "Bash", "Glob", "Grep", "ExitPlanMode", "Read", "Edit", "Write", "N … [truncated]

event: message
data: {"content": [{"id": "toolu_01PPS8yzMBzMnRhG2Hnpk5VL", "name": "WebSearch", "input": {"query": "Claude Agent SDK Anthropic 2026"}}], "model": "claude-sonnet-4-6", "parent_tool_use_id": null, "error": null, "usage": {"input_tokens": 120 … [truncated]

[... 5 events omitted — thinking blocks, tool loading, and web-search result payloads ...]

event: message
data: {"content": [{"text": "The **Claude Agent SDK** is Anthropic's framework that gives developers programmatic access to the same tools, agent loop, and context management that power Claude Code \u2014 enabling the creation of AI agents that can autonomously read files, run commands, search the w … [truncated]

event: message
data: {"subtype": "success", "duration_ms": 12879, "duration_api_ms": 12871, "is_error": false, "num_turns": 3, "session_id": "1566ffe4-2b20-4a68-82ff-283984b64451", "stop_reason": "end_turn", "total_cost_usd": 0.045893199999999995, "usage" … [truncated]

event: done
data:
```

Same interface, same image, different host. When nothing's calling it, Modal scales the sandbox to zero and you pay nothing.

Teardown so you aren't billed for idle resources:



%%bash

python hosting/modal/teardown.py



```
terminating sandbox sb-7R7zQ7TtX0h9eKZ8qslvwo
deleted volume research-agent-sessions
```

---

##  Tier 3 — Kubernetes: when you need to own the infrastructure

Tier 3 is for multi-tenant production, regulated environments, or anywhere you need full control over networking, isolation, and cost. The agent image and interface are still identical; what's new is the machinery *around* it:

* A **gateway** in front that authenticates callers and only forwards `session_id`s they own. This is where the auth that `server.py` leaves out finally happens.
* **Pod-per-session** routing (gateway → Redis → pod) so each conversation gets its own blast radius.
* A **standby pool** of pre-warmed pods so new sessions don't pay cold-start latency.
* **Egress lockdown** (NetworkPolicy + an allowlisting proxy) so a prompt-injected agent can reach `api.anthropic.com` and nothing else.

The full manifests, gateway, and a step-by-step architecture walkthrough live in [`hosting/kubernetes/`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/./hosting/kubernetes/). It runs end-to-end on a local [kind(opens in new tab)](https://kind.sigs.k8s.io/) cluster with no cloud account:



cd hosting/kubernetes

ANTHROPIC\_API\_KEY=sk-ant-... ./kind-quickstart.sh

The quickstart prints bearer tokens for two demo tenants (`alice` and `bob`). The gateway scopes every session to the tenant that created it: the same `curl -N POST /sessions/{id}/messages` as tiers 1 and 2, now aimed at the gateway on `:8080` with an `Authorization: Bearer <alice-token>` header, works for alice, while the same request with bob's token gets a 403. The README's *Deploying to your own cluster* section covers the registry/ingress changes for a real cluster.

*The Kubernetes tier builds on internal work by Joe Shamon and Ben Lehrburger.*

---

##  Making it production-ready

Two production concerns you can wire up in a few lines each. The cells below show the code; the [hosting docs(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/hosting) cover the full production checklist (auth, graceful shutdown, idle-timeout tuning, autoscaling, cost controls).

###  Observability

The SDK emits OpenTelemetry spans for every turn and tool call. Point it at your collector with two env vars, with no code changes to `server.py` ([docs(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/observability)):



# In docker-compose.yml / modal\_app.py / your k8s Deployment:

# OTEL\_EXPORTER\_OTLP\_ENDPOINT=http://your-collector:4317

# OTEL\_SERVICE\_NAME=research-agent

###  Liveness

`GET /health` is already in `server.py`. Point your orchestrator's liveness probe at it (compose `healthcheck:`, Modal health checks, k8s `livenessProbe`).

###  Persistence beyond a volume

The `/data` volume mount is fine for single-host and Modal. For multi-host production, use a [`SessionStore` adapter(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/session-storage) that mirrors transcripts to shared storage (S3, Postgres, Redis). Note that SessionStore is a mirror; the local disk write always happens first, and mirror failures emit `mirror_error` without interrupting the agent.

###  Wire format

`server.py` streams raw SDK message types. That's fine for a cookbook; for a real API you'd define a stable wire format so SDK version bumps don't break clients.

---

##  Choosing your tier

| Tier | What it gives you | Pick it when | Move up when |
| --- | --- | --- | --- |
| **1. Docker** | A container on a machine you control. Compose restarts it and a bind mount keeps `/data`. You operate one Docker host. | Dev loop, internal tools, single-tenant apps, cron/batch jobs. You can restart it by hand and nobody outside your network calls it. | Someone outside that machine needs a URL, or "restart it by hand" stops being acceptable. |
| **2. Modal** | The same image behind a public HTTPS URL with scale-to-zero and remote builds. You operate nothing. | You want a callable endpoint today, traffic is bursty or zero most of the time, and a per-deploy bearer token is enough auth. | You need real multi-tenant isolation, network-level egress control, or your platform team requires workloads on their cluster. |
| **3. Kubernetes** | Pod-per-session isolation, an authenticating gateway with tenant-scoped sessions, egress lockdown, and a warm standby pool. You operate the cluster, the gateway, and Redis. | Multi-tenant production, regulated environments, or you already run Kubernetes and want agents to follow the same operational model as everything else. | This is the top of this notebook's ladder; from here you tune autoscaling, multi-region routing, and durable session stores rather than migrating. |

The [hosting guide(opens in new tab)](https://code.claude.com/docs/en/agent-sdk/hosting)'s deployment patterns map onto these tiers directly. **Ephemeral sessions** (pattern 1: one prompt, one process, exit) are tier 1a: no server, run the container from cron or a queue worker on any host. **Long-running** and **hybrid sessions** (patterns 2 and 3, where a process holds or rehydrates conversation state across turns) are what `server.py` implements with `resume=` plus the `/data` volume; tiers 1b, 2, and 3 all serve this shape and differ only in who keeps that process alive and how callers reach it. **Single containers** (pattern 4, many sessions multiplexed into one container) is exactly what tiers 1b and 2 do; tier 3 exists for when that stops being acceptable and each session needs its own blast radius.

---

##  Appendix — Porting to other providers

Same `hosting/Dockerfile`, different deploy command. Each of these exposes port 8000 and gives you a URL; mount something at `/data` for persistence.

**Fly Machines**



fly launch --dockerfile hosting/Dockerfile --no-deploy # run from claude\_agent\_sdk/

fly volumes create data --size 1

fly deploy

**E2B**



from e2b import Sandbox

sbx = Sandbox(template="research-agent") # template built from hosting/Dockerfile

sbx.commands.run("./hosting/entrypoint.sh serve", background=True)

url = sbx.get\_host(8000)

**Daytona**



from daytona import Daytona, CreateSandboxFromImageParams

sbx = Daytona().create(CreateSandboxFromImageParams(image="research-agent"))

sbx.process.exec("./hosting/entrypoint.sh serve")

**Cloudflare Containers**



// wrangler.toml points at hosting/Dockerfile

export class Agent extends Container { defaultPort = 8000 }

**Vercel Sandbox**



import { Sandbox } from "@vercel/sandbox";

const sbx = await Sandbox.create({ image: "research-agent", ports: [8000] });

await sbx.runCommand({ cmd: "./hosting/entrypoint.sh", args: ["serve"], detached: true });
