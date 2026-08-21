<!-- source: https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills -->

Loading

## What are skills?

Think about the last time you created something with Claude that turned out really well. Maybe it was a presentation, an analysis, or a report. What made it work? Claude brought intelligence and capability, but you also played a crucial part—you explained your standards, you described the structure that works for your needs, you provided examples showing what you wanted, and you caught and fixed things that weren't quite right.

Instead of having to repeat this process the next time you complete a similar task, Skills let you package what you've learned. Then, whenever the context matches, Claude applies the expertise automatically. You're not explaining the same standards repeatedly. You're not hunting for that document with your guidelines. You're not fixing generic output to match what you know works. Claude recognizes the situation, loads your approach, and applies it.

Creating a skill is an act of description. By the time you've built one, you can name the format a task needs, the tone that fits your voice, and an example of what a good result looks like, and hand all three to Claude in one move.

## Why skills matter for your work

You have tasks where you've figured out what works—a way of structuring reports, a framework for analysis, a style for client communication. But every time you start a new conversation with Claude, you're explaining it all over again or fixing the output to match your standards.

**Skills solve this.** Package your approach once, and Claude applies it automatically in any chat.

What you get out of Claude is mostly decided by what you put in. Your format, your standards, and your examples are the most valuable context you can give it, so they're worth writing down once, properly, instead of reconstructing from memory in every chat.

**Before skills:** You ask Claude to create a quarterly business review. Claude can already build presentations, but making them match your standards means explaining your preferences each time. You could document guidelines in a Project, but they don't automatically apply when you need them.

**With skills:** After creating a QBR skill, you ask for the same presentation. Just by mentioning a task related to an existing skill’s name or purpose, Claude can recognize it. In this case, Claude will load your QBR skill. In Claude’s thinking you’ll see “Reading QBR skill”. It automatically applies your brand guidelines and preferred structure, generating a deck that matches your standards from the start.

## Where Skills fit into how you work with Claude

### Projects

You might already use Projects for certain work. Projects make sense when context accumulates over time. Think: a product launch with evolving plans, research that builds on previous findings, a campaign that unfolds over weeks. You can upload documents, build conversation history, and everything stays organized in one workspace. But Projects are bounded, and whatever context you upload to a project only exists there.

Skills work everywhere. Create a Skill once, and it's available in any conversation—regular chats, inside Projects, across all your work with Claude. Skills activate automatically when you reference them, regardless of where you're working.

Use Skills for repeatable procedures you want applied automatically—your brand guidelines, your analysis framework, your report format. Use Projects for work that needs accumulated context—a product launch, a research project, an ongoing campaign. Use both together when your work benefits from persistent context and standardized procedures.

### Custom Instructions

You might also use custom instructions. These are preferences about how Claude works with you in general, like "ask clarifying questions before starting" or "keep explanations concise." They apply universally to everything Claude does for you.

Unlike custom instructions, Skills can contain far more detail. They can include extensive instructions, complete reference libraries and detailed frameworks that would otherwise clutter custom instructions.Skills are also specific to certain types of work and activate only when relevant. For example, "When creating financial models, use this validation framework" lives in a skill, as it won’t apply to everything, only financial modeling work.

### Regular prompting

When you need Claude to do something once, just prompt well. Explain what you want, provide context, refine the output. This works perfectly for one-off tasks or exploratory work.

Skills work differently. They are active everywhere you work with Claude. This means you’re not re-uploading materials and re-explaining standards. Skills also combine automatically when work requires multiple areas of expertise, coordinating without you specifying each one.

Skills also unlock higher quality outputs that would be difficult to achieve through prompting alone. They can package together complete reference libraries, validation frameworks, quality standards, and proven methodologies. This built-in expertise produces results that otherwise would require extensive explanation and rounds of prompting.

## Recognizing when a skill will help your work

Skills range from simple formatting rules to complete workflows that pull data from multiple sources, analyze it, and generate reports. Create a skill when you've figured out how you want a task done and want Claude to follow that approach consistently. This applies in different situations:

### You've refined an approach through experience

While working with Claude, you've figured out how something should be done, and find yourself explaining it to Claude multiple times. When you want Claude to follow that refined approach automatically rather than you explaining it fresh each time, that's a good skill opportunity.

