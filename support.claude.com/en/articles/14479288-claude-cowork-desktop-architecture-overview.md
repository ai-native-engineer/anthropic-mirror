<!-- source: https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview -->

# Claude Cowork desktop architecture overview

Updated over 2 weeks ago

This article explains how Claude Cowork runs on member devices and the admin controls available for restricting its scope on managed devices.

This article is for Enterprise admins. The architecture described here is the same across all plans. The device-level admin controls at the end apply to Team and Enterprise plans.

## Claude Cowork’s two execution environments

Claude Cowork uses two execution environments on each member's device:

* **The agent loop runs natively on the device.** This includes Claude's conversation handling, file reads and writes in connected folders, web fetches, and local plugin MCP servers. Access is gated by an application-layer permission system that enforces the member's connected-folder rules and your organization's network egress settings.
* **Code execution runs in an isolated virtual machine (VM).** Shell commands and any code Claude writes execute inside a dedicated Linux VM, isolated from the host operating system by the platform's hypervisor (Apple Virtualization.framework on macOS, Hyper-V on Windows). The VM enforces its own network egress filtering, syscall restrictions, and per-session user isolation.

For a detailed technical overview, see the **[Claude Cowork desktop security architecture overview](https://trust.anthropic.com/resources?s=2a7bbzo1lyymvdt551q7kl&name=claude-cowork-desktop-security-architecture-overview)** on our Trust Center.

## Admin controls for managed devices

Two MDM keys let you restrict Cowork's scope on managed devices. Both are device-level settings applied through your MDM solution, not from organization settings.

* **Disable local MCP servers:** Set `isLocalDevMcpEnabled` to false to disable plugin-bundled and locally configured MCP servers.
* **Disable desktop extensions:** Set `isDesktopExtensionEnabled` to false to block MCPB and DXT extension servers from running.

Both controls are described in **[Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)**.

The organization-wide Cowork toggle in **Organization settings > Cowork** (**Enable for your organization**) controls whether Cowork is available at all. The device-level controls above only apply when Cowork is enabled.

## Frequently asked questions

### What happens if a member's device can't start the VM?

Cowork continues running file and web tools while the VM is unavailable. Shell commands and code execution report "workspace unavailable" until the VM recovers.

### Does Cowork activity show up in audit logs?

Not currently. Cowork activity isn't captured in audit logs, the Compliance API, or data exports. For guidance on monitoring Cowork activity, see **[Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-cowork-activity-with-opentelemetry)**.

### Can endpoint detection (EDR) tools inspect activity inside the VM?

No. The VM is isolated from host-based security tools by design. If your compliance posture depends on endpoint visibility, account for this before rolling out Cowork.

[Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)[Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)[Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)[Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
