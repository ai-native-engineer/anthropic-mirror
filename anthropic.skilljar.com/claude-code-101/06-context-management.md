<!-- https://anthropic.skilljar.com/claude-code-101/469793 -->

### Video



### Context Management

Context is Claude's working memory. Every file it reads, every command it runs, every message you send — it all takes up space in the context window.

## What is the Context Window?

Think of the context window as the amount of space Claude can hold in its memory. Whenever you enter a prompt, Claude reads a file, runs a tool call, or receives a tool call result, it's all adding to the context window. Since there's a finite amount of space, it becomes important to optimize how you use it.

![Diagram showing the context window as a grid of tokens — some taken, most available](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686395%2Fvideo6contextwindowdiagram.1775686395676.jpg)

## What Happens When Context Fills Up

When you approach the limit, the context window is automatically **compacted**. Compaction summarizes important details and removes unnecessary tool call results to free up space. Note that this process can potentially lose details.

![Claude Code showing 'Compacting conversation...' as it summarizes the context](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686393%2Fvideo6compactingcontext.1775686393619.jpg) ![Claude Code displaying a compact summary of the previous conversation including key technical concepts and files](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686394%2Fvideo6compactingsummary.1775686394575.jpg)

## Commands

You can run compaction manually with the `/compact` command. This compacts everything up to that point. It's handy when you want to free up context space while keeping a memory of what you previously worked on.

![The /compact command in Claude Code's autocomplete menu](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686393%2Fvideo6compactcommand.1775686392964.jpg)

If you want to completely start from scratch with no memory of the previous session, run `/clear`. This removes everything.

![Running /clear in Claude Code to start a fresh session](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686392%2Fvideo6clearcommand.1775686392379.jpg)

To check the state of your context, run the `/context` command. You'll get a high-level overview of your context size, the categories taking up the most space, and a visual graphic showing the breakdown.

![Output of the /context command showing context usage breakdown with a visual bar chart](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686364%2FVideo_2_01_01_11_11.1775686364258.jpg)

## When to Use Which

A general rule of thumb:

* **Use `/compact`** when you're working on a specific feature and running up against the context limit but need to continue. Keeping the context relevant to your current feature is important.
* **Use `/clear`** when you want to start a new feature. You don't want the previous conversation to introduce bias into something new. For things you want Claude to remember across sessions, put them in your CLAUDE.md file so it doesn't have to rediscover things from scratch.   
    
  ![A CLAUDE.md file with commands, important notes, and architecture sections](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686391%2Fvideo6claudemdfile.1775686391669.jpg)

## Tips for Saving Context Space

**Be specific.** A vague prompt might seem smaller, but it actually costs more context in the long run. Without clear instructions, Claude is forced to explore your codebase more and do its own reasoning — which takes up far more context space than a detailed prompt would.

**Manage your MCP servers.** MCP servers load all of their available tools into context by default, even when you're not using them. If you have servers configured for things unrelated to the current project, consider turning them off. You can also try "Skills," which work similarly to MCP servers but don't load everything into context upfront.

**Use subagents.** Subagents run in parallel with your main agent but have a completely separate context window. For tasks where you only need the answer — like "where are the authentication endpoints located?" — a subagent does the work and returns just a summary to your main agent, keeping your primary context clean.

  

## Recap

Managing context within Claude Code is crucial. Use `/compact` to summarize long sessions and `/clear` to start fresh. To use your context window effectively: be specific with your prompts, check what's consuming your current context, and use subagents to delegate tasks where you only need the result.
<!-- youtube: eW3oTyfeWZ0 -->

# Context management

[![Context management](https://img.youtube.com/vi/eW3oTyfeWZ0/hqdefault.jpg)](https://www.youtube.com/watch?v=eW3oTyfeWZ0)

<details>
<summary>자막: Context management</summary>

Context is Claude's working memory. Every file it reads, every command it runs, every message you send, it all takes up space in the context window. Think of the context window as the amount of space that Claude can hold in its memory. Whenever you enter a prompt, Claude reads a file, runs a tool call, gets a tool call result. This is added onto the context window. And since there's only a finite amount you can can put in the context window, it becomes extremely important to optimize this as much as possible. Now, when you approach this limit, the context window is automatically compacted. Compaction will summarize important details and remove the unnecessary tool call results and free up a lot of space in your context window. Do note though that this could potentially lose details in your previous conversation. You can run the compaction manually as well with the {slash} compact command. This will compact everything that you've done up to that point, which could be handy if you want to clear up context space, but also have a memory of what you previously worked on. If you want to completely start from scratch without memory of what was previously worked on, you can also run {slash} clear and that will remove everything, starting from scratch. To check the state of your context, run the {slash} context command. Here, you'll get a big picture of how large your context size is, the different categories that are taking up the most context, and a graphic showing you all of this. A general rule of thumb is when you're working on a specific feature and are going over the context window, but need to continue, then compact. Keeping the context relevant for this feature is important when continuing development. If you have finished the plan and want to start on a new feature, then clear. You don't want the previous conversation to present bias in anything new that you want to create. For things that you do want Claude to remember in other sessions, put it in the Claude.md file. That way, it doesn't have to rediscover things from scratch all over again. Be specific. The irony behind writing a smaller prompt is that it in the long run, it will take up more context. Without being explicit, Claude is forced to look around your code base more and do his own thinking, which takes up a lot more context window space than if you were just a little bit more clear with a sentence or two. MCP servers load all of the tools available into context by default. So, if you have a lot of MCP servers for things that are unrelated to the project, it might be worth turning them off. You can also try out skills, which works similarly to MCP servers, but doesn't put the entire thing into context, saving you space. Sub agents run in parallel with your main agent, but has a complete separate context window. So, for tasks that require an answer without the journey, like where is the authentication endpoints located, you can have the sub agent do the work and return just a summary to your main agent. Managing context within Claude code is crucial. Use /compact to summarize long sessions and /clear to start fresh. To use your context window effectively, be specific with what you want.
>> [music]
>> Check what's using your current context
window and use sub agents to delegate tasks you only need the answer for.

</details>
