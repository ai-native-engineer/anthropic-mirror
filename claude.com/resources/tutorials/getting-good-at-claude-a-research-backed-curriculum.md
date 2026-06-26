<!-- source: https://claude.com/resources/tutorials/getting-good-at-claude-a-research-backed-curriculum -->

# Getting good at Claude: A research-backed curriculum

What research shows about how people get better at working with Claude, and a curriculum model you can adapt for your organization.

  Professional
* Product

  AI Fluency
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/getting-good-at-claude-a-research-backed-curriculum

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cec696e428e4c87beb5612_Fluency%20Curriculum%20%E2%80%94%20dot%20variant%20(5).png)

When we launched the [AI Fluency Index](https://www.anthropic.com/research/AI-fluency-index), we wanted to understand how people get better at working with Claude over time. The early data came from Chat, and it told a consistent story: fluency develops along two tracks that behave very differently. Some skills grow naturally with practice, and others require deliberate, repeated teaching. That finding shaped how we think about onboarding and in-product learning, and it gave organizations a starting point for building their own Claude training.

Since then, we've extended the Index to Claude Code and Claude Cowork, bringing the total to over 50,000 conversations across the 11 behavioral AI fluency indicators. Fluency has a shared structure across all three surfaces, but each product has its own entry point. What "getting good at Claude" looks like depends on which Claude you're using, and if you're responsible for helping a team build fluency, that distinction matters for what you teach first.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cec696e428e4c87beb5612_Fluency%20Curriculum%20%E2%80%94%20dot%20variant%20(5).png)

This piece walks through what we found and offers a simple curriculum model you can adapt for your organization.  
‍

## Each product has a signature move

Each Claude surface rewards a different behavior at the start. We call this the signature move: the gateway behavior that, when present, lifts the other fluency indicators most reliably.

In Chat, the signature move is **iterating**. Users who refine through follow-up turns show stronger fluency on every other dimension we measure, and users who send one message and leave show almost no critical evaluation at all. Iteration creates the space where other skills develop.

In Claude Code and Claude Cowork, the signature move is **clarifying the goal**. Both agentic surfaces reward users who state what they want clearly before Claude starts working. Users who clarify the goal also specify format more often, set interaction style more deliberately, and break down tasks more effectively. Goal clarity clusters with the full range of Description behaviors in a way that iteration doesn't on these surfaces.

For anyone building Claude training for their organization, the implication is that onboarding should teach the signature move first. A Chat curriculum that doesn't establish iteration early will struggle to build anything on top of it. A Claude Code or Claude Cowork curriculum that doesn't establish goal clarity will produce users who hand off vague requests and then wonder why the output missed the mark.

## The Description spectrum develops with practice

After the signature move, learners advance along what we call the Description spectrum: the range of options available for shaping what Claude gives you. The spectrum is organized by durability, or how long the feature affects your interactions with Claude. At the basic end, shaping happens in the moment and affects one response. You iterate, you add context, you upload a file. At the advanced end, shaping happens in configuration and affects every response that follows without as much effort from you. You set up a Project, you write a CLAUDE.md, you schedule a workflow.

The encouraging finding here is that Description skills appear to grow organically and non-linearly with time and exposure. Users who've been around longer provide examples more often, set interaction style more deliberately, and communicate tone expectations more clearly. People who keep using Claude find their way to these skills on their own, so if your training time is limited, simply exposing people to different types of Description they can practice with Claude should prove fruitful.

## The Discernment spiral has to be taught

Discernment, the set of behaviors around evaluating what Claude gives you back, develops very differently. It doesn't grow with tenure. It doesn't transfer from feature familiarity.

Part of this is explained by a shift in how verification happens. When Claude edits a file or produces a report, users can see what it did. They review the diff, run the test, skim the output. This observational verification is real, and our indicators don't fully capture it because you don't type "is this right?" when you can simply look. But observation only catches errors you can see. It misses wrong assumptions, missing context, and plausible-but-false claims. A diff that compiles can still encode the wrong approach, and a report that reads cleanly can still cite the wrong source.

Also, as tasks that were formerly done by early career employees are increasingly automated by Claude, intentional programs to teach people “what good looks like” will be required.

If your training time is limited, Discernment is where to concentrate it.

## A simple curriculum model

Put simply, the teaching sequence is:

1. **Teach the signature move first**
2. **Advance along the Description spectrum**
3. **Revisit Discernment at every step**

Every product learning experience, whether it's a formal module or a quick team session, should reinforce the product's signature move, introduce learner-relevant features, and close with a Discernment check. Building in a "now question it" step is what keeps critical evaluation in the loop.

The tables below map this model to each product. Use them as a starting point for your own curriculum, adapting the features and checks to match what your team actually uses.

### Chat

Signature move: **iterate**. Refining through follow-up turns.

| Durability level | Features | Teaching approach | Discernment check |
| --- | --- | --- | --- |
| Basic | Iteration, model selection, file uploads, web search | Show, then let people explore with their own tasks | Is this response actually usable, or does it need another turn? |
| Middle | Artifacts, extended thinking, connectors | Pair creation with format specification; position thinking as "when you want Claude to think harder" | Read the thinking. Does the reasoning hold, or did Claude just sound confident? |
| Lasting | Projects, custom instructions, memory | Show how a well-set-up Project changes every conversation in it | Is your Project feeding Claude the right context, or just more context? |

### Claude Code

Signature move: **clarify the goal**. Stating what you want before Claude starts running.

| Durability level | Features | Teaching approach | Discernment check |
| --- | --- | --- | --- |
| Basic | Prompt clarity, file references, model selection | One clear goal, one agentic run, then review | Before you accept the diff, ask Claude what it assumed |
| Middle | Skills, slash commands, MCPs | Shape a repeatable capability | Test the capability on a case it might get wrong |
| Lasting | CLAUDE.md, hooks, subagents | Shape every session in the repo | Audit your configuration. Is Claude using it the way you expect? |

### Claude Cowork

Signature move: **clarify the goal**. Writing a brief that names what you need before Claude executes.

| Durability level | Features | Teaching approach | Discernment check |
| --- | --- | --- | --- |
| Basic | The initial prompt, model selection, embedded questions, output review | Write a self-contained prompt; check what you got back | Before you use this, ask: what would make it wrong? |
| Middle | Connectors, plugins, skills | Shape a repeatable fetch-or-produce pattern | Did the connector pull what you actually needed, or just what was easy to find? |
| Lasting | Scheduled workflows, multi-step automations | Shape work that runs without you | When did you last verify this workflow still produces good work? |

## Where to go from here

The AI Fluency Index continues to track these patterns monthly, and we'll keep publishing what we learn as the products evolve and the dataset grows. If you're building Claude training for your organization and want to ground it in this research, the [AI Fluency framework and courseware](https://anthropic.com/ai-fluency) are freely available, and you can sign up for a newsletter to get notified about new research on AI fluency at [anthropic.com/learn](http://anthropic.com/learn)

We're particularly interested in hearing from teams experimenting with Discernment instruction on agentic surfaces, since that's where the data suggests the biggest gap between what users do naturally and what good practice requires. If you're running something along those lines, we'd love to learn from it.

‍

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
