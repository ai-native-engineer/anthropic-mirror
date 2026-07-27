<!-- source: https://platform.claude.com/cookbook/claude-agent-sdk-05-building-a-session-browser -->

# Building a Session Browser

When you ship an agent as a product (a desktop app, an IDE extension, an internal chatbot), the first thing users ask for is the sidebar. They want to see the conversation from last Tuesday, jump back into it, and maybe branch off in a new direction without losing the original. The agent loop is half the product; the other half is session management.

The Claude Agent SDK writes every conversation to a JSONL transcript on disk. It also ships a set of functions that read those transcripts back and organize them, so you can build that sidebar without writing a file parser or walking `~/.claude/projects/` by hand.

**By the end of this cookbook, you'll be able to:**

* List and render past sessions for a project, with pagination and metadata like branch, title, and last-modified time
* Read a stored session's messages back into your UI without spawning the agent
* Rename, tag, and filter sessions so users can organize their history
* Fork a session at any point and resume the fork as a live `query()` call

This is the pattern behind the session sidebar in Claude Code Desktop and the VS Code extension. The same primitives work for any UI you want to put on top of the Agent SDK.

## Prerequisites

Before following this guide, ensure you have:

**Required Knowledge**

* Python fundamentals, including `async`/`await`
* Basic familiarity with the Agent SDK's `query()` function (see [Notebook 00](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/00_The_one_liner_research_agent.ipynb) for an introduction)

**Required Tools**

