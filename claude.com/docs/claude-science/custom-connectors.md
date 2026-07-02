<!-- source: https://claude.com/docs/claude-science/custom-connectors -->

In **Settings > Connectors** > **Add connector**, choose Remote or Local command and enter a **Name** (lowercase letters, digits, hyphens). For Remote, enter the server URL; Advanced settings covers transport (**SSE** or **Streamable HTTP**), OAuth client settings, and the **Headers helper command**. For Local command, enter the command; Advanced settings covers arguments and environment variables. **Browse Connectors Directory** opens the public directory.
Remote servers that need login take you through the provider’s sign-in page.
Every tool from a custom connector starts at **Ask each time**. On the connector’s page, set individual tools to **Always allow** or **Block** under **Tools**, or turn on Skip approvals for the whole connector.

Skip approvals disables the per-call card for every tool on that connector. Only use connectors from developers you trust.

Local-command connectors run inside the sandbox with the same network limits as Claude’s code and a per-connector writable directory. Environment variables for local connectors are saved unencrypted in a configuration file readable by your account only; don’t put high-value secrets there.

[Literature access](/docs/claude-science/literature-access)[Enable Claude Science](/docs/claude-science/enable-claude-science)
