<!-- source: https://claude.com/resources/articles/how-brex-improves-code-quality-and-productivity-with-claude-code -->

When Andy Reed joined [Brex](https://www.brex.com/) as a content designer two years ago, he never imagined he'd be writing code and building Figma plugins.

"I don't know how I would have gotten even half my work done in the past month without [Claude Code](https://claude.com/product/claude-code)," Reed said.

But that's exactly what happened when Reed embraced [Claude Code](https://claude.com/product/claude-code), Anthropic’s agentic coding solution—and his story is just one example of how the intelligent finance platform is transforming the way their company works.

To learn more, we spoke with three Brex team members about how they’re using Claude Code:

* Hércules Gimenes, Software Engineering Lead on the Product AI team
* Sumeet Marwaha, Head of Data & Analytics
* Andy Reed, Senior Content Designer

What emerged from these conversations wasn't just a story about productivity gains, though teams report 3-4x improvements on specific tasks. It's about fundamentally reimagining how the company works together to streamline workflows, inspire creative problem solving, and drive collaboration at scale.

## Adopting a mindset shift with agentic coding

For Hércules Gimenes and the Product AI team, Claude Code represented something more profound than a new tool.

"Claude Code offers a mindset shift," he explained. "Instead of being in the driver's seat, you're the reviewer of the changes that Claude introduces. You're guiding the vision and direction."

This shift has redefined what "writing code" means at Brex—a reflection of the company’s AI-first principles in action. Rather than spending time on implementation details, engineers now focus on architecture and problem-solving. The result? Better code, not just faster code.

"I don't think I save time using Claude Code," Gimenes said. "I refine the problem itself much more. You can try three approaches for the same problem during the same amount of time, and after the third approach, you have a much clearer understanding and a much cleaner interface."

## Breaking down barriers between technical and non-technical roles

While the Product AI team was discovering new ways to iterate on code quality, Reed was experiencing his own revelation.

As a content designer, he found in Claude Code something unexpected: independence.

Previously, updating a simple string meant filing a ticket and waiting for an engineer. Now, Reed makes PRs directly, but the real transformation came when he tackled a project that had been on the backlog indefinitely: integrating comprehensive content guidelines into every component of Brex's design system.

"It would have taken me probably weeks if not months doing it manually," Reed explained. Using Claude Code, he completed the project in a few days, systematically adding content-specific guidelines pulled from internal style guides, accessibility standards and external best practices.

The impact rippled across teams. Engineers and designers now have content guidelines embedded directly in their tools, eliminating the need for constant cross-referencing and reducing errors before they happen. It’s a small but powerful example of intelligent finance at work: systems running in the background, allowing people to focus on higher-value, creative work.

## Democratizing data access across the organization

Meanwhile, Sumeet Marwaha's Data & Analytics team was solving a different but equally important challenge: making data accessible to everyone at Brex, not just SQL experts.

The team built Brex Explorer, a text-to-SQL interface powered by Claude Code and MCP servers. Now, a sales manager can ask in plain text: "How many customers exist with over $10 million in their Brex account in Jacksonville, Florida and were onboarded in the last year?" The system translates the query, runs it and summarizes the results.

The real multiplier effect came from their AI data engineering agent. Tasks that previously required specialized knowledge, like adding data tables with all the necessary file edits and test configurations, can now be completed by any engineer.

"It's like a 4x speed increase across maybe 2x more people that are contributing," Marwaha noted. Claude Code has seen 50% adoption across the org, with Marwaha hoping to reach 100% adoption by month's end.

## The unexpected benefits of having an “everything tool”

As teams across Brex adopted Claude Code, surprising use cases emerged. During a company hackathon, Gimenes used Claude Code's headless mode to build a sophisticated submission agent in just a few hours, something that would typically take days of development.

Reed discovered he could now build tools he never imagined creating, like a Figma plugin that automatically reviews designs against Brex's standards. "It feels like I have the world's best intern," he said.

But perhaps the most significant unexpected benefit has been Claude Code's role as an organizational knowledge repository. With Brex's complex monorepo structure using Kotlin and Bazel, understanding how different systems connect has always been challenging. Now, Claude Code serves as an "oracle" that can answer questions about codebase functionality instantly.

"Traditionally, a design meeting would involve talking about how something should work, but nobody really understands how the sausage was made," Reed explained. "Now I've got the oracle sitting on my other monitor."

## Scaling Claude Code best practices across the company

As Claude Code adoption spread across Brex, teams developed best practices that have become standard:

* **Structured Context Management**: Each major directory in the monorepo now has its own CLAUDE.md file containing domain-specific context. New engineers can understand Mastercard integration details or banking regulations without relying on tribal knowledge.
* **Automated Documentation**: The Product AI team implemented CI/CD checks that verify when code changes might outdate documentation, prompting updates. "Having up-to-date documentation is something you can trust—it's so powerful," Gimenes emphasized.
* **Context-Aware Commands**: Teams created custom commands that automatically load relevant context. The /submit-pr command, for instance, fetches git status, recent changes, and related PR information before executing.
* **Start with Discovery**: "Being able to find what you need is not really stored in some staff engineer's brain anymore," Marwaha observed. "It's in the codebase, accessible to everyone."

## The future of Claude Code at Brex

Teams at Brex are already planning next-generation applications:

* The Data team is preparing to tackle previously untouchable projects, like analyzing trillions of credit card transaction itemization data points, work that was too tedious to justify before Claude Code made it feasible. They're also developing role-specific agents, including one to power RevOps tasks.
* The Product AI team envisions more sophisticated context management, where documentation updates itself automatically and context remains decentralized yet accessible.

From content designers building technical tools to data analysts democratizing access, Claude Code has become what Gimenes calls an “everything tool” — useful for integrating Brex’s domain knowledge with external best practices.

It also highlights a powerful duality: the intelligent finance Brex delivers to customers, helping them spend smarter and move faster, is the same philosophy that shapes how Brex teams work internally, empowering every employee to build with speed and confidence, regardless of their technical background.

[ArticleSep 30, 2026

### How Anthropic's sales team rebuilt inbound with Claude Managed Agents

Carl Johnson, a sales development leader at Anthropic, shares how a Claude-powered buying agent now answers most inbound customers, and how that changed the way our sales team works.

Claude Platform](https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents)[ArticleSep 23, 2026

### How to prepare for AI-driven code modernization projects

How to organize AI-driven modernization projects for critical systems and regulated enterprises.

Claude Code](https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects)[ArticleSep 23, 2026

### How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

CodeRabbit expanded its Vercel plan through Claude Marketplace, and Power Digital and ThoughtSpot expanded their Snowflake capacity using their existing Anthropic commitment.

Claude Platform](https://claude.com/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)[ArticleSep 17, 2026

### Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

Balyasny Asset Management (BAM) Chief AI Officer Charlie Flanagan on why the firm uses Claude Fable 5 and the role of safeguards in deploying frontier intelligence safely and reliably across the organization.
‍

Claude PlatformClaude Code](https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
