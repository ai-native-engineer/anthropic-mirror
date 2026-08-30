<!-- source: https://academy.claude.com/help/mcp -->

[Academy](https://academy.claude.com/)

# Use Claude Academy from Claude

Claude Academy is Anthropic’s free learning site for Claude. The Claude Academy connector lets Claude search Academy’s courses, tutorials and use cases and read them for you in the conversation — read-only, free, no account or sign-in.

* [What the connector does](#what-it-does)
* [How to add it](#add)
* [Try these prompts](#prompts)
* [Troubleshooting](#troubleshooting)
* [Privacy](#privacy)
* [Support](#support)

## What the connector does

The connector is a Model Context Protocol (MCP) server at `https://academy.claude.com/mcp` with three read-only tools. Ask for a course on a topic, browse what is available for a product, or open a tutorial and work through it with Claude. Every answer links back to academy.claude.com so you can continue on the site.

### Search Claude Academy `search_academy`

Keyword search across courses, lessons, tutorials and use cases, optionally limited to one kind of content or one product. Returns ranked results with links.

### Get a Claude Academy item `get_content`

Reads one item by its Academy path or URL. Tutorials and use cases come back in full; a course returns its summary, objectives and ordered lesson list; a lesson returns its summary, objectives and outline — read the lesson itself on the site.

### List Claude Academy content `list_content`

Lists everything published on Academy, optionally filtered by kind or product. Courses show their lesson count; lessons are listed only when you ask for kind=lesson (or through their course).

Content is English-language; Academy’s translated pages are not searched. You can filter by kind (course, lesson, tutorial, use case) and by product — Claude.ai, Claude Cowork, Claude Code, the Claude Platform and the other products Academy covers.

## How to add it

### Claude.ai and Claude Desktop

1. Open [Customize → Connectors(opens in new tab)](https://claude.ai/customize/connectors) and choose **Discover**.
2. Find **Claude Academy** and click **Connect**. There is nothing to sign in to — it is ready immediately.
3. In a chat, open the tools menu and make sure Claude Academy is enabled.

On Team and Enterprise plans an organization owner or admin may need to enable the connector for the organization first. If it is not in the directory yet, add it as a custom connector named “Claude Academy” with the URL `https://academy.claude.com/mcp`.

### Claude Cowork

Cowork uses the same connectors as Claude.ai: connect it once under [Customize → Connectors(opens in new tab)](https://claude.ai/desktop/customize/connectors) and it is available in Cowork sessions.

### Claude Code

`claude mcp add --transport http claude-academy https://academy.claude.com/mcp`

Then `/mcp` inside Claude Code shows it as connected.

### Other MCP clients

It is a standard Streamable HTTP server. Opening [https://academy.claude.com/mcp(opens in new tab)](https://academy.claude.com/mcp) in a browser returns a ready-to-paste JSON configuration snippet.

## Try these prompts

* “Search Claude Academy for courses about building MCP servers and give me the links.”

  search\_academy
* “List every Academy tutorial for Claude Cowork.”

  list\_content
* “Open the Academy tutorial at https://academy.claude.com/tutorials/creating-your-first-skill and walk me through it step by step.”

  get\_content
* “What does the Claude Code 101 course cover? Show me its lesson list.”

  get\_content
* “Which Academy courses are about AI fluency for educators?”

  search\_academy

## Troubleshooting

### Claude Academy is not responding, or shows a connection error

The endpoint is `https://academy.claude.com/mcp` exactly (a trailing slash is fine). Opening it in a browser should show a short JSON configuration — if that works, the server is up and the problem is on the client side: check that the connector is enabled in the chat’s tools menu or, in Claude Code, run `/mcp`. If your network blocks academy.claude.com, ask your IT team to allow it.

### Claude says it cannot find something that is on the site

Search covers English content only, and the index refreshes with each site release, so very new content can lag briefly. Try a broader keyword, or give Claude the page URL and ask it to read that page.

### A lesson came back as an outline only

By design: lessons return their summary, objectives and outline; tutorials and use cases return their full text. Follow the link to read the lesson on academy.claude.com.

### “not\_found” or “invalid\_path” when opening a URL

Reading an item uses the path of the link you give, for example `/tutorials/…`, `/courses/…` or `/use-cases/…` on academy.claude.com, or the full URL starting with https://; a typo gives not\_found. Check the link, or search first and use a result’s URL.

### My progress, badges and certificates are missing

The connector only reads public learning content. Sign in at academy.claude.com for your progress, badges and certificates.

## Privacy

The connector is anonymous: there is no account, sign-in or token, and it does not know who you are or see your conversation. It receives only the search words or page path Claude sends for a tool call and returns public Academy content. Server logs record which tool was called, the filter values used, the Academy page that was read, how many results came back or an error code, and the MCP client’s reported name and version — never the search text or who you are.

Anthropic’s [Privacy Policy(opens in new tab)](https://www.anthropic.com/legal/privacy) and [Usage Policy(opens in new tab)](https://www.anthropic.com/legal/aup) apply.

## Support

Questions or problems with the connector: use the support messenger in the corner of any Academy page, or start with the [Claude Academy FAQ](https://academy.claude.com/help/faq). Found a mistake in a course or tutorial Claude read to you? Send us the page and the snippet through the messenger and we will route it to the content team.

For developers

The server is stateless and POST-only; one request is one JSON-RPC message, and auth-discovery probes get a JSON 404 because there is no authentication.

* [What the connector does](#what-it-does)
* [How to add it](#add)
* [Try these prompts](#prompts)
* [Troubleshooting](#troubleshooting)
* [Privacy](#privacy)
* [Support](#support)
