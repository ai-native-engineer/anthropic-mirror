<!-- https://anthropic.skilljar.com/claude-code-101/469797 -->

### Video



### MCP

Model Context Protocol (MCP) is an open standard that lets Claude Code connect to external tools and data sources. When you ask a question, Claude automatically understands when it should use those tools to better handle your query.

A lot of your context lives outside your codebase — in databases, productivity apps, or public repositories. MCP bridges that gap.

## What Can You Do With It?

First, it's important to understand the concept of "tools" in agentic AI. Tools give agents like Claude Code the ability to perform actions that help them complete tasks more effectively. This is different from typical AI, where you just get a text response back.

For example, if your team uses Linear for project management, you can add a Linear MCP server to bring in the details of your specific issues. If you need up-to-date documentation for a dependency, a docs MCP server like Context7 can provide that to Claude Code.

![Claude Code querying a Linear MCP server to retrieve issue details for ticket MEN-12](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686373%2Fvideo10linearmcp.1775686373076.jpg)
![Claude Code using the Context7 MCP server to look up the latest shadcn/ui documentation](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686372%2Fvideo10context7mcp.1775686371940.jpg)

## Adding an MCP Server

You can add MCP servers with the `claude mcp add` command. There are two main types:

![Running claude mcp add to add an HTTP Linear MCP server from the terminal](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686371%2Fvideo10claudemcpaddcommand.1775686370957.jpg)

* **HTTP servers** are for remote services. These are hosted by the service provider and connect over the network.
* **Stdio servers** are for local processes that run on your machine.

![Running claude mcp add to add a local stdio MCP server with a Python script](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686374%2Fvideo10stdioservers.1775686374586.jpg)

You can manage your servers with `/mcp` inside a Claude Code session to see what's connected, check status, and disable servers you don't need.

![The /mcp command showing connected MCP servers and their status](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686374%2Fvideo10slashmcpcommand.1775686373865.jpg)

## Scoping Servers

MCP servers can be scoped in three ways:

1. **Local** — only available in the current project, just for you.
2. **User** — available across all your projects.
3. **Project** — uses a `.mcp.json` file that you check into version control so anyone on the codebase gets the exact same servers automatically.

## Context Costs

MCP servers add tool definitions to your context window — even when you're not actively using them. If you have a lot of servers configured, this eats into your available context. Run `/mcp` to see what's connected and disable anything you're not actively using.

![The /mcp server detail view with options to view tools, reconnect, or disable a server](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F8lsy243ftffjjy1cx9lm3o2bw%2Fpublic%2F1775686372%2Fvideo10disablingmcpservers.1775686372522.jpg)

If a tool has a CLI equivalent (like `gh` for GitHub or `aws` for AWS), the CLI is more context-efficient because it doesn't add persistent tool definitions.

You might also benefit from using a **Skill** instead. A Skill has a name and description loaded into context, and Claude only loads the full skill contents when it determines it needs to use it.

If your MCP tools exceed 10% of your context window, Claude Code automatically switches to tool search mode, which discovers the right tools on demand — though this may not work as reliably.

## Recap

MCP connects Claude Code to your external tools and data sources. Add servers with `claude mcp add`. Scope them to your project with `.mcp.json` so your team gets them automatically. And keep an eye on context usage by disabling servers you're not actively using.
<!-- youtube: kkBFmwkDzdo -->

# MCP

[![MCP](https://img.youtube.com/vi/kkBFmwkDzdo/hqdefault.jpg)](https://www.youtube.com/watch?v=kkBFmwkDzdo)

<details>
<summary>자막: MCP</summary>

Model contact protocol is an open standard that lets Claude code connect to external tools and data sources.
>> [music]
>> When you ask a question, Claude will
automatically understand when it should use those tools to better understand your query. Context is one of the most important parts when working with Claude code. A lot of your context lives elsewhere like your databases, your productivity apps, or [music] in public repositories. This is where MCP comes [music] in. First, it's important to understand the concept of tools when talking about Agentic AI. Tools give agents like Claude code the ability to perform actions in order for them to better complete their tasks. This is different from other AI where you just get an output back directly in text usually. For example, if your team is using Linear as our project management software, you can add a Linear MCP server to bring in the details of your specific issues. If you want to get up-to-date documentation of a dependency that you're working with, then the Context 7 MCP server will provide Claude code with that. There are also hundreds of different connectors at claude.com/connectors. You can add MCP servers with the Claude MCP add command. There are two main types. HTTP servers are for remote services. These are hosted by the service provider and connect over the network. STDIO servers are for local processes that run on your machine. You can manage your servers with the /mcp inside a Claude code session to see what's connected, the status, and disable servers that you don't want to use. MCP servers can be scoped in three different ways. One, local means it's only available in the current project for you. Two, the user, which means it's available across all your projects. And three, project scope uses a .mcp.json file that you check into your version control, so anyone working on the code base gets the exact same servers automatically. Now, one thing to be aware of is that MCP servers add tool definitions to your context window, even when you're not using them. So, if you have a lot of servers configured, this eats into your available context. Run the {slash} MCP command to see what's connected and disable anything that you're not actively using or don't think that you're going to use. If a tool has a CLI equivalent like GH for GitHub or AWS for AWS, the CLI is more context efficient because it doesn't add persistent tool definitions. You also might benefit from using a skill in this scenario. A skill has a name and a description that is loaded into context. Similar to MCP, when Cloud thinks it needs to use that skill, it then decides to load it into the context window, which is where you could put the command line interface tools. If your MCP tools exceed 10% of your context window, Cloud code will automatically switch to tool search mode, which will discover the right tools on demand, but this might not work as well since it's just not in the context.
>> [music]
>> Now, a quick recap. MCP connects Cloud
code to your external tools and data sources.
>> [music]
>> Add servers with Cloud MCP add, scope
them to your project with .mcp.json so that your team gets them automatically, and keep an eye on the context usage by disabling servers
[music] that you're not actively using.

</details>
