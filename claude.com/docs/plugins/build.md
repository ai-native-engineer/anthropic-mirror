<!-- source: https://claude.com/docs/plugins/build -->

A plugin is a folder that packages skills, MCP connectors, commands, and agents, in any combination, so that people add them together. This page is the reference for that folder: what each file is and contains, the manifest fields every app reads, how an MCP connector and its skill fit together, and how to test the plugin on claude.ai, in Cowork, and in Claude Code.
[Build your first plugin](https://claude.com/docs/plugins/quickstart) walks you through making one end to end.

* If you want a plugin for your own use without writing files, see [Create a plugin with Claude](https://claude.com/docs/plugins/create-with-claude), which makes one from a conversation
* If you’re building for Claude Code only, see its [plugin authoring docs](https://code.claude.com/docs/en/plugins/create). Claude Code supports more component types than the other surfaces, and those docs are the full reference for anything Claude Code-only
* If you’re deciding which pieces your plugin needs, see [Decide what to include in your plugin](https://claude.com/docs/connectors/building/what-to-build)

##  Lay out the plugin folder

A plugin folder has a manifest at `.claude-plugin/plugin.json` and any combination of component directories beside it.

###  Folder layout

Put only the manifest inside `.claude-plugin/`. Everything else goes at the plugin’s top level.
Select a file to see what it’s for and a minimal example; components that only some apps load, such as agents and hooks, are listed after the explorer.

The explorer is the scaled-down set: the pieces that chat, Cowork, and Claude Code all load, plus the README and license that Anthropic’s directory requires. For every other folder and field a plugin can contain, including the pieces only Claude Code loads, see [Plugin components](https://code.claude.com/docs/en/plugins/components) and the [manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) in the Claude Code docs.

###  Check what each app loads

A plugin can carry more than the explorer shows, but not every Claude app uses all of them. Design for the narrowest app you care about:

* **Skills and commands** load everywhere. In chat, a command loads as a skill that Claude applies when it fits
* **A remote MCP server** in `.mcp.json` appears on the plugin’s **Connectors** tab in chat and Cowork, and works once the person adds or connects it there; Claude Code connects to it directly
* **Agents and hooks** load in Cowork and Claude Code; chat ignores them without an error
* **A local MCP server**, one the app starts as a command, loads in Claude Code and in Cowork sessions that run on the person’s computer; chat ignores it
* **A top-level `bin/` directory** stops claude.ai and Cowork from installing the plugin at all

[Plugin support by app](https://claude.com/docs/plugins/platform-support#compare-component-support-by-app) has the full table, including LSP servers, output styles, and `${user_config.*}` references, and compares where installs are stored and what an organization controls on each app.

###  Start from an example

Anthropic’s [knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) repository holds the role plugins listed in the directory, and each one is a working instance of this layout. The [productivity](https://github.com/anthropics/knowledge-work-plugins/tree/main/productivity) plugin is a compact one to read first. It has a short manifest, an `.mcp.json`, and four skills, with no build step. Most plugins need no build step either, because they’re only Markdown and JSON.
Copy the example plugin’s structure rather than its contents.

##  Write the plugin

The examples in this section build a plugin named `expense-reports` for a fictional finance product whose MCP server is at `mcp.example.com`. If you plan to submit the plugin to Anthropic’s directory, keep the [plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist) open while you write: the developer portal validates the manifest, README, license, and scripts when you submit, and building with those checks in mind means validation passes the first time.

###  Write the manifest

Create `.claude-plugin/plugin.json` with the fields every surface and the directory read:

```
{
  "name": "expense-reports",
  "displayName": "Expense Reports",
  "version": "1.0.0",
  "description": "File, track, and approve expense reports from a conversation, using your finance system's connector and your company's approval rules.",
  "author": { "name": "Example Corp", "url": "https://example.com" },
  "license": "MIT"
}
```

* **`name`**: the plugin’s permanent identity. People install and refer to it by this value, so use lowercase words joined by hyphens, make it specific to your product, and never change it after release. Change `displayName` when you want a different label
* **`version`**: the release number people see for the plugin. Raise it on every release
* **`description`**: what people read in the directory and in [**Customize > Plugins**](https://claude.ai/customize/plugins) before installing
* **`license`**: give it here or as a `LICENSE` file. The directory requires one or the other, and a README of at least 40 words

If you have Claude Code installed, run `claude plugin validate ./expense-reports` from the folder’s parent. It prints `✔ Validation passed` when the manifest and any component files parse, and names the field to fix when they don’t. The [full manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference) lists every optional field.

###  Bundle an MCP connector with its skill

A plugin for your own product pairs an MCP server that gives Claude your product’s tools with a skill that tells Claude when and how to use them. A connector alone leaves Claude to work out your workflow from tool names. The skill is where you put the sequence, the defaults, and what good output looks like.
Reference your server by URL in `.mcp.json` at the plugin root:

```
{
  "mcpServers": {
    "expenses": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    }
  }
}
```

On claude.ai and in Cowork, that entry is listed on the plugin’s **Connectors** tab, where the user [adds or connects it](https://claude.com/docs/plugins/overview#bundled-connectors) and signs in through your server’s OAuth flow. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.
Don’t put API keys or other secrets in this file, because every person who installs the plugin receives its files. If your server is already listed in the directory, use the same URL here, so that someone who has both your connector and your plugin sees one set of tools rather than two.
Then write the skill that uses it, at `skills/file-expense/SKILL.md`:

```
---
name: file-expense
description: File an expense report. Use when the user mentions a receipt, reimbursement, or expense, or asks to submit spending for approval.
---

To file an expense:

1. Ask for the receipt if the user hasn't attached one, and read the amount, date, merchant, and currency from it.
2. Call the expenses connector's `create_report` tool with those fields. Default the category from the merchant type; ask only if it's ambiguous.
3. If the amount is over the user's approval limit (check with `get_policy`), add their manager as approver before submitting.
4. Reply with the report number and its approval status. Don't paste the full API response.
```

Claude decides when to load the skill from the `description` line, so write it as the situations a user would be in, not as a summary of the file. [Create custom skills](https://claude.com/docs/skills/how-to) covers the frontmatter fields, resource files, scripts, and testing.

##  Test the plugin on each surface

Test on each surface your users will use.

* **Claude Code**: run `claude --plugin-dir ./expense-reports` to start a session with the plugin loaded from your working copy. Your skills appear as `/expense-reports:file-expense`, and `/mcp` shows the server’s connection state
* **claude.ai and Cowork**: upload the plugin to your own account, then check each component:
  1. Zip the plugin folder. The archive can hold the folder as its single top-level entry or the folder’s contents directly. If the upload says `plugin.json must be at .claude-plugin/plugin.json at the zip root (or inside a single top-level directory)`, the manifest is nested more than one folder deep or the archive has other files beside the plugin folder.
  2. In claude.ai, go to **Customize > Plugins > Add > Upload plugin** and select the zip. The plugin then appears on your own account.
  3. Open a chat and ask Claude which skills it has from plugins.
  4. Connect the bundled connector from the plugin’s **Connectors** tab.
  5. If your plugin has agents, start a Cowork task to confirm they load.
* **A team testing together**: push the folder to a Git repository set up as a [marketplace](https://code.claude.com/docs/en/plugins/create-marketplace), and have each tester add it from **Customize > Plugins > Add > Add marketplace** with the repository URL instead, so everyone installs the same copy

Loading the plugin shows that its parts appear. To measure whether its skills improve Claude’s output, write eval cases and run [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) in Claude Code, which grades the results and compares them against a run without the plugin. To test one skill by itself on any surface, see [Measure whether the skill improves the output](https://claude.com/docs/skills/how-to#measure-whether-the-skill-improves-the-output).
Before you submit the plugin to the directory, run `claude plugin validate ./expense-reports`, then select **Validate** in the [developer portal](https://claude.ai/directory/manage). The portal runs every validation check, and [Run the checks before you submit](https://claude.com/docs/plugins/pre-submission-checklist#run-the-checks-before-you-submit) explains each result.
When something is missing on one surface and present on another, check it against [Check what each app loads](#check-what-each-app-loads) before debugging. An agent that never appears in chat, or a local server that chat doesn’t start, is the surface behaving as designed.

##  Add Claude Code-only components

Claude Code loads everything on this page and also supports components the other apps skip, such as language servers, executables in `bin/`, per-user configuration prompts, output styles, and dependencies between plugins. A plugin that includes them still installs on claude.ai and in Cowork, except that a top-level `bin/` directory stops claude.ai and Cowork from installing it at all. The Claude Code docs cover [each component](https://code.claude.com/docs/en/plugins/components) and [testing and debugging](https://code.claude.com/docs/en/plugins/create#test-and-debug) there.

Once the plugin works, you can distribute it through your organization, your own marketplace, or the directory:

* [Manage plugins for your organization](https://claude.com/docs/plugins/admin): on Team and Enterprise plans, an Owner can make the plugin available or installed by default for members
* [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace): list the plugin in a Git repository’s `marketplace.json`, which anyone you give the URL to can add from **Customize > Plugins** or the Claude Code command line
* [Publish to the directory](https://claude.com/docs/directory/publish): submit the plugin from the [developer portal](https://claude.ai/directory/manage) so people on Pro, Max, Team, and Enterprise plans can find and add it on claude.ai and in Cowork, and use it in Claude Code. Anyone on a paid plan can submit without applying to a partner program first; on Team and Enterprise, an Owner submits
