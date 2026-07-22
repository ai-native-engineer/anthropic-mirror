<!-- source: https://www.anthropic.com/news/skills -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2307f9555d7c1bc46cb_77dd9077412abc790bf2bc6fa3383b37724d6305-1000x1000.svg)

# Introducing Agent Skills

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  October 16, 2025
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/skills

***Update:*** *We've added* [*organization-wide management for skills*](/blog/organization-skills-and-directory)*, a* [*directory*](https://claude.com/connectors) *featuring partner-built skills, and published* [*Agent Skills*](https://agentskills.io) *as an open standard for cross-platform portability. (December 18, 2025)*

Claude can now use *Skills* to improve how it performs specific tasks. Skills are folders that include instructions, scripts, and resources that Claude can load when needed.

Claude will only access a skill when it's relevant to the task at hand. When used, skills make Claude better at specialized tasks like working with Excel or following your organization's brand guidelines.

You've already seen Skills at work in Claude apps, where Claude uses them to create files like spreadsheets and presentations. Now, you can build your own skills and use them across Claude apps, Claude Code, and our API.

## How Skills work

While working on tasks, Claude scans available skills to find relevant matches. When one matches, it loads only the minimal information and files needed—keeping Claude fast while accessing specialized expertise.

Skills are:

* **Composable**: Skills stack together. Claude automatically identifies which skills are needed and coordinates their use.
* **Portable**: Skills use the same format everywhere. Build once, use across Claude apps, Claude Code, and API.
* **Efficient**: Only loads what's needed, when it's needed.
* **Powerful**: Skills can include executable code for tasks where traditional programming is more reliable than token generation.

