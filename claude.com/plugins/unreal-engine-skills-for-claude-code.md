<!-- source: https://claude.com/plugins/unreal-engine-skills-for-claude-code -->

# Unreal Engine MCP

Control Unreal Editor via Claude Code MCP. Hundreds of tools across 30+ toolsets: actors, blueprints, Niagara, etc.

  [Epic Games](https://github.com/EpicGames)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Control Unreal Editor directly from Claude Code through the Model Context Protocol. This plugin exposes hundreds of tools across 30+ toolsets via Unreal's ToolsetRegistry, letting you spawn actors, edit blueprints, author materials, build UI widgets, script Sequencer animations, configure Niagara VFX, set up Control Rigs, wire up Gameplay Ability System logic, run automation tests, and much more — all without leaving your terminal.

The plugin uses a three-step discover-and-dispatch workflow: it lists available toolsets, describes their schemas, then invokes tools with validated arguments. A SessionStart hook auto-detects Unreal projects (including engine source trees) and injects the right context so Claude defaults to UE conventions like UObject patterns, Slate UI, and UHT reflection. Built-in safety rules enforce save-before-and-after for bulk changes, serial execution to avoid game-thread deadlocks, and compilation wait guards.

**How to use:** Make sure the ModelContextProtocol and AllToolsets plugins are enabled in Unreal Editor, then start the MCP server with `ModelContextProtocol.StartServer` in the console. Once connected, ask Claude to work on your Unreal project naturally — for example: "Spawn a BP\_Enemy at the player start location," "Create a new material instance from M\_Base with roughness set to 0.3," "Add a Niagara emitter to the campfire actor," "Set up a montage in Sequencer for the intro cutscene," or "Run the automation tests for the inventory system." The plugin also supports project-specific Agent Skills that override defaults for custom studio workflows.
