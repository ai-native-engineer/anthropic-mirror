<!-- source: https://claude.com/plugins/ralph-loop -->

# Ralph Loop

Interactive AI loops for iterative development using the Ralph Wiggum technique: Claude works on tasks repeatedly, seeing prior work until completion.

* Anthropic Verified
* Install in

  [Claude Code](#)

  [Anthropic](https://anthropic.com)
* Installs

  184186

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Ralph Loop enables iterative, self-referential AI development loops where Claude works on the same task repeatedly until completion. The plugin intercepts session exits via a stop hook and automatically re-feeds your prompt while preserving all file modifications and git history between iterations. This creates autonomous improvement cycles where Claude can refine its work based on test failures and previous attempts.

The technique is ideal for well-defined projects with clear success criteria, greenfield development with automated verification, and any task amenable to iterative refinement. Claude reads its own past work to inform improvements, creating a powerful feedback loop for autonomous problem-solving.

**How to use:** Start an iterative session with `/ralph-loop "your prompt here" --max-iterations 10 --completion-promise "DONE"`. The loop continues until Claude outputs the completion promise or reaches the iteration limit. Cancel anytime with `/cancel-ralph`. Write prompts with explicit completion criteria and success metrics for best results.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
