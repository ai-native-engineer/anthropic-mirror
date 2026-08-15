<!-- source: https://claude.com/blog/whats-new-in-claude-managed-agents -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

# New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  [Claude Platform](https://claude.com/platform/api)
* Date

  June 9, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/whats-new-in-claude-managed-agents

Starting today, [Claude Managed Agents](https://claude.com/blog/claude-managed-agents) can run on a schedule and securely access CLI tools and other authenticated services. Both features are now available in public beta on the Claude Platform.

## **Scheduled deployments: Run agents on a schedule**

Agents can now run on a schedule, completing routine work automatically. A [scheduled deployment](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) runs a Claude Managed Agent on a cron schedule. Each time the schedule fires, the agent starts a new session and completes its task, with no scheduler for you to build or host.

Use it for recurring work like a nightly data sync, a weekly compliance scan, or a daily digest. Once a deployment is live, you can pause, resume, or archive it at any time, or trigger additional runs on demand.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2704ab5b6bc1de3bb952fc_Claude-Console-Scheduled-Deployments.png)

Teams are already using scheduled deployments to automate recurring work:

* [Rakuten](https://claude.com/customers/rakuten-qa) uses scheduled deployments to analyze spreadsheet data and produce reports and decks on a weekly or monthly schedule. Teams also monitor production logs and metrics, allowing product managers to see application health without creating a dashboard.
* [Actively AI](https://actively.ai/) uses Managed Agents to power cross-account agentic search for sales teams. Scheduled deployments refresh answers regularly, simplifying their stack by replacing scheduling infrastructure the team initially built themselves.[‍](https://ando.so)
* [Ando](https://ando.so) uses scheduled deployments to keep hiring and sales teams moving. Agents autonomously watch channels for proposed next steps, follow up when they're due, and send meeting reminders.

## **Vaults: store environment variables to authenticate CLIs and other tools**

[Vaults](https://platform.claude.com/docs/en/managed-agents/vaults) securely store environment variables and credentials for Claude Managed Agents. At runtime, agents access secrets like API keys as environment variables, so they can authenticate CLI tools and other services without hardcoding credentials into prompts or code.

Agents [connect to external systems](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) through direct API calls, CLIs, and MCP. CLIs let agents drive existing command-line tools directly through a shell, making them a fast, lightweight integration path. Register an API key with an environment variable name and the domains it can reach, and the CLIs installed in an agent's sandbox can use it to make authenticated API calls.

The agent never sees your key because the sandbox only holds a placeholder. The real key is attached at the network boundary, and only on requests to domains you allow, so it only goes where you’ve approved. To change a key, update it in the vault, and running sessions will pick up the new value on their next call. Most CLIs that send their key in an HTTP request work this way, including the Browserbase, KERNEL, Notion, Ramp, and Sentry CLIs. [Browserbase](https://docs.browserbase.com/integrations/anthropic/managed-agents/quickstart) and [KERNEL](https://www.kernel.sh/docs/integrations/claude-managed-agents) give Managed Agents browser capabilities for the first time, so agents can navigate and interact with the web alongside their other tools.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a27074e40b19ba74e79b134_Claude-Managed-Agents-CLI-credential-vaults-diagram%20(1).png)

Teams are using environment variables in vaults to give agents secure access to authenticated tools:

* [Notion](https://claude.com/customers/notion-qa) uses environment variables in vaults to roll out its CLI alongside MCP tools, adding file-upload capabilities to its agents without API tokens ever being handed to the model.
* [Browserbase](https://www.browserbase.com/) built its public catalog of browser skills using the [browse CLI](https://www.npmjs.com/package/browse), authenticated through vaults. A scheduled deployment periodically validates the catalog to keep it accurate.
* [KERNEL](https://www.kernel.sh/docs/integrations/claude-managed-agents) uses environment variables in vaults to securely connect agents to the databases where it tracks usage and customer conversations. The agent flags usage surges as they happen, so the team can confirm with customers if the activity is intended.[‍](https://getmilana.ai/)
* [Milana](https://getmilana.ai/) uses environment variables in vaults to securely connect its AI product engineer to a customer's codebase. The agent finds and fixes bugs automatically, with large-scale data analysis running faster than before.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

“Environment variables in vaults let us securely roll out the Notion CLI, meeting our security team’s strict guidelines by ensuring sensitive API tokens are never handed to agents. The CLI is complementary to MCP tools, enabling file-upload capabilities in Claude Managed Agents.”

Quan Nguyen, Public API Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

“Teams across Rakuten use scheduled deployments to analyze data in a spreadsheet and produce a report or deck on a weekly or monthly schedule. Our power users put it on production logs and metrics, so a product manager can see the health of their application without creating an analytics dashboard.”

Yusuke Kaji, General Manager of AI for Business

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcd77828fd211e8ca469_ando-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a1edcdb9e60b6c1a29d80cb_ando-dark.svg)

“Most of our users prefer to work with fewer agents rather than many. With scheduled deployments, they can bundle more capabilities into one autonomous agent. For example, an agent can watch multiple sales and hiring processes, check in with the right people for updates, and push next steps along.”

Sara Du, Founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21d94491a062e83ceac776_actively_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21d9473660bc98f662b338_actively_dark.svg)

“We built a cross-account agentic search system on Claude Managed Agents that lets sales teams ask things like which accounts to reach out to today. Since customers want those answers refreshed regularly, we replaced the scheduling infrastructure we'd built ourselves with scheduled deployments, which greatly simplified our stack and improved our product cycles.”

Mihir Garimella, Co-founder

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21c12cb4f396accc11370b_milana_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a21c12f2f12836173fd5883_milana_dark.svg)

“With Claude Managed Agents, we grounded our agent on a customer's actual codebase. We found it easy to work with and got high-quality results almost instantly. The key unlock was environment variables in vaults, which let our agent invoke private APIs through a CLI without exposing credentials. Large-scale data analysis is now dramatically faster, and with outcomes we can ensure the quality of every output.”

Raghav Sethi, Co-founder & CTO

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a17890e390d07357c12beba_logo_browserbase-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a17891ccfcb6c4d6dcb3ce0_logo_browserbase-dark.svg)

“Environment variables in vaults enabled our engineering team to combine two major compute primitives: the agent and the browser. At Browserbase, we used Claude Managed Agents with the browse CLI to generate our public catalog of browser skills that help agents navigate the web, and scheduled deployments run periodic validation on our public catalog.”

Ziray Hao, Product Lead

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28b0dd0f38383998beeebe_logo-kernel-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a28b0e712c7ce11a06c9665_logo-kernel-dark.svg)

Usage on Kernel's browser infrastructure can surge quickly, often right after a customer deploys. With environment variables in vaults, our agent now connects directly to the databases where we track usage and customer conversations. It pulls 30 days of daily usage in seconds, flags surges as they happen, and helps our team confirm with customers that the activity is intended.

Catherine Jue, Co-founder & CEO

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## **Getting started**

Explore our [documentation](https://platform.claude.com/docs/en/managed-agents/overview) to learn more or visit the [Claude Console](https://platform.claude.com/) to deploy your first agent.

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

Aug 13, 2026

### Claude Tag now reads even more of the room

Product announcements

[Claude Tag now reads even more of the room](#)Claude Tag now reads even more of the room

[Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room)Claude Tag now reads even more of the room

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

Nov 20, 2025

### What’s new in Claude: Turning Claude into your thinking partner

Product announcements

[What’s new in Claude: Turning Claude into your thinking partner](#)What’s new in Claude: Turning Claude into your thinking partner

[What’s new in Claude: Turning Claude into your thinking partner](https://claude.com/blog/your-thinking-partner)What’s new in Claude: Turning Claude into your thinking partner

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

Aug 12, 2026

### The Claude in Chrome side panel is now Claude Cowork

Product announcements

[The Claude in Chrome side panel is now Claude Cowork](#)The Claude in Chrome side panel is now Claude Cowork

[The Claude in Chrome side panel is now Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel)The Claude in Chrome side panel is now Claude Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Aug 11, 2026

### Compliance API coverage extends to Claude Cowork and Claude Code

Enterprise AI

[Compliance API coverage extends to Claude Cowork and Claude Code](#)Compliance API coverage extends to Claude Cowork and Claude Code

[Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)Compliance API coverage extends to Claude Cowork and Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Platform

Agents
