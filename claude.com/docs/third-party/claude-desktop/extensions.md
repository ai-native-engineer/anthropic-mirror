<!-- source: https://claude.com/docs/third-party/claude-desktop/extensions -->

Claude Desktop on third-party (3P) supports the same extensibility model as standard Claude Desktop ([MCP connectors](/docs/connectors/overview), [skills](/docs/skills/overview), and [plugins](/docs/plugins/overview)), with the key difference that administrators provision them through the filesystem and managed configuration rather than the claude.ai admin console.
There are three layers, in order of precedence:

| Layer | Provisioned by | Delivered via |
| --- | --- | --- |
| Managed MCP servers | Admin | `managedMcpServers` configuration key |
| Organization plugins | Admin | A system-wide directory on each device |
| User extensions | End user | In-app Connectors and Plugins UI |

Admins can disable the user layer entirely; see [Controlling user extensions](#controlling-user-extensions).

##  Managed MCP servers (admin)

Use the `managedMcpServers` configuration key to deploy MCP servers (remote HTTP/SSE or local stdio command) to every device. These appear in the user’s connector list automatically, can’t be removed by the user, and support per-tool policy locks (`allow` / `ask` / `blocked`).

[
  {
    "name": "internal-search",
    "url": "https://mcp.example.corp",
    "oauth": true,
    "toolPolicy": { "search": "allow", "delete_document": "blocked" }
  },
  {
    "name": "ticketing",
    "url": "https://tickets.example.corp/mcp",
    "headersHelper": "/usr/local/bin/corp-sso-token",
    "headersHelperTtlSec": 900
  }
]

See the [`managedMcpServers` schema](/docs/third-party/claude-desktop/configuration#managedmcpservers) in the configuration reference for every field, including static headers, OAuth, and the headers-helper executable for short-lived tokens.
In the in-app configuration window, each server you add under **Connectors & extensions** has a **Test this connection** button that runs a live MCP `initialize` and `tools/list` against the server using the headers or OAuth settings you’ve entered, then shows the round-trip latency, the discovered tool list, or the error returned. Use it to validate reachability and credentials before exporting the configuration.

###  Supported MCP servers

Any MCP server reachable from the user’s device over HTTPS works with Claude Desktop on 3P, including public servers from third parties and internal servers you build and host (including on internal gateways).
The [Claude connector directory](https://claude.com/connectors) is the canonical catalog of vetted servers. **Every connector in the directory that is not labeled “Made by Anthropic” is accessible in Claude Desktop on 3P** and can be deployed via `managedMcpServers` or installed by users. Connectors labeled “Made by Anthropic” are hosted on Anthropic infrastructure and are available only in standard Claude Desktop.

###  Recommended MCP servers

The grids below highlight commonly used servers from the directory. Most require an account or license with the vendor; the MCP server itself accesses data through your existing entitlement.

####  Productivity suites

## Google Workspace

Gmail, Calendar, Drive, Docs, and more via Google’s own Workspace MCP servers. See [Google’s setup guide](https://developers.google.com/workspace/guides/configure-mcp-servers) to get started.

## Microsoft 365

Outlook, OneDrive, SharePoint, and Teams. Requires registering an app in your Entra tenant and an Anthropic allowlist step.

####  Collaboration and knowledge work

Vendor-hosted remote MCP servers. Add them to `managedMcpServers` with `"oauth": true`; users authenticate with their existing vendor account.

## Atlassian

Jira, Confluence, and Compass via the Atlassian Rovo MCP Server.

## Notion

Pages, databases, and search.

## Linear

Issues, projects, and cycles.

## Asana

Tasks, projects, and goals.

## Box

Files and document management. Requires a pre-registered Box Custom App; set `oauth` to an object with `clientId`, `clientSecret`, and `authorizationServer: ["https://api.box.com"]` rather than `true`.

## GitHub

Repositories, issues, and pull requests.

## Salesforce

CRM records and Apex.

## Hex

Notebooks and analytics projects.

## Stripe

Payments, customers, and invoices.

####  Financial services

Vendor-published MCP servers from the [Claude connector directory](https://claude.com/connectors). Each requires an account or data license with the respective vendor.

## FactSet

Institutional financial data and analytics.

## LSEG

Multi-asset-class data and analytics.

## Moody's Analytics

Risk insights and decision intelligence.

## Morningstar

Investment and market insights.

## MSCI

Index and ESG data.

## PitchBook

Private-market and deal data.

## CB Insights

Private-company intelligence.

## Daloopa

Fundamental data and KPIs with source links.

## Aiera

Earnings calls, filings, and company publications.

## MT Newswires

Real-time financial news.

## Brex

Spend management and finance automation.

## EdgarTools

SEC EDGAR filings, statements, and insider trading. Open source; no license required.

For licensed data sources without a public MCP server (S&P Capital IQ, internal research databases), build an internal MCP server against your existing API entitlements and deploy it via `managedMcpServers`. For the full catalog of vetted servers across all categories, browse the [Claude connector directory](https://claude.com/connectors).

##  Organization plugins (admin)

[Plugins](/docs/plugins/overview) bundle MCP connectors, skills, slash commands, hooks, and sub-agents into a single directory. In Claude Desktop on 3P, admins distribute plugins by placing them in a system-wide directory on each device, typically via the same MDM or software-distribution channel used for the app itself.

###  Plugin directory location

| Platform | Path |
| macOS | `/Library/Application Support/Claude/org-plugins/` |
| Windows | `C:\Program Files\Claude\org-plugins\` |

On Windows, the directory is under `Program Files` (not `ProgramData`) so that only administrators can create or modify it. Claude Desktop treats the presence of this directory as an admin-provisioned source.

###  Plugin structure

Each subdirectory of `org-plugins/` is one plugin. The directory name is the plugin’s canonical name.

org-plugins/
└── code-reviewer/
    ├── .claude-plugin/
    │   └── plugin.json
    ├── version.json
    ├── .mcp.json
    ├── agents/
    │   └── code-reviewer.md
    ├── commands/
    │   └── find-all-bugs.md
    └── skills/
        └── security-review/
            └── SKILL.md

| File | Purpose |
| `.claude-plugin/plugin.json` | **Required.** Plugin manifest (name, description, version). Directories without this file are ignored. |
| `version.json` | `{"version": "1.2.3"}`. When this string changes, Claude Desktop re-syncs the plugin on next launch. Any string change triggers re-sync (there’s no semver ordering, so a downgrade is just another version string). If absent, the directory’s modification time is used instead. |
| `.mcp.json` | MCP servers bundled with this plugin. A JSON object keyed by server name: `{"mcpServers": {"<name>": {"type": "http", "url": "...", "oauth": true}}}`. Each entry uses `type` (`http` or `sse`), not `transport`, and supports `url`, `headers`, and `oauth` only; `toolPolicy`, `headersHelper`, and `headersHelperTtlSec` are not read from this file. |
| `agents/` | Sub-agent definitions. |
| `commands/` | Slash-command definitions. |
| `skills/` | [Skill](/docs/skills/overview) directories. |
| `hooks/` | Hook definitions that run on agent lifecycle events. |

See the [plugins reference](https://code.claude.com/docs/en/plugins) for the full file format of each component, including the hooks schema.

Symlinks inside a plugin are followed as long as the target resolves to a path inside the plugin directory. Symlinks that point outside the plugin (for example, `skills/foo/SKILL.md → /etc/hosts`) are skipped. A symlinked top-level plugin directory (for example, `org-plugins/my-plugin → /opt/shared/my-plugin`) is also followed.

MCP servers declared in a plugin’s `.mcp.json` don’t carry a `toolPolicy` field in the plugin file itself. To lock tools on a plugin-delivered server, set [`orgPluginSettings`](/docs/third-party/claude-desktop/configuration#orgpluginsettings) in managed configuration, keyed on the server’s `name`.

###  Auto-installing organization plugins

By default, organization plugins appear in the user’s plugin browser as available to install, and each user opts in. To install a plugin automatically for every user, set `installationPreference` in the plugin’s `.claude-plugin/plugin.json`:

{
  "name": "code-reviewer",
  "version": "1.0.0",
  "description": "Internal code review assistant",
  "installationPreference": "required"
}

| Value | Behavior |
| `"required"` | Installs automatically when the user signs in. The Uninstall action is hidden. If the plugin is removed from disk, it reinstalls on the next sign-in. |
| `"auto_install"` | Installs automatically when the user signs in. Users can uninstall it, and it stays uninstalled for that user. |
| `"available"` (or omitted) | Default. Users install manually from the plugin browser. |

This mirrors the installation preference behavior of remote-managed plugins on Claude.ai. Changing a plugin’s `installationPreference` takes effect the next time each user signs in.

###  Updating organization plugins

To roll out a new version of a plugin:

1. Update the plugin contents in `org-plugins/<name>/` via your software-distribution tool
2. Bump the `version` string in `version.json`
3. Users pick up the change on their next app launch

##  User extensions

Unless restricted by an admin, end users can add their own extensions through the in-app UI:

* **Plugins** — install plugins (which can bundle skills, hooks, slash commands, and sub-agents) from the Plugins settings page
* **Connectors** — install local desktop extensions (`.mcpb`) from the Connectors settings page
* **Local MCP servers** — add local MCP server processes from **Settings → Developer**, when enabled by the admin

End users cannot add remote MCP servers; remote servers are available only via admin-provisioned `managedMcpServers` or organization plugins. User-added extensions are stored in the user’s [local data directory](/docs/third-party/claude-desktop/data-storage) and apply only to that device.

##  Controlling user extensions

Admins can restrict or disable each user-extension surface independently via managed configuration:

| Key | Effect when `false` |
| `isLocalDevMcpEnabled` | Users cannot add their own local MCP servers from **Settings → Developer**. |
| `isDesktopExtensionEnabled` | Users cannot install local `.mcpb` desktop extensions. |
| `isDesktopExtensionSignatureRequired` | (When `true`) Unsigned `.mcpb` extensions are rejected. |

Setting the first two to `false` restricts MCP servers and connectors to those delivered through `managedMcpServers` and `org-plugins/`. Users can still add their own skills and plugins regardless of these settings. See the [Locked down profile](/docs/third-party/claude-desktop/configuration#recommended-security-profiles) for a complete example.

##  Related topics

## Code tab

How extensions and managed settings reach the embedded Claude Code engine.

## MCP in Claude Code

Configure MCP servers for the standalone Claude Code CLI.

## Claude Code plugins

Plugin structure, marketplaces, and management for Claude Code.

## Managed MCP in Claude Code

Restrict which MCP servers Claude Code users can add.

[Claude API](/docs/third-party/claude-desktop/claude-api)[Connect to Microsoft 365](/docs/third-party/claude-desktop/connectors-m365)
