<!-- https://anthropic.skilljar.com/claude-platform-101/486254 -->
<!-- youtube: tBIdyIoCQVU -->

# The agent loop explained

You've made API calls, but a single call
only returns [music] one response.
If you want to replace workflows, well,
Claude needs to act, look at the result,
decide what's next, and keep going. And
this is what's commonly known as agentic
workflows.
An agent is an autonomous version of
Claude running both sides of the
messaging loop without human
involvement. Agents receive a task, pick
a tool, and execute code in a loop until
Claude deems the task done.
Here's the easiest way to implement an
agent loop.
First, send a message to Claude with
tools available.
Then, Claude responds with either a
final answer
or uses a tool that you define.
Then, your code executes that tool.
And then that result is sent back to
Claude.
And this repeats until stop reason is
end turn.
I want to see this loop run end to end
without dragging in a database or UI.
So, I'll wire up a fake Get weather, and
ask Claude what to wear in Austin today.
Claude has no way to know the weather on
its own, so it'll have to call the tool,
read the result, and then give you an
answer. So, here's the whole script.
First, the tools array tells Claude
what's available. Name,
description,
and a JSON schema for the inputs.
Run tool is just a hard-coded lookup. In
a real app, this would hit your
database, an API, whatever.
And then our loop here is the agent
loop.
Each iteration sends messages to Claude
and switches on the response stop
reason. And so, if the response is end
turn, then Claude is done. Print the
final text and just break. But, on tool
use, find the tool use block in the
response, run each one, and push the
assistant's response and our tool
results back into messages and loop
again, so Claude can answer.
So, let's run it.
You'll see two turns. Turn one is the
stop reason, which is tool use.
Claude requests get weather, which is
Austin in this case.
Our code returns the temp and the
conditions.
And then turn two, the stop reason is
end turn. And so Claude tells you to
wear something light and breathable. Two
API calls, one tool execution, and one
final answer. And that's the entire
loop. Everything that you make with the
Claude API is going to be similar to
this. And so in a real environment, this
same loop powers something like auto
review endpoint, a compliance agent that
reads a structural report, looks up the
relevant building codes via tool, and
writes risk finding back to the database
one by one as it works. The shape of the
loop is identical to what you just ran.
The differences are real tools instead
of a mock weather lookup, results stream
back to the UI as server-sent events,
and findings persisted to a risk finding
table.
An agent is Claude in a loop. Observe,
decide, act, repeat. You own the loop
and the tools. Claude owns the
reasoning. And when you don't want to
own the loop, managed agents run this
exact loop for you on Anthropic's
infrastructure.
