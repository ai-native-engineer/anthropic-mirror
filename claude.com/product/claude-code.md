<!-- source: https://claude.com/product/claude-code -->

# Claude Code

Work with Claude directly in your codebase. Build, debug, and ship from your terminal, IDE, Slack, web, and more.

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

HomeCode

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

* ![Zapier](https://cdn.sanity.io/images/4zrzovbb/claude-com/45b28686c9eef050f33527795f492fe49d921709-103x28.svg)
* ![PagerDuty](https://cdn.sanity.io/images/4zrzovbb/claude-com/52562bcfc54652e4f0c7dade6549c473fa8b2bc8-133x28.svg)
* ![Workato](https://cdn.sanity.io/images/4zrzovbb/claude-com/4893741894fa7cc707a6b2eb794dcd8f2f139eae-162x24.svg)
* ![Notion](https://cdn.sanity.io/images/4zrzovbb/claude-com/dd2c022495a4655e77541d16bc01b96e2052d6a3-128x36.svg)
* ![Asana](https://cdn.sanity.io/images/4zrzovbb/claude-com/db3f6c16b6956c33c4fad71607c39a62c34bfe0d-124x24.svg)
* ![Rakuten](https://cdn.sanity.io/images/4zrzovbb/claude-com/21aff0f2372e69073154aaba9aa53d0792ed63a2-106x32.svg)
* ![Databricks](https://cdn.sanity.io/images/4zrzovbb/claude-com/3373798a180a90d27215a26eb73b3df37ab5e497-157x24.svg)
* ![Ramp](https://cdn.sanity.io/images/4zrzovbb/claude-com/648a551dca8eaf811bd5228c852a9e65386b0904-118x32.svg)
* ![Plaid](https://cdn.sanity.io/images/4zrzovbb/claude-com/b81ae3b38f93a6fefd5f6484da9ae6877f16ce86-93x35.svg)
* ![Spotify](https://cdn.sanity.io/images/4zrzovbb/claude-com/9854afac4a08917714981581ce7c50479d93ce83-161x44.svg)
* ![StubHub](https://cdn.sanity.io/images/4zrzovbb/claude-com/d553a695bed5872a35c783f88a67ec0eb21f3e00-107x48.svg)
* ![Uber](https://cdn.sanity.io/images/4zrzovbb/claude-com/7bc9c302cc2b3fd6f6d664e5e3126321e5f2ebfa-81x28.svg)
* ![Brex](https://cdn.sanity.io/images/4zrzovbb/claude-com/99d2f4578dc1e2a4e9983d34c49a7e66e3329db9-116x30.svg)
* ![Intercom](https://cdn.sanity.io/images/4zrzovbb/claude-com/fa755cc324f3ead28cea084cb63c403edfccc0da-141x23.svg)
* ![Stripe](https://cdn.sanity.io/images/4zrzovbb/claude-com/d7562d1ee0d6c94849f245da7617a1095bb23f21-92x38.svg)
* ![Shopify](https://cdn.sanity.io/images/4zrzovbb/claude-com/b8d19d3344cc79776137b4ee55024ea919ab2098-148x43.svg)
* ![NASA](https://cdn.sanity.io/images/4zrzovbb/claude-com/2d5f4b13d7785425c2000776e1233ddc9747ec6a-78x64.svg)
* ![Figma](https://cdn.sanity.io/images/4zrzovbb/claude-com/bd0bd7f83f4cd7a5d5d985a5b533d4b1ad8de917-128x35.svg)

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

[### **Dynamic workflows:** Tackle the most challenging tasks by executing across 10s to 100s of parallel subagents, and checking its work before anything reaches you.

BlogMay 28, 2026](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)

[### **Agent view:** One place to manage all your Claude Code sessions.

BlogMay 11, 2026](https://claude.com/blog/agent-view-in-claude-code)

[### **Routines:** Configure a routine once, and it can run on a schedule, from an API call, or in response to an event.

BlogApr 14, 2026](https://claude.com/blog/introducing-routines-in-claude-code)

[### **Computer use:** Claude now opens your apps, navigates your browser, and runs your dev tools to complete tasks.

BlogMar 23, 2026](https://claude.com/blog/dispatch-and-computer-use)

[View changelog (opens in new tab)](https://code.claude.com/docs/en/changelog)

## What could you do with Claude Code?

Get Claude Code

* [Desktop](https://claude.com/download)
* [VS Code](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
* [JetBrains](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)
* [On the web](https://claude.ai/code)
* [Slack](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)

curl -fsSL https://claude.ai/install.sh | bash

Or read the [documentation](https://code.claude.com/docs/en/overview)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](https://code.claude.com/docs/en/overview)

OnboardingTriage issuesRefactor code

```
I'm new to this codebase. Can you explain it to me?

⏺ I'll analyze the Excalidraw codebase structure and provide a high-level overview.

⏺ Analyze(what: "Excalidraw codebase structure and provide a high-level overview of what it is, its main components, and how they're organized. Focus on understanding the project's purpose, architecture, and key features.")

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

  Stop bouncing between tools. Claude Code integrates with GitHub, GitLab, and your command line tools to handle the entire workflow—reading issues, writing code, running tests, and submitting PRs—all from your terminal.
* ### Make powerful edits

  Claude Code's understanding of your codebase and dependencies enables it to make powerful, multi-file edits that work.

## Meets you where you code

![Claude Code running in a terminal](https://cdn.sanity.io/images/4zrzovbb/claude-com/414e92e0a09c3fb2b45b93a9fcfaa8cb3531a341-920x920.webp)

### Start in your terminal

Super powerful terminal integration. Works with all your CLI tools alongside any IDE.

curl -fsSL https://claude.ai/install.sh | bash

Or read the [documentation](https://code.claude.com/docs/en/overview)

[Try Claude Code (opens in new tab)](https://claude.ai/code)[Developer docs (opens in new tab)](https://code.claude.com/docs/en/overview)

![Claude Code extension in VS Code](https://cdn.sanity.io/images/4zrzovbb/claude-com/ad5647024b50754209ac108ad151339a32fde625-920x920.webp)

### Integrate with your editor

Native extensions for VS Code (+ Cursor, Devin Desktop) and JetBrains IDEs.

[VS Code (opens in new tab)](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)[JetBrains (opens in new tab)](https://plugins.jetbrains.com/plugin/27310-claude-code-beta-)

![Claude Code on the web](https://cdn.sanity.io/images/4zrzovbb/claude-com/050b07bf101bc4712abb3a7e1ba6f4d8dde33fcd-920x920.webp)

### Access anywhere

Quick access from browser, mobile app, or Claude on desktop. Great for parallel work or on-the-go coding.

[Open in browser (opens in new tab)](https://claude.ai/code)[Download app](https://claude.com/download)

## Kick off coding tasks in Slack

[Add to Slack (opens in new tab)](https://slack.com/oauth/v2/authorize?client_id=1601185624273.8899143856786&scope=app_mentions:read,assistant:write,channels:history,channels:read,chat:write,files:read,files:write,groups:history,groups:read,im:history,im:read,im:write,mpim:history,reactions:write,users:read,users:read.email,commands,search:read.public&user_scope=bookmarks:read,channels:history,channels:read,chat:write,emoji:read,files:read,groups:history,groups:read,groups:write,im:history,im:read,im:write,links:read,mpim:history,mpim:read,mpim:write,mpim:write.topic,pins:read,reactions:read,reactions:write,remote_files:read,team:read,users:read,users:read.email,search:read.public,search:read.private,search:read.im,search:read.mpim,search:read.files,search:read.users,canvases:read,canvases:write)[Learn more](https://claude.com/claude-for-slack)

## What developers are saying

* ![Ramp](https://cdn.sanity.io/images/4zrzovbb/claude-com/648a551dca8eaf811bd5228c852a9e65386b0904-118x32.svg)

  > “Claude Code has dramatically accelerated our team's coding efficiency. I can now write EDA code in a notebook—pulling data, training a model, and evaluating it with basic metrics—and then ask Claude to convert that into a Metaflow pipeline. This process saves 1-2 days of routine (and often boring!) work per model.”

  Anton Biryukov, Staff Software Engineer

  [Read story](https://claude.com/customers/ramp)
* ![Intercom](https://cdn.sanity.io/images/4zrzovbb/claude-com/fa755cc324f3ead28cea084cb63c403edfccc0da-141x23.svg)

  > “With Claude, we're not just automating customer service—we're elevating it to truly human quality. This lets support teams think more strategically about customer experience and what makes interactions genuinely valuable.”

  Fergal Reid, VP of AI

  [Read story](https://claude.com/customers/intercom)
* ![Notion](https://cdn.sanity.io/images/4zrzovbb/claude-com/dd2c022495a4655e77541d16bc01b96e2052d6a3-128x36.svg)

  > “Claude Code is moving our team up a level: we decide what needs to happen, and smooth the process so it can build and verify end-to-end. A big part of my job now is to keep as many instances of Claude Code busy as possible.”

  Simon Last, Co-founder

  [Read story](https://claude.com/customers/notion)

* ![GitLab](https://cdn.sanity.io/images/4zrzovbb/claude-com/84694a8c9a86c0b8bf37a874c675ccaeec9c6654-111x26.svg)
* ![Dynatrace](https://cdn.sanity.io/images/4zrzovbb/claude-com/05e7af628f73b9ab5ce68b47e2035d292564c421-181x32.svg)
* ![Kubernetes](https://cdn.sanity.io/images/4zrzovbb/claude-com/74ea6c22373a93746176788b31b17ea20ae59223-178x47.svg)
* ![Heroku](https://cdn.sanity.io/images/4zrzovbb/claude-com/14d277edf9089e2db3a1e3c5c004d25f0a496627-143x40.svg)
* ![Stripe](https://cdn.sanity.io/images/4zrzovbb/claude-com/d7562d1ee0d6c94849f245da7617a1095bb23f21-92x38.svg)
* ![Elastic](https://cdn.sanity.io/images/4zrzovbb/claude-com/4114bc17f676c85fd52661ac58205c1b7f2e52c5-117x40.svg)
* ![Terraform](https://cdn.sanity.io/images/4zrzovbb/claude-com/71a735ffc038acaed1889e2baa6108b9c16f0dc5-165x44.svg)
* ![Sentry](https://cdn.sanity.io/images/4zrzovbb/claude-com/f90f7f0b84c285e5a2c3dcc8764aae3eb74cf701-141x31.svg)
* ![AWS](https://cdn.sanity.io/images/4zrzovbb/claude-com/477ff12eca622016612d5837b67bec8fbd3899e8-61x36.svg)
* ![MongoDB](https://cdn.sanity.io/images/4zrzovbb/claude-com/b7e4f274d9789cf6709450c85ee987064b78d784-156x40.svg)
* ![Atlassian](https://cdn.sanity.io/images/4zrzovbb/claude-com/9cdf5ed2ae750f0b6795490071eed41576bd1e1a-189x24.svg)
* ![Datadog](https://cdn.sanity.io/images/4zrzovbb/claude-com/5bd06742093289d7f7dd03b3945cc35d823d5388-146x36.svg)
* ![GitHub](https://cdn.sanity.io/images/4zrzovbb/claude-com/7522fc92399dcb4a68f11c7e147e711fcadbe75b-126x36.svg)
* ![Vercel](https://cdn.sanity.io/images/4zrzovbb/claude-com/dfe2bb49cbe6a11d747deb00e01474b0ac4a8de8-120x24.svg)
* ![New Relic](https://cdn.sanity.io/images/4zrzovbb/claude-com/381cea7f0fc11a867d2e8fa86028a1bc87fd9aad-142x28.svg)

## Connects with your favorite command line tools

Your terminal is where real work happens. Claude Code connects with the tools that power development—deployment, databases, monitoring, version control. Rather than adding another interface to juggle, it enhances your existing stack.

## FAQ

### How do I get started with Claude?

You can access Claude Code with a Claude Pro or Max plan, a Team or Enterprise plan premium seat, or a Claude Console account. [Download Claude Code](https://code.claude.com/docs/en/overview) and sign in with your respective Claude or Console credentials.

### What kinds of tasks can Claude Code handle?

Claude Code excels at both routine development tasks like bug fixes and testing, as well as transformative work like refactors and feature implementation that require deep codebase understanding.

### How does Claude Code work with my existing tools?

Claude Code runs in your terminal and works alongside your preferred IDE and development tools without requiring you to change your workflow. Claude Code can also use command line tools (like Git) and MCP servers (like GitHub) to extend its own capabilities using your tools.

### Is Claude Code secure?

Yes. Claude Code runs locally in your terminal and talks directly to model APIs without requiring a backend server or remote code index. It also asks for permission before making changes to your files or running commands.

### What are the system requirements to run Claude Code?

Claude Code works on macOS, Linux, and Windows. [See full system requirements](https://docs.claude.com/en/docs/claude-code/setup#system-requirements).

### How much does Claude Code cost?

When used with a Claude Console account, Claude Code consumes API tokens at [standard API pricing](https://claude.com/pricing#api).

### Does Claude Code work with the Claude desktop app?

Yes. Max, Pro, Team, and Enterprise users can access Claude Code on the [Claude desktop app](https://claude.com/download).

### What is fast mode on Claude Code?

Fast mode is a high-speed configuration for Opus 5, making the model 2.5x faster at a higher cost per token. Fast mode is available:

* In research preview on Claude Code, and is priced at $10/$50 per million tokens.
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

## Create what's exciting. Maintain what's essential.

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
