<!-- source: https://support.claude.com/en/articles/13851150-install-financial-services-plugins -->

# Install financial services plugins for Claude Cowork

* Category

  Finance
* Product

  Claude Cowork
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/install-financial-services-plugins-for-cowork

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

We offer a set of open-source plugins that extend Claude Cowork with specialized capabilities for financial services workflows, including financial modeling, equity research, investment banking, private equity, and wealth management.

These plugins are available in a [**public GitHub repository**](https://github.com/anthropics/financial-services-plugins/tree/main?tab=readme-ov-file#claude-for-financial-services-plugins) that you can add as a marketplace in Claude Cowork.

## What's included

The repository contains a **core plugin** and several **add-on plugins** that build on it:

* **Financial analysis** (core) — Build comparable company analyses, DCF models, LBO models, and 3-statement financials. This plugin also includes all shared MCP connectors for financial data providers. **Install this first.**
* **Investment banking** — Draft CIMs, teasers, and process letters. Build buyer lists, run merger models, and create strip profiles.
* **Equity research** — Write earnings updates and initiating coverage reports. Track catalysts and screen for new ideas.
* **Private equity** — Source and screen deals, run due diligence checklists, draft IC memos, and monitor portfolio company KPIs.
* **Wealth management** — Prep for client meetings, build financial plans, rebalance portfolios, and identify tax-loss harvesting opportunities.

The repository also includes partner-built plugins from **LSEG** and **S&P Global**, which bring their financial data and analytics directly into Cowork.

## Add the marketplace

1. Open the Claude Desktop app.
2. Look for the mode selector at the top of the app that includes "Chat" and “Cowork.”
3. Click the "Cowork" tab.
4. Click “Customize” on the left sidebar.
5. Click “Browse plugins.”
6. Select “Personal.”
7. Click the “+” button, then select **Add marketplace from GitHub**.
8. Enter the repository URL: [**https://github.com/anthropics/financial-services-plugins**](https://github.com/anthropics/financial-services-plugins)
9. Once added, you'll see the available financial services plugins in your marketplace.

## Install plugins

1. From your plugin marketplace, browse the available financial services plugins.
2. Install the **financial analysis** plugin first—this is the core plugin that provides shared tools and data connectors used by all other plugins.
3. Install any additional plugins based on your workflow needs.

Once installed, plugins activate automatically. Skills are applied when relevant, or you can invoke them manually during your Claude Cowork session by typing "/" or clicking the "+" button.

## Available Skills

After installation, you can use Skills like:

* /comps [company] — Run a comparable company analysis
* /dcf [company] — Build a DCF valuation model
* /earnings [company] [quarter] — Generate a post-earnings update report
* /one-pager [company] — Create a one-page company profile
* /ic-memo [project name] — Draft an investment committee memo
* /source [criteria] — Source deals based on criteria
* /client-review [client] — Prep for a client meeting

## MCP connectors

The financial analysis core plugin includes connectors for third-party financial data providers such as Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and Egnyte.

Access to these connectors may require a separate subscription or API key from the respective provider. Contact your data provider for details.

## Customize plugins for your firm

These plugins are designed as starting points. You can customize them to match your firm's workflows by editing the plugin files directly:

* Add your firm's terminology, processes, and formatting standards to skill files.
* Swap or add MCP connectors to point at your specific data providers.
* Adjust workflow instructions to reflect how your team does analysis.
* Use /ppt-template to teach Claude your firm's branded PowerPoint layouts.

## Good to know

* Plugins are file-based (Markdown and JSON) — no code or infrastructure required to customize.
* These plugins work across both Claude Cowork and Claude Code.
* AI-generated financial analysis should always be reviewed by qualified professionals before being used in decision-making.

## Learn more

See our blog post for more information: [**Cowork and plugins for finance**](https://claude.com/blog/cowork-plugins-finance).

## Related tutorials

[How to build a plugin from scratch in Claude Cowork](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)How to build a plugin from scratch in Claude Cowork

How to build a plugin from scratch in Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)Tutorial

[Getting started with Claude in Excel](/resources/tutorials/getting-started-with-claude-in-excel)Getting started with Claude in Excel

Getting started with Claude in Excel

Tutorial

[Tutorial](/resources/tutorials/getting-started-with-claude-in-excel)Tutorial

[How to use Claude in Excel for accounting: Revenue model validation](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)How to use Claude in Excel for accounting: Revenue model validation

How to use Claude in Excel for accounting: Revenue model validation

Tutorial

[Tutorial](/resources/tutorials/how-to-use-claude-in-excel-for-accounting-revenue-model-validation)Tutorial

[How to use Claude in Excel for HR: Headcount planning](/resources/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning)How to use Claude in Excel for HR: Headcount planning

How to use Claude in Excel for HR: Headcount planning

Tutorial

[Tutorial](/resources/tutorials/how-to-use-claude-in-excel-for-hr-headcount-planning)Tutorial

[Homepage](https://claude.com)Homepage

Thank you! Your submission has been received!

Oops! Something went wrong while submitting the form.

Write

[Button Text](#)Button Text

Learn

[Button Text](#)Button Text

Code

[Button Text](#)Button Text

Write

* Help me develop a unique voice for an audience

  Hi Claude! Could you help me develop a unique voice for an audience? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Improve my writing style

  Hi Claude! Could you improve my writing style? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Brainstorm creative ideas

  Hi Claude! Could you brainstorm creative ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Learn

* Explain a complex topic simply

  Hi Claude! Could you explain a complex topic simply? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Help me make sense of these ideas

  Hi Claude! Could you help me make sense of these ideas? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Prepare for an exam or interview

  Hi Claude! Could you prepare for an exam or interview? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

Code

* Explain a programming concept

  Hi Claude! Could you explain a programming concept? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Look over my code and give me tips

  Hi Claude! Could you look over my code and give me tips? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Vibe code with me

  Hi Claude! Could you vibe code with me? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to— like Google Drive, web search, etc.—if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can—an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!

More

* Write case studies

  This is another test
* Write grant proposals

  Hi Claude! Could you write grant proposals? If you need more information from me, ask me 1-2 key questions right away. If you think I should upload any documents that would help you do a better job, let me know. You can use the tools you have access to — like Google Drive, web search, etc. — if they’ll help you better accomplish this task. Do not use analysis tool. Please keep your responses friendly, brief and conversational.   
    
  Please execute the task as soon as you can - an artifact would be great if it makes sense. If using an artifact, consider what kind of artifact (interactive, visual, checklist, etc.) might be most helpful for this specific task. Thanks for your help!
* Write video scripts

  this is a test

[Anthropic](https://www.anthropic.com/)Anthropic

© [year] Anthropic PBC

Products

* Claude

  [Claude](/product/overview)Claude
* Claude Code

  [Claude Code](/product/claude-code)Claude Code
* Claude Code for Enterprise

  [Claude Code for Enterprise](/product/claude-code/enterprise)Claude Code for Enterprise
* Claude Cowork

  [Claude Cowork](/product/cowork)Claude Cowork
* @Claude

  [@Claude](/product/tag)@Claude
* Claude Design

  [Claude Design](/product/design)Claude Design
* Claude Security

  [Claude Security](/product/claude-security)Claude Security
* Download app

  [Download app](/download)Download app
* Pricing

  [Pricing](/pricing)Pricing
* Log in

  [Log in](https://claude.ai/login)Log in

Features

* Claude for Chrome

  [Claude for Chrome](/claude-for-chrome)Claude for Chrome
* Claude for Microsoft 365

  [Claude for Microsoft 365](/claude-for-microsoft-365)Claude for Microsoft 365
* Skills

  [Skills](/skills)Skills

Models

* Mythos

  [Mythos](https://www.anthropic.com/claude/mythos)Mythos
* Fable

  [Fable](https://www.anthropic.com/claude/fable)Fable
* Opus

  [Opus](https://www.anthropic.com/claude/opus)Opus
* Sonnet

  [Sonnet](https://www.anthropic.com/claude/sonnet)Sonnet
* Haiku

  [Haiku](https://www.anthropic.com/claude/haiku)Haiku

Solutions

* AI agents

  [AI agents](/solutions/agents)AI agents
* Code modernization

  [Code modernization](/solutions/code-modernization)Code modernization
* Coding

  [Coding](/solutions/coding)Coding
* Customer support

  [Customer support](/solutions/customer-support)Customer support
* Education

  [Education](/solutions/education)Education
* Enterprise

  [Enterprise](/solutions/enterprise)Enterprise
* Financial services

  [Financial services](/solutions/financial-services)Financial services
* Government

  [Government](/solutions/government)Government
* Healthcare

  [Healthcare](/solutions/healthcare)Healthcare
* Legal

  [Legal](/solutions/legal)Legal
* Life sciences

  [Life sciences](/solutions/life-sciences)Life sciences
* Nonprofits

  [Nonprofits](/solutions/nonprofits)Nonprofits
* Security

  [Security](/solutions/security)Security
* Small business

  [Small business](/solutions/small-business)Small business
* Startups

  [Startups](/programs/startups)Startups

Claude Platform

* Overview

  [Overview](/platform/api)Overview
* Developer docs

  [Developer docs](https://platform.claude.com/docs)Developer docs
* Pricing

  [Pricing](https://claude.com/pricing#api)Pricing
* Ecosystem

  [Ecosystem](/ecosystem)Ecosystem
* Marketplace

  [Marketplace](/platform/marketplace)Marketplace
* Claude on AWS

  [Claude on AWS](/partners/claude-on-aws)Claude on AWS
* Google Cloud

  [Google Cloud](/partners/google-cloud)Google Cloud
* Microsoft Foundry

  [Microsoft Foundry](/partners/microsoft-foundry)Microsoft Foundry
* Regional compliance

  [Regional compliance](/regional-compliance)Regional compliance
* Console login

  [Console login](https://platform.claude.com/)Console login

Resources

* Blog

  [Blog](/blog)Blog
* Claude partner network

  [Claude partner network](/partners)Claude partner network
* Community

  [Community](/community)Community
* Connectors

  [Connectors](/connectors)Connectors
* Courses

  [Courses](https://www.anthropic.com/learn)Courses
* Customer stories

  [Customer stories](/customers)Customer stories
* Engineering at Anthropic

  [Engineering at Anthropic](https://www.anthropic.com/engineering)Engineering at Anthropic
* Events

  [Events](https://www.anthropic.com/events)Events
* Plugins

  [Plugins](/plugins)Plugins
* Powered by Claude

  [Powered by Claude](/partners/powered-by-claude)Powered by Claude
* Service partners

  [Service partners](/partners/services)Service partners
* Tutorials

  [Tutorials](/resources/tutorials)Tutorials
* Use cases

  [Use cases](/resources/use-cases)Use cases

Company

* Anthropic

  [Anthropic](https://www.anthropic.com/)Anthropic
* Careers

  [Careers](https://www.anthropic.com/careers)Careers
* Policy

  [Policy](https://www.anthropic.com/policy)Policy
* Economic Futures

  [Economic Futures](https://www.anthropic.com/economic-futures)Economic Futures
* Research

  [Research](https://www.anthropic.com/research)Research
* News

  [News](https://www.anthropic.com/news)News
* Policy on the AI Exponential

  [Policy on the AI Exponential](https://www.anthropic.com/policy-on-the-ai-exponential)Policy on the AI Exponential
* Responsible Scaling Policy

  [Responsible Scaling Policy](https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy)Responsible Scaling Policy
* Security and compliance

  [Security and compliance](https://trust.anthropic.com/)Security and compliance
* Transparency

  [Transparency](https://anthropic.com/transparency)Transparency

Help and security

* Availability

  [Availability](https://www.anthropic.com/supported-countries)Availability
* Status

  [Status](https://status.anthropic.com/)Status
* Support center

  [Support center](https://support.claude.com/en/)Support center

Terms and policies

* Privacy choices

  ### Cookie settings

  We use cookies to deliver and improve our services, analyze site usage, and if you agree, to customize or personalize your experience and market our services to you. You can read our Cookie Policy [here](https://www.anthropic.com/legal/cookies).

  Customize cookie settings

  Reject all cookies

  Accept all cookies

  Save preferences
* Privacy policy

  [Privacy policy](https://www.anthropic.com/legal/privacy)Privacy policy
* Responsible disclosure policy

  [Responsible disclosure policy](https://www.anthropic.com/responsible-disclosure-policy)Responsible disclosure policy
* Terms of service: Commercial

  [Terms of service: Commercial](https://www.anthropic.com/legal/commercial-terms)Terms of service: Commercial
* Terms of service: Consumer

  [Terms of service: Consumer](https://www.anthropic.com/legal/consumer-terms)Terms of service: Consumer
* Usage policy

  [Usage policy](https://www.anthropic.com/legal/aup)Usage policy

[x.com](https://x.com/claudeai)x.com

[LinkedIn](https://www.linkedin.com/showcase/claude/)LinkedIn

[YouTube](https://www.youtube.com/@anthropic-ai)YouTube

[Instagram](https://www.instagram.com/claudeai)Instagram

English (US)
