<!-- source: https://claude.com/plugins/unreal-engine-skills-for-claude-code -->

# Unreal Engine MCP

Control Unreal Editor via Claude Code MCP. Hundreds of tools across 30+ toolsets: actors, blueprints, Niagara, etc.

* Install in

  [Claude Code](#)
* Made by

  [Epic Games](https://github.com/EpicGames)
* Installs

  871

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Control Unreal Editor directly from Claude Code through the Model Context Protocol. This plugin exposes hundreds of tools across 30+ toolsets via Unreal's ToolsetRegistry, letting you spawn actors, edit blueprints, author materials, build UI widgets, script Sequencer animations, configure Niagara VFX, set up Control Rigs, wire up Gameplay Ability System logic, run automation tests, and much more — all without leaving your terminal.

The plugin uses a three-step discover-and-dispatch workflow: it lists available toolsets, describes their schemas, then invokes tools with validated arguments. A SessionStart hook auto-detects Unreal projects (including engine source trees) and injects the right context so Claude defaults to UE conventions like UObject patterns, Slate UI, and UHT reflection. Built-in safety rules enforce save-before-and-after for bulk changes, serial execution to avoid game-thread deadlocks, and compilation wait guards.

**How to use:** Make sure the ModelContextProtocol and AllToolsets plugins are enabled in Unreal Editor, then start the MCP server with `ModelContextProtocol.StartServer` in the console. Once connected, ask Claude to work on your Unreal project naturally — for example: "Spawn a BP\_Enemy at the player start location," "Create a new material instance from M\_Base with roughness set to 0.3," "Add a Niagara emitter to the campfire actor," "Set up a montage in Sequencer for the intro cutscene," or "Run the automation tests for the inventory system." The plugin also supports project-specific Agent Skills that override defaults for custom studio workflows.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1134112

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

1009371

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

438525

installs](https://claude.com/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

417801

installs](https://claude.com/plugins/context7)
