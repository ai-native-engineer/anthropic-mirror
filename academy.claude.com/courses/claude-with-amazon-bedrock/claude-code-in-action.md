<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/claude-code-in-action -->

Lesson 59 of 65 · Claude with Amazon BedrockClaude Code in action

Claude Code isn't just a tool for writing code - it's designed to be your coding partner throughout an entire project lifecycle. From initial setup to deployment and maintenance, Claude can help with every step of software development.

![](https://academy.claude.com/assets/media/a7b4baf081b4100802708298bce2a0481adf57c1f574f05da55b83aa84a4aeea.png)

## The /init Command

When starting with a new project, the `/init` command is your first step. Claude Code will scan your codebase, noting project structure, dependencies, commands, and coding patterns. The findings get summarized in a `CLAUDE.md` file that Claude automatically reads in future conversations.

![](https://academy.claude.com/assets/media/022421e70b704c6878a51be989beb0b14a687266cbd3a9ce2aaf2ce62d8abbb3.png)

You can have multiple CLAUDE.md files for different scopes:

* **Project** - checked into git, shared between engineers
* **Local** - not checked into git, your particular notes to Claude
* **User** - used across all projects

When running `/init`, you can add special directions for areas you want Claude to focus on. You can also use the `#` shortcut to add quick notes that get appended to your CLAUDE.md file.

## Common Workflows

Claude works best as an effort multiplier. The more context and structure you provide, the better results you'll get. Here are two effective approaches:

![](https://academy.claude.com/assets/media/4f24df4e60bfce37882a7a719d234680bd3a163bb236186f07fecdad1f2438ed.png)

### Planning-First Workflow

This three-step approach works well for complex features:

1. **Feed context into Claude** - Find files relevant to your feature and ask Claude to read them
2. **Tell Claude to plan a solution** - Describe what you want built, but specifically ask Claude not to write code yet
3. **Ask Claude to implement the solution** - Once you have a solid plan, Claude can write code based on the context and planning it already completed

For example, when building a document conversion tool, you might first ask Claude to examine existing tool examples and helper functions. Then ask it to plan out the implementation steps. Finally, request the actual code implementation.

### Test-Driven Development Workflow

![](https://academy.claude.com/assets/media/69c44a8412c3ec8155606d3f9bf3f4c66b5b7f5bc0b5f2e1483f2624c0ed8a6f.png)

This approach requires more upfront effort but dramatically increases Claude's effectiveness:

1. **Feed context into Claude** - Share relevant files for your feature
2. **Ask Claude to think of test cases** - Tell Claude specifically not to write any code yet
3. **Ask Claude to implement those tests** - Select only the tests that look relevant to your feature
4. **Ask Claude to write code that passes the tests** - Claude will iterate on a solution until the tests pass

This workflow helps ensure your code is robust and handles edge cases you might not have considered initially.

## Practical Tips

Claude can handle routine development tasks beyond just writing code. You can ask it to:

* Set up project environments and install dependencies
* Stage and commit changes with descriptive commit messages
* Run test suites and interpret results
* Clear conversation history with `/clear` to reset context

Remember that Claude Code reads your CLAUDE.md file automatically, so any coding standards, project-specific notes, or architectural decisions you document there will influence all future interactions. This makes Claude increasingly effective as it learns more about your project's patterns and requirements.