* *`Weekly team update skill`*: structures updates with wins, blockers, and priorities in the format that keeps meetings focused
* *`Customer feedback analysis skill`*: categorizes responses, identifies patterns, surfaces priority requests—your framework for making feedback actionable
* *`Sales call prep skill`*: researches accounts, summarizes recent interactions, and generates talking points for effective calls
* *`Research synthesis skill`*: evaluates sources, extracts key findings, identifies contradictions, and organizes by theme

### Quality depends on having specific materials

Some work needs specific examples, templates, domain knowledge, or assets to meet your standards. Skills become powerful for packaging everything together so quality is consistent.

* *`Brand compliance skill`*: bundles logo files, color codes, approved fonts, and layout templates for consistent company standards
* *`Technical documentation skill`*: references notation guides, terminology standards, and uses diagram templates for documentation consistency
* *`Legal contract skill`*: checks against standard terms, validates regulatory requirements, applies clause libraries and approval checklists

### Setup normally requires assembling multiple pieces

Even occasional work might require gathering multiple files or tools, explaining how they work together, coordinating different requirements. Skills eliminate the setup burden—package everything once and have it available whenever that situation arises.

* *`Product launch skill`:* follows your messaging framework, generate contracts from your templates, creates tasks in project tracker
* *`Market analysis skill`:* combines research frameworks, competitive benchmarks, and regulatory context into evaluations
* *`Board presentation skill`:* pulls financial data, operational metrics, and strategic updates into quarterly reviews

## Ready to create a skill?

Skills are available on Pro, Max, Team, and Enterprise plans. They also need **Code execution and file creation** turned on, since Skills run in Claude’s secure sandboxed computing environment. To get started, navigate to `Settings` > `Capabilities` > `Skills`, check that code execution is enabled, and toggle on some of the pre-built example skills. From there, when you describe a task to Claude that references a skill’s name or description, Claude recognizes it and loads the skill automatically.

Learn how to write your own [custom skills(opens in new tab)](https://support.claude.com/en/articles/12512198-creating-custom-skills), incorporating guidance from our [skills best practices(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) to understand the principles that make skills most effective.

You also don’t have to be technical to start creating skills. Try [creating skills using Claude(opens in new tab)](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation). Start by identifying a well-suited task and describing it for Claude to turn into a skill. Claude will build and structure it into a properly formatted skill file.

### Practice: turn one task into a skill

Pick a task you've explained to Claude more than once. The description you give Claude does most of the work, and three moves carry it:

* **Name the format.** "Three sections, wins, blockers, and priorities, each with at most three bullets" hands Claude the exact shape to fill in.
* **Set the tone.** Say who the output is for and how it should read, like "direct and factual, written for a manager to skim".
* **Paste one good example.** A real output you were happy with tells Claude more about your quality bar than any description of it.

Then describe the skill to Claude in one message, with your own details in place of the team-update ones:

Create a skill for my weekly team update. The format: three sections, wins, blockers, and priorities, each with at most three bullets. The tone: direct and factual, written for my manager to skim. Here's an example of an update that worked well: [paste one you were happy with].

### Check that your skill holds up

A skill starts saving you time once you've tested it. Open a new conversation and ask for the task the way you normally would, such as "draft this week's team update from these notes". Two checks tell you whether it worked:

1. In Claude's thinking, look for "Reading [your skill's name]". If it isn't there, the task you described didn't match your skill's name or description, so adjust one of them, or mention the skill by name, and try again.
2. Put the result next to the example you pasted into the skill. Same structure? Same register? Anything you'd still fix by hand is a line worth sharpening in the skill itself.

The habit worth keeping goes beyond skills themselves: whenever you hand Claude work that matters, name the format, the tone, and an example of what good looks like. When you catch yourself naming the same three things for the same task twice, that's your cue to package them into a skill.

## Additional Resources

### Getting started

* [Help Center: Using Skills(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills) - Setup and troubleshooting
* [How to create a skill with Claude(opens in new tab)](https://support.claude.com/en/articles/12599426-how-to-create-a-skill-with-claude-through-conversation) - Build your first Skill with Claude's guidance

### Going deeper

* [Skill authoring best practices(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) - Learn the principles behind effective Skills
* [Agent skills overview(opens in new tab)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) - Understand how Skills work under the hood
* [Skill cookbooks(opens in new tab)](https://platform.claude.com/cookbook) - Working examples you can adapt
