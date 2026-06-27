---
title: "What is Claude Managed Agents?"
channel: claude
url: https://www.youtube.com/watch?v=NLWiIj47IdI
youtube_id: NLWiIj47IdI
published: 2026-04-09
duration: "3:52"
captions: en-orig
---

# What is Claude Managed Agents?

[![What is Claude Managed Agents?](https://img.youtube.com/vi/NLWiIj47IdI/hqdefault.jpg)](https://www.youtube.com/watch?v=NLWiIj47IdI)

<details>
<summary>자막: What is Claude Managed Agents? (3:52)</summary>

[00:00]
Claude Managed Agents is a suite of APIs
for building and deploying agents at
scale.
You define agents with specific tools,
personas, and capabilities.
You configure sandbox environments with
the right packages and network controls.
You fire off sessions from your own
application, and then Claude does the
work inside an isolated container with
full file system access, bash execution,
and web search.
I have a year a Kanban board sitting on
top of Managed Agents.
I drag one over to the in progress, and
then that fires off a session
automatically. Now, the ticket says
"Optimize website performance." So, my
back end creates a session. It points to
an environment that I configured with
Lighthouse and Puppeteer pre-installed,
and mount my GitHub repo into that
container. Claude has the code base, the
tools, and a rubric. Lighthouse score
above 90, no render-blocking resources,

[00:01]
all images lazy loaded. And then we can
see here that Claude runs the audit. It
starts compressing images, inlining CSS,
deferring scripts.
Every tool call streams back to the
board in real time through the event
stream. So, the rubric kicks in. A
separate grader running at its own
context window evaluates the output
against my criteria. Claude reads that
feedback, goes back in, fixes what it
misses, and then resubmits.
Good. We're up to 96.
And note that I can drag a second ticket
over while the first is still running.
Two sessions, two containers, two
separate tasks running in parallel.
So, I have another agent here that's job
is to track prices and plan changes
across every SaaS tool that our company
pays for, and have a report ready before
stand-up. Common.
Claude searches the web for current
pricing pages, checks for plan tier
changes, flags new features that might
affect your contracts. It then runs a

[00:02]
cost analysis in Python inside of that
sandbox. And then it also uses an Excel
spreadsheet skill and writes an
executive summary. And when the report
is ready, Claude posts a link to Slack
and creates a review task in Asana, both
through MCP servers.
The agent also reads from and writes to
a memory store.
Before it starts, it checks what it
found last week. After it finishes, it
stores what's changed. So, next Monday's
report says, "Cloud compute 15% lower
since last week." instead of listing the
same static pricing data.
I have an alert here that fired from my
monitoring stack. A custom tool my back
end receives the alert payload and sends
it into a new session as a tool result.
This session uses multi-agent
coordination. A coordinator agent
receives the alert and delegates to
three specialists, each running in their
own context window on the same shared
file system.
The specialists report back. The
coordinator synthesizes their findings
into a single incident summary. And

[00:03]
before it posts the update to Slack, the
permissions policy fires. And so I see
the draft on screen, approve it, and the
message goes out. Memory ties all of
this together. The coordinator checks
past incidents in the memory store and
flags a pattern. This looks like the DNS
resolution issue from 2 weeks ago that
was caused by a misconfigured TTL. So,
that means that the next time a similar
alert fires, the agent starts with that
context instead of diagnosing from
scratch.
Managed agents gives developers the
tools to deliver a fully managed
stateful agent experience with agents,
sessions, environments, tools, MCP,
memory, outcomes, and multi-agent
coordination.
You define what done looks like. Claude
works until it gets there.

</details>
