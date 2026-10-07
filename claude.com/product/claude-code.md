<!-- source: https://claude.com/product/claude-code -->

# Claude Code

Hand Claude a bug fix, test, or multi-day migration. Steer and review from your terminal, IDE, Slack, or web.

[Download for macOS](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)[Read documentation (opens in new tab)](https://code.claude.com/docs/en/overview)

Available for macOS, Linux, and Windows.

Other ways to use Claude Code:

* [Terminal (opens in new tab)](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)
* [Web (opens in new tab)](https://claude.ai/code)
* [iOS (opens in new tab)](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684)
* [Android (opens in new tab)](https://play.google.com/store/apps/details?id=com.anthropic.claude)
* [GitHub (opens in new tab)](https://code.claude.com/docs/en/github-actions)
* [VS Code (opens in new tab)](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [JetBrains (opens in new tab)](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
* [Slack (opens in new tab)](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

Pinned

Add a dark mode toggle to settings

Scheduled

Weekly dependency audit

Recents

Fix the double-charge bug in checkout

Write tests for the payments module

Explain what this repo does

Layout's broken on mobile

Debug flaky CI tests

Susan Sample

acme-storefront/Fix the double-charge bug in checkout

We're seeing duplicate charges when customers double-click the pay button. Can you find and fix it?

I can reproduce it: the checkout form fires two `POST /charges` requests when the button is clicked twice before the first response lands. Tracing where the idempotency key should be.

just now

Read 3 files, searched the checkout flow

Ran agent · Reproduce the double-submit against a test charge

Root cause: `createCharge()` generates a new idempotency key per call instead of per checkout session, so the gateway treats the second click as a fresh charge. Fixing that and disabling the button while a charge is in flight.

just now

Edited **charges.ts** +9 -3

Auto

OpusExtra high

Pinned

Add a dark mode toggle to settings

Scheduled

Weekly dependency audit

Recents

Fix the double-charge bug in checkout

Write tests for the payments module

Explain what this repo does

Layout's broken on mobile

Debug flaky CI tests

Susan Sample

acme-dashboard/Add a dark mode toggle to settings

Add a dark mode toggle to the settings page. Should remember the choice and follow the system default until they pick one.

There's already a `ThemeProvider` wrapping the app but it's hard-wired to light. I'll lift the mode into context, persist it to `localStorage`, and add a Light / Dark segmented control under **Settings → Appearance**.

just now

Read 4 files, searched the codebase

Edited **ThemeProvider.tsx** +18 -2

src/theme/ThemeProvider.tsx

10`export function ThemeProvider({children}: {children: ReactNode}) {`

11+ `const prefersDark = useMediaQuery('(prefers-color-scheme: dark)')`

12 `const stored = localStorage.getItem('theme')`

13+ `const [mode, setMode] = useState(stored ?? (prefersDark ? 'dark' : 'light'))`

14

15+ `useEffect(() => {`

16+ `localStorage.setItem('theme', mode)`

17+ `}, [mode])`

18

19 `return (`

20 `<ThemeContext.Provider value={{mode, setMode}}>`

21 `{children}`

Edited **settings.tsx** +21 -0

Edited **tokens.css** +24 -0

Ran 2 commands

Done — the **Appearance** section now has the toggle. Preview's on the right; flip it and the whole app should follow. Reduce-motion and density rows are stubbed so the page doesn't look bare.

just now

#112acme-dashboardclaude/settings-dark-mode-Xk4fq CI

Auto

OpusExtra high

localhost:5173/settings

Appearance

Theme

Choose how the dashboard looks.

LightDark

Density

Compact rows for power users.

DefaultCompact

Reduce motion

Disable animations and transitions.

* ![Zapier](https://assets.claude.com/76ec34d2d040fb1dd2dd94a7950788e0a82a09b6.svg)
* ![PagerDuty](https://assets.claude.com/e66fa87cb0236fb0bb7ded4facb4cd6013f01a7f.svg)
* ![Workato](https://assets.claude.com/2fa9dd8ac68a8a9c6348127669c04cb6a7815dda.svg)
* ![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)
* ![Asana](https://assets.claude.com/70b82311c60645181706f46b74bcfc3c712dd4bb.svg)
* ![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)
* ![Databricks](https://assets.claude.com/d46b8e12bcca1888c7cf14a8c0b8b62d98225df1.svg)
* ![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)
* ![Plaid](https://assets.claude.com/40cac5bb60362b9a3d1711447d37e78e78bd547e.svg)
* ![Spotify](https://assets.claude.com/6a77ca9f2ae4ded51e55fcf636be5b5506643666.svg)
* ![StubHub](https://assets.claude.com/d3451a4bfe1c5af7f56f76ab8237c3bab7dd7a9d.svg)
* ![Uber](https://assets.claude.com/ab44ead2b3df736bf289ca296425a2309fc32aac.svg)
* ![Brex](https://assets.claude.com/b6698027075ae08131163eae1022d66d1b0b39dd.svg)
* ![Intercom](https://assets.claude.com/d60d14e07300066206a9765859021f49663f2d38.svg)
* ![Stripe](https://assets.claude.com/0e2493b60dbe1a71a144ca649e1916bade399bf7.svg)
* ![Shopify](https://assets.claude.com/9acc150e16af0c0107fb581c62be2a39ecc178d2.svg)
* ![NASA](https://assets.claude.com/6bdc64f3c9fde30b4b2cecb8544be888a4233887.svg)
* ![Figma](https://assets.claude.com/30df15cbd261edbc52262a1fa2d1339f3a1a372b.svg)

## Get started with Claude Code

IndividualTeam & Enterprise

### Pro

Claude Code is included in your Pro plan. Perfect for short coding sprints in small codebases.

$17

Per month with annual subscription discount ($200 billed up front). $20 if billed monthly.

[Try Claude (opens in new tab)](https://claude.ai/login?plan=pro)

### Max 5x

Claude Code is included in your Max plan. Great value for everyday use in larger codebases.

$100

Per month

[Try Claude (opens in new tab)](https://claude.ai/login?plan=max)

### Max 20x

Even more Claude Code included in your Max plan. Great value for power users with the most access to Claude models.

$200

Per month

[Try Claude (opens in new tab)](https://claude.ai/login?plan=max)

[Usage limits apply](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices). Prices shown don't include applicable tax. Price and plans are subject to change at Anthropic's discretion.

[Usage limits apply](https://support.anthropic.com/en/articles/9797557-usage-limit-best-practices). Price and plans are subject to change at Anthropic's discretion.

## Latest feature announcements

[### **Projects:** Group related coding sessions so you can run and easily supervise multiple Claude agents at once. Available on Claude Code Desktop.

BlogSep 17, 2026](https://claude.com/blog/projects-redesigned)

[### **Auto mode by default:** Claude Code now runs in auto mode by default on Pro, Max, and Team plans, so it can work longer while still catching risky commands.

BlogAug 7, 2026](https://claude.com/blog/auto-mode-default-in-claude-code)

[### **Self-hosted environments:** Run Claude Code sessions on your own infrastructure, inside your network and next to your internal services. Now in public beta.

BlogAug 6, 2026](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute)

[### **Artifacts:** Preview in-progress work as a live, interactive artifact built from your session context, and share it with your team.

BlogJun 18, 2026](https://claude.com/blog/artifacts-in-claude-code)

[View changelog (opens in new tab)](https://code.claude.com/docs/en/changelog)

## What Claude Code can take on

Claude Code builds the plan, asks clarifying questions, and handles work that runs for hours or days.

Get Claude Code

* [Desktop](https://claude.com/download)
* [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
* [On the web](https://claude.ai/code)
* [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh | bash

Or read the [documentation](https://code.claude.com/docs/en/overview)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](https://code.claude.com/docs/en/overview)

OnboardingTriage issuesMigrate code

```
I'm new to this codebase. Can you explain it to me?

⏺︎ I'll analyze the Excalidraw codebase structure and provide a high-level overview.

⏺︎ Analyze(what: "Excalidraw codebase structure and provide a high-level overview of what it is, its main components, and how they're organized. Focus on understanding the project's purpose, architecture, and key features.")

Excalidraw is an open-source virtual whiteboard application with a hand-drawn style. It's designed for creating diagrams, wireframes, and collaborative drawings.

## Purpose
- Web-based drawing tool with infinite canvas
- Hand-drawn aesthetic with support for shapes, arrows, text
- End-to-end encrypted collaboration
- Works offline as a PWA (Progressive Web App)

## Architecture
The project is organized as a monorepo with these main components:

1. Core Package (packages/excalidraw)
- React component library for embedding Excalidraw in any application
- Handles drawing, rendering, and core functionality
- Uses roughjs for the hand-drawn style
- Includes export capabilities (PNG, SVG)

2. Web Application (excalidraw-app/)
- Full-featured web app at excalidraw.com
- Built on top of the core package
- Adds collaboration features, local storage, sharing

3. Support Packages
- common - Shared utilities and constants
- element - Element manipulation and type definitions
- math - Mathematical functions for drawing
- utils - General utility functions

4. Examples
- Integration examples (Next.js, browser script)
- Shows how to embed Excalidraw in different environments

5. Documentation (dev-docs/)
- API documentation
- Integration guides
- Component documentation

## Key Features
- Real-time collaboration with end-to-end encryption
- Export to various formats (PNG, SVG, JSON)
- Customizable drawing tools (rectangle, circle, arrows, freehand)
- Dark mode support
- Localization
- Library of shapes and components
- Arrow bindings and labels
- Image support

## Technology Stack
- React for UI
- TypeScript for type safety
- Firebase for collaboration backend
- Jotai for state management
- Vite for development and building
- IndexedDB/LocalStorage for offline storage

The architecture allows for both using Excalidraw as a component in other applications and as a standalone web application with additional features.
```

* ### Code onboarding

  Claude Code maps and explains entire codebases in a few seconds. It uses agentic search to understand project structure and dependencies without you having to manually select context files.
* ### Turn issues into PRs

  Stop bouncing between tools. Claude Code works with GitHub, GitLab, and your command line tools to read issues, write code, run tests, and open pull requests.
* ### Run multi-hour refactors and migrations

  Claude Code follows imports across the repo, runs your tests, and keeps going when something breaks.

## Meets you where you code

![Claude Code running in a terminal](https://assets.claude.com/d4645137a0c197beee5313fedbf9417d035452fc.webp)

### Start in your terminal

Super powerful terminal integration. Works with all your CLI tools alongside any IDE.

curl -fsSL https://claude.ai/install.sh | bash

Or read the [documentation](https://code.claude.com/docs/en/overview)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](https://code.claude.com/docs/en/overview)

![Claude Code extension in VS Code](https://assets.claude.com/454390de9d9ccefb6082b7c2440c7547c1ec3964.webp)

### Integrate with your editor

Native extensions for VS Code (+ Cursor, Devin Desktop) and JetBrains IDEs.

[VS Code (opens in new tab)](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)[JetBrains (opens in new tab)](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)

![Claude Code on the web](https://assets.claude.com/60bc422c7916679b221ea6d55ba27adc584ac66e.webp)

### Access anywhere

Quick access from browser, mobile app, or Claude on desktop. Great for parallel work or on-the-go coding.

[Open in browser (opens in new tab)](https://claude.ai/code)[Download app](https://claude.com/download)

## Kick off coding tasks in Slack

[Add to Slack (opens in new tab)](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)[Learn more](https://claude.com/claude-for-slack)

## What developers are saying

* ![Ramp](https://assets.claude.com/6db782273272dd89f11df7b54089328994fe718e.svg)

  > “Claude Code has dramatically accelerated our team's coding efficiency. I can now write EDA code in a notebook—pulling data, training a model, and evaluating it with basic metrics—and then ask Claude to convert that into a Metaflow pipeline. This process saves 1-2 days of routine (and often boring!) work per model.”

  Anton Biryukov, Staff Software Engineer

  [Read story](https://claude.com/customers/ramp)
* ![Intercom](https://assets.claude.com/d60d14e07300066206a9765859021f49663f2d38.svg)

  > “With Claude, we're not just automating customer service—we're elevating it to truly human quality. This lets support teams think more strategically about customer experience and what makes interactions genuinely valuable.”

  Fergal Reid, VP of AI

  [Read story](https://claude.com/customers/intercom)
* ![Notion](https://assets.claude.com/19e0cdfaef9d2980bddd19cd993076d62b46c0c7.svg)

  > “Claude Code is moving our team up a level: we decide what needs to happen, and smooth the process so it can build and verify end-to-end. A big part of my job now is to keep as many instances of Claude Code busy as possible.”

  Simon Last, Co-founder

  [Read story](https://claude.com/customers/notion)

* ![GitLab](https://assets.claude.com/9760b31778be76fd66c6b722dced22db12cb59e8.svg)
* ![Dynatrace](https://assets.claude.com/fd2377cce31b2fb5ca8192769f518853a072e2c0.svg)
* ![Kubernetes](https://assets.claude.com/b84d84f9576d1d2e0b4ab65de530ccab8bac0d41.svg)
* ![Heroku](https://assets.claude.com/0ab77011513992a5697712fd2cb8c809f3a88e7e.svg)
* ![Stripe](https://assets.claude.com/0e2493b60dbe1a71a144ca649e1916bade399bf7.svg)
* ![Elastic](https://assets.claude.com/1e6c5ec0a16e29efa8298174620a13235bb414c0.svg)
* ![Terraform](https://assets.claude.com/29f9867e9ce2a0784d68e8f4714faabbc2bb81f2.svg)
* ![Sentry](https://assets.claude.com/410f375f04040180bb6545e287b4ad178b0d7767.svg)
* ![AWS](https://assets.claude.com/723ac3a5a747c466218a5d007ff4839141f462ee.svg)
* ![MongoDB](https://assets.claude.com/45982f0c915b94d8ae0a729f1c24ac69c59cc539.svg)
* ![Atlassian](https://assets.claude.com/4870b3d6c0253cea01b100c98ad2030b8e4f8ce1.svg)
* ![Datadog](https://assets.claude.com/0a17621af2bfc623c9104a3dd9fba2e6ebfc89d5.svg)
* ![GitHub](https://assets.claude.com/ff6655b95f24d2aa0b9bf52c94ef5d5f5e54a70e.svg)
* ![Vercel](https://assets.claude.com/f6f5598aac3be6fd9b2dfc23eced7509c90d387b.svg)
* ![New Relic](https://assets.claude.com/659229862ffd01b50ea108b31624c8c0951bf1a5.svg)

## Connects with your favorite command line tools

Your terminal is where real work happens. Claude Code connects with the tools that power development—deployment, databases, monitoring, version control. Rather than adding another interface to juggle, it enhances your existing stack.

## FAQ

### How do I get started with Claude?

You can access Claude Code with a Claude Pro or Max plan, a Team or Enterprise plan, or a Claude Console account. [Download Claude Code](https://code.claude.com/docs/en/overview) and sign in with your respective Claude or Console credentials.

### What kind of tasks can Claude Code handle?

Claude Code can handle routine work like bug fixes and testing, and larger jobs like refactors and new features that are long-running and asynchronous.

You set the direction as the architect and orchestrator, and Claude Code does the work. Describe what you want and it plans, writes code, runs tests, and opens pull requests. It can work on several tasks at once, and surface decisions you need to make for it to keep going.

### How does Claude Code work with my existing tools?

Claude Code runs in your terminal and works alongside your preferred IDE and development tools without requiring you to change your workflow. Claude Code can also use command line tools (like Git) and MCP servers (like GitHub) to extend its own capabilities using your tools.

### Is Claude Code secure?

Yes. Claude Code runs locally in your terminal and talks directly to model APIs without requiring a backend server or remote code index. It also asks for permission before making changes to your files or running commands.

### What are the system requirements to run Claude Code?

Claude Code works on macOS, Linux, and Windows. [See full system requirements](https://code.claude.com/docs/en/setup#system-requirements).

### How much does Claude Code cost?

When used with a Claude Console account, Claude Code consumes API tokens at [standard API pricing](https://claude.com/pricing#api).

### Does Claude Code work with the Claude desktop app?

Yes. Max, Pro, Team, and Enterprise users can access Claude Code on the [Claude desktop app](https://claude.com/download).

### What is fast mode on Claude Code?

Fast mode is a high-speed configuration for Opus 5.5, making the model 2.5x faster at a higher cost per token. Fast mode is available:

* In research preview on Claude Code, and is priced at $8/$40 per million tokens.
* On consumption-based plans.
* Via usage credits for users on subscription plans.

## Get the technical rundown

[### Claude Code documentation

Developer docs](https://code.claude.com/docs/en/overview)

[### Common workflows

Developer docs](https://code.claude.com/docs/en/common-workflows)

[### Using CLAUDE.md files

Blog](https://claude.com/blog/using-claude-md-files)

[### Introduction to agentic coding

Blog](https://claude.com/blog/introduction-to-agentic-coding)

[### How Anthropic teams use Claude Code

Blog](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

[### Fix software bugs faster with Claude

Blog](https://claude.com/blog/fix-software-bugs-faster-with-claude)

## Create what’s exciting. Maintain what’s essential.

Use Claude Code where you work

Get Claude Code

* [Desktop](https://claude.com/download)
* [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
* [On the web](https://claude.ai/code)
* [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh | bash

Or read the [documentation](https://code.claude.com/docs/en/overview)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](https://code.claude.com/docs/en/overview)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
