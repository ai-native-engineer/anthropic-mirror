<!-- source: https://claude.com/resources/articles/organization-skills-and-directory -->

In October, we introduced [skills](https://claude.com/resources/articles/skills)—a way to teach Claude repeatable workflows tailored to how you work. Today we're making skills easier to deploy, discover, and build: organization-wide management for admins; a directory of partner-built skills from Notion, Canva, Figma, Atlassian, and others; and an open standard so skills work across AI platforms.

## **Manage skills across your organization**

Claude Team and Enterprise plan admins can now provision skills centrally from admin settings. Admin-provisioned skills are enabled by default for all users. Users can still toggle individual skills off if they choose. This gives organizations consistent, approved workflows across teams while letting individual users customize their experience.

![](https://assets.claude.com/9c64e79724254d88623b70d69e969db6bfbf5a87.png)

## **Discover, create, and edit new skills**

Creating skills is now simpler. Describe what you want and Claude helps build it, or write instructions directly. For complex workflows, upload skill folders or use the skill-creator. Claude can also help you edit existing skills, and new previews show full contents so you can understand exactly what a skill does before enabling it.

## **Skills directory**

A growing collection of partner-built skills is now available at [claude.com/connectors](https://claude.com/connectors).

Admins can provision these partner skills across their organization, giving teams immediate access to workflows for tools they already use without any custom development.

![Sentry](https://assets.claude.com/410f375f04040180bb6545e287b4ad178b0d7767.svg)

> “MCP gave us an open foundation for bringing Sentry’s context to developers wherever they work. With skills we can turn that context into focused workflows, and plugins make them easy to ship and keep updated. We’re excited to see how teams use these to build applications and debug issues faster.”

Cody De Arkland, Head of Developer Experience

![Vercel](https://assets.claude.com/f6f5598aac3be6fd9b2dfc23eced7509c90d387b.svg)

> “Skills are a powerful way to extend Claude from figuring out a task to actually doing it. Vercel wants to enable everyone to ship sites, apps, and agents. We built the Vercel Deploy Skill alongside the Claude team to allow more people to go from idea to production.”

Andrew Qu, Chief of Software

![Zapier](https://assets.claude.com/76ec34d2d040fb1dd2dd94a7950788e0a82a09b6.svg)

> “By combining skills with Zapier MCP, organizations get AI that not only knows how work should be done, but actually does it reliably. Skills encode repeatable procedures and best practices; Zapier MCP Tools run them at scale across thousands of apps. The result is faster turnaround, reduced busywork, and repeatable AI-powered processes.”

Lisa Chapello, Head of AI Platform

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Atlassian’s skills bring our decades of teamwork expertise and best practices to Claude. Now Claude doesn’t just see Jira tickets or Confluence pages, it knows what to do: turning specs into backlogs, generating status reports, surfacing company knowledge, triaging issues, and more.”

Josh Devenny, Head of Product, Rovo Skills

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “With Skills, Claude now understands how to work within Canva - not just connect to it. Anyone can create full multi-platform campaigns, generate on-brand presentations, and translate content, all with a single, simple prompt.”

Anwar Haneef, GM & Head of Ecosystem

![Cloudflare](https://assets.claude.com/83dfc3198647a89c08d4b24793456334fa24136a.svg)

> “Skills have made it possible to one-shot deploying AI Agents and MCP servers onto Cloudflare. We're really excited for people to deploy the apps onto Region:Earth from a quick chat.”

Kate Reznykova, Engineering Manager, Cloudflare Agents

![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

> “Figma skills help teams build higher quality, differentiated products with Claude Code. Now, Claude can better understand the context, details, and intent of designs in Figma and translate those designs into code with accuracy and consistency.”

Emil Sjölander, Director of Dev Tools

![Sentry](https://assets.claude.com/410f375f04040180bb6545e287b4ad178b0d7767.svg)

> “MCP gave us an open foundation for bringing Sentry’s context to developers wherever they work. With skills we can turn that context into focused workflows, and plugins make them easy to ship and keep updated. We’re excited to see how teams use these to build applications and debug issues faster.”

Cody De Arkland, Head of Developer Experience

![Vercel](https://assets.claude.com/f6f5598aac3be6fd9b2dfc23eced7509c90d387b.svg)

> “Skills are a powerful way to extend Claude from figuring out a task to actually doing it. Vercel wants to enable everyone to ship sites, apps, and agents. We built the Vercel Deploy Skill alongside the Claude team to allow more people to go from idea to production.”

Andrew Qu, Chief of Software

![Zapier](https://assets.claude.com/76ec34d2d040fb1dd2dd94a7950788e0a82a09b6.svg)

> “By combining skills with Zapier MCP, organizations get AI that not only knows how work should be done, but actually does it reliably. Skills encode repeatable procedures and best practices; Zapier MCP Tools run them at scale across thousands of apps. The result is faster turnaround, reduced busywork, and repeatable AI-powered processes.”

Lisa Chapello, Head of AI Platform

![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)

> “Atlassian’s skills bring our decades of teamwork expertise and best practices to Claude. Now Claude doesn’t just see Jira tickets or Confluence pages, it knows what to do: turning specs into backlogs, generating status reports, surfacing company knowledge, triaging issues, and more.”

Josh Devenny, Head of Product, Rovo Skills

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “With Skills, Claude now understands how to work within Canva - not just connect to it. Anyone can create full multi-platform campaigns, generate on-brand presentations, and translate content, all with a single, simple prompt.”

Anwar Haneef, GM & Head of Ecosystem

![Cloudflare](https://assets.claude.com/83dfc3198647a89c08d4b24793456334fa24136a.svg)

> “Skills have made it possible to one-shot deploying AI Agents and MCP servers onto Cloudflare. We're really excited for people to deploy the apps onto Region:Earth from a quick chat.”

Kate Reznykova, Engineering Manager, Cloudflare Agents

1/7

## **An open standard**

We're also publishing [Agent Skills](https://agentskills.io) as an open standard. Like MCP, we believe skills should be portable across tools and platforms—the same skill should work whether you're using Claude or other AI platforms. We've been collaborating with members of the ecosystem, and we're excited to see early adoption of the standard.

## **Getting started**

* **Claude Apps:** Browse the [skills directory](https://claude.com/connectors) and enable in Settings > Capabilities > Skills.
* **Claude Code:** Install from the plugin directory or check skills into your repository.
* **Claude Developer Platform (API):** Use skills via the /v1/skills endpoint. See [documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Admins can provision skills org-wide through Admin Settings. Skills require [Code Execution and File Creation](https://claude.ai/settings/capabilities) to be enabled.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
