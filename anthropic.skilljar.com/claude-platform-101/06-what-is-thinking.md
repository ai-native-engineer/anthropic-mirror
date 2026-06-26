<!-- https://anthropic.skilljar.com/claude-platform-101/486256 -->
<!-- youtube: 4SunBsMGRwA -->

# What is thinking?

Some tasks need more than a quick
answer, and Claude can work through the
problem before responding. And this is
called extended thinking.
Extended thinking lets Claude reason
step-by-step before producing a final
response. When enabled, Claude generates
internal reasoning tokens, often called
a chain of thought, and then delivers
the answer.
You can see the reasoning in the
response alongside the final text. So,
with Opus 4.7, thinking is adaptive. You
don't pick a token budget. You turn it
on, and Claude decides dynamically when
to think and for how much. Now, to
control how much Claude thinks, use the
effort parameter. But, it goes inside
output config, not next to the thinking
block. The levels are low, medium, high,
extra high, or max. The default is set
to high.
Extended thinking helps with math,
multi-step logic, code debugging,
regulatory analysis, anything that
involves tradeoffs or comparing options.
Skip it for simple classification,
extraction, or boilerplate. It just adds
latency and cost without actually
improving those results.
So, let's see thinking in action. I have
this agent loop with one weather tool,
and I'm going to ask Claude to plan a
road trip out of San Francisco.
Two stops, weighing weather and drive
time. That's a real tradeoff, the kind
of question where thinking earns its
keep. So, let's run it.
The output is more interesting than
usual. You'll see some thinking blocks
where Claude works through the
tradeoffs, followed by tool calls to
check each city, and finally a text
block with the actual recommendation.
The reasoning is visible. That's the
whole point. So, in a production app,
this is the difference between an agent
that finds problems one at a time and an
agent that connects them. So, in this
compliance review app, toggling adaptive
thinking on the auto review call lets
the agent reason across report sections,
catching things like a wind load spec in
section three that conflicts with the
material spec.
>> [music]
>> Extended thinking gives Claude room to
reason before it even answers. With Opus
4.7, turn on with thinking type adaptive
and dial the depth with output config
with your effort level.
Use it for hard trade-off heavy problems
and skip it for simple ones. It just
costs latency and tokens.
