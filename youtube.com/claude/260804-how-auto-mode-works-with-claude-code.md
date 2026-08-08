---
title: "How auto mode works with Claude Code"
channel: claude
url: https://www.youtube.com/watch?v=b8SV4U6fEIc
youtube_id: b8SV4U6fEIc
published: 2026-08-04
duration: "5:42"
captions: en
---

# How auto mode works with Claude Code

[![How auto mode works with Claude Code](https://img.youtube.com/vi/b8SV4U6fEIc/hqdefault.jpg)](https://www.youtube.com/watch?v=b8SV4U6fEIc)

<details>
<summary>자막: How auto mode works with Claude Code (5:42)</summary>

[00:00]
In our research, 97% of permission
prompts in Claude Code get approved.
These permission prompts appear
whenever Claude proposes an action,
like running a command, fetching
from the web, or editing a file.
Approving or denying each
one gives you control,
but it can lead to approval fatigue,
especially on multi-step tasks.
So a few months ago,
we introduced Auto Mode.
Auto Mode checks for potentially harmful
actions while letting Claude complete
long-running work with fewer interruptions.
But if you're no longer approving each
action, what determines if it's safe to run?
Let's look at how Auto Mode works and how
you can configure it
for your environment and team.
It would be easy to assume Claude
is now approving its own actions,
but that would make Claude its own reviewer,
introducing bias through shared code.

[00:01]
That's like writing, reviewing,
and merging your own pull request.
Instead, when Claude proposes an action,
it runs through a classifier,
a separate check that screens
the action and approves or denies it.
The classifier sees your messages
in Claude's tool calls.
It doesn't see Claude's reasoning,
responses to you, or tool output.
So it isn't influenced by them. It
compares each action against your intent.
And approves the ones that match.
What it specifically checks for is Claude
reaching beyond what you intended, towards
something irreversible or destructive.
Like deleting remote branches when
you only asked it to tidy up locally.
If the classifier denies an action,
Claude usually tries to find
a safer way to proceed on its own.
For example, if a force
push to main gets denied,
Claude might try to push
to a new branch instead.
If it keeps getting denied, auto-mode
pauses and you approve the action yourself.

[00:02]
Any webpages or files Claude reads
could carry hidden instructions that try
to steer it away
from your original intent.
So before that content
enters Claude's context,
a server-side probe
scans every tool result
for malicious instructions and floods
anything suspicious with a warning
to treat the content skeptically.
Then, the classifier
checks whether Claude's
next action still lines up
with what you asked for.
So an attack has to clear both layers.
We tested this by running prompt
injection attacks against Claude Code.
With probes and auto-mode enabled,
the attack success rate
in our evaluations dropped to zero.
But not every action needs
to go through the classifier.
Your deny, ask, and allow rules run first.
Then, a tier check decides which actions
the classifier needs to see.
Most of what Claude does
is read-only or recoverable,

[00:03]
like searching your codebase
or editing files in your project.
These actions skip the classifier.
On the other hand, riskier operations
like shell commands, web fetches,
or anything that reaches
outside of your environment
are sent through the classifier.
By default, the classifier only counts
your working directory
in git remotes as internal.
That means everything
else appears external,
including your own
company's infrastructure.
So to get the most out of auto-mode,
it's worth configuring it.
Start by defining your environment.
Admins can set this in managed settings,
which every developer
in your organization inherits.
Developers can add their own
entries in user settings.
But they can't remove
what admins already set.
Use the environment field to describe
your infrastructure in plain English,
such as your GitHub org, cloud
buckets, and internal services.

[00:04]
Setting environment replaces
Claude's built-in entries,
so add the default string to keep them.
If you need more fine-grained control,
use allow for exceptions,
soft deny for actions that should be
blocked unless you explicitly ask,
and hard deny for actions that should
be blocked no matter what you ask.
These fields are guidance the classifier
factors into each check, not hard rules.
For hard limits, add deny rules
to block matching tool calls,
and ask rules to force
a prompt even in auto-mode.
Allow rules also work too.
But anything broad enough to grant
arbitrary code execution
is also sent to the classifier.
All right, that's auto-mode.
We started with a question.
If you're no longer approving each action,
how are they reviewed and now you know?
A classifier that reads
your messages but not Claude's,

[00:05]
a deal check that reserves it for actions
that are hard to undo,
a probe that scans it
for hidden instructions,
and a trust boundary that you configure.
Together, they catch what
manual human reviews might miss.
When you are rolling it out, start narrow.
Watch what gets denied
and then widen it from there.
For high-stake operations like changes
to your production infrastructure,
you should review
Claude's actions yourself.
Or build your own evals
to gain more confidence.
To learn more about our safety research,
read our blog post linked below.

</details>
