<!-- https://anthropic.skilljar.com/claude-platform-101/486252 -->
<!-- youtube: UAeTSBsK71A -->

# Choosing the right model

You're shipping an app with Claude.
Which model do you pick, though? If you
just default to the smartest one, your
API bill will surprise you. Pick the
cheapest and the output might not hold
up. Each model has different trade-offs.
Picking the right one affects both
quality and cost.
Currently, Anthropic offers three model
tiers. Claude Opus, which is the most
intelligent but slowest, as well as the
highest cost. Use it for deep reasoning,
complex analysis, multi-step coding, and
nuanced writing. Clot haiku is the
fastest and cheapest but less
intelligent. Use it for high volume, low
complexity work like classification,
extraction, and routing. And then in
between we have clots, which is the fast
and capable enough for most production
work. The middle tier on cost.
But before you even write production
code, let's just set up a simple
evaluation. That's a set of example
inputs that you run through each model
and score against what good output means
for your use case. 20 or 30
representative examples from your actual
workload is enough to start. So let's
run them through Haiku first.
If the quality holds, well, you're done.
You just saved a lot of money. And if it
doesn't, well, it might be time to step
up to sonnet. Only reach for opus when
the task needs it.
But let's see the difference between the
tiers, not just talk about it. So, I'm
going to send the same prompt through
all three and watch the latency and
token counts. So, two things are going
on here. The loop swaps the model field
on each request. Same prompt, same max
tokens, only the model changes, and
response. Gives you the input and output
tokens straight back from the API, which
is what your bill is calculated on. So,
let's run it. You'll see three models
and three sets of numbers. Opus comes
back first and takes the longest and
reads the most polished, but for a two
sentence definition, that polish is
wasted. Sonic comes after and the
writing is tightened up a little bit.
And then Haiku comes last, often in
under a second with a very competent two
sentence answer. It's honestly perfect
for this type of scenario. And that's
the whole point. The right model is the
cheapest one whose output you'd actually
ship. For a definition, haiku is plenty.
for drafting a regulatory response,
you'd be running the same comparison and
probably ending up on Opus. The Aval is
the same shape every single time. And so
in a real app, you'd route different
kinds of work to different models inside
the same endpoint. So in this operations
dashboard, a document processing route
classifies every incoming file with
Haiku, but then drafts client updates
with Sonnet and only reaches for Opus on
RFP responses. One Q, three models
picked per task.
When it comes to choosing the right
model for the job, choose Opus for hard
problems, Sonnet for daily work, and
Haiku for volume. Run an evaluation from
Haiku upward, and you'll land on the
cheapest model that still does the job.