* Python 3.11 or higher
* The Claude Code CLI (`npm install -g @anthropic-ai/claude-code`)
* An Anthropic API key ([get one here](https://console.anthropic.com))

## Setup

Install the required dependencies. Session management functions landed in `claude-agent-sdk` v0.1.51.

python

```
%%capture
%pip install -U "claude-agent-sdk>=0.1.51" python-dotenv pandas
```

Load your API key from `.env` and configure the model. We use Haiku here because the demo sessions are short and we want them cheap and fast; in a real product you'd pick whatever model fits your agent.

python

```
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

MODEL = "claude-haiku-4-5"

# All demo sessions live under this project directory. Using a dedicated
# cwd keeps the demo isolated from your real Claude Code sessions.
# Note: this path resolves relative to the kernel's working directory
# (claude_agent_sdk/ when launched per the README).
DEMO_DIR = str(Path("session_browser_demo").resolve())
os.makedirs(DEMO_DIR, exist_ok=True)
print(f"Demo project dir: {DEMO_DIR}")
```

# Part 1: Create some sessions to manage

Session management functions read transcripts that `query()` (or the Claude Code CLI) has already written. To have something to browse, we first run three short conversations and capture their session IDs.

The `cwd` option tells the SDK which project directory this conversation belongs to. Transcripts are filed under `~/.claude/projects/<encoded-cwd>/<session-id>.jsonl`, so every call with the same `cwd` ends up in the same bucket. That bucket is what `list_sessions(directory=...)` reads later.

We disable tools and cap each run at one turn to keep token usage minimal.

python

```
from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

async def run_one_turn(prompt: str) -> str:
    """Run a single-turn conversation and return its session_id."""
    opts = ClaudeAgentOptions(
        model=MODEL,
        cwd=DEMO_DIR,
        max_turns=1,
        allowed_tools=[],  # text-only, no tool loop
    )
    session_id = None
    async for msg in query(prompt=prompt, options=opts):
        if isinstance(msg, ResultMessage):
            session_id = msg.session_id
            preview = (msg.result or "")[:80]
            print(f"[{session_id[:8]}] {preview}...")
    if session_id is None:
        raise RuntimeError("No ResultMessage received; check API key and SDK version.")
    return session_id
```

Three prompts, three sessions. In a real product these would be whatever your users asked the agent.

python

```
prompts = [
    "Give me three name ideas for a CLI tool that manages git worktrees.",
    "Explain the difference between a mutex and a semaphore in one paragraph.",
    "Write a haiku about merge conflicts.",
]

demo_session_ids = []
for p in prompts:
    sid = await run_one_turn(p)
    demo_session_ids.append(sid)

print(f"\nCreated {len(demo_session_ids)} sessions.")
```

# Part 2: List and inspect sessions

## Build the session list

`list_sessions()` scans the project's transcript directory and returns metadata for each session, sorted newest first. It reads file stats plus the head and tail of each transcript, so it stays fast even when the directory has hundreds of files. No subprocess is spawned and no API call is made.

Each `SDKSessionInfo` carries what you need to render a row in a picker: a display summary, last-modified timestamp, git branch, working directory, and any custom title or tag you've set.

python

```
from datetime import datetime

import pandas as pd

from claude_agent_sdk import SDKSessionInfo, list_sessions

sessions = list_sessions(directory=DEMO_DIR)

# Render as a table. In a real UI this would be your sidebar component.
rows = []
for s in sessions:
    rows.append(
        {
            "id": s.session_id[:8],
            "summary": (s.summary[:50] + "...") if len(s.summary) > 50 else s.summary,
            "modified": datetime.fromtimestamp(s.last_modified / 1000).strftime("%H:%M:%S"),
            "branch": s.git_branch or "-",
            "tag": s.tag or "-",
        }
    )

pd.DataFrame(rows)
```

For long histories, pass `limit` and `offset` to page through results. A session picker typically loads the first page, then fetches more as the user scrolls:

```
page_2 = list_sessions(directory=DEMO_DIR, limit=20, offset=20)
```

If your app already stored a session ID (say, in your own database alongside a user record) and you just need that one row, `get_session_info()` is cheaper than listing everything.

python

```
from claude_agent_sdk import get_session_info

info = get_session_info(demo_session_ids[0], directory=DEMO_DIR)

print(f"Session:      {info.session_id}")
print(f"Summary:      {info.summary}")
print(f"First prompt: {info.first_prompt}")
print(f"Created:      {datetime.fromtimestamp(info.created_at / 1000)}")
print(f"Size:         {info.file_size:,} bytes")
```

## Read a session's messages

Once a user clicks a session in the sidebar, you load its conversation into the main view. `get_session_messages()` reconstructs the message chain from the transcript and returns user and assistant turns in order. Like the listing function, it's a pure file read: the agent doesn't need to be running.

Each `SessionMessage` has a `type` (`"user"` or `"assistant"`), a `uuid`, and a `message` dict in the same shape as the Anthropic Messages API (`role`, `content`).

python

```
from claude_agent_sdk import get_session_messages

messages = get_session_messages(demo_session_ids[0], directory=DEMO_DIR)

for m in messages:
    role = m.type
    # content is a list of blocks; pull out the text ones
    text_parts = [
        b.get("text", "")
        for b in m.message.get("content", [])
        if isinstance(b, dict) and b.get("type") == "text"
    ]
    text = " ".join(text_parts).strip()
    print(f"[{role:>9}] {text[:100]}")
```

For long sessions, `limit` and `offset` let you load a window at a time. A chat view might load the last 50 messages on open, then fetch older pages as the user scrolls up. Offsets are applied in chronological order (oldest first), so page 0 is the start of the conversation.

# Part 3: Organize with titles and tags

## Rename a session

Auto-generated summaries are fine for a quick glance, but users often want to give a session a real name. `rename_session()` appends a title entry to the transcript; `list_sessions()` picks it up as `custom_title` on the next read.

Appends are cheap and idempotent: calling rename twice just means the newer title wins. No file rewrite happens.

python

```
from claude_agent_sdk import rename_session

rename_session(demo_session_ids[0], "Worktree CLI naming brainstorm", directory=DEMO_DIR)
rename_session(demo_session_ids[2], "Haiku corner", directory=DEMO_DIR)

# Verify the titles stuck
for s in list_sessions(directory=DEMO_DIR):
    label = s.custom_title or "(auto)"
    print(f"{s.session_id[:8]}  custom_title={label!r}  summary={s.summary[:40]!r}")
```

## Tag and filter

Tags are a single string attached to a session. Use them for whatever categorization your product needs: `"archived"`, `"needs-review"`, `"favorite"`. Pass `None` to clear a tag.

A common pattern is soft-delete: instead of removing the transcript file, tag it `"__hidden"` and filter that out in your list view. The data stays recoverable.

python

```
from claude_agent_sdk import tag_session

# Mark two sessions as favorites, hide the other
tag_session(demo_session_ids[0], "favorite", directory=DEMO_DIR)
tag_session(demo_session_ids[2], "favorite", directory=DEMO_DIR)
tag_session(demo_session_ids[1], "__hidden", directory=DEMO_DIR)

def visible_sessions(directory: str, tag_filter: str | None = None) -> list[SDKSessionInfo]:
    """List sessions, hiding soft-deletes and optionally filtering by tag."""
    results = []
    for s in list_sessions(directory=directory):
        if s.tag == "__hidden":
            continue
        if tag_filter is not None and s.tag != tag_filter:
            continue
        results.append(s)
    return results

favorites = visible_sessions(DEMO_DIR, tag_filter="favorite")
print(f"Visible favorites: {len(favorites)}")
for s in favorites:
    print(f"  {s.session_id[:8]}  [{s.tag}]  {s.custom_title or s.summary}")
```

Tags are single values, not lists. If you need multiple axes (say, a status plus a category), encode them into one string like `"review:urgent"` and parse on read, or store richer state in your own database keyed on `session_id`.

# Part 4: Fork and resume

## Branch from an existing conversation

Forking copies a session's transcript into a new file with freshly remapped message IDs. The original stays untouched. This is the primitive behind "try a different approach" features: the user keeps their original thread and gets a new one to experiment in.

`fork_session()` writes the new file and returns its ID. It doesn't run the agent, so the fork sits on disk until you resume it with `query()`.

python

```
from claude_agent_sdk import fork_session

source = demo_session_ids[0]

fork = fork_session(
    source,
    directory=DEMO_DIR,
    title="Worktree CLI names (round 2)",
)

print(f"Source: {source}")
print(f"Fork:   {fork.session_id}")

# The fork starts with the same message history as the source
source_msgs = get_session_messages(source, directory=DEMO_DIR)
fork_msgs = get_session_messages(fork.session_id, directory=DEMO_DIR)
print(f"Source has {len(source_msgs)} messages, fork has {len(fork_msgs)}")
```

To branch from a specific point rather than the full history, pass `up_to_message_id`. The fork will contain the source transcript up to and including that message. You can get message UUIDs from `get_session_messages()[i].uuid`.

## Resume the fork into a live query

The fork is just a transcript file. To turn it back into a running conversation, hand its ID to `ClaudeAgentOptions.resume`. The agent loads the forked history and continues from there.

python

```
resume_opts = ClaudeAgentOptions(
    model=MODEL,
    cwd=DEMO_DIR,
    max_turns=1,
    allowed_tools=[],
    resume=fork.session_id,
)

async for msg in query(
    prompt="Those were okay. Give me three more names, but punnier.",
    options=resume_opts,
):
    if isinstance(msg, ResultMessage):
        print(f"[fork {fork.session_id[:8]} resumed]")
        print(msg.result)
```

The original session is still sitting there unchanged. List again and you'll see both the source and the fork as separate rows with independent histories.

python

```
for s in list_sessions(directory=DEMO_DIR):
    marker = "(fork)" if s.session_id == fork.session_id else "      "
    print(f"{marker} {s.session_id[:8]}  {s.custom_title or s.summary[:50]}")
```

# Cleanup

`delete_session()` removes a transcript file. It's a hard delete, which is why the soft-delete tag pattern from Part 3 is usually the safer default for user-facing UIs.

Here we use it to tidy up everything the demo created.

python

```
from claude_agent_sdk import delete_session

# Clean up every session in the demo dir, including the fork
for s in list_sessions(directory=DEMO_DIR):
    delete_session(s.session_id, directory=DEMO_DIR)
    print(f"Deleted {s.session_id[:8]}")

remaining = list_sessions(directory=DEMO_DIR)
print(f"\n{len(remaining)} session(s) remaining.")
```

# Recap

We built the core of a session browser against the Agent SDK's local transcript store:

* **Listing** with `list_sessions()` gives you everything needed to render a sidebar, and it scales because it reads file stats and head/tail slices rather than parsing whole transcripts.
* **Reading** with `get_session_messages()` loads a conversation back for display without spawning the agent.
* **Organizing** with `rename_session()` and `tag_session()` appends metadata entries, so it's cheap and the most recent call wins.
* **Forking** with `fork_session()` plus `options.resume` lets users branch a conversation and keep going without touching the original.

All of these are pure file operations on `~/.claude/projects/`. They work whether or not the agent subprocess is running, and they see the same transcripts the Claude Code CLI writes.

## Where to go next

* **Wire it to a UI.** These functions are UI-agnostic; drop them behind a FastAPI route or an Electron IPC handler and you have the backend for a session sidebar.
* **Cross-host sessions.** Transcripts live on the local disk. To share sessions across machines, sync the files or index session IDs and messages into your own store. See [Manage sessions on disk](https://docs.claude.com/en/agent-sdk/local-session-management) for patterns.
* **TypeScript.** The same API exists in `@anthropic-ai/claude-agent-sdk` with camelCase names (`listSessions`, `forkSession`, and so on). See the [TypeScript SDK reference](https://docs.claude.com/en/agent-sdk/typescript).
* **The bigger picture.** Notebooks [00](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/00_The_one_liner_research_agent.ipynb) through [03](https://github.com/anthropics/claude-cookbooks/blob/main/claude_agent_sdk/03_The_site_reliability_agent.ipynb) cover building the agent itself. This notebook covers managing what it leaves behind.
