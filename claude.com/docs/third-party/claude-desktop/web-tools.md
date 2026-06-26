<!-- source: https://claude.com/docs/third-party/claude-desktop/web-tools -->

Claude Desktop includes two built-in tools for reaching the web:

* **Web Search** runs a search-engine query and returns ranked results.
* **Web Fetch** retrieves the contents of a specific URL.

In Claude Desktop on third-party (3P), both are subject to your configuration: search depends on your inference provider, and fetch is gated by the sandbox network allowlist.

##  Web Search

Web Search is a **server-side tool** executed by your inference provider, not by the desktop app. Availability depends on which provider you’ve configured:

| Provider | Web Search |
| Google Cloud’s Vertex AI | Available |
| Microsoft Foundry | Available |
| Amazon Bedrock | Not available |
| Anthropic API | Available |
| Gateway | Available if your gateway implements Anthropic’s `web_search` server tool |

Because the search runs on the provider’s infrastructure, queries and results travel over the same path as model inference and are subject to your provider’s data-handling terms. No additional firewall rules are needed beyond the inference endpoint itself.

`coworkEgressAllowedHosts` does **not** apply to Web Search. The allowlist governs client-side egress — Web Fetch and in-sandbox shell network activity — while search executes server-side at your inference provider. To let the agent fetch pages it finds via search, add the relevant hosts to `coworkEgressAllowedHosts` or set it to `["*"]`. To disable search, add `"WebSearch"` to `disabledBuiltinTools`.

###  Workarounds for Bedrock

Amazon Bedrock does not implement Anthropic’s `web_search` server tool. Two common patterns restore search:

* **Route through a LiteLLM gateway.** Configure `inferenceProvider: "gateway"` pointing at a LiteLLM instance that fronts Bedrock, and enable LiteLLM’s web-search handling so the gateway executes search on the model’s behalf. See LiteLLM’s [proxy configuration for Claude web search](https://docs.litellm.ai/docs/tutorials/claude_code_websearch#proxy-configuration). This keeps the built-in Web Search tool working unchanged and is a common pattern in production deployments.
* **Add a search MCP server.** Deploy a search server via [`managedMcpServers`](/docs/third-party/claude-desktop/configuration#managedmcpservers) — for example [Brave Search MCP](https://github.com/brave/brave-search-mcp-server) (requires a Brave Search API key) or [Exa](https://exa.ai/mcp) — and add `"WebSearch"` to `disabledBuiltinTools` so the model uses the MCP tool instead.

The same options apply if your provider supports search but you want a different backend.

##  Web Fetch

Web Fetch runs in the Claude Desktop main process on the user’s device. The model supplies only the target URL; it cannot set headers, a request body, or credentials. Every fetch, including redirect targets, is checked against `coworkEgressAllowedHosts` before the request is sent.
By default, the sandbox can reach only your inference provider’s endpoint, so Web Fetch will fail for any other host unless you’ve allowed it. To permit fetches:

| Goal | Set `coworkEgressAllowedHosts` to |
| Allow specific domains | `["docs.example.com", "*.example.corp"]` |
| Allow all hosts (no sandbox filtering) | `["*"]` |
| Block all fetches | `[]` and add `"WebFetch"` to `disabledBuiltinTools` |

Wildcards match one or more leading subdomain labels (`*.example.com` matches `a.example.com` and `a.b.example.com`, but not `example.com`).

`coworkEgressAllowedHosts` controls what the agent’s tools can reach. Your perimeter firewall is a separate, outer layer, so a host allowed by this key still won’t be reachable if your corporate network blocks it. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry#required-egress-paths) for the distinction.

The same allowlist governs other in-sandbox network activity (for example, `curl` or `pip install` from the agent’s shell), not just the Web Fetch tool.

##  Disabling web tools

To remove web tools entirely, add them to `disabledBuiltinTools`:

["WebSearch", "WebFetch"]

With both disabled and `coworkEgressAllowedHosts` empty, the agent has no path to the public internet from inside the sandbox. It can still read and write local files, run code against them, and call any MCP servers you’ve provisioned. See the [Locked down profile](/docs/third-party/claude-desktop/configuration#recommended-security-profiles).

[Connect to Microsoft 365](/docs/third-party/claude-desktop/connectors-m365)[Desktop and filesystem access](/docs/third-party/claude-desktop/local-access)
