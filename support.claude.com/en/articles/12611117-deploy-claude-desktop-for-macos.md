<!-- source: https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos -->

# Deploy Claude Desktop for macOS

Administrators on Team or Enterprise plans can deploy Claude Desktop automatically to manage installations and updates centrally. Claude Desktop installs to `/Applications` and updates automatically when new versions are released, unless disabled via enterprise policies.

## Available installation formats

* **`.pkg`** - Standard macOS installer package (recommended for enterprise)
* **`.dmg`** - Drag-and-drop installation

## Cowork requirements

Cowork will be installed automatically when you download and install Claude Desktop for macOS.

## Download

**[Universal (x64 or arm64) Claude PKG](https://claude.ai/api/desktop/darwin/universal/pkg/latest/redirect)**

The Universal build is compatible with both Intel and Apple Silicon machines and supports all Mac hardware.

## Deploy via MDM

Upload the PKG to your MDM solution (Jamf, Kandji, Microsoft Intune) and deploy to target machines.

## Configuration

To configure Claude Desktop settings such as auto-updates, extensions, and MCP servers, see the **[Enterprise Configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)** article.

## Troubleshooting

### Users cannot update Claude Desktop

Claude Desktop can be installed to either the user's Applications folder or the system Applications folder, which affects update permissions.

* `~/Applications` (user folder): Users can update without administrator privileges
* `/Applications` (system folder): Users need administrator access and write permissions to `/Applications`, `Claude.app`, and all contained files

For shared machines, disable auto-updates via enterprise policies and manage updates centrally through your MDM solution.

[Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)[Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)[Deploy Claude Desktop for Windows](https://support.claude.com/en/articles/12622703-deploy-claude-desktop-for-windows)[Claude Cowork desktop architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-desktop-architecture-overview)
