<!-- source: https://www.anthropic.com/news/fine-tune-claude-3-haiku -->

Explore here

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d227246bc2b5a3cc3626_9f6a378a1e3592cf8d27447457409ba12284faef-1000x1000.svg)

# Fine-tune Claude 3 Haiku in Amazon Bedrock

Claude 3 Haiku can now be fine-tuned in Amazon Bedrock with custom training data, enabling faster, more accurate performance at lower cost.

* Category

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

  Claude Platform
* Date

  July 10, 2024
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/fine-tune-claude-3-haiku

![Graph showing fine-tuning with Claude 3 Haiku](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9554e6002385ccd593_aaf4aaf19584a566ab3687e64cd31da018b17b44-2880x1620.png)

***Update:*** *Fine-tuning Claude 3 Haiku in Amazon Bedrock is generally available. (November 1, 2024)*

Customers can now fine-tune Claude 3 Haiku—our fastest and most cost-effective model—in [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/) to customize its knowledge and capabilities for their business, making the model more effective for specialized tasks.

## Overview of fine-tuning

Fine-tuning is a popular technique to improve model performance. By creating a customized version of the model, you can train the model to excel at highly tailored workflows.

To fine-tune Claude 3 Haiku, you first prepare a set of high quality prompt-completion pairs—the ideal outputs that you want Claude to provide for a given task. The fine-tuning API, now available in preview, will use your data to create your own custom Claude 3 Haiku. Using the Amazon Bedrock console or API, you can test and refine your custom Claude 3 Haiku model until it meets your performance goals and is ready for deployment.

## Benefits

Fine-tuning allows you to customize Claude 3 Haiku so it can acquire specialized business knowledge, leading to improved accuracy and consistency. Benefits include:

* **Better results on specialized tasks**: Enhance performance for domain-specific actions such as classification, interactions with custom APIs, or industry-specific data interpretation. Fine-tuning allows Claude 3 Haiku to excel in areas crucial to your business compared to more general models by encoding company and domain knowledge.
* **Faster speeds at lower cost**: Reduce costs for production deployments where Claude 3 Haiku can be used in place of Sonnet or Opus, while also returning results faster.
* **Consistent, brand-aligned formatting**: Generate consistently structured outputs tailored to your exact specifications like standardized reports or custom schemas, ensuring compliance with regulatory requirements and internal protocols.
* **Easy-to-use API**: Companies of all sizes can innovate efficiently without extensive in-house AI expertise or resources. Anyone can fine-tune models seamlessly, no deep technical expertise required.
* **Safe and secure**: Proprietary training data remains within customers’ AWS environment. Anthropic’s fine-tuning technique preserves the Claude 3 model family’s low risk of harmful outputs.

We fine-tuned Haiku to moderate online comments on internet forums1, including identifying insults, threats, and explicit content. Fine-tuning improved classification accuracy from 81.5% to 99.6% while reducing tokens per query by 85%.

![Graph illustrating fine-tuning on Claude 3 Haiku](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9454e6002385ccd587_7e7063ef5b33399cf7f891b43b343ab2692a2e14-2200x1936.png)

## Customer spotlight

[SK Telecom](https://www.claude.com/customers/skt), one of the largest telecommunications operators in South Korea, trained a custom Claude model to improve support workflows and enable better customer experiences by leveraging their industry-specific expertise.

"Embedding a fine-tuned Claude in our customer support operations has measurably improved our internal processes and overall customer satisfaction. **By customizing Claude, we've seen a 73% increase in positive feedback for our agents' responses and a 37% improvement in key performance indicators for telecommunications-related tasks**. The fine-tuned model now efficiently generates topics, action items, and summaries from customer call logs, and breaks down complex customer issues into manageable steps for better problem-solving," said Eric Davis, Vice President, AI Tech Collaboration Group.

[Thomson Reuters](https://www.claude.com/customers/thomson-reuters), a global content and technology company, has seen positive results with Claude 3 Haiku. The company, which serves professionals in legal, tax, accounting, compliance, government, and media, anticipates even faster and more relevant AI results by fine-tuning Claude with their industry expertise.

“We are excited to fine-tune Anthropic’s Claude 3 Haiku model in Amazon Bedrock to further enhance our Claude-powered solutions. Thomson Reuters aims to provide accurate, fast, and consistent user experiences. By optimizing Claude around our industry expertise and specific requirements, we anticipate measurable improvements that deliver high-quality results at even faster speeds. **We’ve already seen positive results with Claude 3 Haiku, and fine-tuning will enable us to tailor AI assistance more precisely**,” said Joel Hron, Head of AI and Labs, Thomson Reuters.

## How to get started

Fine-tuning for Claude 3 Haiku in Amazon Bedrock is now available in preview in the US West (Oregon) AWS Region. At launch, we're supporting text-based fine-tuning with context lengths up to 32K tokens, with plans to introduce vision capabilities in the future. Additional details are available in the [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/) and [documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-supported.html).

To request access, contact your AWS account team or submit a support ticket in the [AWS Management Console](https://console.aws.amazon.com/bedrock/).

No items found.

[Prev](#)Prev

0/5

[Next](#)Next

eBook

##

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Jun 17, 2026

### Secure access to the Claude Platform with Workload Identity Federation

Product announcements

[Secure access to the Claude Platform with Workload Identity Federation](#)Secure access to the Claude Platform with Workload Identity Federation

[Secure access to the Claude Platform with Workload Identity Federation](/blog/workload-identity-federation)Secure access to the Claude Platform with Workload Identity Federation

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

May 7, 2026

### Collaborate with Claude across Excel, PowerPoint, Word and Outlook

Product announcements

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](#) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

[Collaborate with Claude across Excel, PowerPoint, Word and Outlook](/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) Collaborate with Claude across Excel, PowerPoint, Word and Outlook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

May 19, 2026

### New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

Product announcements

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](#)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

[New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](/blog/new-in-claude-managed-agents)New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

Apr 30, 2026

### Claude Security is now in public beta

Product announcements

[Claude Security is now in public beta](#)Claude Security is now in public beta

[Claude Security is now in public beta](/blog/claude-security-public-beta)Claude Security is now in public beta

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

Claude Platform

Business
