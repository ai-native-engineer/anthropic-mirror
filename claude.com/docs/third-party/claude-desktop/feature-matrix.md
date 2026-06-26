<!-- source: https://claude.com/docs/third-party/claude-desktop/feature-matrix -->

The tables below compare the feature set of Claude Desktop on third-party (3P) to Claude Enterprise.

##  Key differences

**Configuration.** Claude Enterprise uses a web-based admin console. Claude Desktop on 3P is configured entirely via MDM (Jamf, Intune, Group Policy) or a [bootstrap server](/docs/third-party/claude-desktop/bootstrap), with no Anthropic-hosted admin interface.
**Telemetry.** Claude Desktop on 3P sends usage and debugging metrics only, and these can be fully disabled via managed configuration. Claude Enterprise does not offer telemetry toggles. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry).
**Inference.** Claude Desktop on 3P routes all inference through the provider you configure. When using Vertex AI or Bedrock, Anthropic never sees prompts or completions; during the Microsoft Foundry preview, Claude models run on Anthropic’s infrastructure — see the [Overview](/docs/third-party/claude-desktop/overview) for details.
**Pricing.** Claude Desktop on 3P is token-based consumption billed by your cloud provider, with no seat licensing.
**Features not available in 3P.** Features marked with — are absent from the UI. Users see a clean interface without error states for unavailable features.

##  User features

| Feature | Claude Enterprise | Claude Desktop on 3P |
| --- | --- | --- |
| Cowork tab | ✓ | ✓ |
| Code tab | ✓ | ✓ |
| Auto mode / Act without asking | ✓ | ✓ (admin opt-in) |
| Chat tab | ✓ | ✓ |
| Projects | ✓ | ✓ |
| Code execution for analysis | ✓ | ✓ |
| File access, upload, and export | ✓ | ✓ |
| Local MCP | ✓ | ✓ |
| Remote MCP | ✓ | ✓ |
| Anthropic 1P Connectors | ✓ | — \* |
| Skills, plugins, and hooks | ✓ | ✓ |
| Artifacts | ✓ | ✓ |
| Memory | ✓ | ✓ † |
| Scheduled tasks | ✓ | ✓ |
| Global languages | ✓ | ✓ |
| Project and plugin sharing | ✓ | — |
| Plugin Marketplaces | ✓ | ✓ \*\* |
| Dispatch / mobile | ✓ | — |
| Voice mode | ✓ | — |
| Claude in Chrome | ✓ | — |
| Computer use | — | — |

\* The Anthropic Microsoft 365 connector is available in Claude Desktop on 3P; see the [setup guide](/docs/third-party/claude-desktop/connectors-m365). For Google Workspace availability, see [Productivity suites](/docs/third-party/claude-desktop/extensions#productivity-suites).
\*\* Plugins distributed via the [org-plugins directory](/docs/third-party/claude-desktop/extensions#organization-plugins-admin) appear to users as an organization marketplace. The public Anthropic plugin marketplace is not available.
† Memory in Claude Desktop on 3P is stored on the device, not on Anthropic infrastructure. Users can review, delete, or pause it under **Settings → Cowork → Memory**; see [Memory](/docs/third-party/claude-desktop/data-storage#memory). Chat-history search and nightly summary generation are Chat-tab features and are not applicable in 3P.

##  Admin features

| Feature | Claude Enterprise | Claude Desktop on 3P |
| --- | --- | --- |
| Endpoint / gateway configuration | — | ✓ |
| Skills, hooks, and plugins distribution | ✓ | ✓ |
| MCP server allowlist | ✓ | ✓ |
| Feature toggles (web search, local MCP, etc.) | ✓ | ✓ |
| Auto-updates | ✓ | ✓ (configurable) |
| Per-user spend caps | ✓ (differentiated) | ✓ (blanket only) |
| Compliance API | ✓ | — ‡ |
| Analytics API | ✓ | — ‡ |
| OpenTelemetry export | ✓ | ✓ |
| User management via UI | ✓ | — |
| RBAC | ✓ | via MDM |

‡ Many of these capabilities can be achieved via OpenTelemetry export to your own collector. See [Monitoring](/docs/cowork/monitoring).

[Overview](/docs/third-party/claude-desktop/overview)[Installation and setup](/docs/third-party/claude-desktop/installation)
