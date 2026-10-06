<!-- source: https://claude.com/solutions/coding -->

# The best AI for developers

Claude is the not-so-secret advantage for world class engineering teams and software companies.

[Start building (opens in new tab)](https://platform.claude.com/)[Contact sales](https://claude.com/contact-sales)

[![](https://assets.claude.com/2b058b37151273b2dfff681861d4f99dc28a882d.png)](https://assets.claude.com/27884c4362fe884eca5dba08fe5c7efb1bbf567a.mp4)

* 66.4%

  Opus 5.5 on Terminal-Bench 4.0
* ## 60x

  faster code review feedback for an AI platform customer
* ## 95%

  reduction in time to run tests for an enterprise software customer

* ![Augment Code](https://assets.claude.com/7c991eec0ef2ebdbb312e3a55072965c105f343e.svg)
* ![GitLab](https://assets.claude.com/9760b31778be76fd66c6b722dced22db12cb59e8.svg)
* ![Vercel](https://assets.claude.com/f6f5598aac3be6fd9b2dfc23eced7509c90d387b.svg)
* ![GitHub Copilot](https://assets.claude.com/ca4926c8671ff31babf492320985b02d2ce36f3c.svg)
* ![Cursor](https://assets.claude.com/ff9cb146ba10268aa06e6488b4a5528bc06e0830.svg)
* ![Sourcegraph](https://assets.claude.com/4c92243e3dd5b307a7ddc1b4ef279a0839b7f3e1.svg)
* ![Replit](https://assets.claude.com/28b18c56c8aea46930c7b90ecfe004893de1d250.svg)
* ![Cognition](https://assets.claude.com/668e21fde8e649dceecf16e585196cbf01f4f916.svg)

## Write code with Claude

Get complete insight into your codebase and accelerate exceptional software.

```
I'll investigate the auth error. Let me look at the relevant files.

Examining auth-related files...
* src/services/authService.js
* src/components/Login.jsx
* src/store/authSlice.js

Running the login flow...

Error detected: "401 Unauthorized: Token expired"

Root cause:
* Token refresh mechanism not handling expired tokens correctly
* Refresh token missing from request header
* Improper error handling for 401 responses

Updating authService.js with proper refresh logic...
Updating request interceptor for 401 handling...
Testing the fix...

* Login successful ✓
* Token refresh working ✓
* Proper redirection on expired tokens ✓

Authentication error fixed! The login flow now properly handles token expiration.
```

### Scale coding impact, not overhead

Write, test, and debug complex software with [Claude](https://claude.ai), analyze codebases with expert-level reasoning via GitHub integration, delegate development tasks through computer use, and fast-track smarter engineering decisions in a shared workspace.

[Learn more](https://claude.com/product/claude-code/enterprise)

![](https://assets.claude.com/cdad5485cfc8dd3d4d226ed395f619acd7062ef6.jpg)

### Explore agentic coding with Claude Code

Claude Code brings Fable 5.1 to your terminal, with deep codebase awareness and the ability to edit files and run commands directly in your environment.

[Learn more](https://claude.com/product/claude-code)

## Developers love Claude

> “I know this sounds cringe, but I literally have clammy hands and a racing heart because of how powerful Claude + Cursor is. Like I just made a whole new feature, frontend and backend, built on top of my own custom APIs without touching code, then I had it switch from a SwiftUI.”

Majd Taby, @jtaby

> “Anthropic is leading the Industry with models - like Sonnet and Opus - and developer tools - like Claude Code.”

Jon Meyers, @jonmeyers\_io

> “With new Claude i officially feel like a fraud when i code, I’m the guy in the corner saying um nice job boss keep going.”

Nick, @nickcammarata

> “I taught a friend who has never written code in her life how to use Claude to build a simple app and deploy it on Cloudflare today. Watching someone realize that they can now build software is a great experience. Enable everyone to build anything.”

Logan Grasby, @LoganGrasby

> “I introduced someone to Claude Code, Opus last night, and we were up til 4 am building a project. It was crazy! 20K lines of codes, audit logging, a full Prisma Database, complete architecture, and a complete roadmap with 4 phases for complete implementation.”

Teneika Askew, @teneikaask\_you

> “Just taught my fiancée how to use claude to write code that automates dumb tasks that have been making her work life miserable for months. She went from being downtrodden and skeptical to dancing around the room in about 15 minutes. END USER PROGRAMMING IS NOW.”

Kasey, @kaseyklimes

> “I know this sounds cringe, but I literally have clammy hands and a racing heart because of how powerful Claude + Cursor is. Like I just made a whole new feature, frontend and backend, built on top of my own custom APIs without touching code, then I had it switch from a SwiftUI.”

Majd Taby, @jtaby

> “Anthropic is leading the Industry with models - like Sonnet and Opus - and developer tools - like Claude Code.”

Jon Meyers, @jonmeyers\_io

> “With new Claude i officially feel like a fraud when i code, I’m the guy in the corner saying um nice job boss keep going.”

Nick, @nickcammarata

> “I taught a friend who has never written code in her life how to use Claude to build a simple app and deploy it on Cloudflare today. Watching someone realize that they can now build software is a great experience. Enable everyone to build anything.”

Logan Grasby, @LoganGrasby

> “I introduced someone to Claude Code, Opus last night, and we were up til 4 am building a project. It was crazy! 20K lines of codes, audit logging, a full Prisma Database, complete architecture, and a complete roadmap with 4 phases for complete implementation.”

Teneika Askew, @teneikaask\_you

> “Just taught my fiancée how to use claude to write code that automates dumb tasks that have been making her work life miserable for months. She went from being downtrodden and skeptical to dancing around the room in about 15 minutes. END USER PROGRAMMING IS NOW.”

Kasey, @kaseyklimes

1/6

## Build products with the Claude Platform

Integrate Claude’s powerful AI capabilities into your apps and deliver production-grade solutions faster.

Existing prompt

Classify all customer support tickets into the most relevant category.
Here is the list of categories to choose from:
{{CATEGORY\_LIST}}
Here is the content of the support ticket:
{{TICKET\_CONTENT}}

What would you like to improve?

Please include a rationale for the classification.

You are an AI assistant specialized in classifying customer support tickets. Your task is to analyze the content of a given ticket and assign it to the most appropriate category from a predefined list. You will also provide reasoning for your classification decision.

First, let's review the available categories:

<category\_list>
{{CATEGORY\_LIST}}
</category\_list>

Now, here is the content of the support ticket you need to classify:

<ticket\_content>
{{TICKET\_CONTENT}}
</ticket\_content>

Please follow these steps to complete the task:
– Carefully read and analyze the ticket content.
– Consider how the content relates to each of the available categories.
– Choose the most appropriate category for the ticket.
– Provide a detailed explanation of your reasoning process.

Use the following structure for your response:
<classification\_analysis>
In this section, break down your thought process:
– Quote the most relevant parts of the ticket content.
– List each category and note how it relates to the ticket content.
– For each category, provide arguments for and against classifying the ticket into that category.
– Rank the top 3 most likely categories.
</classification\_analysis>

<classification>
<category>Your chosen category goes here</category>
<reasoning>A concise summary of your reasoning for choosing this category</reasoning>
</classification>

Remember to be thorough in your analysis and clear in your explanation. Your goal is to provide an accurate classification with well-supported reasoning.

### Deliver amazing AI experiences

* Customize how Claude fits into your solution with our API
* Improve and evaluate your prompts in the Workbench
* Build frontier intelligence into your applications
* Turn anyone into an AI developer with rich docs and tooling

## See why companies choose Claude

![Red Hat](https://assets.claude.com/144df01d20c51393e75bf99327301d061c3ef9ef.svg)

> “As part of our ongoing evaluation of AI models, Claude Fable 5.1 delivered impressive results in our tests. Using Claude Code, it correctly identified the root cause of every broken build we tested, across all the effort levels. It also communicates more effectively than earlier Anthropic models, with updates that are more concise and easier to follow.”

Josh Boyer, Distinguished Engineer

![Deloitte](https://assets.claude.com/d799180e9a468d82dc23a32c1ddfe94dcee116d0.svg)

> “Even at its lowest effort setting, Claude Opus 5.5 caught 72% of known bugs in our code reviews to Opus 5’s 56% at high effort, with fewer false alarms and a fraction of the output. On US consulting analysis, low thinking effort matched its higher thinking settings on half the output and passed our quality checks. When more lower thinking efforts are deployed in production, that’s client-ready work delivered efficiently.”

Carl Bennett, CIO

![GitHub](https://assets.claude.com/ff6655b95f24d2aa0b9bf52c94ef5d5f5e54a70e.svg)

> “Developers want agents that can take on real software work and finish it. In our testing across GitHub Copilot CLI and VS Code, Claude Opus 5.5 used among the fewest tokens and steps we measured. In VS Code, it solved more terminal tasks than Opus 5 in less than half the steps. More than making individual tasks more efficient, it’s making developers’ bigger projects more achievable.”

Mario Rodriguez, Chief Product Officer

![Clio](https://assets.claude.com/f72cb9a169e05b3415b3e122dd687e6a012f0509.svg)

> “I handed Claude Opus 5.5 a large engineering task across six of our repositories and let it run overnight, unattended. It stayed on task for over 18 hours defining how our services talk to each other and working out how each one should apply that. Compared with Opus 5, it hit milestones faster and required minimal reworking. Its code comments were short and useful instead of long and prose-heavy. I’m struggling to find anything negative to say.”

Sean Heintz, Staff Software Developer

![Lovable](https://assets.claude.com/696241c910e095691021db3ee35efd8dfac8f4f2.svg)

> “For Lovable builders, Opus 5.5 means faster builds with the same quality, whether you’re starting from scratch or working on a live app. It gathers context once, makes fewer and more complete edits, and doesn’t get stuck retrying, finishing in a third to half fewer steps and using significantly fewer tokens along the way.”

Fabian Hedin, CTO & Co-founder

![Spotify](https://assets.claude.com/ca907a6ebfed4932cb7766ca322936b3c65b2a94.svg)

> “With Claude Opus 5.5, we’ve seen a clear improvement in token efficiency across our internal evaluations, as we’ve been able to complete the same tasks both cheaper and faster.”

Aleksandar Mitic, Senior Engineer

![Optiver](https://assets.claude.com/89d6d866124763400d2482d2aae68c663590fd2a.svg)

> “We test models on real engineering and trading-desk work. On our agentic coding tasks, Claude Opus 5.5 matched Opus 5’s quality in about half the turns, time and output tokens, cutting the cost of that workload by 40 to 50%. It posted the highest score we’ve recorded on one desk’s trading-support suite, passing tasks earlier Claude models had failed, and topped all eight models on our analysis task.”

Noyan Tokgozoglu, Global Head of AI Engineering

![Cognition](https://assets.claude.com/668e21fde8e649dceecf16e585196cbf01f4f916.svg)

> “We're moving our Opus 5 traffic in Devin to Claude Fable 5.1 on launch day. It matched or edged out Fable 5 in our testing at a lower cost per task, and with the new cache read pricing a Fable-class model is finally economical for the workloads we'd kept on Opus, starting with code review.”

Walden Yan, Co-founder and CPO

![Shopify](https://assets.claude.com/33de1bc0b1b2c92e879e513e3c14ec213c311ff1.svg)

> “Claude Fable 5.1 is more comfortable with long, unattended work than Fable 5. I've had workflows run for a long stretch without losing the plot: it keeps its own records, reprioritizes as things change, and picks up where it left off.”

Ben Lafferty, Senior Staff Engineer

![iGent AI](https://assets.claude.com/0b0944f9ca032d4531865d2fa22d1f43a31c4daf.svg)

> “On the hardest problems we work on, Claude Fable 5.1 separates strongly from any other model we've tried. On a grand challenge-tier problem we've used as a testbed for 18 months, it actually produced material progress. Rather than being trapped in stamp collecting, it made clear white-space connections I have yet to see elsewhere. It also optimized a compute kernel that Fable 5 had tapped out on by about 35%.”

Sean Ward, Co-founder and CEO

![Plaid](https://assets.claude.com/40cac5bb60362b9a3d1711447d37e78e78bd547e.svg)

> “We had a change that touched more than eight services across three codebases. Claude Fable 5.1 mapped the whole workflow end to end, in extremely fine detail, from the incoming service call down to the individual function and the database tables and rows, and it was accurate all the way down. We appreciated the opportunity to test the model and provide feedback, helping us prepare for a new frontier where we can increasingly rely on these tools to take on bolder initiatives.”

Aditya Gupta, Staff Software Engineer

![SpaceX](https://assets.claude.com/16b96e8bd9d142709aad56da70ef3a9f46b69dc3.svg)

> “Claude Fable 5.1 is the most capable model we've run on CursorBench 3.2, scoring 73.4% at max effort. We found it especially skilled at verifying its own work, allowing it to take on difficult coding tasks from start to finish.”

Sualeh Asif, Director of ML

![Canva](https://assets.claude.com/f047885ca3dadf9a16509752ef150ebb9bd424bb.svg)

> “The standout in Claude Fable 5.1 is the writing: more understandable, more meaningful, and it follows our writing guidance better. In blind tests against Fable 5, I preferred its writing and output. And in Canva Code it built a rhythm game with real music and on-beat gameplay matched to the level it generated, something no other model we tested delivered.”

Danny Wu, Head of AI

![Rakuten](https://assets.claude.com/5463fa5a44d12868ceec5ae30bfc8c412cafdeae.svg)

> “We asked Claude Fable 5.1 to review a clinical research project for Rakuten Medical that three other frontier models had signed off on. It found a gap none of them had seen and insisted on testing it further. It then proposed a completely new hypothesis, turning a dataset we had written off into a new research direction in one afternoon. It's the first time a frontier model like Claude has empowered us to explore new research in this way.”

Felix Giovanni Virgo, Principal AI Engineer

![Red Hat](https://assets.claude.com/144df01d20c51393e75bf99327301d061c3ef9ef.svg)

> “As part of our ongoing evaluation of AI models, Claude Fable 5.1 delivered impressive results in our tests. Using Claude Code, it correctly identified the root cause of every broken build we tested, across all the effort levels. It also communicates more effectively than earlier Anthropic models, with updates that are more concise and easier to follow.”

Josh Boyer, Distinguished Engineer

![Deloitte](https://assets.claude.com/d799180e9a468d82dc23a32c1ddfe94dcee116d0.svg)

> “Even at its lowest effort setting, Claude Opus 5.5 caught 72% of known bugs in our code reviews to Opus 5’s 56% at high effort, with fewer false alarms and a fraction of the output. On US consulting analysis, low thinking effort matched its higher thinking settings on half the output and passed our quality checks. When more lower thinking efforts are deployed in production, that’s client-ready work delivered efficiently.”

Carl Bennett, CIO

1/14

![Replit](https://assets.claude.com/28b18c56c8aea46930c7b90ecfe004893de1d250.svg)

100K+

applications deployed on Google Cloud run

![Block](https://assets.claude.com/172f59075049c2af9b7896e868bc60122e3dd0f3.svg)

75%

engineers saving 8–10+ hours every week

![Replit](https://assets.claude.com/28b18c56c8aea46930c7b90ecfe004893de1d250.svg)

100K+

applications deployed on Google Cloud run

![Block](https://assets.claude.com/172f59075049c2af9b7896e868bc60122e3dd0f3.svg)

75%

engineers saving 8–10+ hours every week

## Coding resources

[Learn how to use Claude Code

Developer docs](https://code.claude.com/docs)

[Start building with our quickstart guides

Quickstart](https://docs.claude.com/en/docs/get-started)

[How Anthropic teams use Claude Code

Case study](https://www.anthropic.com/news/how-anthropic-teams-use-claude-code)

Why do programmers prefer dark mode?

I don't know
