<!-- https://anthropic.skilljar.com/introduction-to-subagents/450698 -->

Subagents are specialized assistants that Claude Code can delegate tasks to. Think of them as focused helpers: each one runs in its own conversation context window, does its work, and returns a summary to the main thread. The intermediate steps -- all the file reads, searches, and tool calls -- stay isolated and never clutter your main conversation.

## Why Subagents Matter

Every time you chat with Claude Code, you're adding to the main context window. Every tool call, every file read, every search result gets stored there. That space is finite, and once it fills up, Claude starts losing track of earlier parts of the conversation.

  

Subagents solve this by spinning up a separate context window. The subagent receives two things:

* **A custom system prompt** from your configuration file that defines the subagent's role and behavior
* **A task description** written by the parent agent based on what you asked for

The subagent then works on its own. It reads files, runs searches, edits code -- whatever it needs to do. When it's done, only a summary comes back to your main conversation. The entire subagent conversation is then discarded.

This means your main context stays clean. You get the answer without all the noise of the journey it took to find it. The tradeoff is that you lose visibility into how the subagent reached its conclusions.

## A Practical Example

Say you're exploring an unfamiliar codebase and you want to know which service handles refunds. Without a subagent, Claude might read 15 files, run several searches, and trace through multiple function calls. All of that fills your context window, even though you only needed one fact.

With a subagent, the experience is much cleaner. You ask the question, the Explore subagent spins up, does all that digging in its own context, and hands back a focused answer.

Your main context window only records the question and the summary -- not the 15 files that were read along the way.

## Built-in Subagents

Claude Code ships with several built-in subagents you can use right away:

* **General purpose subagent** -- for multi-step tasks that require both exploration and action
* **Explore** -- for fast searching and navigation of codebases
* **Plan** -- used during plan mode for research and analysis of your codebase before presenting a plan

## Custom Subagents

Beyond the built-in options, you can create your own subagents with custom system prompts and tool access. This lets you define specialized agents tailored to your workflow -- a code reviewer, a test writer, a documentation generator, or anything else you need.

## Key Takeaways

Subagents give you three main benefits:

* They break work into focused pieces, letting each subagent concentrate on a specific task
* They keep your main context window clean by isolating all the intermediate work
* They bring back just the information you need as a concise summary

Whether you're using the built-in subagents or creating your own, they're a practical way to get more out of longer Claude Code sessions. The less noise in your main context, the longer and more effectively you can work.

<!-- youtube: jKErNxuxPXg -->

[![What Are Subagents](https://img.youtube.com/vi/jKErNxuxPXg/hqdefault.jpg)](https://www.youtube.com/watch?v=jKErNxuxPXg)

<details>
<summary>자막: What Are Subagents</summary>

Sub-agents are specialized assistants that Claude can delegate tasks to. Each sub-agent runs in its own conversation contacts window with a custom system prompt that you define. When finished, it returns a summary to the main thread while all the intermediate work stays isolated. One of the main advantages of sub-agents is that they help manage context window usage. When you chat with Claude Code, you're adding context to the main context window. Every tool call and its results get stored in this main context window. And so, when Claude uses a sub-agent, a separate window starts. The sub-agent receives two inputs, a custom system prompt from your configuration file, and a task description written by the parent or parent agent based on what you ask for. The sub-agent then works autonomously. When it reads files, edits files, or uses tools, none of these will appear in the main conversation. Just a summary is returned back. The entire sub-agent conversation then gets completely discarded. Consider a task like investigating how the payment system works in an unfamiliar code base. Maybe you're trying to use Claude Code to figure out which service handles refunds. Well, without a sub-agent, Claude might read 15 files, run several searches, and trace through multiple function calls. All of that context fills your context window, even if you only needed one single fact, which service handles refunds. With a sub-agent, you get the answer without the journey. The sub-agent explores, discovers the answer, and returns a focused summary, keeping your main context clean. But, the main window loses visibility into how the sub-agent reaches its conclusions and what it discovered along the way. Claude Code includes several built-in sub-agents that you can use immediately, like the general-purpose sub-agent, used for multi-step tasks that require both exploration and action. The explore sub-agent, used for fast searching of code bases. The plan sub-agent, used during plan mode for research and analysis of your code base before presenting a plan. And you can also create your own sub-agents with custom system prompts and tool access. Sub-agents like Claude Code break work into focused pieces, keep your main context window clean, and bring back just what you need, whether you're using the built-in ones or creating your own. They're a practical way to get more out of longer Claude Code sessions.

</details>
