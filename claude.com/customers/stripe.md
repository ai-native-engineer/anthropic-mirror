<!-- source: https://claude.com/customers/stripe -->

Case study | Claude Code

# Stripe deploys Claude Code to 1,370 engineers with zero-configuration enterprise rollout

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![Stripe logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5adf8d23ff734739d3a80_Stripe_light.svg)![Stripe logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5adfff1546febae66f812_Stripe_dark.svg)

Industry:

Software

Company size:

Large

Product:

Claude Code

Location:

North America

1,370 engineers using Claude Code

enabled company-wide

10,000 lines of code migrated in 4 days

A Scala-to-Java migration using Claude models that would have taken an estimated 10 engineering weeks by hand

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Read more

[Read more](/product/claude-code)Read more

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

How enterprises are building AI agents in 2026

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6938f1ba14ef8dffb304fae8_2026%20State%20of%20AI%20Agents%20Report%20-%20Blog%20-%201200%20x%20630%20E.png)

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

Read more

[Read more](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026)Read more

How enterprises are building AI agents in 2026

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

How enterprises are building AI agents in 2026

New research from 500+ technical leaders reveals how enterprises are deploying AI agents—and why 80% already report measurable ROI.

[Prev](#)Prev

[Next](#)Next

[**Stripe**](https://stripe.com) builds financial infrastructure for the internet, powering payments for millions of businesses worldwide. The company's developer infrastructure team ensures that Stripe engineers have the most productive experience of their careers through tooling and platform capabilities.

## With Claude, Stripe:

* Deployed Claude Code to 1,370 engineers with a zero-configuration setup that works immediately on every developer's machine
* Migrated 10,000 lines of Scala to Java in four days, a project estimated at ten engineering weeks without AI assistance
* Collaborated with Anthropic to produce a signed enterprise binary, solving security concerns that had initially blocked deployment
* Created an education program that reframed AI assistants as capable new engineers who need context, not replacements who work autonomously
* Built a foundation for AI-powered agents focused on maintaining Stripe's 5.5 nines of reliability

# The challenge

Stripe needed a CLI-native coding assistant that met enterprise security requirements. For Stripe's developer infrastructure team, led by Scott MacVicar, the challenge wasn't choosing a single winner; it was enabling engineers to find the tools that fit their individual workflows while maintaining enterprise-grade security.

"Things are rapidly evolving here," said MacVicar, who runs Stripe's developer infrastructure group. "We're really just going broad and haven't started doing any consolidation." The team enabled six different coding assistants, recognizing that different engineering personas gravitate toward different interaction models. Infrastructure engineers prefer command-line tools. Product engineers want in-editor experiences. Forcing everyone into one tool would mean leaving productivity on the table.

But breadth created its own problems. Enterprise security requirements meant Stripe couldn't simply let engineers install whatever they wanted. Supply chain attacks are a real concern, and random JavaScript packages on corporate laptops posed unacceptable risk.

# Claude Code enables zero-friction adoption

The path to deployment required collaboration. MacVicar worked directly with Anthropic to produce an enterprise binary version of Claude Code, a process that took two to three months of testing and iteration. The result was a signed binary that could be deployed safely across the organization, bypassing the npm dependency chain that had posed security concerns.

# Treating AI assistants like capable new engineers

"We came up with our internal distribution mechanism," MacVicar explained. "It's pre-installed on everyone's laptop. It's pre-installed on everyone's development box. It's pre-configured with the rules, the tokens, the authentication. It just works out of the box so no one has to go make an account or read all the configurations."

This philosophy extends to all of Stripe's developer tooling: engineers shouldn't spend time reading manuals or figuring out ideal configurations. The infrastructure team handles that complexity so developers can focus on building. Claude Code found its niche among developers who wanted a capable assistant that fit into their existing command-line workflows without requiring them to switch editors.

The biggest challenge hasn't been technical—it's been educational. Engineers initially approached AI assistants with unrealistic expectations, treating them as replacements rather than collaborators.

"People think it is a replacement for themselves and then don't quite give it the right amount of context," MacVicar said. The team developed a mental model that resonated: think of AI as a “new, capable engineer that knows all the programming languages but lacks business context, doesn't understand your codebase, and doesn't know the Stripe way of doing things."

This framing changed how engineers prompted their AI assistants. Instead of expecting magic, they learned to provide context: point to documentation, show example code, explain architectural patterns. The team reinforced this through engineering all-hands presentations, dedicated training sessions, and strategically placed "hint buttons" throughout internal tools. Local examples proved more effective than centralized training. Teams that discovered effective prompts for their specific codebases shared those patterns within their groups, creating organic knowledge transfer. For MacVicar's team, this education work is as important as the tooling itself. This approach to onboarding, treating AI as a collaborator that needs context rather than a replacement, reflects how Stripe and Anthropic see the future of AI-assisted development.

# The results: Building towards AI agents for reliability

Engineers report higher satisfaction with their tooling. While the team hasn't isolated metrics attributable to any single AI assistant, the signals are positive across the board. One concrete example: a team used Claude models to migrate 10,000 lines of Scala to Java in four days, a project estimated at ten engineering weeks by hand. The migration enabled a newer version of the JDK, enabling performance improvements that had been stuck behind the manual effort required. "Sentiment's up,” MacVicar said. "People like it. The vibes are good."

The real ambition lies ahead. Stripe maintains 5.5 nines of reliability, and MacVicar sees AI agents as the path to even higher standards. "If we rely on a human doing something, those are measured in minutes. If we have an agent doing it, we can measure that in seconds."

The team is exploring Claude's agent SDK to build specialized tools focused on incident detection and resolution. In a business where downtime directly impacts customers' revenue, shaving minutes off response times translates to real value.

MacVicar frames the opportunity in four quadrants: humans only, humans with agents, agents with humans, and agents only. "We're pushing things into humans with agents and agents with humans," he said. "The desire is to get to that top quadrant of agents only."

For now, Stripe continues learning what works across its suite of AI tools. The investment in broad enablement, secure deployment, and developer education has created a foundation for whatever comes next in this fast-moving space.

‍

"Claude Code is pre-installed on everyone's laptop. It just works out of the box."

Scott MacVicar

Developer infrastructure team lead, Stripe

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Prev](#)Prev

[Next](#)Next

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[Juno helps people with chronic illness find patterns in their symptoms with Claude](/customers/juno)Juno helps people with chronic illness find patterns in their symptoms with Claude

Juno helps people with chronic illness find patterns in their symptoms with Claude

Customer story

[Customer story](/customers/juno)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story
