<!-- source: https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22949f86cd1968deb9f_33dbe8f783d4835a838b4c4ae85d3c04e352fee1-1000x1000.svg)

# Building agents with Skills: Equipping agents for specialized work

Skills package domain expertise in files agents can access and apply—turning general-purpose agents into knowledgeable specialists for real work.

  [Agents](https://claude.com/blog/category/agents)

  [Claude Code](https://claude.com/blog/category/claude-code)
* Product

  Claude Code
* Date

  January 22, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work

A lot has changed in the past year. MCP became the standard for agent connectivity with rapid adoption from industry leaders and the developer community. [Claude Code launched](https://www.anthropic.com/news/claude-3-7-sonnet) as a general-purpose coding agent. And we launched the [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk), which now provides a production-ready agent out of the box.

But as we've built and deployed these agents, we keep running into the same gap: agents have intelligence and capabilities, but not always the expertise to effectively tackle real work. This led us to [create Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills). Skills are organized collections of files that package domain expertise - workflows, best practices, scripts - in a format agents can access and apply. They turn a capable generalist into a knowledgeable specialist.

In this post, we'll explain why we stopped building specialized agents and started building skills instead, and how this shift is changing how we think about extending agent capabilities.

## **The new paradigm: code is all you need**

We used to think agents in different domains would look very different. A coding agent, a research agent, one for finance, one for marketing—each seemed to need its own tools and scaffolding. The industry initially embraced this model of domain-specific agents. But as models improved in intelligence and agent capabilities progressed, we converged on a different approach.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972a852db1883d8c862151f_building-agents-with-skills-fig1-v3%402x.png)

We came to see code less as just a use case and more as an interface for agents to do almost any digital work. Claude Code is a coding agent, but also a general-purpose agent that happens to work through code.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972a8b8cb336e177c409445_building-agents-with-skills-fig2-v4%402x.png)

Consider working with Claude Code to generate a financial report. It can call APIs for research, store data in the filesystem, analyze it with Python, and synthesize insights. All of that happens through code. The scaffolding becomes as simple as bash and a filesystem.

But general capability isn't the same as expertise. When we started using Claude Code for real work, a gap emerged.

## **The missing piece: domain expertise**

Who would you want filing your taxes: a math genius figuring it out from first principles, or an experienced tax professional who's filed thousands of returns? Most people would choose the tax professional. Not because they're smarter, but because they have the right expertise.

Agents today are like that math genius: brilliant at reasoning through novel situations, but often lacking the accumulated expertise of a seasoned professional. They can do amazing things with proper guidance. However, they're often missing important context, can't easily absorb your organization's expertise, and don't automatically learn from repeated tasks.

Skills bridge this gap by packaging domain expertise in a format that agents can progressively access and apply.

## **What are Agent Skills?**

Skills package domain expertise and procedural knowledge for agents.

```
anthropic_brand/
├── SKILL.md
├── docs.md
├── slide-decks.md
└── apply_template.py
```

The simplicity of skills is deliberate. Files are a universal primitive that works with what you already have. You can version them with Git, store them in Google Drive, and share them with your team. This simplicity also means skill creation isn't limited to engineers. Product managers, analysts, and domain experts are already building skills to codify their workflows.

## **Progressive disclosure**

Skills can contain extensive information. To protect the context window and make skills composable, they use progressive disclosure: at runtime, only the metadata (name and description from the YAML frontmatter) is shown to the model.

```
---
name: Anthropic Brand Style Guidelines
description: Anthropic's official brand colors and typography…
---
```

If Claude determines a skill is needed, it reads the full SKILL.md file. For additional detail, skills can include a references/ directory with supporting documentation loaded only on demand.

This three-tier approach means you can equip an agent with hundreds of skills without overwhelming its context window—metadata uses ~50 tokens, full SKILL.md files ~500 tokens, and reference files 2,000+ tokens and only when specifically needed.

## **Skills can include scripts as tools**

Traditional tools have problems: some have poorly written instructions, the model can't always modify or extend them, and they often bloat the context window. Code, on the other hand, is self-documenting, modifiable, and doesn't need to be in context at all times.

Here's a real example: we kept seeing Claude write the same script to apply Anthropic styling to slides. So we asked Claude to save it as a tool for itself:

```
# anthropic/brand_styling/apply_template.py
import sys
from pptx import Presentation

if len(sys.argv) != 2:
    print("USAGE: apply_template.py <pptx>")
    sys.exit(1)

prs = Presentation(sys.argv[1])
for slide in prs.slides:
    ...
```

The corresponding documentation in slide-decks.md simply references this script:

```
## Anthropic Slide Decks
- Intro/outro slides
  - background color: `#141413`
  - foreground color: oat
- Section slides:
  - background color: `#da7857`
  - foreground color: `#141413`

Use the `./apply_template.py` script to update a pptx file in-place.
```

## **The skills ecosystem**

The skills ecosystem has emerged quickly, and so far we've seen three major types of skills being built:

### **Foundational skills**

These provide core capabilities everyone needs: working with documents, spreadsheets, presentations, etc. They encode best practices for document generation and manipulation. You can see what this looks like in practice by exploring the [foundational skills in our public repository](https://github.com/anthropics/skills/tree/main/skills/public).

### **Partner skills**

As skills standardize how agents interact with specialized capabilities, companies are building skills to make their services agent-accessible. [K-Dense](https://github.com/K-Dense-AI/claude-scientific-skills), [Browserbase](https://github.com/browserbase/agent-browse), [Notion](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0), and [many others](https://claude.com/blog/organization-skills-and-directory) are creating skills that integrate their services directly, extending Claude's capabilities in specific domains while maintaining the simplicity of the skills format.

### **Enterprise skills**

Organizations build proprietary skills encoding their internal processes and domain expertise. Skills help capture the specific workflows, compliance requirements, and institutional knowledge that make an agent useful for enterprise work.

## **Trends we see**

As skills adoption grows, several patterns are emerging that point to where this paradigm may be heading. These trends shape how we think about skill design and the tooling we're building to support skill developers.

### **Increasing complexity**

Early skills were simple documentation references. Now we're seeing sophisticated multi-step workflows that coordinate data retrieval, complex calculations, and formatted output across multiple tools.

* **Simple**: "Status report writer" (~100 lines) - Templates and formatting
* **Intermediate**: "Financial model builder" (~800 lines) - Data retrieval, Excel modeling with Python
* **Complex**: "RNA sequencing pipeline" (2,500+ lines) - Coordinates HISAT2, StringTie, DESeq2 analysis

### **Skills and MCP**

[Skills and MCP servers work together](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) naturally. A competitive analysis skill might coordinate web search, internal databases via MCP, Slack message history, and Notion pages to synthesize a comprehensive report.

### **Non-developer adoption**

Skill creation is expanding beyond engineers to product managers, analysts, and domain experts across disciplines. They can create and test their first skill in under 30 minutes using the skill-creator tool, which guides them through the process interactively. We're working  to make skill creation even more accessible, with improved tooling and templates that let anyone capture and share expertise.

## **The complete architecture**

Putting it all together, the emerging agent architecture looks like a combination of:

1. **Agent loop**: The core reasoning system that decides what to do next
2. **Agent runtime**: Execution environment (code, filesystem)
3. **MCP servers**: Connections to external tools and data sources
4. **Skills library**: Domain expertise and procedural knowledge

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972ab24ac6df74ad6704f37_building-agents-with-skills-fig3-v2%402x.png)

Each layer has a clear purpose: the loop reasons, the runtime executes, MCP connects, and skills guide. This separation makes the system comprehensible and allows each piece to evolve independently.

Consider what happens when you add a single skill to this architecture. The [frontend design skill](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) transforms Claude's frontend capabilities instantly. It provides specialized guidance on typography, color theory, and animation, activating only when building web interfaces. Progressive disclosure means it loads only when relevant. Adding new capabilities is straightforward.

## **Deploying skills to new verticals**

This emerging pattern of general agents equipped with MCP servers and skills is already helping us deploy Claude to new verticals.

### **Financial Services**

Just after launching skills, we enhanced [Claude for the financial services](https://www.anthropic.com/news/claude-for-financial-services) sector with skills that make Claude more useful for finance professionals:

* **DCF model builder**: Constructs discounted cash flow models with proper WACC calculations and sensitivity analysis
* **Comparable company analysis**: Generates comps tables with relevant multiples and benchmarking
* **Earnings analysis**: Processes quarterly results and creates investment update reports
* **Initiation coverage**: Builds comprehensive research reports with financial models
* **Due diligence**: Structures M&A analysis with standardized frameworks
* **Pitch materials**: Creates client presentations following industry standards

### **Healthcare & Life Sciences**

We've also enhanced our [healthcare and life sciences offerings](https://www.anthropic.com/news/healthcare-life-sciences) with skills that make Claude more useful for researchers, clinicians, and healthcare developers:

* **Bioinformatics bundles**: Skills for scVI-tools and Nextflow deployments, essential for managing genomic pipelines and single-cell RNA sequencing
* **Clinical trial protocol generation**: Accelerates protocol development for clinical research
* **Scientific problem selection**: Helps researchers identify and frame impactful research questions
* **FHIR development**: Helps developers write more accurate code for health data interoperability, connecting healthcare systems faster with fewer errors
* **Prior authorization review**: Cuts administrative burden and accelerates patient access to needed care by cross-referencing coverage requirements, clinical guidelines, and patient records

## **Standardizing Agent Skills**

To enable this vision, we're publishing [Agent Skills](https://agentskills.io) as an open standard. Like MCP, we believe skills should be portable across tools and platforms. The same skill should work whether you're using Claude or other AI platforms. We've been collaborating with members of the ecosystem on the standard, and we're excited to see early adoption.

When someone starts using an AI agent for the first time, it should already know what you and your team care about because skills capture and transfer that expertise. As this ecosystem grows, a skill built by someone else in the community can make your agent more useful, reliable, and capable - regardless of which AI platform they're using.

## **Getting started**

We're converging on an architecture for general agents, and skills provide a paradigm for shipping and sharing new capabilities. The real value emerges from the collective knowledge base we build together: capturing expertise, transferring it across teams, and making every agent more capable than the last.

**Resources:**

* [Don’t Build Agents, Build Skills Instead](https://youtu.be/CEvIs9y1uog?si=yhYQH-ZTX0DfNdtm) (YouTube Video)

<!-- yt-inline:CEvIs9y1uog -->
[![Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic](https://img.youtube.com/vi/CEvIs9y1uog/hqdefault.jpg)](https://www.youtube.com/watch?v=CEvIs9y1uog)

<details>
<summary>자막: Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic (16:22)</summary>

[00:00]
[music]
All right, good morning and thank you
for having us again. Last time we were
here, we're still figuring out what an
agent even is. Today, many of us are
using agents on a daily basis. But we
still notice gaps. We still have slots,
right? Agents have intelligence and
capabilities, but not always expertise
that we need for real work. I'm Barry.
This is Mahes. We created agent skills.
In this talk, we'll show you why we
stopped building agents and started
building skills instead.
A lot of things have changed since our
last talk. MCP became the standard for
agent connectivity. Cloud Code, our
first coding agent, launched to the
world and our cloud agent SDK now

[00:01]
provides a production ready agent out of
the box. We have a more mature ecosystem
and we're moving towards a new paradigm
for agents. That paradigm is a tighter
coupling between the model and a runtime
environment.
Put simply, we think code is all we
need.
We used to think agents in different
domains will look very different. Each
one will need its own tools and
scaffolding and that means we'll have a
separate agent for each use case for
each domain. Well, customization is
still important for each domain. The
agent underneath is actually more
universal than we thought.
What we realized is that code is not
just a use case but the universal
interface to the digital world.
After we built cloud code, we realized
that cloud code is actually a general
purpose agent.
Think about generating a financial
report. The model can call the API to
pull in data and do research. It can
organize that data in the file system.
It can analyze it with Python and then

[00:02]
synthesize the insight in old file
format all through code. The core
scaffolding can suddenly become as thin
as just bash and file system which is
great and really scalable. But we very
quickly run into a different problem
and that problem is domain expertise.
Who do you want doing your taxes? Is it
going to be Mahesh, the 300 IQ
mathematical genius, or is it Barry, an
experienced tax professional, right? I
would pick Barry every time. I don't
want Mahesh to figure out the 2025 tax
code from first principles. I need
consistent execution from from a domain
expert. As agents today are a lot like
Mahes. They're brilliant, but they lack
expertise.
They can do no more slow. They can do
amazing things when you really put in
the effort and give proper guidance, but
they're often missing the important
context up front. They can't really
absorb your expertise super well, and
they don't learn over time.
That's why we created agent skills.

[00:03]
Skills are organized collections of
files that package composable procedural
knowledge for agents.
In other words, they're folders. This
simplicity is deliberate. We want
something that anyone human or agent can
create and use as long as they have a
computer. These also work with what you
already have. You can version them in
Git, you can throw them in Google Drive
and you can zip them up and share with
your team. We have used files for uh as
a primitive for decades and we like
them. So why change now?
Because of that skills can also include
a lot of scripts as tools. Traditional
tools have pretty obvious problems. Some
tools have poorly written instructions
and are pretty ambiguous and when the
model is struggling, it can't really
make a change to the tool. So, it's just
kind of stuck with a code start problem
and they always live in the context
window. Code solves some of these
issues. It's self-documenting. It is
modifiable and can live in the file
system until they're really needed and
used. Here's an example of a script

[00:04]
inside of a skill. We kept seeing Claude
write the same Python script over and
over again to apply styling to slides.
So we just ask cloud to save it inside
of the skill as a tool for his version
for his future self. Now we can just run
the script and that makes everything a
lot more consistent and a lot more
efficient.
At this point skills can contain a lot
of information and we want to protect
the context window so that we can fit in
hundreds of skills and make them truly
composable. That's why skills are
progressively disclosed. At runtime,
only this metadata is shown to the model
just to indicate that he has the skill.
When an agent needs to use a skill, it
can read in the rest of the skill.md,
which contains the core instruction and
directory for the rest of the folder.
Everything else is just organized for
ease of access. So that's all skills
are. They're organized folders with
scripts as tools.
Since our launch five weeks ago, this

[00:05]
very simple design has translated into a
very quickly growing ecosystem of
thousands of skills. And we've seen this
be split across a couple of different
types of skills. There are foundational
skills, third party skills created by
partners in the ecosystem, and skills
built within an enterprise and within
teams.
To start, foundational skills are those
that give agents new general
capabilities or domain specific
capabilities that it didn't have before.
We ourselves with our launch built
document skills that give Claude the
ability to create and edit professional
quality office documents. We're also
really excited to see people like
Cadence build scientific research skills
that give Claude new capabilities like
EHR data analysis and using common
Python bioinformatics libraries better
than it could before.
We've also seen partners in the
ecosystem build skills that help Claude
better with their own software and their

[00:06]
own products. Browserbase is a pretty
good example of this. They built a skill
for their open- source browser
automation tooling, stage hand. And now
Claude equipped that this skill and with
stage hand can now go navigate the web
and use a browser more effectively to
get work done.
And notion launched a bunch of skills
that help claude better understand your
notion workspace and do deep research
over your entire workspace.
And I think where I've seen the most
excitement and traction with skills is
within large enterprises. These are
company and team specific skills built
for an organization.
We've been talking to Fortune 100s that
are using skills as a way to teach
agents about their organizational best
practices and the weird and unique ways
that they use this bespoke internal
software.
We're also talking to really large
developer productivity teams. These are
teams serving thousands or even tens of
thousands of developers in an

[00:07]
organization that are using skills as a
way to deploy agents like cloud code and
teach them about code style best
practices and other ways that they want
their developers to work internally.
So all of these different types of
skills are created and consumed by
different people inside of an
organization or in the world. But what
they have in common is anyone can create
them and they give agents the new
capabilities that they didn't have
before.
So, as this ecosystem has grown, we've
started to observe a couple of
interesting trends. First, skills are
starting to get more complex. The most
basic skill today can still be a
skill.md markdown file with some prompts
and some really basic instructions, but
we're starting to see skills that
package software, executables, binaries,
files, code, scripts, assets, and a lot
more. And a lot of the skills that are
being built today might take minutes or
hours to build and put into an agent.
But we think that increasingly much like

[00:08]
a lot of the software we use today,
these skills might take weeks or months
to build and be maintained.
We're also seeing that this ecosystem of
skills is complementing the existing
ecosystem of MCP servers that was built
up over the course of this year.
Developers are using and building skills
that orchestrate workflows of multiple
MCP tools stitched together to do more
complex things with external data and
connectivity. And in these cases, MCP
MCP is providing the connection to the
outside world while skills are providing
the expertise.
And finally, and I think most excitingly
for me personally, is we're seeing
skills that are being built by people
that aren't technical. These are people
in functions like finance, recruiting,
accounting, legal, and a lot more. Um,
and I think this is pretty early
validation of our initial idea that
skills help people that aren't doing
coding work extend these general agents
and they make these agents more

[00:09]
accessible for the day-to-day of what
these people are working on.
So tying this all together, let's talk
about how these all fit into this
emerging architecture of general agents.
First, we think this architecture is
converging on a couple of things. The
first is this agent loop that helps
manage the the model's internal context
and manages what tokens are going in and
out. And this is coupled with a runtime
environment that provides the agent with
a file system and the ability to read
and write code.
This agent, as many of us have done
throughout this year, can be connected
to MCP servers. And these are tools and
data from the outside world that make
the the agent more relevant and more
effective.
And now we can give the same agent a
library of hundreds or thousands of
skills that it can decide to pull into
context only at runtime when it's
deciding to work on a particular task.
Today, giving an agent a new capability

[00:10]
in a new domain might just involve
equipping it with the right set of MCP
servers and the right library of skills.
And this emerging pattern of an agent
with an MCP server and a set of skills
is something that's already helping us
at Enthropic deploy Claude to new
verticals. Just after we launched skills
5 weeks ago, we immediately launched new
offerings in financial services and life
sciences. And each of these came with a
set of MCP servers and a set of skills
that immediately make Claude more
effective for professionals in each of
these domains.
We're also starting to think about some
of the other open questions and areas
that we want to focus on for how skills
evolve in the future as they start to
become more complex. We really want to
support developers, enterprises, and
other skill builders by starting to
treat skills like we treat software.
This means exploring testing and
evaluation, better tooling to make sure
that these agents are loading and

[00:11]
triggering skills at the right time and
for the right task, and tooling to help
measure the output quality of an agent
equipped with the skill to make sure
that's on par with what the agent is
supposed to be doing.
We'd also like to focus on versioning.
as a skill evolves and the resulting
agent behavior uh evolves, we want this
to be uh clearly tracked and to have a
clear lineage over time.
And finally, we'd also like to explore
skills that can explicitly depend on and
refer to either other skills, MCP
servers, and dependencies and packages
within the agents environment. We think
that this is going to make agents a lot
more predictable in different runtime
environments. and the composability of
multiple skills together will help
agents like Claude elicit even more
complex and relevant behavior from these
agents.
Overall, these set of things should
hopefully make skills easier to build
and easier to integrate into agent
products, even those besides claude.

[00:12]
Finally, a huge part of the value of
skills we think is going to come from
sharing and distribution. Barry and I
think a lot about the future of
companies that are deploying these
agents at scale. And the vision that
excites us most is one of a collecting
and collective and evolving knowledge
base of capabilities that's curated by
people and agents inside of an
organization. We think skills are a big
step towards this vision. They provide
the procedural knowledge for your agents
to do useful things. And as you interact
with an agent and give it feedback and
more institutional knowledge, it starts
to get better and all of the agents
inside your team and your org get better
as well. And when someone joins your
team and starts using Claude for the
first time, it already knows what your
team cares about. It knows about your
day-to-day and it knows about how to be
most effective for the work that you're
doing.
And as this grows and this ecosystem
starts to develop even more, this was

[00:13]
going to this compounding value is going
to extend outside of just your organ
into the broader community. So just like
when someone else across the world
builds an MCP server that makes your
agent more useful, a skill built by
someone else in the community will help
make your own agents more capable,
reliable, and useful as well.
This vision of a evolving knowledge base
gets even more powerful when claw starts
to create these skills. We design skills
specifically as a concrete steps towards
uh continuous learning.
When you first start using cloud, this
standardized format gives a very
important guarantee. Anything that cloud
writes down can be used efficiently by a
future version of itself. This makes the
learning actually transferable.
As you build up the context skills makes
the concept of memory more tangible.
They don't capture everything. They
don't capture every type of information.
Just procedural knowledge that cloud can
use on specific tasks.
When you have worked with cloud for
quite a while, the flexibility of skills

[00:14]
matters even more. Cloud can acquire new
capabilities instantly, evolve them as
needed, and then drop the ones that
become obsolete. This is what we have
always known. The power of in in context
learning makes this a lot more cost-
effective for information that change on
daily basis.
Our goal is that claude on day 30 of
working with you is going to be a lot
better on cloud on day one. CL can
already create skills for you today
using our skill creator skill and we're
going to continue pushing in that
direction.
We're going to conclude by comparing the
agent stack to what we have already seen
computing.
In a rough analogy, models are like
processors. Both require massive
investment and contain immense
potential, but only so useful by
themselves.
Then we start building operating system.
The OS made processors far more valuable
by orchestrating the processes,
resources, and data around the
processor. In AI, we believe that agent

[00:15]
runtime is starting to play this role.
We're all trying to build the cleanest,
most efficient, and most scalable uh
abstractions to get the right tokens in
and out of the model.
But once we have a platform, the real
value comes from applications. A few
companies build uh processors and
operating systems, but millions of
developers like us have built software
that encoded domain expertise and our
unique points of view. We hope that
skills can help us open up this layer
for everyone. This is where we get
creative and solve concrete problem for
ourselves, for each other, and for the
world just by putting stuff in the
folder. So skills are just the starting
point.
To close out, we think we're now
converging on this general architecture
for general agents. We've created skills
as a new paradigm for shipping and
sharing new capabilities. So we think
it's time to stop rebuilding agents and
start building skills instead. And if
you're excited about this, come work
with us and start building some skills

[00:16]
today. Thank you.
[music]
>> [music]

</details>

* [Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
* [GitHub repository](https://github.com/anthropics/skills)
* [Skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction)
* [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
* [Skills API quickstart](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
* [Skills best practices documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

### **Acknowledgments:**

Barry Zhang, Mahesh Murag, Keith Lazuka, Ryan Whitehead

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

Jun 24, 2026

### Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

Claude Code

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](#)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

[Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](/blog/agent-identity-access-model)Agent identity in Claude Tag: a new access model for autonomous, team-wide AI

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

Jun 3, 2026

### Running an AI-native engineering org

Claude Code

[Running an AI-native engineering org](#)Running an AI-native engineering org

[Running an AI-native engineering org](/blog/running-an-ai-native-engineering-org)Running an AI-native engineering org

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

May 12, 2026

### How Anthropic's cybersecurity team built a threat detection platform with Claude Code

Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](#)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

[How Anthropic's cybersecurity team built a threat detection platform with Claude Code](/blog/how-anthropic-uses-claude-cybersecurity)How Anthropic's cybersecurity team built a threat detection platform with Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

Apr 20, 2026

### Meet the winners of our Built with Opus 4.6 Claude Code hackathon

Claude Code

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](#) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

[Meet the winners of our Built with Opus 4.6 Claude Code hackathon](/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) Meet the winners of our Built with Opus 4.6 Claude Code hackathon

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code
