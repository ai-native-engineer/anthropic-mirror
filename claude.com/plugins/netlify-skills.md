<!-- source: https://claude.com/plugins/netlify-skills -->

# Netlify Skills

Netlify platform skills for Claude Code — functions, edge functions, blobs, database, image CDN, forms, config, CLI, ...

* Install in

  [Claude Code](#)

  [Netlify](https://www.netlify.com)
* Installs

  3728

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

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

## Related plugins

[### Frontend Design

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

Anthropic verified

948012

installs](/plugins/frontend-design)

[### Superpowers

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

855112

installs](/plugins/superpowers)

[### Code Review

AI code review with specialized agents and confidence-based filtering for pull requests

Anthropic verified

383892

installs](/plugins/code-review)

[### Context7

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

377529

installs](/plugins/context7)
