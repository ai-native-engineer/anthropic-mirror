<!-- source: https://claude.com/blog/claude-code-plugins -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

# Customize Claude Code with plugins

Claude Code now supports plugins: custom collections of slash commands, agents, MCP servers, and hooks that install with a single command.

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code
* Date

  October 9, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/claude-code-plugins

### Share your Claude Code setup with plugins

Slash commands, agents, MCP servers, and hooks are all extension points you can use to customize your experience with Claude Code. As we've rolled them out, we've seen users build increasingly powerful setups that they want to share with teammates and the broader community. We built plugins to make this easier.

Plugins are a lightweight way to package and share any combination of:

* **Slash commands**: Create custom shortcuts for frequently-used operations
* **Subagents**: Install purpose-built agents for specialized development tasks
* **MCP servers**: Connect to tools and data sources through the Model Context Protocol
* **Hooks**: Customize Claude Code's behavior at key points in its workflow

You can install plugins directly within Claude Code using the `/plugin` command, now in public beta. They’re designed to toggle on and off as needed. Enable them when you need specific capabilities and disable them when you don’t to reduce system prompt context and complexity.

![Product screenshot showing Claude Code plugin menu](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d95ecae26885bafdfde_81805a2d45f087f2cc153168759f8bf015706b04-1920x1035.png)

Moving forward, plugins will be our standard way to bundle and share Claude Code customizations, and we’ll continue to evolve the format as we add more extension points.

### Use cases

Plugins help you standardize Claude Code environments around a set of shared best practices. Common plugin use cases include:

* **Enforcing standards:** Engineering leaders can maintain consistency across their team by using plugins to ensure specific hooks run for code reviews or testing workflows
* **Supporting users**: Open source maintainers, for example, can provide slash commands that help developers use their packages correctly
* **Sharing workflows:** Developers who build productivity-boosting workflows—like debugging setups, deployment pipelines, or testing harnesses—can easily share them with others
* **Connecting tools:** Teams that need to connect internal tools and data sources through MCP servers can use plugins with the same security and configuration protocols to speed up the process
* **Bundling customizations:** Framework authors or technical leads can package multiple customizations that work together for specific use cases

### Plugin marketplaces

To make it easier to share these customizations, anyone can build and host plugins and create plugin marketplaces—curated collections where other developers can discover and install plugins.

You can use plugin marketplaces to share plugins with the community, distribute approved plugins across your organization, and build on existing solutions for common development challenges.

To host a marketplace, all you need is a git repository, GitHub repository, or URL with a properly formatted `.claude-plugin/marketplace.json` file. See our documentation for details.

To use plugins from a marketplace, run `/plugin marketplace add user-or-org/repo-name`, then browse and install plugins using the `/plugin` menu.

### Discover new marketplaces

Plugin marketplaces amplify the best practices our community has already developed, and community members are leading the way. For instance, engineer Dan Ávila's [plugin marketplace](https://www.aitmpl.com/plugins) offers plugins for DevOps automation, documentation generation, project management, and testing suites, while engineer Seth Hobson has curated over 80 specialized sub-agents in his [GitHub repository](https://github.com/wshobson/agents), giving developers instant access via plugins.

You can also check out a few [example plugins](https://github.com/anthropics/claude-code) we've developed for PR reviews, security guidance, [Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) development, and even a meta-plugin for creating new plugins.

### Getting started

Plugins are now in public beta for all Claude Code users. Install them with the `/plugin` command and they'll work across your terminal and VS Code.

Check out our documentation to [get started](https://docs.claude.com/en/docs/claude-code/plugins-reference), [build your own plugins](https://docs.claude.com/en/docs/claude-code/plugins), or [publish a marketplace](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces). To see plugins in action, try this multi-agent workflow we use to develop Claude Code:

`/plugin marketplace add anthropics/claude-code`

```
/plugin marketplace add anthropics/claude-code
```

```
/plugin install feature-dev
```

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude Code

Coding
