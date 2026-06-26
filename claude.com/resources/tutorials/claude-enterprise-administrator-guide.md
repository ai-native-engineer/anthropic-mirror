<!-- source: https://claude.com/resources/tutorials/claude-enterprise-administrator-guide -->

# Claude Enterprise Administrator Guide

Walk through the four phases of a successful Claude Enterprise deployment: Technical Setup, Change Management & Launch, Enablement & Training, and Scaling Adoption. Includes Claude Code seat configuration and a complete resource directory.

  Professional
* Product

  Claude.ai
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/claude-enterprise-administrator-guide

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

*Deployment, Configuration, and Adoption Playbook*

This guide walks you through the four phases of a successful Claude Enterprise deployment: Technical Setup, Change Management & Launch, Enablement & Training, and Scaling Adoption. It also covers Claude.ai and Claude Code access controls, configuration options, and seat management.

**Phase 1: Technical Setup**

* Authentication & Access
* User Provisioning Options
* Security & Compliance
* Claude Code Access & Seat Configuration

**Phase 2: Change Management & Launch**

* Define Success Metrics
* Identify & Enable Champions
* Launch Communications

**Phase 3: Enablement & Training**

* Self-Service Learning Resources
* Feature-Specific Guides
* Claude Code Training Resources
* Internal Support Channels

**Phase 4: Scaling Adoption**

* Expanding Across Teams
* Measuring Impact
* Feature Rollout & Governance
* Sustaining Momentum

**Appendix:** Resource Directory

## Phase 1: Technical Setup

**Complete these technical configuration steps before launching Claude to your organization.**

### Authentication & Access

**Follow these steps to configure SSO:**

Claude Enterprise supports SAML 2.0 and OIDC (OpenID Connect) for single sign-on (SSO). See [Setting Up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso) for detailed configuration steps.

1. **Test SSO:** Configure with a small pilot group before broad rollout.
2. **Enable domain capture:** Automatically route users from your domain to your workspace. See [Domain Capture Setup](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning).
3. **Enforce SSO:** Require SSO for all access once configuration is validated.

### User Provisioning Options

Choose your provisioning method based on your organization's needs. See [User Provisioning Overview](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning) for setup instructions.

1. **SCIM (recommended):** System for Cross-domain Identity Management enables automatic sync from your identity provider (IdP). See [SCIM Setup Guide](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning).
2. **Just-in-Time (JIT):** Users are created upon first SSO login. Simple to set up but offers less control over access.
3. **Manual:** Admin-managed invitations via the [Admin Console](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans). Best for small, controlled pilots.

> **Example: Phased Rollout with SCIM**
>
> Many organizations use SCIM for a phased rollout approach:
>
> 1. Start with a pilot group of 50-100 users synced via SCIM
> 2. Monitor adoption and gather feedback for 2–4 weeks
> 3. Gradually expand SCIM groups to include additional departments
> 4. Enable organization-wide access once processes are established

### Security & Compliance

Claude Enterprise includes robust security and compliance features designed for enterprise environments:

