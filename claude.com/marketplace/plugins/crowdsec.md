<!-- source: https://claude.com/marketplace/plugins/crowdsec -->

An operational skill that turns Claude into a hands-on CrowdSec operator. Install, configure, manage, and debug the CrowdSec Security Engine directly from your terminal — across bare-metal/systemd, Docker, and Kubernetes environments. Covers the full operational lifecycle: installation and upgrades, hub collection management, bouncer deployment (iptables, nftables, nginx, traefik, caddy, haproxy, apache), WAF/AppSec setup, Console enrollment, LAPI/CAPI connectivity, and fail2ban migration.

The skill automatically detects your environment, verifies you're running an up-to-date version from the official repository, and routes your requests to the right operational workflow. It enforces safety confirmations before destructive operations like purging all decisions or mutating firewall state. Covers troubleshooting for parsing failures, missing alerts, and blocking issues with structured diagnostic steps.

**How to use:** Simply describe what you need in natural language. Try prompts like `"Install CrowdSec and set up the nginx bouncer"`, `"Enroll my Kubernetes cluster in the CrowdSec Console"`, `"Enable the WAF/AppSec component for my web app"`, `"Why isn't CrowdSec detecting SSH brute-force attacks?"`, `"Migrate my fail2ban setup to CrowdSec"`, or `"Check CrowdSec health and show me current metrics"`.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
