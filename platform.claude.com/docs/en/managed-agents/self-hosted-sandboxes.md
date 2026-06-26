<!-- source: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes -->

# Self-hosted sandboxes
Run agent sessions in your own self-hosted sandbox environment.
By default, Managed Agents executes tools and code inside [Anthropic-managed cloud sandboxes](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment.
Tool execution stays on your host: the filesystem the agent reads and writes, the processes it spawns, and the network it can reach are all under your control. Tool inputs and outputs still flow to Anthropic's control plane (where Claude runs) so the model can see results and determine what to do next. See the [security model](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security) for the full data-flow boundary.
Self-hosted sandboxes support all Claude models available in Managed Agents, including Claude Opus 4.8. The model is configured on the [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup), not the environment.
How it differs from cloud environments  
|   | Cloud environment  | Self-hosted sandbox  |  
| --- | --- | --- |  
| Where tools run  | Anthropic-managed sandboxes  | Your infrastructure  |  
| Network reach  | Anthropic's egress controls  | Your network policy  |  
| File and GitHub repo mounting  | Managed by Anthropic  | Managed by you  |  
| Lifecycle  | Managed by Anthropic  | Managed by you  |  
Self-hosting is a good fit when the agent needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable, or run under your organization's own compliance and audit controls.
For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).
When to combine with MCP tunnels
Self-hosting controls _where the agent's code executes_. [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) control _how Anthropic reaches MCP servers in your network_. They are independent: a session running in Anthropic's cloud sandboxes can still reach private MCP servers through a tunnel, and a self-hosted session can use either tunneled or public MCP servers. Use both when you want execution and tool access to stay inside your boundary.
Environment worker

