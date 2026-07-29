<!-- source: https://claude.com/docs/government/connectors/overview -->

> ## Documentation Index
>
> Fetch the complete documentation index at: [/docs/llms.txt](https://claude.com/docs/llms.txt)
>
> Use this file to discover all available pages before exploring further.

[Skip to main content](#content-area)

> **Who this is for:** Tenant administrators and organization owners who want Claude to reach their agency’s own systems (for example, an internal search service or a ticketing tool) from Claude Desktop and other Claude products.

Use this page to add Model Context Protocol servers for your own systems, choose which Claude products receive each one, and set which of their tools are available to users.
A **connector** is a link between Claude and an external service. The service runs a Model Context Protocol (MCP) server, which is a standard way for a service to publish a set of tools that Claude can call. You add the server once here, and Claude for Government delivers it to the products you select.

##  The Connectors card

The **Connectors** card appears on your [tenant](https://claude.com/docs/government/tenant-admin/configuration) or [organization](https://claude.com/docs/government/org-admin/configuration) Config page alongside the built-in connector cards. It lists every connector you have added, with each one’s name, address, the products it applies to, and a summary of how many of its tools are allowed. Click **Add connector** to open the wizard, or click the edit icon next to a connector to change it.
Connectors are set at the tenant or organization level. When you are viewing a group scope, the card is read-only and points you to the organization or tenant settings where connectors are configured.

##  Adding a connector

The **Add connector** button opens a three-step wizard.

###  Step 1: Server

Enter the details of the MCP server.

* **Name** is a short identifier for the connector. It must be lowercase letters, digits, hyphens, or underscores.
* **Server URL** is the address of the server’s MCP endpoint. It must begin with `https://`.
* **Transport** selects how Claude talks to the server. Choose HTTP or SSE to match what your server supports.
* **Authentication** selects how Claude proves who it is to the server. **None** sends no credentials. **Header (shared secret)** sends a fixed header (for example, an authorization token) with every request; the value is stored securely and shown as `••••` after you save. **OAuth (users sign in)** has each user sign in on first use, and their tokens stay on their own machine.

When you choose OAuth, a confirmation checkbox appears on the final step asking you to confirm that the server address is exactly the one you intend, because users will be sent to a sign-in page that the server chooses.

###  Step 2: Discover tools

This step tries to list the tools the server offers so that you can set policy on the next step. Discovery runs from your own browser and is best-effort; many servers cannot be reached this way (for example, because they require authentication or are on a private network), and you can always add tools by name on the next step instead.
Click **Discover tools** to run the probe. If the server answers, the tools it advertises are listed. If the server asks for sign-in, a **Sign in to discover** option appears: confirm the sign-in host, sign in through the popup, and the probe runs again with that one-time credential. The credential is used once in your browser for this probe and is never stored; it is separate from the **Authentication** choice on the Server step, which controls how your users authenticate later.

###  Step 3: Policy & scope

Choose which products receive this connector and which of its tools are available.
Under **Apply to**, tick the products that should receive this connector: Claude Desktop and Microsoft 365. A connector with no products ticked is saved but delivered nowhere, which is a way to pause it. A connector that uses OAuth cannot be applied to Microsoft 365, because per-user sign-in is not available there. A connector with any tool switched off in the table below also cannot be applied to Microsoft 365, and the checkbox is disabled with a **needs every tool on** note until every tool is on.
Under **Tool policy**, the table lists the tools found during discovery with an on/off switch for each. **Refresh tools** probes the server again and fills in any tools that are new since you last looked, keeping the switches you have already set. **Add tool** lets you type a tool name by hand when discovery could not reach the server.
On Claude Desktop, a tool you switch off is blocked, a tool you switch on is available and each user still approves its use, and a tool that is not listed at all is left to the user to enable or disable. You cannot apply this connector to Microsoft 365 while any tool in this table is switched off. If you are editing a connector that already applies to Microsoft 365 and you switch a tool off, a warning tells you that saving will remove it from Microsoft 365.
Click **Save** to create the connector. It appears in the **Connectors** card and is delivered to the products you ticked.

##  Editing and removing a connector

Click the edit icon next to a connector in the card to open the same wizard with its current values filled in. Changing the authentication method clears any stored secret. Click the remove button next to a connector to delete it; it is withdrawn from every product at the next refresh.
