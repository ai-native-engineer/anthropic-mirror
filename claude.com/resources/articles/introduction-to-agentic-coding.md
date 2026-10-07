<!-- source: https://claude.com/resources/articles/introduction-to-agentic-coding -->

AI-assisted coding has evolved rapidly over the last few years. Tools that once suggested the next line now predict entire functions by analyzing patterns in your code.

The latest evolution takes this further: instead of predicting what you'll type next, these systems autonomously execute multi-step development tasks by reading files across your codebase, running tests, and iterating until your goal is complete.

## What is agentic coding?

Agentic coding shifts AI from autocomplete to autonomous task executor. Traditional coding assistants wait for you to type each line and suggest what comes next. Agentic systems take a high-level goal, break it into discrete steps, execute those steps independently, and adjust their approach based on feedback from your environment.

The key distinction lies in autonomy and scope. Traditional AI tools analyze code visible in your editor and suggest the next fragment. Agentic coding tools read entire codebases, understand file relationships across directories, execute commands to verify changes work, and iterate until tests pass and requirements are met. This autonomy extends across the development cycle, with each step happening without requiring you to manually orchestrate the workflow.

## How AI coding tools have evolved

### Code prediction and completion

Tools like IDE autocomplete extensions analyze code visible in your editor to predict what you might type next. These systems excel at repetitive patterns like generating REST endpoint boilerplate, creating test structures following established conventions, and implementing common algorithms.

The prediction model considers your immediate context. When you write a function signature, the tool suggests an implementation based on the function name, parameter types, and surrounding code. When you start typing an import statement, it recommends packages based on what's already imported and common usage patterns.

The limitation lies in scope. Autocomplete tools work with limited context windows, typically analyzing only your current file or a small number of nearby files. They can't trace data flow through your application architecture or understand how changes in one service affect dependent services.

### Conversational AI chat interfaces

Browser-based coding assistants like Claude.ai added conversational capabilities to AI coding tools. Instead of suggesting code as you type, these tools engage in conversation about your code problems through analyzing pasted snippets, bug descriptions, and optimization questions.

These interfaces excel at analysis and guidance. Paste a slow database query to get optimization recommendations. Describe an architectural decision to receive trade-off analysis. Share an error message to explore troubleshooting approaches.

The conversational format supports iterative refinement. You ask a general question, receive an initial response, clarify your requirements based on that response, and progressively narrow toward a specific solution. This back-and-forth works well when problems aren't fully defined or when you need to explore different approaches before committing to implementation.

This becomes impractical for tasks involving multiple files. Refactoring a module imported by thirty other files means pasting each file into the chat, manually tracking which files need updates, copying suggested changes back to each file, and ensuring consistency across all modifications. Chat interfaces provide guidance, but orchestrating implementation remains manual. This is the gap that agentic coding systems are designed to fill.

## How agentic coding works

### Context gathering and planning

Agentic coding systems operate at the project level rather than the file level. When you provide a goal, the system analyzes the relevant context needed to accomplish it by reading configuration files to understand your project setup, examining test files to see existing coverage patterns, and tracing imports to map dependencies between modules.

The system then creates a plan for accomplishing the goal. This isn't a static list but an adaptive approach that evolves as the system gathers more information. If your goal is "add authentication to the API," the plan might start with analyzing existing route definitions, identifying which endpoints need protection, checking whether authentication middleware already exists, and determining where user session management should be implemented.

### Implementation and coordination

The implementation phase involves reading and writing files across your codebase. Unlike autocomplete tools that suggest changes within a single file, agentic systems modify multiple related files to maintain consistency. Adding authentication might require updating route handlers, creating middleware functions, modifying database schemas, adjusting API client code, updating documentation, and adding test coverage across all these changes.

This autonomous workflow transforms development from "write code, run tests, read errors, fix code, repeat" into "define goal, review proposed changes, approve implementation." You maintain control by reviewing plans and approving file changes while the system handles the iterative debugging cycle, research into existing code patterns, and coordination of changes across multiple files.

## Agentic coding with Claude Code

