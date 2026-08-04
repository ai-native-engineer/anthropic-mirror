<!-- source: https://claude.com/blog/automate-security-reviews-with-claude-code -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

# Automate security reviews with Claude Code

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Code
* Date

  August 6, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/automate-security-reviews-with-claude-code

Today we're introducing automated security reviews in Claude Code. Using our GitHub Actions integration and a new /security-review command, developers can easily ask Claude to identify security concerns—and then have it fix them.

As developers increasingly rely on AI to ship faster and build more complex systems, ensuring code security becomes even more critical. These new features let you integrate security reviews into your existing workflows, helping you catch vulnerabilities before they reach production.

### Review code for vulnerabilities from your terminal

The new /security-review command lets you run ad-hoc security analyses from your terminal before committing code. Run the command in Claude Code, and Claude will search your codebase for potential vulnerabilities and provide detailed explanations of any issues found.

This command uses a specialized security-focused prompt that checks for common vulnerability patterns including:

* SQL injection risks
* Cross-site scripting (XSS) vulnerabilities
* Authentication and authorization flaws
* Insecure data handling
* Dependency vulnerabilities

You can also ask Claude Code to implement fixes for each issue after they’re identified. This keeps security reviews in your inner development loop, catching issues early when they're easiest to fix.

### Automate security reviews for new pull requests

The new GitHub action for Claude Code takes security reviews a step further by automatically analyzing every pull request when it's opened. When configured, the action:

* Triggers automatically on new pull requests
* Reviews code changes for security vulnerabilities
* Applies customizable rules to filter out false-positives and known issues
* Posts comments inline on the PR with any concerns found, including recommendations for fixes

This creates a consistent security review process across your entire team, ensuring no code reaches production without a baseline security review. The action integrates with your existing CI/CD pipeline and can be customized to match your team's security policies.

![2 screenshots showing vulnerabilities that were caught by Claude Code, leaving comments in GitHub.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcbe_37aa77df52f1a4e8d81f398f48dbb98a5ba1d5ec-1920x1080.png)

### Improving product security at Anthropic

We're using these features ourselves to help secure the code our team ships to production, including Claude Code itself. Since setting up the GitHub action, this has already caught security vulnerabilities in our own code and prevented them from being shipped.

For example, last week, our team built a new feature for an internal tool that relied on starting a local HTTP server meant to accept local connections. The GitHub action identified a remote code execution vulnerability exploitable through DNS rebinding and it was fixed before the PR was ever merged.

![A GitHub comment showing a remote code execution vulnerability](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcc2_a370dba2f6e5095cdbcb23ef878dda4befd61d95-1920x1080.png)

In another case, an engineer built a proxy system to enable secure management of internal credentials. The GitHub action automatically flagged that this proxy was vulnerable to SSRF attacks, and we promptly fixed this issue.

![A GitHub comment showing a SSRF attack vulnerability](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcb8_23dd3b5404c6f7dc812df83a7de95babab286865-1920x1080.png)

### Getting started

Both features are available now for all Claude Code users. To start using automated security reviews:

* **For the /security-review command**: Simply update Claude Code to the latest version and run /security-review in your project directory. [See the documentation](https://github.com/anthropics/claude-code-security-review/tree/main?tab=readme-ov-file#security-review-slash-command) to customize your own version of the command
* **For the GitHub action**: [See the documentation](https://github.com/anthropics/claude-code-security-review) for step-by-step installation and configuration instructions

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

Jul 28, 2026

### Bringing MCP 2026-07-28 to Claude

Product announcements

[Bringing MCP 2026-07-28 to Claude](#)Bringing MCP 2026-07-28 to Claude

[Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

Jul 2, 2026

### Giving admins more visibility and control over Claude spend

Product announcements

[Giving admins more visibility and control over Claude spend](#)Giving admins more visibility and control over Claude spend

[Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend)Giving admins more visibility and control over Claude spend

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

Jun 18, 2026

### Centrally manage authorization for MCP connectors

Enterprise AI

[Centrally manage authorization for MCP connectors](#) Centrally manage authorization for MCP connectors

[Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Sep 10, 2024

### Claude for Enterprise

Product announcements

[Claude for Enterprise](#)Claude for Enterprise

[Claude for Enterprise](https://claude.com/blog/claude-for-enterprise)Claude for Enterprise

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

Claude Code
