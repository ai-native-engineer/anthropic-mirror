<!-- https://anthropic.skilljar.com/claude-platform-101/486264 -->
<!-- youtube: 1Rl3gZrlQJo -->

# Building your first managed agent

We know what it's like to build an agent
loop by hand.
While loops, stop reason switches, tool
executions, and all that works. And for
a lot of features, it's actually the
right shape. But sometimes that loop is
going to run for a very long time.
Minutes, maybe even hours across many
tools with state to keep, files to
write, work to resume after a network
hiccup. At that point, you don't want to
run the loop on your server. You want to
delegate it. And that's what managed
agents are.
A managed agent is an agent loop that
runs on Anthropic's infrastructure
instead of yours. You describe the agent
once.
You give it an environment to work in.
And you start a session.
Anthropic runs the loop. And you just
stream the events back out as it works.
So, here's the four primitives in order.
First, we have the agent, which is the
persona, model, system prompt, and tool
set. This is reusable across many runs.
Then you have an environment where the
agent runs. Cloud, local, networking
config, etc.
Then you have a session, which is a
single run of an agent inside of a
certain environment. And then you have
events, which is the messages flowing
in, aka your prompts, and out, the
agent's actions, the tool calls, the
results, the replies. So, here you're
not running a while loop. You're sending
events and reading events.
I want the smallest possible managed
agent that does something. So, let's
create a file in our temp drive, count
its lines, report back.
And that uses the agent tool set.
Anthropic's bundled file {slash} bash
{slash} web tools will work fine. So, I
don't have to define any of the tools
myself.
So, first we create our agent here.
Note that we have the agent tool set
defined right here. That's the bundle
tool set. Then we create our
environment. This spins up the container
template. Cloud networking unrestricted.
This is the sandbox where the file
actually gets written to. Then we create
a session with our agent and environment
as well as an optional title. And the
session is the unit of work. And then we
open the event stream. Notice how we do
this first. The stream only delivers
events that occur after it opens. So,
always open it before sending the
kickoff. And that's when we send the
user message into the live stream.
Notice it's events, it's plural.
Events are how everything flows in this
API.
And then we consume the stream. Here are
three event types that matter for this
demo. First, we have the agent.message,
which is Claude's text.
Then we have agent.tool_use, which is
what tool Claude picked.
And then we have session.status_idle,
and this is when the agent is done.
So, let's run it. As you can see, the
output is the agent reasoning out loud.
There's actual text here and the tools
that it picks, as well as a final
answer. And this is all running inside
of Anthropic's container. Managed agents
is enabled by default for every API
account. No special access needed. And
this is the trade. Usually with agents,
we have our own loop where we have to
control everything. But with managed
agents, you just delegate that loop, the
sandbox, the resumability, and just
consume the event stream as it comes in.
So, in a production app, this is the
shape for long-running file-touching, go
organize this for me tasks. So, in this
file share clean up, a managed agent
reads a target directory structure spec,
walks the messy income folder,
moves files into the right project
folders,
archives duplicates and zero-byte
garbage, and then it flags anything it
can't confidently place. All in a
session that can run for minutes against
thousands of files.
Managed agents are the agent [music]
loop run for you. Create an agent,
create an environment, create a session,
send events in, and stream events out.
Reach for them when the loop would
[music] run too long, do too much, or
need to survive a hiccup, and then reach
for a manual loop when you want full
control.
