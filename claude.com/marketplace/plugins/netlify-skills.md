<!-- source: https://claude.com/marketplace/plugins/netlify-skills -->

Provides comprehensive Netlify platform knowledge directly in Claude Code. This plugin bundles 12 factual, up-to-date skill references covering the full Netlify ecosystem — serverless functions, edge functions, Blobs object storage, managed Postgres (Netlify DB), Image CDN, forms, caching, configuration, CLI and deployment, framework adapters, and AI Gateway. Each skill is loaded on demand when relevant, giving Claude precise guidance on modern Netlify patterns, APIs, and best practices.

Skills cover practical details like the modern function syntax (`export default async (req, context)`), Drizzle ORM setup for Netlify DB, edge function middleware with Deno runtime, CDN cache control, image transformation URLs, `netlify.toml` configuration, and deployment workflows. The plugin emphasizes current Netlify conventions — v2 functions, `Netlify.env.get()` for environment variables, and framework-aware adapters for Vite, Astro, Next.js, and TanStack.

**How to use:** Once installed, the skills activate automatically when you're working on Netlify projects. Ask Claude to help with any Netlify feature and it will draw on the relevant skill. Example prompts:

* *"Create a serverless function that handles POST requests at /api/submit"*
* *"Set up Netlify DB with Drizzle ORM and create a users table"*
* *"Add an edge function for geolocation-based redirects"*
* *"Configure image CDN transforms for responsive thumbnails"*
* *"Set up caching headers and CDN purging for my API routes"*
* *"Deploy my site with the Netlify CLI and set up environment variables"*
* *"Route AI requests through the Netlify AI Gateway"*

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
