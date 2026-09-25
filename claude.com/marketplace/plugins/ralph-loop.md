<!-- source: https://claude.com/marketplace/plugins/ralph-loop -->

Ralph Loop enables iterative, self-referential AI development loops where Claude works on the same task repeatedly until completion. The plugin intercepts session exits via a stop hook and automatically re-feeds your prompt while preserving all file modifications and git history between iterations. This creates autonomous improvement cycles where Claude can refine its work based on test failures and previous attempts.

The technique is ideal for well-defined projects with clear success criteria, greenfield development with automated verification, and any task amenable to iterative refinement. Claude reads its own past work to inform improvements, creating a powerful feedback loop for autonomous problem-solving.

**How to use:** Start an iterative session with `/ralph-loop "your prompt here" --max-iterations 10 --completion-promise "DONE"`. The loop continues until Claude outputs the completion promise or reaches the iteration limit. Cancel anytime with `/cancel-ralph`. Write prompts with explicit completion criteria and success metrics for best results.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
