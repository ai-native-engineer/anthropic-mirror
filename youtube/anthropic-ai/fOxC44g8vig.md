---
title: "Claude Agent Skills Explained"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=fOxC44g8vig
youtube_id: fOxC44g8vig
published: 2025-11-26
duration: "3:14"
---

# Claude Agent Skills Explained

[![Claude Agent Skills Explained](https://img.youtube.com/vi/fOxC44g8vig/hqdefault.jpg)](https://www.youtube.com/watch?v=fOxC44g8vig)

<details>
<summary>자막: Claude Agent Skills Explained (3:14)</summary>

[00:00]
Hi, my name is Otto and in this video
we're going to discuss agent skills.
Agents today are pretty intelligent, but
they don't always have the domain
expertise you need for real work and
skills help solve this. You can think of
skills as organized folders that package
expertise that Cloud can automatically
invoke when relevant to the task at
hand. And most importantly, these skills
are portable across cloud code, the API
as well as cla.ai. And the way skills
work is at startup only the name and
description of every installed skill is
loaded in the system prompt. This is
going to consume about 30 to 50 tokens
per skill and make Claude aware of the
skill's existence. Then when a user
prompt matches a skills description,
Claude is going to dynamically load the
full skill.md file into context. And
finally, if the skill references other
files or scripts, they are also
progressively loaded and run as needed.
This progressive disclosure allows you
to install many different skills to
perform complex tasks without bloating

[00:01]
your context window. But let's see how
skills fit in with the other Claude
features. While skills teach Claude how
to do specialized tasks, Claude.md files
tell Claude about the specific project.
Things like your text stack, coding
conventions, and repo structure. CloudMD
files live alongside your code in the
repository. A CloudMD file may say
things like we [music] use Nex.js JS and
Tailwind. But skills on the other hand
are portable expertise that work across
any project. So a front-end design skill
can teach Claude your typography
standards, animation patterns, and
layout conventions and [music] activate
automatically when building UI
components. MCP servers on the other
hand provide universal integration, a
single protocol that connects Claude to
external context sources like GitHub,
linear, Postgress, and many many others.
MCP connects to data. Skills teach
Claude what to do with it. So an MCP
server may give Claude access to your
database, but a database query skill can

[00:02]
teach Claude your team's query
optimization patterns. Finally, sub
agents are specialized AI assistants
with fixed roles. Each sub agent has its
own context window, custom prompt, and
specific tool permissions. skills
provide portable expertise that any
agent can use. So your front-end
developer sub agent can use a component
pattern skill. Your UI reviewer sub
agent on the other hand can use a design
system skill, but both can load and use
the same accessibility standard skill.
And the best part is these capabilities
are designed to work together. Your
cloudMD file sets the foundation. MCP
[music] servers connect the data. Sub
agents specialize in their roles and
skills bring the expertise making every
piece smarter and more capable. At the
end of the day, skills let you package
workflows into reusable capabilities
like helping onboard new hires to your
team's coding standards, ensuring every
PR follows a specific security best
practices or sharing your data analysis

[00:03]
methodology across your team. And that's
how skills can help you achieve more
with Claude. We encourage you to give
them a try and see how they can improve
your workflows.

</details>
