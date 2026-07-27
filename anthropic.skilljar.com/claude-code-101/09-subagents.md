<!-- https://anthropic.skilljar.com/claude-code-101/469796 -->

### Video



### Subagents

Claude can delegate tasks to subagents that break them down and run component tasks in parallel, improving your context management. Each subagent operates in its own isolated context window.

## How It Works

Managing context in Claude Code is important. A lot of the context window gets consumed by things like tool calls exploring your codebase or running web searches for research. What Claude discovers during that exploration isn't always relevant to the main feature you're developing.

This is where subagents come in. Claude spawns a subagent to handle a task like "explore this codebase for me." The subagent runs in parallel with its own context window, does all the exploration work, and once finished, summarizes its findings and returns that summary back to Claude.

The result: you get the answer you were looking for, without the entire journey it took to get there cluttering your main context.

## Creating Your Own Subagent

Subagents are defined in Markdown files with YAML frontmatter. The easiest way to get started is to let Claude generate one for you. Run:

```
/agents
```

Then select "Create new agent." You'll walk through steps including choosing the scope of the agent, defining its purpose, selecting the tools it has access to, and even picking a color for it.

Claude will generate a name, description, and prompt for the subagent. This also tells Claude when to call the subagent based on the prompts you give it.

## Further Customization

Subagents can be customized further. Here are some highlights:

* **Persistent memory** lets your subagent retain memory across conversations. This is great if you're using it consistently on the same projects.
* **Preload skills** into subagents by adding the `skill` key and listing skills by name. Note that unlike skills in your main conversation, the entire skill is loaded into context here.

## Recap

Keeping your context window clean is one of the best ways to stay productive with Claude Code. With subagents, you can run an agent in the background to handle the heavy lifting and return just the answer to your main context window.

**Want to go deeper?** Check out our dedicated course: [Introduction to subagents](https://anthropic.skilljar.com/introduction-to-subagents)
<!-- youtube: jKErNxuxPXg -->

# Subagents

[![Subagents](https://img.youtube.com/vi/jKErNxuxPXg/hqdefault.jpg)](https://www.youtube.com/watch?v=jKErNxuxPXg)

<details>
<summary>자막: Subagents</summary>

Sub-agents are specialized assistants that Claude can delegate tasks to. Each sub-agent runs in its own conversation contacts window with a custom system prompt that you define. When finished, it returns a summary to the main thread while all the intermediate work stays isolated. One of the main advantages of sub-agents is that they help manage context window usage. When you chat with Claude Code, you're adding context to the main context window. Every tool call and its results get stored in this main context window. And so, when Claude uses a sub-agent, a separate window starts. The sub-agent receives two inputs, a custom system prompt from your configuration file, and a task description written by the parent or parent agent based on what you ask for. The sub-agent then works autonomously. When it reads files, edits files, or uses tools, none of these will appear in the main conversation. Just a summary is returned back. The entire sub-agent conversation then gets completely discarded. Consider a task like investigating how the payment system works in an unfamiliar code base. Maybe you're trying to use Claude Code to figure out which service handles refunds. Well, without a sub-agent, Claude might read 15 files, run several searches, and trace through multiple function calls. All of that context fills your context window, even if you only needed one single fact, which service handles refunds. With a sub-agent, you get the answer without the journey. The sub-agent explores, discovers the answer, and returns a focused summary, keeping your main context clean. But, the main window loses visibility into how the sub-agent reaches its conclusions and what it discovered along the way. Claude Code includes several built-in sub-agents that you can use immediately, like the general-purpose sub-agent, used for multi-step tasks that require both exploration and action. The explore sub-agent, used for fast searching of code bases. The plan sub-agent, used during plan mode for research and analysis of your code base before presenting a plan. And you can also create your own sub-agents with custom system prompts and tool access. Sub-agents like Claude Code break work into focused pieces, keep your main context window clean, and bring back just what you need, whether you're using the built-in ones or creating your own. They're a practical way to get more out of longer Claude Code sessions.

</details>
