<!-- source: https://platform.claude.com/cookbook/managed-agents-slack-data-bot -->

#  Build a Slack data analyst bot with Claude Managed Agents

##  Introduction

You'll wrap the agent from [`data_analyst_agent.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb) in a Slack bot built with [Bolt for Python(opens in new tab)](https://docs.slack.dev/tools/bolt-python/), Slack's official framework for building apps. Mention the bot with a question and a CSV attachment to get a narrative report posted back to the thread. Follow-up messages continue the same session.



user: @databot what's driving Q1 revenue? [sales.csv]

│

▼

bot uploads the CSV and starts an agent session

│

▼

bot streams the agent's progress back to the thread

│

▼

bot posts the finished report to the thread

###  What you'll learn

* Kick off an agent run from a Slack mention
* Show the agent's progress as thread updates
* Post the finished report back to the thread
* Keep the conversation going with follow-up replies

###  Prerequisites

1. Run the install cell below.
2. Create a [Slack app(opens in new tab)](https://api.slack.com/apps): choose **Create New App → From a manifest**, paste [`slack_app_manifest.yaml`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/example_data/slack_data_bot/slack_app_manifest.yaml), and install it to your workspace. The manifest enables Socket Mode (Slack delivers events over a WebSocket, so you don't need a public URL) and the required scopes. Then grab two tokens:

   * **OAuth & Permissions** → copy the Bot User OAuth Token (`xoxb-...`)
   * **Basic Information → App-Level Tokens** → generate one with scope `connections:write` (`xapp-...`)

   In a channel you want the bot in, run `/invite @databot`.
3. Run [`data_analyst_agent.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb), which saves `ANALYST_ENV_ID`, `ANALYST_AGENT_ID`, and `ANALYST_AGENT_VERSION` to `.env`.

The setup cell below prompts for your Slack tokens and saves them to `.env` so you don't re-enter them on restart (or add them to `.env` beforehand to skip the prompt). `.env` is already in `.gitignore` – never commit it to version control. If you don't have a Slack workspace handy you can still read through the code – each section explains what it does – but you'll need one to run the bot.



%%capture

%pip install -q "anthropic>=0.91.0" python-dotenv slack\_bolt requests markdown-to-mrkdwn



import io

import os

import threading

from getpass import getpass

import requests

from anthropic import Anthropic

from dotenv import load\_dotenv, set\_key

from markdown\_to\_mrkdwn import SlackMarkdownConverter

from slack\_bolt import App

from slack\_bolt.adapter.socket\_mode import SocketModeHandler

load\_dotenv(override=True)

# Prompt for Slack tokens on first run and save them to .env.

for key in ("SLACK\_BOT\_TOKEN", "SLACK\_APP\_TOKEN"):

if not os.environ.get(key):

os.environ[key] = getpass(f"{key}: ")

set\_key(".env", key, os.environ[key])

client = Anthropic()

app = App(token=os.environ["SLACK\_BOT\_TOKEN"])

for key in ("ANALYST\_ENV\_ID", "ANALYST\_AGENT\_ID", "ANALYST\_AGENT\_VERSION"):

if not os.environ.get(key):

raise RuntimeError(f"{key} not set. Run data\_analyst\_agent.ipynb first.")

# Set these from the IDs saved by the data analyst notebook. Reusing

# the agent and environment avoids re-provisioning on every bot restart.

ANALYST\_AGENT = {

"id": os.environ["ANALYST\_AGENT\_ID"],

"version": int(os.environ["ANALYST\_AGENT\_VERSION"]),

}

ANALYST\_ENV\_ID = os.environ["ANALYST\_ENV\_ID"]

# thread\_ts -> session\_id, so follow-ups land in the same session.

# Sessions stay open for replies. In production, persist this and

# archive sessions when threads go stale.

thread\_sessions: dict[str, str] = {}

mrkdwn = SlackMarkdownConverter()

##  1. Start a session when the bot is mentioned

Bolt passes an `ack` callback into every handler; calling it tells Slack the event was received. Slack retries anything not acknowledged [within three seconds(opens in new tab)](https://docs.slack.dev/apis/events-api/#responding), so `on_mention` calls `ack()` immediately and hands the slow work (file upload, session creation, streaming) to `start_analysis` on a background thread.

Each mention creates a session you can open in the [Console(opens in new tab)](https://platform.claude.com/) under **Sessions** to watch the full trace.



@app.event("app\_mention")

def on\_mention(event, say, ack):

ack()

channel = event["channel"]

thread\_ts = event.get("thread\_ts") or event["ts"]

# Mention text arrives as "<@BOTID> question"; drop the mention prefix.

question = event["text"].split(">", 1)[-1].strip()

slack\_file = (event.get("files") or [None])[0]

say(text="On it. Analyzing now.", thread\_ts=thread\_ts)

# Run the slow work in a background thread so this handler

# returns within Slack's 3s limit.

threading.Thread(target=start\_analysis, args=(channel, thread\_ts, question, slack\_file)).start()

def start\_analysis(channel: str, thread\_ts: str, question: str, slack\_file: dict | None) -> None:

try:

# If the mention had a file attached, pull it from Slack and

# re-upload to the Anthropic Files API so the session can mount it.

resources = []

if slack\_file:

resp = requests.get(

slack\_file["url\_private"],

headers={"Authorization": f"Bearer {app.client.token}"},

timeout=30,

)

resp.raise\_for\_status()

mime = slack\_file.get("mimetype", "text/csv")

uploaded = client.beta.files.upload(

file=(slack\_file["name"], io.BytesIO(resp.content), mime)

)

mount = "/mnt/session/uploads/data.csv"

resources.append({"type": "file", "file\_id": uploaded.id, "mount\_path": mount})

question += f"\n\nThe data is mounted at {mount}."

# One session per Slack thread. Store the thread coordinates in

# metadata so anyone reading the event stream knows where to reply.

session = client.beta.sessions.create(

environment\_id=ANALYST\_ENV\_ID,

agent={"type": "agent", \*\*ANALYST\_AGENT},

resources=resources,

# Titles are capped at 80 chars and can't contain Unicode

# control/format characters (Slack sometimes inserts them).

title="".join(c for c in question if c.isprintable())[:80],

metadata={"slack\_channel": channel, "slack\_thread\_ts": thread\_ts},

)

thread\_sessions[thread\_ts] = session.id

# Send the question as a user.message event. The agent starts

# working immediately; relay\_stream posts its progress to the thread.

client.beta.sessions.events.send(

session.id,

events=[{"type": "user.message", "content": [{"type": "text", "text": question}]}],

)

relay\_stream(session.id, channel, thread\_ts)

except Exception as e:

app.client.chat\_postMessage(

channel=channel, thread\_ts=thread\_ts, text=f"Analysis failed: {type(e).\_\_name\_\_}: {e}"

)

##  2. Relay progress and results to the thread

The `relay_stream` function defined below is the bridge between the two APIs: it reads from the Anthropic session event stream and posts to Slack. It loops until the agent goes idle, then posts the final summary and uploads any files the agent wrote.

`files.list(scope_id=...)` returns every file in the session – both the CSV we uploaded and anything the agent wrote. We filter to `downloadable == True` so only agent-generated outputs (the report, charts) get posted back to Slack, not the user's own input.



def relay\_stream(session\_id: str, channel: str, thread\_ts: str) -> None:

summary = ""

posted\_progress = False

for ev in client.beta.sessions.events.stream(session\_id):

t = ev.type

if t == "agent.message":

# Keep the latest text block; it becomes the final summary.

for b in ev.content:

if b.type == "text" and b.text.strip():

summary = b.text

elif t == "agent.tool\_use" and not posted\_progress:

# Post a one-time progress update when the agent starts

# running commands.

app.client.chat\_postMessage(

channel=channel, thread\_ts=thread\_ts, text="Running analysis..."

)

posted\_progress = True

elif t == "session.status\_idle":

break

elif t == "session.status\_terminated":

trace = f"https://platform.claude.com/sessions/{session\_id}"

app.client.chat\_postMessage(

channel=channel,

thread\_ts=thread\_ts,

text=f"Session terminated unexpectedly. Trace: {trace}",

)

return

# Turn is done. Post the summary, then upload any generated files.

if summary:

text = mrkdwn.convert(summary)

if len(text) > 3900: # Slack text limit ~4000 chars

text = text[:3900] + "\n\_(truncated)\_"

app.client.chat\_postMessage(channel=channel, thread\_ts=thread\_ts, text=text)

outputs = client.beta.files.list(scope\_id=session\_id, betas=["managed-agents-2026-04-01"])

for f in outputs.data:

if not f.downloadable:

continue

content = client.beta.files.download(f.id).read()

app.client.files\_upload\_v2(

channel=channel, thread\_ts=thread\_ts, filename=f.filename, content=content

)

##  3. Handle follow-ups in the same session

A reply in the thread becomes another turn in the existing session – you don't need to `@mention` the bot again. The container filesystem and conversation history persist across turns.



def continue\_session(session\_id: str, channel: str, thread\_ts: str, text: str) -> None:

try:

client.beta.sessions.events.send(

session\_id,

events=[{"type": "user.message", "content": [{"type": "text", "text": text}]}],

)

relay\_stream(session\_id, channel, thread\_ts)

except Exception as e:

app.client.chat\_postMessage(

channel=channel, thread\_ts=thread\_ts, text=f"Analysis failed: {type(e).\_\_name\_\_}: {e}"

)

@app.event("message")

def on\_thread\_reply(event, ack):

ack()

thread\_ts = event.get("thread\_ts")

# Only handle human replies in a thread where we already started

# a session. Skip edits/deletes and other message subtypes.

if event.get("subtype"):

return

if not thread\_ts or event.get("bot\_id") or thread\_ts not in thread\_sessions:

return

threading.Thread(

target=continue\_session,

args=(thread\_sessions[thread\_ts], event["channel"], thread\_ts, event["text"]),

).start()

##  4. Run the bot

The cell below connects to Slack and starts listening. It blocks while the bot runs – stop it with the ■ interrupt button when you're done.

In any channel the bot is in, mention it with a CSV attached. It posts progress, then the summary and `report.html` in the thread:

![Slack thread showing the bot's analysis](https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/managed_agents/example_data/slack_data_bot/slack_thread.png)

Reply in-thread to go deeper on the same data.



SocketModeHandler(app, os.environ["SLACK\_APP\_TOKEN"]).start()

##  Next steps

You've wrapped the analyst agent in a Slack bot: mentions start a session, the event stream relays progress to the thread, outputs get uploaded, and replies continue the same conversation.

* Swap the agent's system prompt in [`data_analyst_agent.ipynb`(opens in new tab)](https://github.com/anthropics/claude-cookbooks/blob/main/managed_agents/data_analyst_agent.ipynb) to change its analysis style. Re-running that notebook creates a new agent and saves its ID to `.env` for the bot to pick up.
* Persist `thread_sessions` to a database so conversations survive bot restarts.
* Move the bot out of this notebook: copy the code to a `.py` file and deploy it anywhere that can hold a long-lived WebSocket connection.
