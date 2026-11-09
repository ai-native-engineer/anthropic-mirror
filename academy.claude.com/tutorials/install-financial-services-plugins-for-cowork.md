<!-- source: https://academy.claude.com/tutorials/install-financial-services-plugins-for-cowork -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Install financial services plugins for Claude

Add Anthropic's open-source financial services plugins to Claude for financial modeling, equity research, investment banking, private equity, and fund administration workflows.

3 minClaude Cowork

[Open Cowork](https://claude.ai/new?surface=cowork)

![](https://academy.claude.com/assets/v1/thumbnail.light-hiukxeka.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-j0tcbi0h.png)

We offer a set of open-source plugins that extend Claude with specialized capabilities for financial services workflows, including financial modeling, equity research, investment banking, private equity, and fund administration.

These plugins are available in a [**public GitHub repository**(opens in new tab)](https://github.com/anthropics/financial-services) that you can add as a marketplace in Claude.

## What's included[](#whats-included)

The repository contains a **core plugin** and several **add-on plugins** that build on it:

* **Financial analysis** (core) — Build comparable company analyses, DCF models, LBO models, and 3-statement financials. This plugin also includes all shared MCP connectors for financial data providers. **Add this first.**
* **Investment banking** — Draft CIMs, teasers, and process letters. Build buyer lists, run merger models, and create strip profiles.
* **Equity research** — Write earnings updates and initiating coverage reports. Track catalysts and screen for new ideas.
* **Private equity** — Source and screen deals, run due diligence checklists, draft IC memos, and monitor portfolio company KPIs.
* **Fund administration** — Reconcile the general ledger, trace breaks, prepare accruals and roll-forwards, write variance commentary, and tie out NAV.
* **Operations** — Parse KYC documents and check them against a rules grid.

The repository also includes partner-built plugins from **LSEG** and **S&P Global**, which bring their financial data and analytics directly into Claude.

## Add the marketplace[](#add-the-marketplace)

1. Open Claude.
2. Go to **Customize > Plugins > Add > Add marketplace**.
3. Select **Browse Anthropic sources**.
4. Select **Add** next to Financial Services, then select **Done**.
5. Once the marketplace is added, its plugins are available for you to add.

On a Team or Enterprise plan, you won't see **Browse Anthropic sources**. An admin adds Financial Services for the whole organization from **Organization settings > Plugins & skills**.

## Add plugins[](#add-plugins)

1. On the **Plugins** page, find the financial services plugins.
2. Select the **financial analysis** plugin, then **Add**. Add this one first, because it is the core plugin that provides shared tools and data connectors used by all other plugins.
3. Add any additional plugins based on your workflow needs.
4. If a plugin has connectors, connect them when asked.

Once added, plugins activate automatically. Skills are applied when relevant, or you can invoke them manually during your session by typing "/" or clicking the "+" button.

## Available Skills[](#available-skills)

After you add them, you can use Skills like:

* /comps [company] — Run a comparable company analysis
* /dcf [company] — Build a DCF valuation model
* /earnings [company] [quarter] — Generate a post-earnings update report
* /one-pager [company] — Create a one-page company profile
* /ic-memo [project name] — Draft an investment committee memo
* /source [criteria] — Source deals based on criteria

## MCP connectors[](#mcp-connectors)

The financial analysis core plugin includes connectors for third-party financial data providers such as Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and Egnyte.

Access to these connectors may require a separate subscription or API key from the respective provider. Contact your data provider for details.

## Customize plugins for your firm[](#customize-plugins-for-your-firm)

These plugins are designed as starting points. You can customize them to match your firm's workflows. Ask Claude to customize a plugin for your firm, or edit the plugin files in your own copy of the repository:

* Add your firm's terminology, processes, and formatting standards to skill files.
* Swap or add MCP connectors to point at your specific data providers.
* Adjust workflow instructions to reflect how your team does analysis.
* Use /ppt-template to teach Claude your firm's branded PowerPoint layouts.

When Claude makes the changes, it shows the result as a file card. Select **Save plugin** to add it to your account.

## Good to know[](#good-to-know)

* Plugins are file-based. A skill can include executable scripts (Python, JavaScript, or Bash) in an optional `scripts/` directory, and you can still customize a plugin without writing code or setting up infrastructure.
* These plugins work across both Claude and Claude Code.
* AI-generated financial analysis should always be reviewed by qualified professionals before being used in decision-making.

## Learn more[](#learn-more)

See our blog post for more information: [**Cowork and plugins for finance**(opens in new tab)](https://claude.com/blog/cowork-plugins-finance).

* [What's included](#whats-included)
* [Add the marketplace](#add-the-marketplace)
* [Add plugins](#add-plugins)
* [Available Skills](#available-skills)
* [MCP connectors](#mcp-connectors)
* [Customize plugins for your firm](#customize-plugins-for-your-firm)
* [Good to know](#good-to-know)
* [Learn more](#learn-more)
