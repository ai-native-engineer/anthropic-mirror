<!-- source: https://claude.com/plugins/modern-web-guidance -->

# Modern Web Guidance

Keep your coding agent up to date with the latest web best practices

  [Google Chrome](https://developer.chrome.com)

  22

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Modern Web Guidance embeds up-to-date web platform expertise directly into your coding agent's context. Backed by the Google Chrome team, it covers 102 modern web features across CSS & Layout, HTML & DOM, and JavaScript & APIs, plus 129 real-world developer use cases spanning accessibility, forms, performance, and UI components. The plugin steers your agent toward native browser APIs and modern standards instead of legacy patterns or unnecessary dependencies.

The skill uses an offline, CPU-efficient search model to find relevant guides — no API keys required. It distinguishes between "Baseline Widely available" features that need no fallbacks and newer features that require progressive enhancement, providing nuanced fallback recommendations for each. Evaluation results show agents improve from roughly 50–57% accuracy without guidance to 78–88% with it.

**How to use:** The skill activates automatically when your agent works on web UI, layout, scroll/motion features, performance optimization, or Web APIs. You can also invoke it directly:

* Ask your agent to implement a feature — e.g., `"Add a popover menu using modern web APIs"` — and the skill will search for and retrieve the latest best-practice guide before writing code.
* Use `/modern-web-guidance` to explicitly trigger a search for guidance on a specific web feature or use case.
* Ask about specific modern features like View Transitions, Container Queries, Popover API, Anchor Positioning, or scroll-driven animations, and the agent will consult the latest standards-based patterns.

Works across frameworks (React, Vue, Angular) by adapting framework-agnostic guidance to your specific setup. Runs entirely offline with no external API calls — anonymous telemetry can be disabled via `DISABLE_TELEMETRY=1`.