Review security details at the [Anthropic Trust Center](https://trust.anthropic.com) and in the [Enterprise Plan Overview](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan).

1. **Data retention:** Conversations are retained per your policy and exportable via the [Compliance API](https://trust.anthropic.com/) and [Audit Logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs), which also provide full activity logging for security monitoring.
2. **No model training:** Your organization's data is not used to train Claude models by default.
3. **Role-based access:** Primary Owner, Owner, and Member roles provide granular permissions. See [Member Roles Guide](https://support.claude.com/en/articles/9267276-roles-and-permissions).

### Pre-Launch Checklist

* Important considerations before setting up Identity Management — [Important Considerations](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
* SSO configured and tested — [Setting Up SSO](https://support.claude.com/en/articles/13132885-setting-up-single-sign-on-sso)
* User provisioning configured — [Provisioning Guide](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)
* Security review completed with IT and information security teams
* Data retention policies documented
* Compliance API and Audit log access configured — [Trust Center](https://trust.anthropic.com/) and [Audit Logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs)
* Set up Connectors — [Information on Connectors](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp)
* Admin roles assigned — [Member Roles](https://support.claude.com/en/articles/9267276-roles-and-permissions)
* Claude Code seat configuration completed (see next section)

### Claude Code Access & Seat Configuration

#### Understanding Claude Enterprise Seat Types for Claude Code

Claude Enterprise offers different seat types depending on your pricing model. The following table summarizes the options and their Claude Code access implications:

| Pricing Model | Seat Type | Claude Code Access |
| --- | --- | --- |
| Seat-Based (Legacy) | Standard | No |
| Seat-Based (Legacy) | Premium | Yes |
| Usage-Based | Chat | No |
| Usage-Based | Chat + Code | Yes |
| Usage-Based | Claude Enterprise | Yes |

#### Admin Steps to Enable Claude Code

Follow these steps to enable Claude Code access for your users:

1. **Navigate to Settings > Organization > Members** in your Claude Enterprise admin console.
2. **For legacy seat-based plans:** Purchase Premium seats and assign them to users who need Claude Code access. Only Primary Owners/Owners can manage seat assignments.
3. **For usage-based plans:** Assign seats to users who need Claude Code. Configure spend limits as needed (defaults to $0). [See information here on setting spend limits.](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan#h_f7838fc97d)

#### User Authentication for Claude Code

Share the following steps with end users to connect Claude Code to their enterprise account:

* **Install Claude Code:** Run the command below that corresponds to your operating system to install Claude Code.
  + **macOS / Linux / WSL:** `curl -fsSL https://claude.ai/install.sh | bash`
  + **Windows (PowerShell):** `irm https://claude.ai/install.ps1 | iex`
* **Start Claude Code:** Type "claude" in your terminal.
* **Select login method:** Choose "Claude account with subscription".
* **Authenticate via Enterprise SSO** with your corporate credentials.
* **Your seat subscription will be linked to Claude Code** automatically upon successful authentication.

> **Troubleshooting**
>
> * If already logged in via a different account, run `/logout` first, then `/login`
> * Run "claude update" if not seeing the enterprise auth option
>   + Restart terminal after updates
>   + Console API key users switching to access via Claude Enterprise seats: Run `/logout`, then `/login` and select "Claude account with subscription"

#### Admin Monitoring for Claude Code

Monitor and manage Claude Code usage across your organization:

* Navigate to Analytics > Claude Code to view usage analytics
* Monitor usage across all surfaces (Claude.ai + Claude Code)

> **Important**
>
> Claude Code access requires a Premium seat (legacy model), or a Chat + Code or Claude Enterprise seat (usage-based model). Standard and Chat-only seats do NOT include Claude Code access.
>
> For organizations migrating from Console/API-based Claude Code access, users must re-authenticate via Enterprise SSO to link their subscription.

## Phase 2: Change Management & Launch

A successful Claude deployment requires thoughtful change management to drive adoption and demonstrate value.

### Define Success Metrics

Establish clear metrics to measure the success of your Claude deployment:

| Metric Category | Metric | Target | Measurement Method |
| --- | --- | --- | --- |
| Activity | Weekly Active Users | 70% of licensed seats | Admin Dashboard |
| Activity | Messages per User per Week | 25+ messages | Usage Analytics |
| Activity | Feature Adoption (Projects, Artifacts) | 40% of active users | Feature Analytics |
| Impact | Time Saved per User per Week | 3+ hours | User Survey |
| Impact | User Satisfaction Score | 4.0+ / 5.0 | Quarterly Survey |
| Impact | Tasks Augmented by Claude | 5+ per week | User Self-Report |

### Identify & Enable Champions

Champions are enthusiastic early adopters who can help drive adoption across their teams:

* Select 2–3 champions per department or team
* Provide champions with early access and advanced training
* Equip champions with talking points and demo guidance
* Create a champions Slack channel or Teams group for peer support
* Recognize and reward champion contributions to adoption

### Launch Communications

Plan a multi-channel communication strategy for your launch:

* **Pre-Launch (2 weeks before):** Communications highlighting benefits and use cases
* **Launch Day:** Executive announcement, getting started guide, training schedule
* **Post-Launch (Week 1):** Tips and tricks, success stories from pilot users
* **Ongoing:** Weekly tips, monthly newsletters, quarterly business reviews

## Phase 3: Enablement & Training

Provide comprehensive training resources to help users get the most from Claude.

### Structured Training Programs

Deploying Claude is a technical milestone, but adoption depends on whether people know how to use it effectively. A structured training program ensures users move past initial curiosity into productive, habitual use — and reduces the support burden on your IT and champion teams.

* **All-Staff 101 Sessions:** Workshops (30–60 min) covering the basics — navigating the interface, writing effective prompts, and using core features like Projects and Artifacts. Run at launch and repeat for new hire cohorts.
* **Department-Level Enablement:** Targeted sessions built around each team's actual workflows, with an executive sponsor to signal leadership support. Partner with team leads to identify high-value use cases and provide ready-to-use prompt templates. Schedule a follow-up 2–4 weeks later to address questions from real usage.
* **Office Hours:** Weekly or biweekly drop-in sessions where users bring real work and get hands-on help from champions. Especially valuable in the first 30–60 days.
* **LMS Integration:** If your organization uses an LMS, package Claude training into trackable courses to monitor enablement coverage and tie completion to access or feature rollout milestones.

### Self-Service Learning Resources

Direct users to these Anthropic-provided learning resources:

* [Anthropic Academy](https://anthropic.skilljar.com) — Interactive courses covering Claude fundamentals, prompt engineering, and advanced features
* [Use Case Library](https://claude.com/resources/use-cases/category/professional) — Curated examples of Claude applications across different business functions
* [Help Center](https://support.claude.com) — Comprehensive documentation and FAQs on Claude Enterprise
* [Docs Site](https://docs.claude.com/) — Comprehensive support for Claude Code and API use

### Feature-Specific Guides

Ensure users understand key enterprise features:

[**Projects**](https://support.claude.com/en/articles/9517075-what-are-projects)**:** Organize conversations by topic, client, or workflow. Projects maintain context across conversations and can be shared with team members.

[**Artifacts**](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)**:** Create and iterate on documents, code, analyses, and visualizations within conversations. Artifacts can be exported and shared.

[**Skills**](https://support.claude.com/en/articles/12512176-what-are-skills)**:** Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

[**Enterprise Search**](https://support.claude.com/en/articles/12489464-using-enterprise-search)**:** Connect internal knowledge bases and documents to Claude for organization-specific answers. Supports various file formats and integrations.

### Claude Code Training Resources

Provide these resources to help users get started with Claude Code:

* [Quick Start Guide](https://code.claude.com/docs/en/overview)
* [Claude Code Walkthrough](https://anthropic.skilljar.com/claude-code-in-action)
* [Mastering Claude Code in 30 minutes](https://www.youtube.com/watch?v=6eBSHbLKuN0)

<!-- yt-inline:6eBSHbLKuN0 -->
[![Mastering Claude Code in 30 minutes](https://img.youtube.com/vi/6eBSHbLKuN0/hqdefault.jpg)](https://www.youtube.com/watch?v=6eBSHbLKuN0)

<details>
<summary>자막: Mastering Claude Code in 30 minutes (28:07)</summary>

[00:00]
[Music]
[Applause]
Hello. Hey everyone. Uh, I'm Boris. I'm
a member of technical staff here at
Anthropic and I created quad code and
here to talk to you a little bit about
some practical tips and tricks for using
quad code. Um it's going to be very
practical. I'm not going to go too much
into the history or the theory or
anything like this. Uh and yeah, before
we start actually can we get a quick
show of hands? Who has used quad code
before? Yeah. All right. That's what we
like to see. For everyone that didn't
raise your hands, uh I know you're not
supposed to do this while people are
talking, but if you can open your laptop
and type
this and this will help you install quad
code. Uh just so you can follow along

[00:01]
for the rest of the
talk. All you need is NodeJS. If if you
have it, this should work.
Yeah, if you well, you don't have to you
don't have to follow along, but if you
don't have it yet, yeah, this is your
chance to install it so you can follow
along. So, what is quad code? Quad code
is a new kind of AI assistant and
there's been different generations of AI
assistance for coding. Most of them have
been about completing, you know, like a
line at a time, completing a few lines
of code at a time. Cloud code is not for
that. It's fully agentic. So, it's meant
for building features, for writing
entire functions, entire files, fixing
entire bugs at at the same
time. And what's kind of cool about
Cloud Code is it works with all of your
tools and you don't have to change out
your workflow, you don't have to swap
everything to start using it. So,

[00:02]
whatever IDE you use, if you use VS Code
or if you use Xcode or if you use uh Jet
Brains IDEs, there's some people at
Anthropic that you can't pry Vim from
their cold dead hands, but they use quad
code because quad code works with every
single ID, every terminal out there.
It'll work locally uh over remote SSH,
over T-Max, whatever environment you're
in, you can run it.
It's general purpose and this is
something where if you haven't used
these kind of free form coding
assistants in the in the past, it can be
kind of hard to figure out how to get
started because you open it up and you
just see a prompt bar and you might
wonder like what do I what do I do with
this? What do I type in? It's a power
tool so you can use it for a lot of
things. Um, but also because it can do
so much, we don't try to guide you
towards a particular workflow because
really you should be able to use it
however you want as an engineer.
As you open up Cloud Code for the first
time, there's a few things that we
recommend doing uh to get your

[00:03]
environment set up. And these are pretty
straightforward. So run terminal setup.
This will give you shift enter for new
lines. So you don't have to do like
backslashes to enter new lines. This is,
you know, it it makes it a little bit
nicer to use. Do theme to set light mode
or dark mode or doltonize
themes. Um you can do slashinstall
github app. So today we in we announced
a GitHub app where you can at mention uh
claude on any GitHub issue or pull
request. So to install it just run this
command in in your
terminal. Um you can customize the set
of allowed tools that you can use so
you're not prompted for it every time.
This is pretty convenient. Um for stuff
that I'm prompted about a bunch, I'll
definitely customize it in this way so I
don't have to accept it every time. And
something that I actually do is for a
lot of my prompts I won't handype them
into cloud code. If you're on Mac OS,
you can go into your system settings
under accessibility is dictation and you
can enable it. And so something I do is
you just hit like that dictation key
twice and you can just speak your

[00:04]
prompt. And it helps a lot to have
specific prompts. So this is actually
pretty awesome. You can just talk to
quad code and uh like you would another
engineer and you don't have to type a
lot of
code. So when you're starting out with
quad code, it's so free form and it can
do everything. What do you start with?
The thing I recommend above everything
else is starting with codebased Q&A. So
just asking your question, asking
questions to your codebase. This is
something that we teach new hires at
Enthropic. So on the first day in
technical onboarding, you learn about
cloud code, you download it, you get it
set up, and then you immediately start
asking questions about the codebase. And
in the past when you're doing technical
onboarding, it's something that taxes
the team a lot, right? You have to ask
other engineers on the team questions.
You have to look around the code and
this takes a while. You have to figure
out how to use the tools. It t this
takes a long
time. With cloud code, you can just ask
cloud code and it'll explore the
codebase. It'll answer these kind of
questions. And so at Anthropic,
onboarding used to take about two or
three weeks for technical hires. It's

[00:05]
now about two or three
days. What's also kind of cool about Q&A
is we uh we don't do any sort of
indexing. So there's no remote database
with your code. We don't upload it
anywhere. Your code stays local. We do
not train generative models on the code.
So it's there, you control it. There's
no indices or anything like this. And
what that means is also there's no
setup. So you start cla you download it,
you start it. There's no indexing. You
don't have to wait. You can just use it
right
away. This is a technical talk. So um
I'm going to show some very specific
prompts and very specific code samples
that you can use and hopefully improve
and up your quad code experience.
So some kind of questions that you can
ask is uh you know like how is this
particular piece of code used or how do
I instantiate this thing and cloud code
it won't just do like a text search and
try to answer this. It'll often go a
level deeper and it'll try to find
examples of how is this class
instantiated how is it used and it'll
give you a much deeper answer. So
something that you would get out of a
wiki or documentation instead of just

[00:06]
like command
f something that I do a lot also is ask
it about git history. So for example,
you know, why does this function have 15
arguments and why are the arguments
named this weird way? And this is
something I bet in all of our code
bases, you have some function like this
or some class like this and cloud code
can look through git history and it'll
look to figure out how did these
arguments get introduced and who
introduced them and what was the
situation what are the issues that those
commits linked to and it'll look through
all this and summarize it and you don't
have to tell it that in all these in all
this detail you just ask it. So just say
look through git history and it'll know
to do
this. The reason it knows it by the way
is not because we prompted it to.
There's nothing in the system prompt
about looking through git history. It
knows it because the model is awesome
and if you tell it to use git, it'll
know how to use git. So we're lucky to
be building on such a good
model. I often ask about uh GitHub
issues. So um you know it can use web
fetch and it can fetch issues and look
up context on issues too. And this is

[00:07]
pretty
awesome. Yeah. And this is something
that I do every single Monday in our
weekly standup is I ask what did I ship
this week? And Quad Code looks the log.
It knows my username and it'll just give
me a nice readout of everything I I
shipped and I'll just copy and paste
that into a
document. So yeah, that's tip number one
for people that have not used Cloud Code
before. If you're just showing it to
someone for the first time, on boarding
your team, the thing we definitely
recommend is start with codebased Q&A.
Don't start by using fancy tools. Don't
start by editing code. Just start by
asking questions about the codebase. And
that'll teach people how to prompt. And
it'll start teaching them this boundary
of like what can claude code do? What is
it capable of versus what do you need to
hold its hand with a little bit more?
What can be oneshotted? What can be
two-shotted, threeshotted? What do you
need to use interactive mode for in a
ripple? Once you're pretty comfortable
with Q&A, you can dive into editing
code. This is the next thing. And the
cool thing about uh any sort of agentic

[00:08]
uh you know like using a LM in a agentic
way is you give it tools and it it's
just like magical. It figures out how to
use the tools. And with cloud code we
give it a pretty small set of tools.
It's not a lot. And so it has a tool to
edit files. It has a tool to run bash
commands. Uh it has a tool to search
files. And it'll string these together
to explore the code, brainstorm and then
finally make
edits. And you don't have to prompt it
specifically to use this tool and this
tool and this tool. You just say, you
know, do this thing and it'll figure out
how to do it. It'll string it together
in the right way that makes sense for
quad
code. There's a lot of ways to use this.
Something I like to do sometimes is
before having quad jump in to write
code, I'll ask it to brainstorm a little
bit or make a plan. This is something we
highly recommend and something I see
sometimes is people, you know, they take
quad code and they ask it, hey,
implement this enormous like 30,000 wine
uh feature and sometimes it gets this
right on the first shot. But sometimes
what happens is the thing that it builds

[00:09]
is not at all the thing that you wanted.
And the easiest way to get the result
you want is ask it to think first. So
brainstorm ideas, make a plan, run it by
me, ask for approval before you write
code. And you don't have to use plan
mode. You don't have to use any special
tools to do this. All you have to do is
ask claud and it'll know to do this. So
just say before you write code, make a
plan. That's
it. This is also I wanted to include
this one. This commit push. This is a
really common incantation that I use.
There's nothing special about it, but
Claude is kind of smart enough to
interpret this. So it'll make a commit.
It'll push it to the branch, make a
branch, and then make a pull request for
me on GitHub. You don't have to explain
anything. It'll look through the code.
It'll look through the history. It'll
look through the git log by itself to
figure out the commit format and all the
stuff and it'll make the commit and push
it the right
way. Again, we're not system prompting
it to do this. It just knows how to do
this. The model is
good. As you get a little bit more
advanced, you're going to want to start
to plug in your team's tools. And this

[00:10]
is where Cloud Code starts to really
shine. And there's generally two kinds
of tools. So, one is batch tools. And an
example of this, I just made up this
like barley CLA. This isn't a real
thing. Um, but you can say use the CLI
to do something and you can tell quad
code about this and you can tell it to
use for example like d-help to figure
out how to use it. And this is
efficient. If you find yourself using it
a lot, you can also dump this into your
quadm which we'll talk about in a bit.
So cloud can remember this across
sessions. But this is a common pattern
we follow at anthropic and we see
external customers use too. And same
thing with MCP. Um, quad code can use
batch tools, it can use MCP tools. So,
you know, just tell it about the tools
and you can add the MCP tool and you can
tell it how to use it and it'll it'll
just start using
it. And this is extremely powerful cuz
when you start to use code on a new
codebase, you can just give it all of
your tools, all the tools your team
already uses for this codebase and cloud
code can use it on your

[00:11]
behalf. There's a few common
workflows and this is the one that I
talked about already. So kind of do a
little bit of exploration, do a little
bit of planning and ask ask me for
confirmation before you start to write
code. These other two on the right are
extremely powerful when cla has some way
to check its work. So for example by
writing unit tests or screenshotting and
puppeteer or screenshotting the iOS
simulator, then it can iterate. And this
is incredible because if you give it for
example a mock and you say build this
web UI, it'll get it pretty good. But if
you let it iterate two or three times,
often it gets it almost perfect. So the
trick is give it some sort of tool that
it can use for feedback to check its
work and then based on that it will
iterate by itself and you're going to
get a much better result. So whatever
your domain is, if it's unit test or
integration test or screenshots for apps
or web or anything, just give it a way
to see its result and it'll iterate and
get
better. So these are the next tips.

[00:12]
teach Quad how to use your tools and
figure out the right workflow. Um, if
you want Quad to jump in and code, if
you wanted to brainstorm a little bit,
make a plan, if you wanted to iterate,
kind of have some sense of that so you
know how to prompt Quad to do what you
want. As you go deeper beyond tools, you
want to start to give Quad more context.
And the more context, the smarter the
decisions will be because as an engineer
working in a codebase, you have a ton of
context in your head about your systems
and all the history and and everything
else. So you can there's different ways
to give this to Claude and as you give
Cloud more context it'll do
better. There's different ways to do
this. The simplest one is what we call
quad MD and quad.mmd is the special file
name. The simplest place to put it is in
the project route. So the same directory
you start quad in. Put a quad MD in
there and that'll get automatically read
into context at the start of every
session and essentially the first user
turn will include the quad MD.
You can also have a local cloudmomd and

[00:13]
uh this one you don't usually check into
source control. So cloudmd you should
check into source control share with
your team so that you can write it once
and share it with your team. This one
you don't check in it's just for you.
The kinds of things you put in cloudmd
it's like common bash commands common
mcp tools uh architectural decisions
important files anything that you would
kind of typically need to know in order
to work in this codebase. Try to keep it
pretty short because if it gets too
long, it's just going to use up a bunch
of context and it's usually not that
useful. So just try to keep it as short
as you can. And for for example, in our
codebase, we have uh common batch
commands, we have a style guide, we have
a few core files, kind of things like
that. All the other quad MDs, you can
put them in other nested child
directories and cloud will pull them in
on
demand. So these are the quadmds that
will get pulled in automatically. Um but
then also you can put in put cloudmds in
nested directories and those will get
put those will get automatically pulled
when cloud works in those

[00:14]
directories. Um and of course if you're
you know a company maybe you want a
quadd that's shared across all the
different code bases and you want to
manage it on behalf of your users and
you can put it in your enterprise route
and that'll get pulled in
automatically. There's a ton of ways to
pull in context. I actually had a lot of
trouble putting this slide together just
to communicate the breath of ways you
can do this. But quadmd is pulled in
automatically. You can also use slash
commands. So this is quad/comands and
this can be in your home directory or it
can be checked into your project. And
this is for
slashcomands. And over
here we have a few examples of the slash
commands that we have in cloud code
itself. And so for example, if you're in
the cloud code repo and you see issues
getting labeled, that's actually this
workflow running here. It's label GitHub
issues and we have a GitHub action
running, the same one we talked about
this
morning where Cloud Code will run this
command and it's just a slash command.
It'll run and it'll label the issues so

[00:15]
humans don't have to. It just saves us a
bunch of
time. And of course, you can atmention
files to pull them into context. Um, and
like I said before, quadm in a nested
directory get pulled in when quad works
in that
directory. So give quad more context and
it's definitely worth taking the time to
tune context. You can run it through a
prompt improver. Consider who the
context is for. If you want to pull it
in every time, if you want to pull it in
on demand, if you want to share it with
a team, if it's a personal preference,
definitely take the time to tune it.
This will improve performance
dramatically uh if you do it
right. As you get more advanced, you're
going to want to think about this a
little bit more. This kind of hierarchy
of different ways to pull in everything.
So like not just quadmd, but also config
and uh kind of everything about quad you
can pull in in this hierarchical way. So
projects uh are specific to your git
repo and this you can check in or you

[00:16]
can make it just for you. You can also
have global configs that are across all
your projects or you can have enterprise
policies and this is essentially a
global config that you row out for all
of your employees, everyone on your team
automatically. And this slide is like
pretty information dense, but the point
is this applies to a lot of stuff. So
you can do this for slash commands, you
can do it for permissions. So for
example, if you have a batch command
that you would run for all your
employees uh like all your employees use
this like test command for example, you
can actually just check it into this
enterprise policies file and then any
employee when they run this command, it
will be auto approved which is pretty
convenient. And you can also use this to
block commands. So for example, let's
say there's a URL that should never be
fetched. Um just add it to this config
and that'll make it so an employee
cannot overwrite it and that that URL
can never be fetched. So pretty
convenient both to unblock people and
also just to keep your codebase
safe. And then same thing for MCP
servers. Have a MCP JSON file, check it
into the codebase. That way anytime

[00:17]
someone runs quad code in your codebase,
they'll be prompted to install the MCP
servers and share it with the
team. If you're not sure which of these
to use, this is like a kind of an insane
matrix because we support a lot of stuff
and engineer workflows are very flexible
and every company is different, so we
kind of want to support everything. So
if you're not sure how to get started, I
would recommend start with shared
project
context, you write this once and then
you share it with everyone on the team
and you get this kind of network effect
where you know someone does a little bit
of work and everyone on the team
benefits. There's a lot of tools built
into quad to manage this. Uh so as an
example, if you run memory, you can see
all the different memory files that are
getting pulled in. So maybe I have an
enterprise policy. I have my user
memory. I have project quadd. And then
maybe there's a nested quadmd that's
only pulled in for certain
directories. And then similarly when you
do slashmemory you can edit particular
memory files. When you type pound sign
to remember something you can pick which

[00:18]
memory you want it to go
to. So yeah that's the next tip. take
the time to configure QuantumD, MCP
servers, all the stuff that your team
uses so that you can use it once,
configure it once, and then share it
with
everyone. Um, an example of this is uh
in our apps repo uh for anthropic. This
is like the repo that we have all of our
uh web and apps code in. There's a
Puppeteer MCP server and we share this
with the team. Um, and there's an MCP
JSON checked in. So any engineer working
that repo can use Puppeteer in order to
pilot end to end tests and to screenshot
automatically and iterate so that every
engineer doesn't have to install it
themselves. This is a talk about pro
tips. So I I just want to take a quick
inter key bindings that people may not
know. It's a it's very hard to build for
terminal. It's also very fun. It feels
like rediscovering this new design
language. But something about terminal
is it's it's extremely minimal. And so

[00:19]
sometimes it's hard to discover these
key bindings. And here's just a quick
reference sheet. So anytime you can hit
shift tab to accept edits. Uh and this
switches you into auto accept edits
mode. So bash commands still need
approval, but edits are auto accepted.
And you can always ask quad to undo them
later. Um for example, I'll do this if I
know Claude's on the right track or if
it's writing unit tests and iterating on
tests. I'll usually just switch into
auto accept mode so I don't have to okay
every single
ite. So, for example, if it's not using
a tool correctly and you want it to use
it correctly from then on, just type the
pound sign and then tell it what to
remember and it'll remember it. It'll
incorporate it into QuadMD
automatically. If you ever want to drop
down to bash mode, so just run a bash
command. You can hit the exclamation
mark and type in your command. That'll
run locally, but that also goes into the
context window. So, Claude will see it
on the next turn. Um, and this is pretty
good for longunning commands if you know
exactly what you want to do or any
command that you want to get into
context and cloud will see the command

[00:20]
and the
output. You can appment mention files
and folders. Uh, anytime you can hit
escape to stop what Claude is doing. Um,
no matter what Claude is doing, you can
always safely hit escape. It's not going
to corrupt the session. It's not going
to mess anything up. So maybe Claude is
doing a file edit. I'll hit escape. I'll
tell it what to do differently. Or maybe
it suggested a 20 line edit and I'm like
actually 19 of these lines look perfect
but one line you should change. I'll hit
escape. I'll tell it that and then I'll
tell it to redo the
edit. Uh you can hit escape twice to
jump back in history. Um and then after
you're done with the session you can
start quad with resume to resume that
session if you want. Um or d-
continue. And then anytime if you want
to see more output, hit control R and
that'll show you the entire output. The
same thing that Claude sees in its
context
window. The next thing I want to talk
about is the Cloud Code SDK. So we
talked about this at the top. Uh right
after this, Sid is doing a session I

[00:21]
think just across the hallway and he's
going to go super deep on the SDK. If
you hadn't played around with this, if
you used the -p flag in Claude, this is
what the SDK is. And we've been learning
a bunch of features over the last few
weeks to make it even even
better. Um, so yeah, you can you can
build on top of this. You can do cool
stuff. This is exactly the thing that
claude code uses. It's exactly the same
SDK. And so, for example, something you
can do is claw-p. So, this is the the
CLI SDK. You can pass up you can pass a
prompt. You can pass some allowed tools
which could include specific batch
commands and you can tell it which
format you want. So you might want JSON
or you might want streaming JSON if you
want to process this somehow. So this is
awesome for for building on. We use this
in CI all the time. We use this for
incident response. We use this in all
sorts of pipelines. So really
convenient. Just think of it as like a
Unix utility. You give it a prompt, it
gives you JSON. You can use this in any
way. You can pipe into it. You can pipe
out of it.

[00:22]
The piping is also pretty cool. So you
can use like for example git status and
pipe this in and you know use jq to
select the result. It the combinations
are endless and it's sort of this new
idea. It's like a super intelligent Unix
utility and I think we barely scratched
the surface of how to use this. We're
just figuring this
out. You can read from like a GCP bucket
read you know like a giant log and pipe
it in and tell cloud to figure out
what's interesting about this log. Um,
you can fetch data from like the Sentry
uh CLI. You can also pipe it in and have
Claude do something with
it. The final thing, and this is
probably like the most advanced use
cases we see. I'm sort of a quad normy.
So, I'll have usually like one cloud
running at a time and maybe I'll have
like a few terminal tabs for a few
different repos running at a time. When
I look at power users in an ad of
anthropic, almost always they're going
to have like SSH sessions. They'll have
uh like T-Max tunnels into their quad
sessions. They're going to have a bunch

[00:23]
of checkouts of the same repo so that
they can run a bunch of quads in
parallel in that repo or they're using
git work trees to have some kind of
isolation as they do this. And we're
actively working on making this easier
to use. But uh for now like these these
are some ideas for how to do more work
in parallel with quad. You can run as
many sessions as you want.
Uh, and there's a lot that you can get
done in
Perl. So, yeah, that's it. I wanted to
also leave some time for Q&A. So, I
think this is the last slide that I
have. And yeah, if folks have questions,
there's mics on both
sides. And yeah, we'd love to answer any
questions.
[Applause]
I did.

[00:24]
Hey Boris, thanks for building a cloud
code and I was wondering what was the
hardest implementation like part of the
implementation for you of building it.
I think there's a lot of tricky
parts. Um I think one part that is
especially tricky is the things that we
do to make bash commands safe. Um bash
is inherently pretty dangerous and it
can change system state in unexpected
ways. But at the same time, if you have
to manually approve every single batch
command, it's super annoying as an
engineer and you can't really be
productive because you're just
constantly approving every command. And
just kind of navigating how to do this
safely in a way that that scales across
the different kinds of code bases people
have because not everyone runs their
code in a Docker container um was was
pretty tricky. And essentially the thing
we landed on is there's some commands
that are readon. There's some static
analysis that we do in order to figure
out which commands can be combined in
safe ways. And then we have this pretty
complex tiered permission system so that
you can allow list and block list

[00:25]
commands at different levels.
Hi Boris, you mentioned uh giving an
image to cloud code which made me wonder
if there's some sort of multimodal
functionality that I'm not aware of. Is
that are you just pointing it at an
image on the file system or something?
Yeah, so cloud code is fully multimodal.
Um, it has been from the start. It's in
a terminal, so it's a little uh hard to
discover. Uh, but yeah, you can take an
image and just drag and drop it in.
That'll work. Uh, you can give it a file
path. That'll work. Um, you can copy and
paste the image in and that works
too. Um, so I'll use this pretty often
for if I have like a mock of something,
I'll just drag and drop in the mock.
I'll tell it to implement it. I'll give
it up a tier server so it can iterate
against it. And yeah, it's just fully
automated.
Um, hey, uh, why did you build a CLI
tool instead of an IDE?
Yeah, it's a it's a good question. I
think there's probably two reasons. One
is, uh, we started this at anthropic and

[00:26]
at anthropic people use a broad range of
IDEs and some people use VS Code, other
people use Zed or Xcode or Vim or Emacs
and it was just hard to build something
that works for everyone and so terminal
is just the common denominator. The
second thing is at Enthropic we're uh we
see up close how fast the model is
getting better and so I think there's a
good chance that by the end of the year
people aren't using IDs anymore and so
we want to get ready for this future and
we want to avoid overinvesting in UI and
other layers on top given that the the
way the models are progressing it just
it may not be useful work pretty soon.
Yeah. How much have you I don't know if
this is is this on how much you used
quad code for machine learning modeling
and almost that autoML experience. I was
curious what the experience has been so
far with that. Yeah, I think I think the
question was how much are we using cloud
code for machine learning and and

[00:27]
modeling? We actually use it for this a
bunch. So both engineers and researchers
at anthropic use quad code every day. Um
I think about 80% of people at Enthropic
that are technical use quad code every
day. And hopefully you can see that in
the product and kind of the amount of
love and dog fooding we've put into it.
Um, but this includes researchers who
use tools like the notebook notebook
tool to edit and run notebooks. Okay,
very cool. Thank you.
All right, I think that's it.
[Music]
Thanks. Heat. Heat.
[Music]

</details>

* [Claude Code — DeepLearning.ai Short Course](https://www.deeplearning.ai/short-courses/claude-code-a-highly-agentic-coding-assistant/)
* [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
* [Building and Prototyping with Claude Code](https://www.youtube.com/watch?v=DAQJvGjlgVM)

<!-- yt-inline:DAQJvGjlgVM -->
[![Building and prototyping with Claude Code](https://img.youtube.com/vi/DAQJvGjlgVM/hqdefault.jpg)](https://www.youtube.com/watch?v=DAQJvGjlgVM)

<details>
<summary>자막: Building and prototyping with Claude Code (14:03)</summary>

[00:00]
- These developers tend to like to run
multiple Claude sessions at once,
and they've started calling
this multi-Clauding.
So you might see sessions
where people have like six Claudes open
on their computer at the same time.
- Hey, I'm Alex.
I lead Claude Relations here at Anthropic.
Today we're gonna be
talking about Claude Code,
and I'm joined by my colleague Cat.
- Hey, I'm Cat.
I'm the product manager for Claude Code.
- Cat, I wanna kick this
off just talking about
the insane rate of
shipping in Claude Code.
It feels like literally every time
I open it up in my terminal,
there's a new product or a new feature,
something for me to use.
Can you walk me through
what the process looks like
of the team going from an idea
to actually shipping
something to end users?
- Yeah, so the Claude Code team is full
of very product-minded engineers
and a lot of these features
are just built bottom-up.
It's like you're a developer
and you really wish you had this thing,
and then you build it for yourself.
And the way that our process works
is instead of writing a doc,
it's so fast to use Claude Code

[00:01]
to prototype a feature
that most of the time people
just prototype the feature
and then they ship it
internally to "Ants".
And if the reception is really positive,
then that's a very strong signal
that the external world will like it too.
And that's actually our bar
for shipping it externally.
And then of course there's always features
that like aren't exactly right
that need some tweaking.
And if we feel like, okay,
"Ants" aren't really using it
that much, then we just go
back to the drawing board
and we say like, okay,
what else could we change about this?
- And when we say "Ants," do
we mean Anthropic employees?
- Yes, yes.
- Yeah.
That's really fascinating.
I've never seen a product have as strong
of like a "dogfooding"
loop as Claude Code.
Do you think that's
something we purposely did
or that just kind of naturally arise
from the product itself?
- It is quite intentional,
and it's also a really important reason
why Claude Code works so well.
Because it's so easy to prototype
features on Claude Code,
we do push people to
prototype as much as possible,

[00:02]
but it's hard to reason about
like exactly how a
developer will use a tool
because developers are so heterogeneous
in their workflows.
So oftentimes, even if
you theoretically know
you wanna do something,
like even if you theoretically know
that you wanna build an IDE integration,
there's still a range
of like potential ways
you could go about it.
And often prototyping is the only way
that you can really feel how the product
will actually be in your workflow.
So yeah, it's through the
process of "dogfooding"
that we decide what version of
a feature we decide to ship.
- I see.
And there's something about the,
almost like the flexibility
but also the constraints
of the terminal too
that allows for easy addition
of like new features,
which I've kind of
noticed where it's like,
because we have the primitives built out
of like slash commands and things,
it's easy to add another
one on top of that.
- Yeah, it's totally
designed to be customizable.
And because so many developers
are familiar with the terminal,

[00:03]
it makes like new feature
onboarding super straightforward,
because for example, for
a feature like hooks,
which lets you add a bit of determinism
around Claude Code events,
because every developer
knows how to write a script,
and really at the end of the day,
all a hook is, is a script.
And so you don't need to
learn a new technology
to customize Claude Code.
You write this script that
you already know how to do
and then you add it to one
of the Claude Code events
and now you have some determinism.
- We're really trying to meet customers
or developers where they are
with this tool.
- Definitely.
- Switching gears slightly,
so alongside this insane rate of shipping
is also the insane growth
rate of Claude Code
with developers everywhere.
Can you walk me through
what that's been like
to kind of be on this rocket ship
and how are we seeing various developers,
whether it's at startups or individuals
or at even large enterprises, use Claude?

[00:04]
- So one of the magical
things about Claude Code
is that the onboarding is so smooth.
After you do the NPM install,
Claude Code kind of just
like works out of the box
without any configuration.
And this is true whether
you are an indie developer
through to if you're an
engineer at a Fortune 500.
I think this is the
magic behind Claude Code.
Because it has access to
all of the local tools
and files that you have,
you have this like very clear mental model
for what Claude Code is capable of.
We do see different use
case patterns though
between smaller companies and larger ones.
We find that engineers
at smaller companies
tend to run Claude more autonomously
using things like "auto-accept mode,"
which lets Claude make edits by itself
without approval of each one.
We also find that these developers
tend to like to run multiple
Claude sessions at once,
and they've started calling
this multi-Clauding.
So you might see sessions

[00:05]
where people have like six Claudes open
on their computer at the same time.
Maybe each of them are in
a different Git workspace
or in a different copy of the Git repo,
and they're just like
managing each of them.
Whenever anyone stops
and asks for feedback,
they'll jump in there and then send it off
and let it continue running.
And on the other end of the spectrum
for larger companies,
we find that engineers really
like to use "plan mode."
So "plan mode" is a way for developers
to tell Claude Code to take a second,
explore the code base,
understand the architecture,
and create an engineering plan
before actually jumping
into the code itself.
And so we find that this is really useful
for harder tasks and more complex changes.
- So going back to multi-Clauding
just 'cause I think that's
a fascinating concept.
I'm sure we kind of imagined folks
wanting to do things like that,
but it was like somewhat surprising.
Is there other things
in that domain of like,

[00:06]
oh wow, this is a usage pattern
that we really did not expect
that have kind of popped up organically
and we've shifted our
roadmap around a little bit?
- Yeah, I think multi-Clauding
is the biggest one
because this is something that we thought
was just a power user feature
that like a few people would wanna do.
But in fact this is
actually a really common way
in which people use Claude.
And so for example,
they might have one Claude instance
where they only ask questions
and this one doesn't edit code.
That way they can have
another Claude instance
in the same repo that does edit code
and these two don't
interfere with each other.
Other things that we've seen
are people really like
to customize Claude Code
to handle specialized tasks.
So we've seen people build
like SRE agents on Claude Code,
security agents, incident response agents.
And what that made us realize
is that integrations are so important
for making sure Claude Code works well.
And so we've been encouraging people

[00:07]
to spend more time to
tell Claude Code about,
hey, these are the CLI
tools we commonly use
or to set up remote MCP servers
to get access to logs and
ticket management software.
- When these engineers are
customizing Claude Code,
does that mean they're creating sub-agents
or are they creating markdown files
like CLAUDE.md files?
How exactly are they creating these
different types of agents?
- Yeah, I think the most common ways
that we've seen people customize
is by investing a lot
into the CLAUDE.md file.
So the CLAUDE.md file is
our concept of memory.
And so it's the best place for you
to tell Claude Code about
what your team's goals are,
how the code is architected,
any gotchas in the code base,
any best practices.
And investing in CLAUDE.md
we've heard dramatically improves
the quality of the output.
The other way that people
customize Claude Code
is by adding custom slash commands.

[00:08]
So if there's a prompt
that you're always typing,
you can add that into
the custom slash commands
and you could also check these in
so that you share them
with the rest of your team.
And then you can also add custom hooks.
So if for example,
you want Claude Code to run lints
before it makes a commit,
this is something that's great for a hook.
If you want Claude Code to
send you a Slack notification
every time it's done working,
this is actually the original inspiration
for making hooks.
And so these are all customizations
that people are building today.
- Tell me more about,
what is the Claude Code SDK?
- The Claude Code SDK is a great way
to build general agents.
The Claude Code SDK gives you access
to all of the core building
blocks of an agent,
including you can bring
your own system prompt,
you can bring your own custom tools,
and what you get from the
SDK is a core agentic loop
where we handle the user turns
and we handle executing
the tool calls for you.

[00:09]
You get to use our
existing permission system
so that you don't need to
build one from scratch.
And we also handle interacting
with the underlying API.
So we make sure that we have backoff
if there's any API errors.
We very aggressively prompt cache
to make sure that your
requests are token-efficient.
If you are prototyping
building an agent from scratch,
if you use the Claude Code SDK,
you can get up and running with something
pretty powerful within
like 30 minutes or so.
We've been seeing people build
really cool things with it.
We open-sourced our Claude
Code on GitHub integration,
which is completely built on the SDK,
and we've seen people build
security agents on it,
SRE agents, incident response agents.
And these are just
within the coding domain.
Outside of coding, we've seen people
prototype legal agents, compliance agents.
This is very much intended
to be a general SDK
for all your agent needs.
- The SDK is pretty amazing to me.
I feel like we've lived in
the single request API world

[00:10]
for so long.
And now we're moving to like
a next level abstraction
almost where we're gonna handle
all the nitty-gritty of
the things you mentioned.
Where is the SDK headed?
What's next there?
- We're really excited about the SDK
as the next way to unlock
another generation of agents.
We're investing very heavily
in making sure the SDK is best-in-class
for building agents.
So all of the nice features
that you have in Claude Code
will be available out
of the box in the SDK,
and you can pick and choose
which ones you wanna keep.
So for example, if you want your agent
to be able to have a to-do list, great.
You have the to-do list
tool out of the box.
If you don't want that,
it's really easy to just delete that tool.
If your agent needs to
edit files, for example,
to update its memory, you
get that out of the box.
And if you decide, okay,
mine won't edit files

[00:11]
or it'll edit files in a different way,
you can just bring your
own implementation.
- Okay, so it's extremely customizable,
basically general purpose in the sense
that you could swap out the system prompt
or the tools for your own implementations.
And they just nicely slot in
to whatever thing you're building for,
whether it's in an entirely
different domain than code.
Right?
- Yeah, totally.
I'm really excited to see what
people hack on top of this.
I think like especially for people
who are just trying to prototype an agent,
this is like, I think
by far the fastest way
to get started.
Like we really spent almost a year
perfecting this harness,
and this is the same harness
that Claude Code runs on.
And so if you want to just jump
right into the specific
integrations that your agent needs
and you wanna jump right into like
just working on the system prompt
to share context about the
problems faced with the agent,
and you don't wanna deal
with the agent loop,
this is like the best way to circumvent

[00:12]
all the general purpose harness
and just add your like
special sauce to it.
- Hmm, all right.
Well, you heard it here.
You gotta go build on the SDK.
Before we wrap up here,
I'm really curious to hear your own tips
for how you use Claude Code,
and what are some best practices
we can share with developers?
- When you work with Claude
Code or any agentic tool,
I think the most important thing
is to clearly communicate what
your goals are to the tool.
I think a lot of people
think that prompting
is this like magical
thing, but it really isn't.
It's very much about, okay,
did I clearly articulate
what my purpose is?
Like what my purpose with this task is,
how I'm evaluating the output of the task,
any constraints in the design system.
And I think usually
when you can clearly
communicate these things,
Claude Code will either be able to do them
or just tell you that
like, "Okay, this thing,

[00:13]
like I'm not able to do because A, B, C
and do you wanna try
like D, E, F instead?"
- So it's all about the communication
just as if you're working
with another engineer.
- Yeah, totally.
And another thing is if you notice
that Claude Code did something weird,
you could actually just ask
it why it wanted to do that.
And it might tell you something like,
oh, okay, there was something
in CLAUDE.md that said this,
or I read something in this file
that like gave me this like impression.
And then that way you can actually use
like talking to Claude as a way to debug.
It doesn't always work,
but I think it's definitely worth trying.
And it's like a common
technique that we use.
- You use Claude Code
to debug Claude Code.
I love it.
- Yeah, yeah.
Like the same way that
when working with a human,
if they say something
that you didn't expect,
you might feel like, "Oh, interesting.
Like, what gave you that impression?
Or why did you think this?"
And I think you can do
the same with agents too.
- That's fascinating.
Well, Cat, this has been great.
Really, we appreciate the time.
Thank you.
- Thanks for having me.

</details>


### Internal Support Channels

Establish ongoing support infrastructure for your Claude users:

* Dedicated Slack/Teams channel for Claude questions and tips
* Weekly office hours with champions or power users
* IT helpdesk integration for access and technical issues
* Monthly user group meetings to share best practices
* Dedicated Claude Code support channel for developer-specific questions

## Phase 4: Scaling Adoption

After initial deployment, focus on expanding usage, building internal ownership, and demonstrating sustained value across the organization.

### Expanding Across Teams

Prioritize teams with strong use case fit and willing champions. For each new team:

* Conduct a brief needs assessment to identify high-value workflows
* Provision seats (including Claude Code for developer teams) and deliver tailored onboarding
* Appoint a local champion to drive adoption and share early wins across the organization

### Measuring Impact

Shift from tracking activity metrics to demonstrating business value. Focus on outcomes that matter to leadership:

* Track adoption (active users, department penetration, feature usage) via the Admin dashboards and API
* Measure productivity gains (hours saved, tasks augmented) through periodic user surveys
* Pair quantitative data with qualitative examples – short case studies from team leads illustrating real impact
* Establish a regular reporting cadence (e.g., quarterly business reviews) to keep stakeholders informed

### Feature Rollout & Governance

Introduce advanced capabilities gradually so teams can build confidence without feeling overwhelmed. A natural progression might move from core features (Projects, Artifacts, Connectors) to intelligence features (Enterprise Search, Research) to integrations (Claude Code, Skills) and finally to automation (Cowork, custom connectors).

As usage grows, revisit your governance posture:

* Review data retention policies, audit log cadences, and project visibility defaults
* Maintain an allowlist of approved connectors and extensions, routing new requests through your standard IT governance process
* Configure usage guardrails to manage consumption as the user base expands

### Sustaining Momentum

Long-term success depends on building internal ownership and feedback loops:

* Designate a program owner and consider forming a lightweight Center of Excellence to curate prompts, Skills, and playbooks
* Run periodic user surveys, champion roundtables, and usage analytics reviews to surface what's working and what needs attention
* Refresh training materials quarterly to reflect new features and lessons learned
* Incorporate Claude onboarding into your standard new hire orientation
* At each phase of rollout, consider a brief retrospective:
  + What use cases emerged?
  + What barriers remain?
  + What should change for the next phase?

## Appendix: Resource Directory

A comprehensive directory of support, training, and enablement resources for Claude Enterprise administrators and end users.

### Getting Started

**Essential resources for new deployments and first-time users:**

* [Getting started with Claude](https://support.claude.com/en/articles/8114491-getting-started-with-claude) — First steps, basic navigation, and starting your first conversation
* [What are some things I can use Claude for?](https://support.claude.com/en/articles/7996845-what-are-some-things-i-can-use-claude-for) — Common use cases including writing, analysis, coding, research, and creative tasks
* [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan) — Enterprise features including SSO, SCIM, audit logs, custom retention, and dedicated support
* [Release Notes](https://support.claude.com/en/articles/12138966-release-notes) — Chronological log of new features, improvements, and changes across all Claude products
* [How to get support](https://support.claude.com/en/articles/9015913-how-to-get-support) — Contacting Anthropic support, submitting tickets, and self-service resources

### Training & Enablement

**Resources to upskill your organization on Claude:**

* [Anthropic Academy](https://anthropic.skilljar.com) — Self-paced courses on prompt engineering, Claude features, and best practices
* [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) — Comprehensive documentation on advanced prompt engineering techniques
* [Introduction to Prompt Design](https://support.claude.com/en/articles/7996853-introduction-to-prompt-design) — Foundational prompt engineering principles
* [Claude Enterprise Help Center](https://support.claude.com) — Central hub for all Claude help articles and documentation
* [Use Case Library](https://www.anthropic.com/customers) — Real-world examples of how organizations use Claude

### Identity & Access Management

* [Identity Management](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim) — SSO setup (SAML 2.0 / OIDC), JIT and SCIM provisioning, and IdP migration
* [Restrict access with IP allowlisting](https://support.claude.com/en/articles/13200993-restrict-access-to-claude-with-ip-allowlisting) — Network-level access control by restricting Claude to approved IP ranges
* [Enforce Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions) — Prevent users from accessing unauthorized Claude organizations from your network
* [Configuring session security settings](https://support.claude.com/en/articles/13163631-configuring-session-security-settings) — Session timeout, re-authentication, and session management policies

### User & Seat Management

* [Managing members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans) — Inviting, removing, and managing user roles from the admin console
* [Roles and Permissions](https://support.claude.com/en/articles/9267276-roles-and-permissions) — Owner, Admin, and Member permission levels
* [Purchasing and managing seats](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans) — Seat allocation, scaling, and license management
* [Find and join your organization](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization) — How end users discover and join their company's Claude organization
* [Migrating individual accounts to Enterprise](https://support.claude.com/en/articles/9267400-can-individuals-with-pro-or-max-plan-accounts-migrate-them-to-team-or-enterprise-plan-organizations) — Migration paths and data handling when transitioning plan types
* [What happens to a user's data when removed?](https://support.claude.com/en/articles/12053672-what-happens-to-a-user-s-data-when-they-are-removed-from-a-team-or-enterprise-organization) — Data retention and cleanup policies when removing users

### Governance & Compliance

* [Exporting organization data](https://support.claude.com/en/articles/13346720-how-can-i-export-my-organization-s-data) — Bulk data export for compliance, migration, or backup
* [Usage analytics](https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans) — Dashboard for tracking adoption, usage patterns, and seat utilization
* [Audit logs](https://support.claude.com/en/articles/9970975-how-to-access-audit-logs) — Track user activity, conversations, and admin changes
* [Custom Data Retention Controls](https://support.claude.com/en/articles/10440198-custom-data-retention-controls-for-enterprise-plans) — Configure retention windows from 1 day to indefinite
* [Compliance API](https://support.claude.com/en/articles/13015708-how-can-i-access-the-compliance-api) — Programmatic access for DLP, eDiscovery, and regulatory needs
* [HIPAA-ready Enterprise plans](https://support.claude.com/en/articles/13296973-hipaa-ready-enterprise-plans) — HIPAA compliance capabilities, BAA availability, and healthcare configuration
* [Business Associate Agreements (BAA)](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers) — How to request and execute a BAA with Anthropic
* [Security & Compliance Overview (Trust Center)](https://trust.anthropic.com) — Certifications (SOC 2 Type II, CSA STAR), pen test reports, and compliance documentation

### Billing & Usage

* [Enterprise billing](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan) — Billing structure, invoicing, and payment options
* [Extra usage controls](https://support.claude.com/en/articles/12005970-extra-usage-for-team-and-seat-based-enterprise-plans) — Overage pricing and usage guardrails for organizational plans
* [Usage limits and best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices) — Tips for staying within limits and optimizing conversation efficiency

### Admin Controls

* [Project visibility and sharing](https://support.claude.com/en/articles/9519189-project-visibility-and-sharing) — Admin controls for project sharing policies
* [Disabling public projects](https://support.claude.com/en/articles/9927533-how-can-i-disable-public-projects) — Restrict project sharing to internal-only
* [Managing user feedback settings](https://support.claude.com/en/articles/10504844-managing-user-feedback-settings-on-team-and-enterprise-plans) — Configure whether user feedback is shared with Anthropic
* [Cowork for Enterprise](https://support.claude.com/en/articles/13455879-cowork-for-team-and-enterprise-plans) — Enabling and configuring Cowork mode for your organization
* [Visual and interactive content controls](https://support.claude.com/en/articles/13663666-visual-and-interactive-content-for-team-and-enterprise-plans) — Admin controls for visual content generation features

### Projects & Knowledge Management

* [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) — Persistent workspaces for grouping conversations, uploading reference files, and setting custom instructions
* [Examples of projects you can create](https://support.claude.com/en/articles/9529781-examples-of-projects-you-can-create) — Use case inspiration across different roles and workflows
* [RAG for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) — How Claude searches uploaded project files for grounded, accurate responses
* [Chat search and memory](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context) — Search past conversations and let Claude remember key details across sessions

### Content Creation & Artifacts

* [What are artifacts?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them) — Interactive content blocks for code, documents, websites, and visualizations
* [Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude) — Generate Word docs, spreadsheets, presentations, and other file types
* [Visual and interactive content](https://support.claude.com/en/articles/13641943-visual-and-interactive-content) — Charts, diagrams, interactive web apps, and visual outputs
* [Uploading files to Claude](https://support.claude.com/en/articles/8241126-uploading-files-to-claude) — Supported file types, size limits, and best practices

### Research & Reasoning

* [Using Research](https://support.claude.com/en/articles/11088861-using-research-on-claude) — Deep research mode that searches the web and synthesizes findings into comprehensive reports
* [Web search](https://support.claude.com/en/articles/10684626-enabling-and-using-web-search) — Real-time web search to supplement Claude's knowledge with current information
* [Extended thinking](https://support.claude.com/en/articles/10574485-using-extended-thinking) — Step-by-step reasoning for complex problems
* [When to use search vs. thinking vs. Research](https://support.claude.com/en/articles/11095361-when-should-i-use-web-search-extended-thinking-and-research) — Decision guide for choosing the right tool

### Skills & Customization

* [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills) — Reusable instruction sets that teach Claude specialized workflows and domain expertise
* [How to create custom Skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) — Build skills through natural conversation or manual configuration
* [Provisioning Skills for your organization](https://support.claude.com/en/articles/13119606-provisioning-and-managing-skills-for-your-organization) — Deploy skills across teams and manage the organizational skills catalog

### Cowork & Desktop Agent

* [Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) — Desktop agent mode where Claude creates files, runs code, and automates workflows
* [Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely) — Safety guidelines and sandboxing details

### Personalization

* [Personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features) — Memory, preferred name, and options that shape Claude's responses
* [Custom styles](https://support.claude.com/en/articles/10181068-configure-and-use-styles) — Create and apply response styles (concise, detailed, formal, casual, etc.)
* [Language preferences](https://support.claude.com/en/articles/10769299-how-to-use-claude-in-your-preferred-language) — Multilingual support and language settings

### Enterprise Search & Data

* [Using Enterprise Search](https://support.claude.com/en/articles/12489464-using-enterprise-search) — Search across connected organizational data sources within Claude

### Integration Overview

* [When to use desktop vs. web connectors](https://support.claude.com/en/articles/11725091-when-to-use-desktop-and-web-connectors) — Comparison of web-based (Remote MCP) and desktop connector architectures
* [Interactive Connectors](https://support.claude.com/en/articles/13454812-using-interactive-connectors-in-claude) — Connectors that let Claude take actions (not just read data) in external tools

### Pre-Built Connectors

**Ready-to-use integrations with popular enterprise tools:**

* [Google Drive](https://support.claude.com/en/articles/10166901-using-the-google-drive-integration) — Access, search, and reference Google Drive files in conversations
* [GitHub](https://support.claude.com/en/articles/10167454-using-the-github-integration) — Browse repos, review PRs, search code, and manage issues
* [Slack](https://support.claude.com/en/articles/11506255-getting-started-with-claude-in-slack) — Install and use the Claude Slack app in your workspace
* [Microsoft 365](https://support.claude.com/en/articles/12542951-enabling-and-using-the-microsoft-365-connector) — Connect Outlook, OneDrive, Teams, and other M365 services
* [Microsoft 365 Security Guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide) — Data handling, permissions, and security architecture for the M365 connector
* [All pre-built web connectors](https://support.claude.com/en/articles/11176164-pre-built-web-connectors-using-remote-mcp) — Full list of available pre-built connectors using Remote MCP

### Custom Connectors

**Build your own connectors for proprietary or specialized tools:**

* [Building custom connectors](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers) — Technical guide for developing and deploying Remote MCP server connectors
* [Building desktop extensions with MCPB](https://support.claude.com/en/articles/12922929-building-desktop-extensions-with-mcpb) — MCPB tooling for installable desktop extensions

### Desktop & Browser

* [Claude Desktop](https://support.claude.com/en/collections/16163169-claude-desktop) — Installation, enterprise deployment (Windows/macOS via MDM), managed configuration, and extension allowlists
* [Claude in Chrome](https://support.claude.com/en/collections/18031491-claude-in-chrome) — Browser extension setup, permissions, admin controls, safety best practices, and troubleshooting

### Mobile

* [Claude Mobile Apps](https://support.claude.com/en/collections/9387080-claude-mobile-apps) — iOS and Android installation, voice mode, dictation, widgets, and shortcuts

### Productivity Suites

* [Claude in Excel](https://support.claude.com/en/articles/12650343-using-claude-in-excel) — AI-powered formulas, data analysis, and chart creation within Excel
* [Claude in PowerPoint](https://support.claude.com/en/articles/13521390-using-claude-in-powerpoint) — Generate and edit slide decks directly inside PowerPoint
* [Google Sheets add-on](https://support.claude.com/en/articles/13162029-google-sheets-add-on) — Data analysis and formula help directly in Google Sheets

### Developer Tools

* [Claude in Xcode](https://support.claude.com/en/articles/12293051-using-claude-in-xcode) — Code completion, debugging, and refactoring in Apple's Xcode IDE
* [Claude in Microsoft Foundry](https://support.claude.com/en/articles/12864745-using-claude-in-microsoft-foundry) — Access Claude models through Microsoft's AI Foundry platform

### Claude Code Setup & Configuration

* [Claude Code](https://support.claude.com/en/collections/14445694-claude-code) — Team/Enterprise setup, model configuration, security reviews, and usage analytics
* [Using Claude Code with Team or Enterprise Plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan) — Configuration and deployment for organizational plans
* [Claude Code Usage Analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics) — Track adoption and usage across your organization
* [Claude Code Troubleshooting](https://support.claude.com/en/articles/12386420-claude-code-faq) — Common issues, fixes, and debugging steps

### Claude Code Training

* [Anthropic Academy — Claude Code in Action](https://anthropic.skilljar.com) — Self-paced course on Claude Code workflows

### Function-Specific Guides

**Share these guides with team leads to accelerate adoption in their departments:**

* [Claude for Engineering Teams](https://support.claude.com/en/articles/9945689-claude-for-engineering) — Code review, debugging, architecture, and technical workflows
* [Claude for Marketing Teams](https://support.claude.com/en/articles/9945697-claude-for-marketing) — Content creation, campaign analysis, and brand voice
* [Claude for Sales Teams](https://support.claude.com/en/articles/9945703-claude-for-sales) — Outreach drafting, research, and pipeline management
* [Claude for Product Management](https://support.claude.com/en/articles/9999062-claude-for-product-management) — PRDs, competitive analysis, and user research synthesis
* [Claude for Human Resources](https://support.claude.com/en/articles/9998942-claude-for-human-resources) — Policy drafting, interview prep, and employee communications

### Industry Solutions

**Specialized resources and connectors for regulated and vertical industries:**

* [Claude for Financial Services](https://support.claude.com/en/collections/13972013-claude-for-financial-services) — Getting started, workflows, prompting strategies, skills, and market data connectors (FactSet, S&P Global, Moody's, Morningstar, PitchBook, LSEG, Aiera, Daloopa)
* [Claude for Life Sciences](https://support.claude.com/en/collections/16142619-claude-for-life-sciences) — Getting started plus connectors for BioRender, PubMed, Benchling, Synapse.org, 10x Genomics, and Scholar Gateway
* [Claude for Education](https://support.claude.com/en/collections/12630177-claude-for-education) — Admin deployment guide, Canvas LTI integration, FERPA-compliant data controls, and end-user FAQs
* [Claude for Nonprofits](https://support.claude.com/en/collections/17047088-claude-for-nonprofits) — Getting started plus connectors for Benevity, Blackbaud, and Candid

### Privacy & Data Handling

* [Privacy practices](https://support.claude.com/en/articles/10035659-where-can-i-learn-more-about-anthropic-s-privacy-practices) — How Anthropic handles user data, model training, and privacy controls
* [Who can view my conversations?](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations) — Data visibility, access controls, and conversation privacy by plan type
* [Data ownership for teams](https://support.claude.com/en/articles/9265372-who-owns-and-manages-the-data-of-my-team) — Data ownership policies for organizational plans
* [Data Processor vs. Controller](https://support.claude.com/en/articles/9267385-does-anthropic-act-as-a-data-processor-or-controller) — GDPR role clarification for Anthropic's data handling
* [Data deletion for Enterprise](https://support.claude.com/en/articles/9796617-can-you-delete-data-that-i-sent-via-team-and-enterprise-plans) — Data deletion requests and processes for organizational plans
* [Data Processing Addendum (DPA)](https://support.claude.com/en/articles/7996862-how-do-i-view-and-sign-your-data-processing-addendum-dpa) — Self-service DPA signing for GDPR compliance
* [Safeguards](https://support.claude.com/en/collections/4078535-safeguards) — Usage policy, safeguard appeals, agent guidelines, content reporting, and vulnerability reporting

### Troubleshooting

**Common issues and resolution guides:**

* [Understanding error messages](https://support.claude.com/en/articles/12466728-understanding-claude-error-messages) — Decode common error messages and their solutions
* [Incorrect or misleading responses](https://support.claude.com/en/articles/8525154-claude-is-providing-incorrect-or-misleading-responses-what-s-going-on) — Understanding hallucinations and how to get more accurate answers
* [Content filtering errors](https://support.claude.com/en/articles/9205721-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error) — Why outputs may be blocked and how to adjust your approach

### Video Tutorials

**Share these video walkthroughs with your team for visual, hands-on learning.**

#### Getting Started Videos

* [Getting started with Claude.ai](https://support.claude.com/en/articles/12997377-getting-started-with-claude-ai) — Interface walkthrough, first conversation, and key features
* [Intro to Artifacts](https://support.claude.com/en/articles/9945615-intro-to-artifacts) — Creating and using artifacts in conversations
* [Intro to Projects](https://support.claude.com/en/articles/9945648-intro-to-projects) — Setting up and managing projects
* [Intro to Connectors](https://support.claude.com/en/articles/13123742-intro-to-connectors) — Connecting external tools and data sources
* [Using Research](https://support.claude.com/en/articles/11106443-using-research) — Demo of deep research capabilities

#### Feature Deep Dives

* [Connect your tools for a smarter AI companion](https://support.claude.com/en/articles/11817150-connect-your-tools-to-unlock-a-smarter-more-capable-ai-companion) — Setting up integrations for enhanced capabilities
* [Create and edit files to eliminate busy work](https://support.claude.com/en/articles/12143746-create-and-edit-files-with-claude-to-eliminate-hours-of-busy-work) — Document automation with Claude's file creation features
* [Prototype AI apps with artifacts](https://support.claude.com/en/articles/11649438-prototype-ai-powered-apps-with-claude-artifacts) — Building functional app prototypes using artifacts
* [Teach Claude your way of working using skills](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) — Creating and applying skills for consistent outputs
* [Create a skill through conversation](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) — Building skills via natural conversation
* [Claude in Chrome](https://support.claude.com/en/articles/12431227-simplify-your-browsing-experience-with-claude-in-chrome) — Walkthrough of the Claude in Chrome extension

#### Integration Tutorials

* [Using the GitHub integration](https://support.claude.com/en/articles/9945670-using-the-github-integration) — GitHub connector setup and usage
* [Using the Google Docs integration](https://support.claude.com/en/articles/10389539-using-the-google-docs-integration) — Working with Google Docs in Claude

#### Function & Industry Videos

* [Claude for Engineering](https://support.claude.com/en/articles/9945689-claude-for-engineering) — Code review, debugging, architecture, and technical workflows
* [Claude for Marketing](https://support.claude.com/en/articles/9945697-claude-for-marketing) — Content creation, campaign analysis, and brand voice
* [Claude for Sales](https://support.claude.com/en/articles/9945703-claude-for-sales) — Outreach drafting, research, and pipeline management
* [Claude for Product Management](https://support.claude.com/en/articles/9999062-claude-for-product-management) — PRDs, competitive analysis, and user research synthesis
* [Claude for Human Resources](https://support.claude.com/en/articles/9998942-claude-for-human-resources) — Policy drafting, interview prep, and employee communications
* [Investment Research](https://support.claude.com/en/articles/12068906-using-claude-for-financial-services-for-investment-research) — Market data connectors for equity research workflows
* [Analysis and Modeling](https://support.claude.com/en/articles/12068923-using-claude-for-financial-services-for-analysis-and-modeling) — DCF modeling, comp analysis, and financial statement analysis
* [Investment Memos](https://support.claude.com/en/articles/12068945-using-claude-for-financial-services-for-investment-memos) — Drafting investment memos and thesis documentation
* [Browse all video tutorials](https://support.claude.com/en/collections/10548294-video-tutorials) — Full collection of 26 video tutorials

## Related tutorials

[Tasks to try with @Claude in your workspace](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace

Tasks to try with @Claude in your workspace

Tutorial

[Tutorial](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial

[Best practices for using @Claude](/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude

Best practices for using @Claude

Tutorial

[Tutorial](/resources/tutorials/best-practices-using-claude-tag)Tutorial

[Using Claude Cowork for legal: answer fast questions on past decisions](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions

Using Claude Cowork for legal: answer fast questions on past decisions

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial

[Using Claude Cowork for marketing ops: run a weekly review that preps itself](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself

Using Claude Cowork for marketing ops: run a weekly review that preps itself

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