This guide describes how to build a worker with any generic sandboxing platform. Additional, platform-specific guides are available for [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html), [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents), [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [E2B](https://e2b.dev/docs/agents/claude-managed-agents), [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox), [Namespace](https://namespace.so/docs/integrations/claude), [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents), and [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox).
An environment worker is a process you run on your own infrastructure. It receives tool execution requests from Anthropic and runs them locally. The `self_hosted` environment acts as a work queue: when a [session](https://platform.claude.com/docs/en/managed-agents/sessions) is assigned to it, Anthropic enqueues the session as a work item. Your worker claims work items from that queue, spawns an execution context for each one, downloads the agent's [skills](https://platform.claude.com/docs/en/managed-agents/skills) (reusable, filesystem-based resources that give the agent domain-specific expertise), runs the tool calls, and posts the results back.
Work items are claimed by polling the environment's queue: either by an **always-on worker** that polls continuously, or a **webhook-triggered handler** that wakes on `session.status_run_started` and starts polling.
The CLI and SDK both ship pre-built workers. The `ant` CLI supports the always-on pattern only; the SDK supports both always-on and webhook-triggered. Both are configurable: see [Self-hosted worker](https://platform.claude.com/docs/en/managed-agents/reference#self-hosted-worker) in the reference for CLI flags, and [SDK helpers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sdk-helpers) on this page for the SDK options. For more control, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) directly and implement your own worker.
### 
Sandbox filesystem
  * **`/workspace`:** the system default working directory for tool execution and skill download. The CLI's `--workdir` flag defaults to the current directory; pass `--workdir /workspace` to match the system default. Skills are downloaded to `<workdir>/skills/<name>/`. If you use a different working directory, update your agent's system prompt so Claude can locate the skill files.
  * **`/mnt/session/outputs`:** the worker harness instructs Claude to write final deliverables here. In sandbox mode, mount a host directory at this path to retrieve outputs after the session ends. In in-process mode, the worker's file tools write under the working directory instead, so this path does not apply.

Before you begin
You need:
  * **An existing agent.** If you don't have one, complete the [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) first and note its agent ID.
  * **A Linux host** with `/bin/bash` at that exact path. The TypeScript SDK additionally requires `unzip`, `tar`, and Node.js 22 or later; the Python SDK uses the standard library for archive extraction and has no additional binary requirements. These dependencies are resolved at fixed paths and do not respect `PATH` overrides.
  * **The`ant` CLI or an Anthropic SDK** (Python, TypeScript, or Go) on the worker host.
  * **Two credentials:** an environment key (generated in the steps that follow) authenticates the worker to its queue; your Claude API key creates sessions and reads queue stats from outside the worker host.

On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.
  1. 1
Create a self-hosted environment
In the [Console](https://platform.claude.com/workspaces/default/environments): **Workspace > Environments > New > Self-hosted**
Or through the API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

environment = client.beta.environments.create(
    name="self-hosted", config={"type": "self_hosted"}
)
print(environment.id)

  2. 2
Generate an environment key
In the Console, open the environment and click **Generate environment key**. Key generation is Console-only, regardless of whether you created the environment through the Console or the API. Then export the environment ID and key on the worker host:

export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
export ANTHROPIC_ENVIRONMENT_ID="env_..."

Skills can include executables that the agent may run directly. The CLI and SDK workers automatically mark downloaded skill files as executable in the sandbox. If you implement skills download manually, you are responsible for setting executable permissions.
Run a worker
Choose **always-on** for the simplest setup: a long-running process polls the queue continuously and needs only outbound HTTPS. Choose **webhook-triggered** to avoid running an idle poller; it requires a webhook endpoint that Anthropic can reach (see [Webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) for endpoint setup and signature verification).
Always-on (ant CLI)
Always-on (ant CLI)
Always-on (SDK)
Always-on (SDK)
Webhook-triggered (SDK)
Webhook-triggered (SDK)
  1. 1
Install the ant CLI
Run this on the worker host.

VERSION=1.12.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant

  2. 2
Run the worker
**In-process**
`ant beta:worker poll` claims work items assigned to the environment, downloads skills, executes tool calls in the working directory, and posts results back.

ant beta:worker poll \
  --workdir "/workspace"

The worker exits cleanly on SIGTERM or SIGINT, draining in-flight tool calls before stopping.
**Sandbox per session**
If you need stronger isolation (a fresh filesystem, resource limits, or per-session network controls), run each session in its own sandbox. Build an image with `ant` installed and `ant beta:worker run` as the entrypoint. The base image must provide `/bin/bash`; `curl` is only used at build time. When a sandbox starts, it reads session details from environment variables, handles that session, and exits:

FROM your-base-image
ARG ANT_VERSION=1.12.0
ARG TARGETARCH
RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
    curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
      | tar -xz -C /usr/local/bin ant
WORKDIR /workspace
VOLUME /mnt/session/outputs
ENTRYPOINT ["ant", "beta:worker", "run"]

Then write a spawn script that forwards session details into a fresh sandbox. The poller injects `ANTHROPIC_SESSION_ID`, `ANTHROPIC_WORK_ID`, `ANTHROPIC_ENVIRONMENT_ID`, and `ANTHROPIC_ENVIRONMENT_KEY` into the script's environment. `ANTHROPIC_BASE_URL` is optional and is passed through only if it was set on the poller host; it overrides the default API endpoint. In the example, `/host/outputs` is a host directory you choose; it is bind-mounted to the sandbox's `/mnt/session/outputs` so you can retrieve session deliverables after the sandbox exits.

#!/bin/bash
# spawn.sh: called once per session
mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
exec docker run --rm \
  -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
  -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
  -v "/host/outputs/$ANTHROPIC_SESSION_ID":/mnt/session/outputs \
  your-image

Start the poller pointing at the script:

ant beta:worker poll \
  --on-work ./spawn.sh

### 
SDK helpers
The SDK provides three helpers at different levels of control. `EnvironmentWorker` covers most use cases; drop to the lower-level helpers when you need to launch your own per-session process or run tools against an already-claimed session.
  * **`EnvironmentWorker`:** the out-of-the-box worker. Handles polling, setup, and execution end to end.
    * `.run()`: runs indefinitely, picking up sessions as they arrive. Exits cleanly on SIGTERM.
    * `.handle_item()`: picks up one pending session, handles it, and exits.
  * **`work.poller()`:** polls the work queue on your behalf and gives you each claimed session. Use this when you want to decide what happens for each session, for example launching a sandbox rather than running tools in-process.
    * `drain`: whether to stop polling once the queue is empty rather than waiting for new work.
    * `block_ms`: how long to wait for work to arrive before returning, in milliseconds. Must be between 1 and 999 (per-poll wait; the helper re-polls automatically). Pass `null` (`None` in Python, `param.Null[int64]()` in Go) for a non-blocking check; omitting the parameter uses the default 999 ms long-poll.
    * `reclaim_older_than_ms`: re-claim work items leased to a worker that has stopped responding.
    * `auto_stop`: whether to post a stop signal on the work item after the iterator exits. The Go poller has no opt-out and always posts the stop signal, so block in the loop body until the session completes rather than detaching.
  * **`client.beta.sessions.events.tool_runner()`:** runs tool calls for a single session, given the session ID and a tool list. Use when you've already claimed the work and only need the execution layer.

Use the work poller directly when you want to launch your own per-session process, for example spinning up a sandbox for each claimed session:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import asyncio
import os

from anthropic import AsyncAnthropic
from anthropic.types.beta.environments import BetaSelfHostedWork

async def launch_container(work: BetaSelfHostedWork) -> None:
    # Replace with your own per-session sandbox launcher. Pass
    # ANTHROPIC_ENVIRONMENT_KEY into the launched sandbox, never
    # your API key.
    print(f"claimed session {work.data.id}")

async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        async for work in client.beta.environments.work.poller(
            environment_id=environment_id,
            environment_key=environment_key,
            auto_stop=False,  # the launched sandbox owns the stop call
        ):
            await launch_container(work)

asyncio.run(main())

**`AgentToolContext`**is the execution context for tool calls. It defines the working directory and path policy, and optionally downloads the session's skills when used as a context manager.**`beta_agent_toolset_20260401(env)`**takes an`AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).
**With`EnvironmentWorker` :** both are managed automatically. Pass a `tools` factory to customize the tool list:
Python

EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])

**With`work.poller()` and `tool_runner()`:** pass a tool list as `tools` to `client.beta.sessions.events.tool_runner()`. To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)`:
PythonTypeScriptC#GoJavaPHPRuby

from anthropic.lib.tools.agent_toolset import (
    AgentToolContext,
    beta_agent_toolset_20260401,
)

async with AgentToolContext(
    workdir="/workspace", client=client, session_id=work.data.id
) as env:
    # skills downloaded to /workspace/skills/<name>/
    tools = beta_agent_toolset_20260401(env)

### 
Verify the worker is connected
From a separate shell, using your Claude API key (not the environment key), confirm `workers_polling` is at least 1:

ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"

If `workers_polling` stays at 0, the worker isn't reaching the queue: confirm `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host. See [Read queue depth](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#read-queue-depth) for the full stats response and other language examples.
Start a session
Once your worker is running, create a session that targets the environment. The session enters the environment's work queue and waits there until a worker claims it; if no worker is connected, the session stays queued rather than failing.
Anthropic doesn't mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available, pass file references (such as an S3 path or commit SHA) in the session `metadata` field. Your spawn script or `--on-work` handler reads that metadata from the claimed work item (through the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work)) and stages the files into the working directory before tool execution begins.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    metadata={"input_file": "s3://my-bucket/data.csv"},
)

[Memory](https://platform.claude.com/docs/en/managed-agents/memory) is not currently supported with self-hosted sandboxes.
See [Self-hosted worker](https://platform.claude.com/docs/en/managed-agents/reference#self-hosted-worker) in the reference for the full list of CLI flags, and [SDK helpers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sdk-helpers) for the SDK helper options.
Monitoring and operations
These calls run from your monitoring or operations tooling, authenticated with your Claude API key, to observe and manage the worker fleet. The claim and keep-alive loop is handled inside the worker helpers, so you don't call those endpoints directly.

These endpoints authenticate with your organization API key, not the environment key. Call them from outside the worker host. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.
### 
Read queue depth
`work.stats` returns the queue state for an environment:
  * `depth` is the number of items waiting to be claimed. Scale your worker fleet or alert on backlog based on this value.
  * `pending` is the number of items a worker has claimed and is currently processing.
  * `oldest_queued_at` is the timestamp of the oldest item in the queue, or `null` if the queue is empty.
  * `workers_polling` is the number of workers that have polled in the last 30 seconds. Use this for liveness alerting.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import os

import anthropic

client = anthropic.Anthropic()

stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
print(f"depth={stats.depth} pending={stats.pending}")

  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0

### 
Stop a session gracefully
Use `work.stop` to ask the worker handling a specific session to shut it down cleanly. The worker finishes any in-flight tool call, posts a final status, and releases the session. Pass `force: true` in the request body to interrupt immediately instead of waiting for the current tool call to complete.
Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import os

import anthropic

client = anthropic.Anthropic()

work = client.beta.environments.work.stop(
    os.environ["ANTHROPIC_WORK_ID"],
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
)
print(work.state)

Next steps
[  Managed Agent sessions Create a session to run your agent and begin executing tasks. ](https://platform.claude.com/docs/en/managed-agents/sessions)[  MCP tunnels overview Reach MCP servers inside your private network from any execution environment. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)[  Security model Understand the shared responsibility model for self-hosted sandbox environments. ](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security)
  * [How it differs from cloud environments](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#how-it-differs-from-cloud-environments)
  * [When to combine with MCP tunnels](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#when-to-combine-with-mcp-tunnels)
  * [Environment worker](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#environment-worker)
  * [Sandbox filesystem](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sandbox-filesystem)
  * [Before you begin](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#before-you-begin)
  * [Run a worker](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-a-worker)
  * [SDK helpers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sdk-helpers)
  * [Verify the worker is connected](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#verify-the-worker-is-connected)
  * [Start a session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#start-a-session)
  * [Monitoring and operations](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#monitoring-and-operations)
  * [Read queue depth](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#read-queue-depth)
  * [Stop a session gracefully](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#stop-a-session-gracefully)
  * [Next steps](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#next-steps)

Managed Agents/Self-hosted sandboxes
# Self-hosted sandboxes
Run agent sessions in your own self-hosted sandbox environment.
By default, Managed Agents executes tools and code inside [Anthropic-managed cloud sandboxes](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control, so the agent's code, filesystem, and network egress never leave your environment.
Tool execution stays on your host: the filesystem the agent reads and writes, the processes it spawns, and the network it can reach are all under your control. Tool inputs and outputs still flow to Anthropic's control plane (where Claude runs) so the model can see results and determine what to do next. See the [security model](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security) for the full data-flow boundary.
Self-hosted sandboxes support all Claude models available in Managed Agents, including Claude Opus 4.8. The model is configured on the [agent](https://platform.claude.com/docs/en/managed-agents/agent-setup), not the environment.
How it differs from cloud environments  
|   | Cloud environment  | Self-hosted sandbox  |  
| --- | --- | --- |  
| Where tools run  | Anthropic-managed sandboxes  | Your infrastructure  |  
| Network reach  | Anthropic's egress controls  | Your network policy  |  
| File and GitHub repo mounting  | Managed by Anthropic  | Managed by you  |  
| Lifecycle  | Managed by Anthropic  | Managed by you  |  
Self-hosting is a good fit when the agent needs to operate on data that cannot leave your network boundary, reach internal services that are not publicly routable, or run under your organization's own compliance and audit controls.
For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).
When to combine with MCP tunnels
Self-hosting controls _where the agent's code executes_. [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) control _how Anthropic reaches MCP servers in your network_. They are independent: a session running in Anthropic's cloud sandboxes can still reach private MCP servers through a tunnel, and a self-hosted session can use either tunneled or public MCP servers. Use both when you want execution and tool access to stay inside your boundary.
Environment worker

This guide describes how to build a worker with any generic sandboxing platform. Additional, platform-specific guides are available for [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html), [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents), [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/), [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents), [E2B](https://e2b.dev/docs/agents/claude-managed-agents), [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox), [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox), [Namespace](https://namespace.so/docs/integrations/claude), [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents), and [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox).
An environment worker is a process you run on your own infrastructure. It receives tool execution requests from Anthropic and runs them locally. The `self_hosted` environment acts as a work queue: when a [session](https://platform.claude.com/docs/en/managed-agents/sessions) is assigned to it, Anthropic enqueues the session as a work item. Your worker claims work items from that queue, spawns an execution context for each one, downloads the agent's [skills](https://platform.claude.com/docs/en/managed-agents/skills) (reusable, filesystem-based resources that give the agent domain-specific expertise), runs the tool calls, and posts the results back.
Work items are claimed by polling the environment's queue: either by an **always-on worker** that polls continuously, or a **webhook-triggered handler** that wakes on `session.status_run_started` and starts polling.
The CLI and SDK both ship pre-built workers. The `ant` CLI supports the always-on pattern only; the SDK supports both always-on and webhook-triggered. Both are configurable: see [Self-hosted worker](https://platform.claude.com/docs/en/managed-agents/reference#self-hosted-worker) in the reference for CLI flags, and [SDK helpers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sdk-helpers) on this page for the SDK options. For more control, call the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work) directly and implement your own worker.
### 
Sandbox filesystem
  * **`/workspace`:** the system default working directory for tool execution and skill download. The CLI's `--workdir` flag defaults to the current directory; pass `--workdir /workspace` to match the system default. Skills are downloaded to `<workdir>/skills/<name>/`. If you use a different working directory, update your agent's system prompt so Claude can locate the skill files.
  * **`/mnt/session/outputs`:** the worker harness instructs Claude to write final deliverables here. In sandbox mode, mount a host directory at this path to retrieve outputs after the session ends. In in-process mode, the worker's file tools write under the working directory instead, so this path does not apply.

Before you begin
You need:
  * **An existing agent.** If you don't have one, complete the [Quickstart](https://platform.claude.com/docs/en/managed-agents/quickstart) first and note its agent ID.
  * **A Linux host** with `/bin/bash` at that exact path. The TypeScript SDK additionally requires `unzip`, `tar`, and Node.js 22 or later; the Python SDK uses the standard library for archive extraction and has no additional binary requirements. These dependencies are resolved at fixed paths and do not respect `PATH` overrides.
  * **The`ant` CLI or an Anthropic SDK** (Python, TypeScript, or Go) on the worker host.
  * **Two credentials:** an environment key (generated in the steps that follow) authenticates the worker to its queue; your Claude API key creates sessions and reads queue stats from outside the worker host.

On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.
  1. 1
Create a self-hosted environment
In the [Console](https://platform.claude.com/workspaces/default/environments): **Workspace > Environments > New > Self-hosted**
Or through the API:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

client = anthropic.Anthropic()

environment = client.beta.environments.create(
    name="self-hosted", config={"type": "self_hosted"}
)
print(environment.id)

  2. 2
Generate an environment key
In the Console, open the environment and click **Generate environment key**. Key generation is Console-only, regardless of whether you created the environment through the Console or the API. Then export the environment ID and key on the worker host:

export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
export ANTHROPIC_ENVIRONMENT_ID="env_..."

Skills can include executables that the agent may run directly. The CLI and SDK workers automatically mark downloaded skill files as executable in the sandbox. If you implement skills download manually, you are responsible for setting executable permissions.
Run a worker
Choose **always-on** for the simplest setup: a long-running process polls the queue continuously and needs only outbound HTTPS. Choose **webhook-triggered** to avoid running an idle poller; it requires a webhook endpoint that Anthropic can reach (see [Webhooks](https://platform.claude.com/docs/en/managed-agents/webhooks) for endpoint setup and signature verification).
Always-on (ant CLI)
Always-on (ant CLI)
Always-on (SDK)
Always-on (SDK)
Webhook-triggered (SDK)
Webhook-triggered (SDK)
  1. 1
Install the ant CLI
Run this on the worker host.

VERSION=1.12.0
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')
curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
  | sudo tar -xz -C /usr/local/bin ant

  2. 2
Run the worker
**In-process**
`ant beta:worker poll` claims work items assigned to the environment, downloads skills, executes tool calls in the working directory, and posts results back.

ant beta:worker poll \
  --workdir "/workspace"

The worker exits cleanly on SIGTERM or SIGINT, draining in-flight tool calls before stopping.
**Sandbox per session**
If you need stronger isolation (a fresh filesystem, resource limits, or per-session network controls), run each session in its own sandbox. Build an image with `ant` installed and `ant beta:worker run` as the entrypoint. The base image must provide `/bin/bash`; `curl` is only used at build time. When a sandbox starts, it reads session details from environment variables, handles that session, and exits:

FROM your-base-image
ARG ANT_VERSION=1.12.0
ARG TARGETARCH
RUN ARCH=$([ "$TARGETARCH" = "arm64" ] && echo arm64 || echo amd64) && \
    curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${ANT_VERSION}/ant_${ANT_VERSION}_linux_${ARCH}.tar.gz" \
      | tar -xz -C /usr/local/bin ant
WORKDIR /workspace
VOLUME /mnt/session/outputs
ENTRYPOINT ["ant", "beta:worker", "run"]

Then write a spawn script that forwards session details into a fresh sandbox. The poller injects `ANTHROPIC_SESSION_ID`, `ANTHROPIC_WORK_ID`, `ANTHROPIC_ENVIRONMENT_ID`, and `ANTHROPIC_ENVIRONMENT_KEY` into the script's environment. `ANTHROPIC_BASE_URL` is optional and is passed through only if it was set on the poller host; it overrides the default API endpoint. In the example, `/host/outputs` is a host directory you choose; it is bind-mounted to the sandbox's `/mnt/session/outputs` so you can retrieve session deliverables after the sandbox exits.

#!/bin/bash
# spawn.sh: called once per session
mkdir -p "/host/outputs/$ANTHROPIC_SESSION_ID"
exec docker run --rm \
  -e ANTHROPIC_SESSION_ID -e ANTHROPIC_ENVIRONMENT_KEY \
  -e ANTHROPIC_WORK_ID -e ANTHROPIC_ENVIRONMENT_ID -e ANTHROPIC_BASE_URL \
  -v "/host/outputs/$ANTHROPIC_SESSION_ID":/mnt/session/outputs \
  your-image

Start the poller pointing at the script:

ant beta:worker poll \
  --on-work ./spawn.sh

### 
SDK helpers
The SDK provides three helpers at different levels of control. `EnvironmentWorker` covers most use cases; drop to the lower-level helpers when you need to launch your own per-session process or run tools against an already-claimed session.
  * **`EnvironmentWorker`:** the out-of-the-box worker. Handles polling, setup, and execution end to end.
    * `.run()`: runs indefinitely, picking up sessions as they arrive. Exits cleanly on SIGTERM.
    * `.handle_item()`: picks up one pending session, handles it, and exits.
  * **`work.poller()`:** polls the work queue on your behalf and gives you each claimed session. Use this when you want to decide what happens for each session, for example launching a sandbox rather than running tools in-process.
    * `drain`: whether to stop polling once the queue is empty rather than waiting for new work.
    * `block_ms`: how long to wait for work to arrive before returning, in milliseconds. Must be between 1 and 999 (per-poll wait; the helper re-polls automatically). Pass `null` (`None` in Python, `param.Null[int64]()` in Go) for a non-blocking check; omitting the parameter uses the default 999 ms long-poll.
    * `reclaim_older_than_ms`: re-claim work items leased to a worker that has stopped responding.
    * `auto_stop`: whether to post a stop signal on the work item after the iterator exits. The Go poller has no opt-out and always posts the stop signal, so block in the loop body until the session completes rather than detaching.
  * **`client.beta.sessions.events.tool_runner()`:** runs tool calls for a single session, given the session ID and a tool list. Use when you've already claimed the work and only need the execution layer.

Use the work poller directly when you want to launch your own per-session process, for example spinning up a sandbox for each claimed session:
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import asyncio
import os

from anthropic import AsyncAnthropic
from anthropic.types.beta.environments import BetaSelfHostedWork

async def launch_container(work: BetaSelfHostedWork) -> None:
    # Replace with your own per-session sandbox launcher. Pass
    # ANTHROPIC_ENVIRONMENT_KEY into the launched sandbox, never
    # your API key.
    print(f"claimed session {work.data.id}")

async def main() -> None:
    environment_key = os.environ["ANTHROPIC_ENVIRONMENT_KEY"]
    environment_id = os.environ["ANTHROPIC_ENVIRONMENT_ID"]
    async with AsyncAnthropic(auth_token=environment_key) as client:
        async for work in client.beta.environments.work.poller(
            environment_id=environment_id,
            environment_key=environment_key,
            auto_stop=False,  # the launched sandbox owns the stop call
        ):
            await launch_container(work)

asyncio.run(main())

**`AgentToolContext`**is the execution context for tool calls. It defines the working directory and path policy, and optionally downloads the session's skills when used as a context manager.**`beta_agent_toolset_20260401(env)`**takes an`AgentToolContext` and returns the standard tool implementations (`bash`, `read`, `write`, `edit`, `glob`, `grep`).
**With`EnvironmentWorker` :** both are managed automatically. Pass a `tools` factory to customize the tool list:
Python

EnvironmentWorker(client, ..., tools=lambda env: [beta_bash_tool(env), my_custom_tool])

**With`work.poller()` and `tool_runner()`:** pass a tool list as `tools` to `client.beta.sessions.events.tool_runner()`. To build that list, set up `AgentToolContext` yourself and call `beta_agent_toolset_20260401(env)`:
PythonTypeScriptC#GoJavaPHPRuby

from anthropic.lib.tools.agent_toolset import (
    AgentToolContext,
    beta_agent_toolset_20260401,
)

async with AgentToolContext(
    workdir="/workspace", client=client, session_id=work.data.id
) as env:
    # skills downloaded to /workspace/skills/<name>/
    tools = beta_agent_toolset_20260401(env)

### 
Verify the worker is connected
From a separate shell, using your Claude API key (not the environment key), confirm `workers_polling` is at least 1:

ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"

If `workers_polling` stays at 0, the worker isn't reaching the queue: confirm `ANTHROPIC_ENVIRONMENT_KEY` and `ANTHROPIC_ENVIRONMENT_ID` are set on the worker host. See [Read queue depth](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#read-queue-depth) for the full stats response and other language examples.
Start a session
Once your worker is running, create a session that targets the environment. The session enters the environment's work queue and waits there until a worker claims it; if no worker is connected, the session stays queued rather than failing.
Anthropic doesn't mount files or GitHub repositories into self-hosted sandboxes. To make session-specific files available, pass file references (such as an S3 path or commit SHA) in the session `metadata` field. Your spawn script or `--on-work` handler reads that metadata from the claimed work item (through the [Environments Work endpoints](https://platform.claude.com/docs/en/api/beta/environments/work)) and stages the files into the working directory before tool execution begins.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    metadata={"input_file": "s3://my-bucket/data.csv"},
)

[Memory](https://platform.claude.com/docs/en/managed-agents/memory) is not currently supported with self-hosted sandboxes.
See [Self-hosted worker](https://platform.claude.com/docs/en/managed-agents/reference#self-hosted-worker) in the reference for the full list of CLI flags, and [SDK helpers](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#sdk-helpers) for the SDK helper options.
Monitoring and operations
These calls run from your monitoring or operations tooling, authenticated with your Claude API key, to observe and manage the worker fleet. The claim and keep-alive loop is handled inside the worker helpers, so you don't call those endpoints directly.

These endpoints authenticate with your organization API key, not the environment key. Call them from outside the worker host. Setting `ANTHROPIC_API_KEY` on the worker host exposes an organization-scoped credential to agent tool calls.
### 
Read queue depth
`work.stats` returns the queue state for an environment:
  * `depth` is the number of items waiting to be claimed. Scale your worker fleet or alert on backlog based on this value.
  * `pending` is the number of items a worker has claimed and is currently processing.
  * `oldest_queued_at` is the timestamp of the oldest item in the queue, or `null` if the queue is empty.
  * `workers_polling` is the number of workers that have polled in the last 30 seconds. Use this for liveness alerting.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import os

import anthropic

client = anthropic.Anthropic()

stats = client.beta.environments.work.stats(os.environ["ANTHROPIC_ENVIRONMENT_ID"])
print(f"depth={stats.depth} pending={stats.pending}")

  "type": "work_queue_stats",
  "depth": 0,
  "pending": 0,
  "oldest_queued_at": null,
  "workers_polling": 0

### 
Stop a session gracefully
Use `work.stop` to ask the worker handling a specific session to shut it down cleanly. The worker finishes any in-flight tool call, posts a final status, and releases the session. Pass `force: true` in the request body to interrupt immediately instead of waiting for the current tool call to complete.
Because these calls run from your operations tooling rather than the worker host, `ANTHROPIC_WORK_ID` isn't set automatically. Set it to the target work item's ID before running the following examples.
cURLCLIPythonTypeScriptC#GoJavaPHPRuby

import os

import anthropic

client = anthropic.Anthropic()

work = client.beta.environments.work.stop(
    os.environ["ANTHROPIC_WORK_ID"],
    environment_id=os.environ["ANTHROPIC_ENVIRONMENT_ID"],
)
print(work.state)

Next steps
[  Managed Agent sessions Create a session to run your agent and begin executing tasks. ](https://platform.claude.com/docs/en/managed-agents/sessions)[  MCP tunnels overview Reach MCP servers inside your private network from any execution environment. ](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)[  Security model Understand the shared responsibility model for self-hosted sandbox environments. ](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security)
