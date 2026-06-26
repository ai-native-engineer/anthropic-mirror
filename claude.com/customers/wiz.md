<!-- source: https://claude.com/customers/wiz -->

Case study | Claude Code

# Wiz migrates a 50,000-line codebase with Claude Code, achieving 2x performance gains

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![wiz_logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cc1a95a6ba3eb3b970a550_New_Logo_Blue%201.svg)![wiz_logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69cc1a9cc702022153c8556b_logo_wiz-dark-mode%201.svg)

Industry:

Software

Company size:

Large

Product:

Claude Code

Partner:

AWS

Location:

EMEA

50,000 lines of Python to Go in ~20 hours

A migration estimated at 2–3 months of specialized engineering effort

1.5x increase in merged PRs

among top 100 contributors, with 90%+ of engineers using Claude Code daily

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

[Prev](#)Prev

[Next](#)Next

[Wiz](https://www.wiz.io/) is a cloud security platform with over 2,000 employees that helps security teams gain visibility into their cloud environments, manage security posture, and take remediation steps across the full development lifecycle. Wiz’s Data Security Posture Management (DSPM) team is responsible for scanning customer files across every environment and reading their contents to identify security issues like exposed credentials or sensitive data.

## With Claude, Wiz achieved:

* **~1 day of active development** to migrate a 50,000-line Python library to Go — a project estimated at 2-3 human months manually
* **2x+ faster PDF processing in production**, with the new Go library fully replacing the sandboxed Python solution
* **Full codebase ownership**, enabling bug fixes and customizations impossible in the original open-source library (including Hebrew language support)
* **A 20,000-line C++ library migrated to Go in 2 days**, with Claude Code generating Go assembly code as part of the process
* **20-30x estimated output multiplication** as the team integrates Claude Code across engineering workflows

## The challenge: Parsing PDF files at scale

Wiz's entire codebase is written in Go, a programming language known for its memory safety and security properties. But for one critical task—parsing PDF files—no adequate Go library existed. The PDF specification is decades old, with hundreds of different implementations across applications and devices, making comprehensive parsing extremely complex. As Liron Levin, a software engineer on the DSPM team, explained: “If you go to Reddit or any other blog, you will see tons of questions like ‘how do I solve this in Go?’ and they will tell you, you can’t.”

The only reliable solution was pypdf, a Python library with over 20 years of development and more than 50,000 lines of code. But running Python inside a Go environment meant wrapping it in a resource-intensive sandbox—essentially a mini virtual machine—that hurt performance and couldn’t run everywhere. Some environments used the sandboxed Python approach; others relied on incomplete Go packages. The result was inconsistency: different tools producing different results for the same file.

“We had a large discrepancy,” Levin said. “It made the code more complicated, and I never felt safe just running it. I wanted to fix this for two years, but the manual effort to port 50,000 lines of a 20-year-old Python library to Go would have taken two to three months of a highly specialized engineer's time. No product manager would ever prioritize that." The project stayed on the backlog.

## The solution: From experiment to production in 20 hours

The team’s initial use of Claude Code was simple: understand unfamiliar code faster. But within a short time, the use case expanded. They use it to review code, plan architecture, and get up to speed on codebases they’ve never touched.

When Levin evaluated tools for the migration project specifically, Claude Code’s contextual understanding was the differentiator. “Its problem-solving abilities are on another level compared to other tools,” he said.

Levin tried the migration on a Saturday. Within one hour of prompting, the basic functionality was working against hundreds of test PDFs. After roughly ten hours of iterative development, the new Go library handled all 500 of his pathological test cases. “I was amazed,” Levin said. “It reminds me of the best developer in the world.”

Claude Code migrated the 50,000-line Python library into an 18,413-line Go codebase in roughly 20 hours—10 hours of active development and 10 hours of testing. Liran Benodis, the DSPM team lead, put it simply: “This project would never have happened without Claude Code. The amount of effort and time that we would have needed to invest—we just wouldn’t do it.”

But migrating the code was only part of the challenge. When Levin deployed the new library to production with a feature flag, 99% of results matched the original—but the remaining 1% required debugging against real customer data. Since this sensitive data had to remain on-premises, Levin developed what his team calls 'polymorphic zero-knowledge debugging.' He would ask Claude Code to generate a diagnostic tool that extracts only structural, non-sensitive information about a problematic file, run that tool in a secure sandbox environment, and feed the redacted output back to Claude.

Through five to ten iterations per file, Claude could identify and fix bugs without ever seeing customer data. The team resolved 20 to 30 distinct issues this way.

## The results: Impact across the engineering organization

The new library was deployed to production within days and now processes PDFs at least 2x faster than the original Python implementation, while eliminating the resource-intensive sandboxing that had constrained the team. The partnership with Anthropic runs across several layers — the team uses Claude Code for engineering work, and Wiz’s broader AI platform (including its ASKI agentic platform and Mikaii assistant) is built on Claude models via Amazon Bedrock.

The migration gave the team full ownership of their PDF parsing for the first time. They consolidated fragmented implementations into a single codebase that runs consistently across all environments—CLI tools, cloud buckets, and virtual machines. For customers, this means consistent, faster scanning results regardless of where their files live, which is core to the DSPM promise. Issues that were previously unfixable in the open-source library, like inadequate Hebrew language support, could now be patched directly.

Levin then completed a second migration: converting fastText, a 20,000-line C++ data classification library, to Go in just two days—including Claude Code writing Go assembly code. The resulting 5,434 lines of verified Go code passed 100% of model validation tests. Across Wiz more broadly, the top 100 contributors have seen a 1.5x increase in merged PRs since adopting AI coding tools, with more than 90% of engineers now using Claude Code as part of their daily workflow.

“It enables us to do stuff that we wouldn’t even consider,” said Benodis. “Nowadays, when we’re planning our workload, we just multiply it. We can do 20 to 30 times the things we did before.”

Wiz’s engineers now consult Claude Code before reaching out to colleagues, use it to plan and execute new features, and review code with it as a standard part of their workflow. Some developers have moved away from traditional IDEs entirely, working primarily through Claude Code. The team has also built custom MCP connectors for their monitoring systems, enabling Claude Code to help detect and debug issues in production and test environments.

Benodis sees the current mission as embedding Claude Code into every part of the development process. The team is also building an agent powered by Claude that monitors code in production, detects bugs and anomalies, and surfaces issues before they escalate. Individual developers now run multiple Claude Code instances simultaneously, each working on separate features in parallel. “It can't get any better than this,” said Levin. “It makes things that were impossible, possible.”

‍

Claude Code on the web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69093b56f1035860a3cfe774_og_claude-code-on-the-web.jpg)

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Read more

[Read more](https://claude.com/blog/claude-code-on-the-web)Read more

Claude Code on the web

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code on the web

Delegate coding tasks directly from your browser. Kick off multiple sessions in parallel across repositories, with real-time progress tracking.

"This project would never have happened without Claude Code. The amount of effort and time that we would have needed to invest—we just wouldn’t do it.”

Liran Benodis

Team Lead, Data Security Posture Management, Wiz

Piloting Claude in Chrome

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69050ff880f9a5c13932b7df_og_claude-for-chrome.jpg)

We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

Piloting Claude in Chrome

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

Video caption

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Piloting Claude in Chrome

We're testing browser-based AI capabilities while building the safety measures needed for wider release. See how Claude works inside your browser.

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
