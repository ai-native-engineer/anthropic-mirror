<!-- https://anthropic.skilljar.com/introduction-to-subagents/450699 -->

Claude Code comes with built-in subagents, but you can also create your own. Custom subagents specialize in specific tasks -- like reviewing code, writing tests, or checking documentation. They are defined as markdown files with YAML frontmatter that tell Claude when to use the subagent and how the subagent should behave.

## Creating a Subagent

The easiest way to create a subagent is with the `/agents` slash command. This opens the main interface for managing your subagents. From there, select **Create new agent**.

You will first be asked to choose the scope of your subagent:

* **Project-level** -- available only in the current project
* **User-level** -- shared across all projects on your machine

Next, you can choose how to create it. You can write the configuration manually, but the recommended approach is to let Claude generate it for you. Just describe what you want the subagent to do, and Claude will produce a name, description, and system prompt based on your input.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773974844%2Fsubagentsvideo2version3_04.1773974843174.png)  

## Customizing Tools

During creation, you get the chance to customize which tools the subagent can access. The tool categories include:

* Read-only tools
* Edit tools
* Execution tools
* MCP tools
* Other tools

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773974881%2Fsubagentsvideo2version3_06.1773974881320.png)  

Think about what your subagent actually needs. A code reviewer probably does not need edit tools -- it should read and analyze code, not change it. However, you might want to keep execution tools enabled so it can more easily identify pending changes.

## Choosing a Model and Color

After configuring tools, you select which Claude model powers the subagent. The model picker offers four options:

* **Haiku** -- best for fast, lightweight tasks
* **Sonnet** -- a good middle ground between speed and depth
* **Opus** -- best for complex analysis
* **Inherit** -- uses whatever model your main conversation is running

Finally, you pick a color. This shows up in the UI so you can quickly tell which subagent is active. It is a small touch, but it helps when you have multiple subagents running.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773974921%2Fsubagentsvideo2version3_07.1773974921584.png)  

## The Config File

Once creation is complete, the subagent config file is saved into your project (typically at `.claude/agents/your-agent-name.md`). Here is what a typical subagent config looks like:

  

```
--- name: code-quality-reviewer description: Use this agent when you need to review recently written or modified code for quality, security, and best practice compliance. tools: Bash, Glob, Grep, Read, WebFetch, WebSearch model: sonnet color: purple ---

You are an expert code reviewer specializing in quality assurance, security best practices, and adherence to project standards. Your role is to thoroughly examine recently written or modified code and identify issues that could impact reliability, security, maintainability, or performance.
```

Let's break down each field:

* **`name`** -- A unique identifier for the subagent. This is how you reference it, either by asking Claude directly or by typing `@agent code-quality-reviewer` in your message.
* **`description`** -- Controls when Claude decides to use the subagent. This must be a single line (use escaped newline characters `\n` if you need breaks). You can include example conversations here to help Claude understand when delegation is appropriate.
* **`tools`** -- Lists which tools the subagent can access. This matches whatever you selected during generation, but you can edit the list here at any time.
* **`model`** -- Specifies which Claude model to use: `sonnet`, `opus`, `haiku`, or `inherit`.
* **`color`** -- The UI color for identifying the subagent.

## System Prompts

The body of the markdown file (everything below the YAML frontmatter) is the system prompt. This is where you give the subagent its instructions: what it should focus on, how it should analyze things, and how it should report findings back to the main agent.

A well-written system prompt is the difference between a useful subagent and one that misses the point. Be specific about what the subagent should look for and how it should structure its output.

## Making Claude Use Your Subagent Automatically

If you want Claude to delegate tasks to the subagent without you explicitly asking, include the word **"proactively"** in the description field. For example:

```
description: Proactively suggest running this agent after major code changes...
```

You can also add example conversations to the description to help Claude understand specific scenarios where the subagent should be used. The more concrete your examples, the better Claude gets at knowing when to delegate.

## Testing Your Subagent

After creating your subagent, test it by making some code changes and asking Claude to review them.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1773974991%2Fsubagentsvideo2version3_14.1773974991791.png)  

If the subagent is not being used when you expect it to be, go back and check the description. Adding more specific examples and trigger scenarios helps Claude understand when to delegate work to your subagent.
