<!-- source: https://claude.com/plugins/crowdsec -->

# CrowdSec

Operational skill for installing, configuring, operating, and debugging CrowdSec (cscli, LAPI/CAPI, hub, bouncers, WA...

* Install in

  [Claude Code](#)
* Made by

  [CrowdSec](https://www.crowdsec.net)
* Installs

  42

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

An operational skill that turns Claude into a hands-on CrowdSec operator. Install, configure, manage, and debug the CrowdSec Security Engine directly from your terminal — across bare-metal/systemd, Docker, and Kubernetes environments. Covers the full operational lifecycle: installation and upgrades, hub collection management, bouncer deployment (iptables, nftables, nginx, traefik, caddy, haproxy, apache), WAF/AppSec setup, Console enrollment, LAPI/CAPI connectivity, and fail2ban migration.

The skill automatically detects your environment, verifies you're running an up-to-date version from the official repository, and routes your requests to the right operational workflow. It enforces safety confirmations before destructive operations like purging all decisions or mutating firewall state. Covers troubleshooting for parsing failures, missing alerts, and blocking issues with structured diagnostic steps.

**How to use:** Simply describe what you need in natural language. Try prompts like `"Install CrowdSec and set up the nginx bouncer"`, `"Enroll my Kubernetes cluster in the CrowdSec Console"`, `"Enable the WAF/AppSec component for my web app"`, `"Why isn't CrowdSec detecting SSH brute-force attacks?"`, `"Migrate my fail2ban setup to CrowdSec"`, or `"Check CrowdSec health and show me current metrics"`.

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

1134112

installs](https://claude.com/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

1009371

installs](https://claude.com/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

438525

installs](https://claude.com/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

417801

installs](https://claude.com/plugins/context7)