Think of Skills as custom onboarding materials that let you package expertise, making Claude a specialist on what matters most to you. For a technical deep-dive on the Agent Skills design pattern, architecture, and development best practices, read our [engineering blog.](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

## Skills work with every Claude product

### **Claude apps**

Skills are available to Pro, Max, Team and Enterprise users. We provide skills for common tasks like document creation, examples you can customize, and the ability to create your own custom skills.

![The Skills capabilities interface in Claude.ai with example Skills toggled on. ](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690267e194f8fd4618cb330e_image.webp)

Claude automatically invokes relevant skills based on your task—no manual selection needed. You'll even see skills in Claude's chain of thought as it works.  
  
Creating skills is simple. The "skill-creator" skill provides interactive guidance: Claude asks about your workflow, generates the folder structure, formats the SKILL.md file, and bundles the resources you need. No manual file editing required.

Enable Skills in [Settings](https://claude.ai/redirect/website.v1.51f73c97-b077-44e7-85ba-8b27a025dfdf/settings/features). For Team and Enterprise users, admins must first enable Skills organization-wide.

### **Claude Developer Platform (API)**

Agent Skills, which we often refer to simply as Skills, can now be added to Messages API requests and the new `/v1/skills` endpoint gives developers programmatic control over custom skill versioning and management. Skills require the [Code Execution Tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/code-execution-tool) beta, which provides the secure environment they need to run.

Use Anthropic-created skills to have Claude read and generate professional Excel spreadsheets with formulas, PowerPoint presentations, Word documents, and fillable PDFs. Developers can create custom Skills to extend Claude's capabilities for their specific use cases.

Developers can also easily create, view, and upgrade skill versions through the Claude Console.

Explore the [documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) , our [skills cookbook](https://platform.claude.com/cookbook/skills-notebooks-01-skills-introduction), or [Anthropic Academy](https://www.anthropic.com/learn/build-with-claude) to learn more.

‍

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

Skills teaches Claude how to work with Box content. Users can transform stored files into PowerPoint presentations, Excel spreadsheets, and Word documents that follow their organization's standards—saving hours of effort.

Yashodha Bhavnani, Head of AI

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

Canva plans to leverage Skills to customize agents and expand what they can do. This unlocks new ways to bring Canva deeper into agentic workflows—helping teams capture their unique context and create stunning, high-quality designs effortlessly.

Anwar Haneef, GM & Head of Ecosystem

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

With Skills, Claude works seamlessly with Notion - taking users from questions to action faster. Less prompt wrangling on complex tasks, more predictable results.

MJ Felix, Product Manager

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills streamline our management accounting and finance workflows. Claude processes multiple spreadsheets, catches critical anomalies, and generates reports using our procedures. What once took a day, we can now accomplish in an hour.

Yusuke Kaji, General Manager AI

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### **Claude Code**

Skills extend Claude Code with your team's expertise and workflows. Install skills via plugins from the anthropics/skills marketplace. Claude loads them automatically when relevant. Share skills through version control with your team. You can also manually install skills by adding them to `~/.claude/skills`. The Claude Agent SDK provides the same Agent Skills support for building custom agents.

## Getting started

* **Claude apps:** [User Guide](https://support.claude.com/en/articles/12580051-teach-claude-your-way-of-working-using-skills) & [Help Center](https://support.claude.com/en/articles/12512176-what-are-skills)
* **API developers:** [Documentation](https://docs.claude.com/en/api/skills-guide)
* **Claude Code:** [Documentation](https://docs.claude.com/en/docs/claude-code/skills)
* **Example Skills to customize:** [GitHub repository](https://github.com/anthropics/skills)

## What's next

We're working toward simplified skill creation workflows and enterprise-wide deployment capabilities, making it easier for organizations to distribute skills across teams.

Keep in mind, this feature gives Claude access to execute code. While powerful, it means being mindful about which skills you use—stick to trusted sources to keep your data safe. [Learn more](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_2746475e70).

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

May 12, 2026

### Claude for the legal industry

Product announcements

[Claude for the legal industry](#)Claude for the legal industry

[Claude for the legal industry](/blog/claude-for-the-legal-industry)Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

Jul 7, 2026

### Claude Cowork is coming to mobile and web

Product announcements

[Claude Cowork is coming to mobile and web](#)Claude Cowork is coming to mobile and web

[Claude Cowork is coming to mobile and web](/blog/cowork-web-mobile)Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

Apr 9, 2026

### Making Claude Cowork ready for enterprise

Product announcements

[Making Claude Cowork ready for enterprise](#)Making Claude Cowork ready for enterprise

[Making Claude Cowork ready for enterprise](/blog/cowork-for-enterprise)Making Claude Cowork ready for enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225c16d1b0cc3b1ded5_6457c34fbcb012acf0f27f15a6006f700d0f50de-1000x1000.svg)

Mar 24, 2026

### Auto mode for Claude Code

Claude Code

[Auto mode for Claude Code](#)Auto mode for Claude Code

[Auto mode for Claude Code](/blog/auto-mode)Auto mode for Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

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
* Claude Science

  [Claude Science](/product/claude-science)Claude Science
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
* Cybersecurity

  [Cybersecurity](/solutions/cybersecurity)Cybersecurity
* Enterprise

  [Enterprise](/solutions/enterprise)Enterprise
* Financial services

  [Financial services](/solutions/financial-services)Financial services
* Government

  [Government](/solutions/government)Government
* Healthcare

  [Healthcare](/solutions/healthcare)Healthcare
* Higher education

  [Higher education](/solutions/education)Higher education
* K-12 teachers

  [K-12 teachers](/solutions/teachers)K-12 teachers
* Legal

  [Legal](/solutions/legal)Legal
* Life sciences

  [Life sciences](/solutions/life-sciences)Life sciences
* Nonprofits

  [Nonprofits](/solutions/nonprofits)Nonprofits
* Small business

  [Small business](/solutions/small-business)Small business

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

Programs

* Startups

  [Startups](https://claude.com/programs/startups)Startups
* Research Labs

  [Research Labs](https://claude.com/programs/claude-team-plan-for-research-labs)Research Labs

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
* Terms of Service: US K-12

  [Terms of Service: US K-12](https://anthropic.com/legal/k12-terms)Terms of Service: US K-12
* Data Processing Agreement: US K-12

  [Data Processing Agreement: US K-12](https://anthropic.com/legal/k12-dpa)Data Processing Agreement: US K-12
* Usage policy

  [Usage policy](https://www.anthropic.com/legal/aup)Usage policy

[x.com](https://x.com/claudeai)x.com

[LinkedIn](https://www.linkedin.com/showcase/claude/)LinkedIn

[YouTube](https://www.youtube.com/@anthropic-ai)YouTube

[Instagram](https://www.instagram.com/claudeai)Instagram

English (US)

Claude Platform

Agents
