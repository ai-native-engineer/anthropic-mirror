<!-- https://anthropic.skilljar.com/claude-platform-101/486258 -->
<!-- youtube: pm8iwdSIs3M -->

# Built-in tools

You can build your own custom tools, but
some capabilities are common enough that
Anthropic ships them pre-built.
You don't write the code, you don't host
the sandbox, you just declare the tool
and Anthropic runs it.
Anthropic provides server tools that run
on their infrastructure. You don't
execute these, Anthropic does, which
means you don't need an agent loop for
these calls. Claude calls the tools on
their own. The result comes back inside
the same response. So, the main ones is
a web search, which searches the
internet, returns results with
citations, code execution, which writes
and runs Python in a sandbox, and web
fetch, which retrieves full content from
URLs.
So, let's check out some of the big ones
in one file. Two message.create calls,
one with the web search,
and one with code execution.
Now, two things to notice. First,
there's no agent loop here. We don't
switch on stop reason. We don't push
tool results back. Anthropic runs the
tool server-side, and the response
already contains the result. Second, the
response now has new block types, server
tool use for the tool call, code
execution tool result for the output,
plus the regular text blocks. So, let's
run it.
For web search, you'll see that Claude's
tool call printed, then a one-sentence
answer about the latest model release
with the search citations folded in.
For code execution, you'll see the
actual Python Claude wrote, the stdout
from the sandbox running it, and a final
text answer. We didn't have to start up
a search crawler. We didn't run a Python
sandbox. We declared two tools and got
both for free.
Worth knowing the other category exists.
Client tools run where your code runs.
They're shipped in the Claude SDK, so
you don't have to define the schema
yourself. Two of these examples are
memory, which Claude reads and writes
memory across sessions, and bash, a
persistent bash shell so Claude can
execute commands. Same shape as a custom
tool, but the SDK gives you the schema
and a sensible runner.
So, in a production app, this is the
shortest path to features that would
otherwise take weeks. Web search powers
a fact check endpoint that verifies
every numeric and regulatory claim in a
draft against the live web. But, a
reminder, just because it's validated on
the internet, doesn't mean that it's
true. So, always double-check Claude's
work.
Server tools, web search, code
execution, web fetch are declared in
your tools array. Anthropic runs them.
You get the result in the same response
with no loop required. And that hosted
by Anthropic idea scales all the way up
with managed agents, which apply it to
the entire agent, not just one tool.