[**Claude Code**](https://claude.com/product/claude-code) brings agentic capabilities to your terminal environment. Unlike browser-based tools requiring constant code copying or IDE extensions analyzing only visible files, Claude Code operates directly within your project directory with full access to your codebase.

![](https://assets.claude.com/28bee07bc13c3fd99bca98a1a6f9b3342f142c5f.png)

### Installation and launch

Install Claude Code in your terminal:

Copy

```
npm install -g @anthropic-ai/claude-code
```

Then launch it in your project directory to start coding:

Copy

```
claude
```

### How Claude Code works

Claude Code reads your entire project context upon request. When you ask about architecture or request changes, it analyzes file structures, understands dependencies declared in package.json or requirements.txt, traces how modules interact, and identifies existing patterns established across your codebase.

Multi-file operations become straightforward. Request "refactor this callback-based code to use async/await," and Claude Code identifies all files using the callback pattern, updates each with async/await syntax, modifies error handling to use try/catch blocks, updates related tests to handle async patterns, and verifies your entire test suite still passes.

### File system access and permissions

File system access enables workflows that web-based tools can't handle. Claude Code creates new files with appropriate naming conventions, organizes code into logical directory structures, updates configuration files when adding dependencies, and maintains consistency with your existing project organization patterns.

The permission model ensures you maintain control. By default, Claude Code requests approval before modifying files and shows exactly what changes it plans to make. You review the proposed modifications, approve changes you agree with, and request revisions for changes that don't meet requirements.

### Integration with development workflows

Integration with your development workflows means Claude Code interacts with tools you already use. It runs npm commands to install dependencies, executes test runners like Jest or pytest, uses Git for commits and branching, and starts development servers to verify changes work in running applications.

You can extend these capabilities further by connecting Model Context Protocol (MCP) servers, which provide Claude Code with comprehensive context from additional tools and systems across your development environment.

## Real-world applications

### Rakuten's seven-hour autonomous implementation

[Rakuten's](https://www.claude.com/customers/rakuten) engineering team challenged Claude Code's agentic capabilities with implementing a specific activation vector extraction method in vLLM, an open-source library containing 12.5 million lines of code across Python, C++, and CUDA. Claude Code completed the entire implementation in seven hours of sustained autonomous work.

> “"I didn't write any code during those seven hours, I just provided occasional guidance"”

- Kenta Naruse, Machine Learning Engineer at Rakuten

The final implementation achieved 99.9% numerical accuracy compared to the reference method, demonstrating the system's ability to understand complex, multi-language codebases, plan implementation approaches for sophisticated algorithms, and deliver production-quality results.

**Rakuten's transformation metrics:**

* **79% faster** feature delivery (24 days → 5 days)
* **7-hour** autonomous implementations with minimal human intervention
* **99.9%** accuracy on complex algorithmic refactoring
* **5x** parallel task execution capacity for engineering teams

As Yusuke Kaji, General Manager of AI for Business at Rakuten, explained: "You can have five tasks running in parallel by delegating four to Claude Code while focusing on the remaining one."

## Getting started with Claude Code

After installing [Claude Code](https://claude.com/product/claude-code) with npm, navigate to a project directory and start a session:

Copy

```
claude
```

Experiment with a few different tasks to see how Claude Code understands your codebase.

### Understand project architecture

Copy

```
Explain the structure of this codebase and how the main components interact
```

Claude Code reads your files and provides an architectural overview, helping you or new team members understand project organization.

### Analyze code quality

Copy

```
Review the authentication module for potential security issues
```

Claude Code examines the relevant code, identifies concerns like exposed credentials or insufficient validation, and suggests specific improvements.

### Debug and fix errors

Copy

```
Find all N+1 query problems in our GraphQL resolvers and implement DataLoader batching
```

Claude Code analyzes your entire codebase, identifies specific ORM patterns causing N+1 problems, and implements a fix.

![](https://assets.claude.com/7e07257129d4da98f2d7d472c40cbb422e100c3d.png)

## Start slow, then expand

As you work with Claude Code, you develop intuition for which tasks benefit most from autonomous execution versus tasks better handled with traditional development tools. Some immediate applications that provide quick wins include:

* **Test automation** for your uncovered code paths
* **Documentation generation** for your legacy systems
* **Routine refactoring** of your technical debt
* **Feature implementation** for well-understood requirements

Each interaction provides an opportunity to learn how Claude Code approaches problems within your specific codebase. Get started with [Claude Code](https://claude.com/product/claude-code) or visit our [docs](https://docs.claude.com/en/docs/claude-code/overview) to learn more.

## FAQ

What's the difference between agentic coding and traditional AI coding assistants?

Traditional AI coding tools suggest individual functions or code snippets based on immediate context. You handle integration, testing, and ensuring the code follows your project conventions.

Agentic coding tools understand your entire project, plan implementation approaches, and execute complete workflows autonomously. They deliver tested, integrated features that follow your established patterns.

‍

How long can agentic coding tools work autonomously?

Agentic coding tools like Claude Code can work for extended periods maintaining context and building on previous work. Rakuten's seven-hour autonomous refactoring session demonstrates sustained technical work without human intervention. The duration depends on your task complexity and project requirements.

Do I need to change my development workflow to use agentic coding?

[Claude Code](https://claude.com/product/claude-code) integrates with your existing development workflows through terminal integration. You can incorporate it into your current practices gradually, starting with specific tasks like testing or documentation before expanding to complete feature development.

What types of projects work best with agentic coding?

Agentic coding works across project types and languages. It's particularly valuable for projects with established patterns and conventions, complex integration requirements, or routine development tasks that consume significant time.

Your TypeScript/JavaScript, Python, Go, and Rust projects see immediate benefits, but [Claude Code](https://claude.com/product/claude-code) supports all major languages and frameworks.

‍

How does agentic coding handle project-specific requirements?

Claude Code uses **CLAUDE.md** configuration files that document your coding standards, architectural decisions, and project-specific requirements. These files persist across your sessions, ensuring consistent implementations that follow your established practices.

[ArticleSep 24, 2026

### Coding sessions are longer and use more context. Claude Opus 5.5 is built with that in mind.

Our latest Opus model is priced and trained to optimize costs for how developers code now.

Claude CodeClaude Enterprise](https://claude.com/resources/articles/claude-opus-5-5-built-for-coding-sessions-that-use-more-context)[ArticleSep 14, 2026

### Agentic coding is straining CI. Here’s how we scaled test impact analysis at Anthropic

Our CI job volume increased 25x over 6 months. We patched our test selection service three times before finding a sustainable solution.

Claude CodeClaude Enterprise1 more: Claude TagClaude Tag](https://claude.com/resources/articles/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic)[ArticleAug 24, 2026

### How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

Adam Ward, on Anthropic’s marketing team, shares how he uses Claude to turn one weekly sales report into a personalized Monday briefing for every account executive he supports.

Claude Code](https://claude.com/resources/articles/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep)[ArticleAug 20, 2026

### The Claude Code guide for startups

How fast-growing startups use Claude Code to ship—five operating principles drawn from interviews with more than a dozen companies.

Claude Code](https://claude.com/resources/articles/claude-code-guide-for-startups)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
