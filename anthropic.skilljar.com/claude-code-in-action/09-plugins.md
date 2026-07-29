<!-- https://anthropic.skilljar.com/claude-code-in-action/486939 -->

A setup you trust is worth a lot more once your whole team is running it. The problem is moving it around. You build a great `.claude` directory with skills, subagents, and hooks, and then what? Everyone copies and pastes files between machines and hopes they stay in sync. Plugins fix that. A plugin is how Claude Code packages a setup and moves it from one person to the next.

There are two sides to this, and we'll cover both. First, using plugins that other people publish. Second, packaging your own once you've built something worth sharing.

## What a plugin is

A plugin is one installable unit. It bundles everything you'd otherwise share by hand: skills, subagents, hooks, and MCP server configs, plus the longer tail of stuff like language server protocol servers, background monitors, themes, and a slice of `settings.json`. One version, one install.

Where the plugin lives decides how you install it. Inside a session, you can install one directly by name:

```
/plugin install org-name@plugin-name
```

Here's what that looks like. Claude Code installs it and tells you to run `/reload-plugins` to apply the change.

## Adding a marketplace for your team

For a team, the better move is to add a private marketplace once. A marketplace is a shared source that plugins resolve through:

```
/plugin marketplace add your-org/claude-plugins
```

Call it whatever you want. Once it's added, every install after that resolves through it. You get centralized discovery, version tracking, and updates in one place instead of scattered across everyone's laptop.

You can browse what's available from the Discover tab. It lists the plugins on your marketplaces so you can search and pick.

## Read before you install

Here's the part that matters most. A plugin runs code on your machine, with your privileges. Its hooks fire on every matching tool call. So if you install a plugin for its skills, you also get its PreToolUse and Stop hooks whether you read them or not.

Think about what that means. A community plugin could ship a Stop hook that calls out to a network endpoint every time, and nothing in your configuration would warn you about it. That's not a reason to avoid plugins. It's a reason to look first.

Before you install, check the plugin's details. Claude Code shows you what it will install and estimates the context cost, along with a plain warning that Anthropic doesn't control what's inside third-party plugins.

Two things worth knowing about where plugins come from:

* The in-app submission form posts to the community marketplace after Anthropic's automated review.
* The official marketplace is curated on its own separate track.

But reviewed isn't the same as trusted. Automated review catches some things, not everything. So the rule stands: install plugins and add marketplaces only from sources you truly trust, and check what a plugin actually does before turning it on.

## Components run alongside yours

A plugin doesn't overwrite your configuration. Its components run alongside your own. That's mostly good, but it has consequences you should understand.

Hooks stack. A plugin's PreToolUse hook and your own PreToolUse hook both fire on every tool call. Neither replaces the other. This is exactly why you read the details first.

Skills, agents, and commands are namespaced under the plugin name, so they never clash with yours. A plugin can also ship a `settings.json` file, but only a narrow one. Claude Code honors just two keys from it: the agent and subagent status line keys.

That agent key is worth a pause. Setting it promotes one of the plugin's subagents to the main thread, along with its system prompt, tool restrictions, and model. In other words, enabling the plugin can change how Claude Code behaves by default. That's one of the main reasons to look before you even turn it on.

Once a plugin is installed you can see everything it added, manage it, and uninstall it from the plugin panel.

## Packaging your own plugin

Now the other side. Once you've built a `.claude` directory that works, don't make your team copy and paste it between machines. Package it instead.

The good news is you don't have to restructure anything. A plugin uses the same `.claude` shape you already use:

* One folder per skill.
* One markdown file per subagent under `agents`.
* `hooks/hooks.json` and `.mcp.json`, at the plugin root.

The directory structure does most of the work. Claude Code discovers components by convention.

## The manifest

On top of that, there's an optional manifest. It lives at `.claude-plugin/plugin.json` and holds the name, version, description, and author:

```
{
  "name": "svg-splitter-review",
  "version": "0.1.0",
  "description": "Reviews the SVG Splitter repo",
  "author": {
    "name": "Lewis Menelaws"
  }
}
```

The manifest is optional. Leave it out and Claude Code still discovers your components by directory convention. But a couple of details are worth knowing:

* **Name is the only required field.** It namespaces your skills as `company-name:skill-name`, which keeps them from colliding with anyone else's.
* **Version it like any other dependency.** That's what makes updates and version tracking work across your team.

## The takeaway

Two simple rules cover most of this:

* When you use plugins, read before you install. A plugin runs code with your privileges, so look at its hooks, agents, and MCP servers first.
* When you build one, package your `.claude` the moment it works. One manifest, one install.

That's the whole point. One installable unit, and the setup you trust reaches your entire team.

<!-- youtube: k4kZwJ0FtX0 -->

[![Plugins](https://img.youtube.com/vi/k4kZwJ0FtX0/hqdefault.jpg)](https://www.youtube.com/watch?v=k4kZwJ0FtX0)

<details>
<summary>자막: Plugins</summary>

A setup you trust is worth more when your whole team runs it. Plugins are how ClogCode packages a setup and moves it between people. And there are two sides to that, using the plugins, other people publish, and packaging your own once you've built something worth sharing. A plugin is one installable unit. Where it lives sets how you install it. Inside a session, slash plugin install the organization name at the plugin name does the same thing. For a team, add a private marketplace once with the slash plugin marketplace at your organization slash cloud plugins or whatever you want to call it. And every install after that resolves through it with centralized discovery, version tracking, and updates. Now, a plugin runs code on your machine with your privileges, and its hooks fire on every matching tool call. Install it for the skills, and you also get its pre-tool use and stop hooks whether you read them or not. A community plugin can ship a stop hook that calls out to a network endpoint, and nothing in your configuration will warn you. See every hook, agent, and MCP server that it adds. Install plugins and add marketplaces only from sources that you truly trust. The in-app submission form posts to the community marketplace after Anthropix automated review. and the official marketplace is curated on its own track. Reviewed isn't the same as Trusted, though, so check what it does. A plugin doesn't overwrite your configuration. Its components run alongside yours. So first, hooks stack together. A plugin's pre-tool use and your own both fire on every tool call, which is the reason you read the details first. Skills, agents, and commands are namespaced under the plugin name, so they never clash. A plugin can also ship a settings.json file, but a narrow one. So Cloud Code honors only the agent and subagent status line keys. Setting agent promotes one of the plugin's subagents to the main thread with its system prompt, tool, restrictions, and model. And enabling that plugin changes how Cloud Code behaves by default, which is one of the main reasons to look before you even turn it on. So once you've built a .claw directory, instead of your team copying and pasting between machines, package it instead. A plugin bundles all of it as one version installable unit, skills, subagents, hooks, and MCP server configs, plus the longer tail of the language server protocol servers, background monitors, themes, and a settings.json slice. The manifest lives at .cloud plugin slash plugin.json and holds the name, version, description, and author. It's optional, but leave it out and Cloud Code discovers components by directory convention. The directory structure does the rest. The same .cloud shape that you already use with skills with one folder per skill, agents with one markdown file per subagent, hooks slash hooks.json and .mcp.json, all at the plugin root. Name is the only required field. and it namespaces your skills as the company name, skill name. Version it like any other dependency. When you use plugins, read before you install. When you build one, package your dot cloud the moment it works. One manifest, one install, and the setup you trust reaches your entire team.

</details>
