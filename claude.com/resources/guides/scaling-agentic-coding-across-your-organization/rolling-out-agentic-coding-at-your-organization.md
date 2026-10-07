<!-- source: https://claude.com/resources/guides/scaling-agentic-coding-across-your-organization/rolling-out-agentic-coding-at-your-organization -->

Chapter 035 min read

# Rolling out agentic coding at your organization

5 min read

32 min remaining

The most successful agentic coding rollouts follow a deliberate expansion strategy that builds expertise and enthusiasm organically. Here's what we've seen work:

### Start with power users

Begin with a pilot group of 20-50 developers who are already comfortable with AI-assisted tools. These aren't just your early adopters—they're your future agentic coding champions. Task them with:

* Ask them to spend time using Claude Code for common use cases. This is the best way to realize what customizations are useful and make sure the tool works well with your codebase.
* Creating custom slash commands in Claude Code tailored to your organization's codebase and standards, such as /migrate-db for database schema updates, /add-feature with company-specific boilerplate, and /fix-security for common vulnerability patches.
* Creating documentation files with your coding standards, outlining gotchas, and highlighting best practices via CLAUDE.md files, special files that Claude automatically pulls into context when starting a new conversation (Remember: take time to iterate on your CLAUDE.md files as you would any other agentic prompt. The devil is in the details!)
* Identifying repetitive coding workflows that Claude Code can automate by engaging with development teams, DevOps engineers, and technical leads across the organization to understand their pain points - such as boilerplate code generation, test suite creation, documentation updates, code refactoring tasks, API client generation, dependency updates, and routine bug fixes that consume significant developer time
* Establish a dedicated Slack or Teams channel for sharing best practices, troubleshooting issues, and broader discussion
* Build wrapper scripts to handle authentication for third-party tools, like AWS and GCP

For more tips, check out our [Eng Blog article (opens in new tab)](https://www.anthropic.com/engineering/claude-code-best-practices) on Claude Code best practices.

### Launch with a hackathon

Rather than a phased rollout that leaves teams waiting their turn, unite your organization with a kick-off hackathon. Your pilot users become mentors, sharing prompts and techniques while everyone learns together. This creates network effects that accelerate adoption and organic learnings. Bonus points if you order pizzas to stave off hunger and drive participation.

### Scale through internal expertise

As adoption grows, your pilot users evolve into internal consultants. Eventually, your organization will get to the place where they can run their own agentic coding workshops, with early adopters leading sessions and creating ongoing educational content inspired by their own learnings.

### Sharing CLAUDE.md files

CLAUDE.md files are an ideal place for documenting repository etiquette, developer environment setup, and any unexpected behaviors particular to a given project. However, the real power of CLAUDE.md files emerges when they're shared strategically across teams and organizations, creating a knowledge layer that scales AI-powered development. Here are some best practices for using them at scale:

**Create project-level CLAUDE.md files:** Name it CLAUDE.md and check it into git so that you can share it across sessions and with your team. This simple practice transforms individual Claude Code sessions into team-aligned development experiences.

**Commit to main branch:** Place CLAUDE.md in your repository root and commit it to your main branch. This ensures every developer who clones the repository automatically inherits the project's Claude Code configuration and context.

**Include in onboarding checklists:** Make reviewing and understanding the project's CLAUDE.md file part of your developer onboarding process. New team members should understand not just the codebase, but how Claude Code should be used within the project context.

**Version control like documentation:** Treat CLAUDE.md changes with the same rigor as documentation updates. Include updates in pull requests when architectural decisions change, new development patterns emerge, or team conventions evolve.

**Branch-specific variations:** For projects with significantly different development patterns across branches (feature branches, release branches), consider branch-specific CLAUDE.md content that reflects the current development focus.

See the appendix for an example project-level **CLAUDE.md** structure.
