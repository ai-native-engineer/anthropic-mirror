<!-- source: https://claude.com/resources/guides/the-2026-state-of-ai-agents-report/ai-agents-in-production -->

Chapter 0527 min read

# AI agents in production

27 min read

37 min remaining

AI agents have moved from pilot programs to production systems faster than most enterprises anticipated. And they're not operating as order-takers or task-managers. Leading organizations have moved agents from the periphery of operations to the center of how work gets done.

Take web development startup, [Lovable (opens in new tab)](https://claude.com/resources/webinars/production-ready-use-cases-lovable) for example. With agentic coding tools, the company now ships code 20x faster than writing it manually. [Thomson Reuters (opens in new tab)](https://www.claude.com/customers/thomson-reuters) can deliver comprehensive legal analysis pulled from 150 years of legal expertise in minutes. And cybersecurity leader [eSentire (opens in new tab)](https://www.claude.com/customers/esentire) compressed threat analysis from 5 hours to 7 minutes. And these examples just scratch the surface.

In 2025, companies have transitioned agents from efficiency plays (coding, process automation, etc.) to sources of competitive advantage (product development, research, etc.) and we anticipate adoption of long-running, multi-step agentic systems will only accelerate. The following stories show what that looks like in practice across healthcare, retail, financial services, cybersecurity, and beyond.

## Healthcare and life sciences

Healthcare and life sciences organizations face a mounting tension: the need to move fast to improve patient outcomes while maintaining the highest standards for safety, privacy, and regulatory compliance. All too often, it can feel like the pressure to build agents stands in stark contrast to existing protocols. But as we're finding, the organizations succeeding with agents aren't choosing between speed and rigor–they're achieving both.

### Novo Nordisk transforms clinical documentation from months to minutes

[Novo Nordisk (opens in new tab)](https://www.claude.com/customers/novo-nordisk), a global pharmaceutical company and maker of Ozempic, develops innovative medicines for chronic diseases including diabetes and obesity. The company serves millions of patients worldwide with life-changing treatments that require extensive regulatory documentation before reaching patients.

The challenge

Documentation delays drug discovery

For pharmaceutical companies, the path from drug discovery to patient access is paved with paperwork. Each new treatment comes with its own mountain of required documentation: clinical study reports running hundreds of pages, highly technical device verification protocols, and guides explaining complex treatments in consumer-friendly ways.

The pinnacle of this process is the clinical study report (CSR), a document up to 300 pages long. Staff writers averaged only 2.3 CSRs per year, and the manual process remained prone to errors. With each day of delay costing up to $15 million in potential revenue—and patients with diabetes and obesity continuing to wait—the stakes couldn't have been higher.

The solution

AI-powered documentation platform delivers regulatory-grade content

Novo Nordisk developed NovoScribe, a generative AI platform built with Claude Code on Amazon Bedrock and MongoDB Atlas, with Claude models as the frontier intelligence driving the entire system. The platform combines retrieval-augmented generation with domain expert-approved text and case-specific variables to produce accurate, compliant documentation.

Claude Code has also fundamentally changed product development at Novo Nordisk by enabling non-technical team members to prototype ideas. This ability to spin up a prototype in hours instead of days or weeks has been a strategic catalyst for their 11-person development team, allowing them to maintain a small size while dramatically expanding capabilities.

#### Results and impact

* **10+ weeks to 10 minutes** for clinical study documentation production
* **95% reduction in resources** needed to create device verification protocols
* **Review cycles cut in half** as output quality improved

### Doctolib cuts engineering cycle time from weeks to hours

[Doctolib (opens in new tab)](https://www.claude.com/customers/doctolib), Europe's leading healthcare technology company, serves 420,000 health professionals and 90 million patients across France, Germany, Italy, and the Netherlands. With a comprehensive digital healthcare ecosystem that manages everything from appointments to electronic health records, Doctolib's engineering team faced a familiar challenge: administrative development tasks consumed time that could be spent solving complex healthcare problems.

The challenge

Repeatable tasks consuming time meant for solving healthcare problems

Engineers spent significant time on repeatable administrative tasks, including writing documentation, creating tests, and addressing technical debt. The team needed to refocus on solving complex healthcare challenges rather than wrestling with routine engineering work.

The solution

Autonomous development workflow cuts infrastructure replacement from weeks to hours

After a successful pilot with 30 engineers, Doctolib rolled out Claude Code across their entire development team. Engineers self-onboard in under five minutes across any IDE. The platform team created a centralized repository of prompts, custom commands, and subagents that all developers pull during initial setup—every engineer starts with proven, reusable workflows on day one.

The team embedded Claude Code directly into their CI pipeline through headless mode, automatically opening pull requests for routine maintenance. Every code change triggers a CI job that updates technical documentation automatically, keeping technical docs current without manual intervention.

#### Results and impact

* Legacy testing infrastructure replaced in **hours instead of weeks**
* **300 daily active users**, making Claude Code the most-used AI tool at the company
* Engineering ships features **40% faster** while maintaining code quality

## Retail

Retail and consumer brands generate massive amounts of customer data but can't always operationalize it. AI agents help close that gap. Employees who couldn't write SQL queries yesterday are pulling complex analytics today to better understand and act on customer needs.

### L'Oréal achieves 99.9% customer analytics accuracy with AI agents

[L'Oréal (opens in new tab)](https://www.claude.com/customers/loreal) is the world's largest cosmetics and beauty company, operating in over 150 countries with a portfolio of 37+ international brands across skincare, haircare, makeup, and fragrance.

The company is positioning itself as a tech leader in the category, combining cutting-edge research and innovation with AI, data, and digital capabilities. But its massive amounts of customer data created bottlenecks. Regional teams couldn't answer customer questions without requesting custom reports, while marketing decisions often waited on technical teams to build dashboards

The challenge

Democratizing data access without sacrificing accuracy

For a company competing across global markets, data access delays meant missed opportunities. L'Oréal needed to democratize AI capabilities across its global workforce while maintaining security and governance. A key challenge was enabling employees to access and analyze data without requiring technical expertise or custom dashboard development. Previous GenAI approaches achieved only 90% accuracy on conversational analytics—not effective enough for building user trust at scale.

The solution

Orchestrated AI agents achieve 99.9% accuracy on complex analytics queries

L'Oreal needed AI that could pull data for its employees across multiple systems simultaneously without losing accuracy. L'Oréal selected Claude for conversational analytics through rigorous testing. Claude serves as the main orchestrator of multiple specialized agents that work together to transform user questions into insights and visualizations.

When an employee asks a question, Claude coordinates with semantic API agents, data retrieval systems, and specialized agents for calculations, product master data, and geography master data. This orchestration allows Claude to determine which specialized agents to engage based on the user's question and synthesize results into clear answers.

#### Results and impact

* **99.9% accuracy** on conversational analytics applications, up from 90% with previous GenAI approaches
* **44,000 monthly users** generating 2.5 million messages monthly
* Employees now query data directly rather than building custom dashboards

## Technology

Digital-first companies are embedding agents directly into their products. For these organizations, agents aren't just improving operations, they're becoming the product experience itself.

### Shopify transforms merchant empowerment with AI commerce assistant

[Shopify (opens in new tab)](https://claude.com/customers/shopify) powers commerce for millions of businesses worldwide, from first-time entrepreneurs to enterprise brands. The platform makes it simple for anyone to start, run, and grow a business across online stores, brick-and-mortar locations, and everything in between. But this presents a unique challenge for Shopify's customer support team, as each customer arrives with unique backgrounds and challenges. For instance, many non-technical founders launching their first store needed guidance from basic setup to sophisticated analytics queries that typically require deep knowledge of Shopify's query language (ShopifyQL).

The challenge

Scaling expert-level support across millions of merchants

Merchants needed deep technical knowledge to extract insights about their own businesses. To do so, many had to really learn how to use ShopifyQL and get pretty deep into understanding the query language to get the insights they needed. That barrier kept many entrepreneurs from, and traditional support couldn't scale to the diverse needs of its millions of global users.

The solution

Always-available AI guides merchants from setup to first sale

To address this challenge, Shopify built Sidekick, an AI-enabled commerce assistant that acts as an always-available expert for merchants. Instead of learning Shopify's complex query language, merchants simply ask questions in plain English. Sidekick translates those questions into sophisticated data analytics, pulls in relevant product information and business context, then delivers clear answers.

The system works fast enough to feel conversational. When merchants ask complex questions requiring multiple data sources, Sidekick coordinates the analysis behind the scenes in real-time. Shopify leverages Claude's advanced reasoning capabilities and Google Cloud's infrastructure to support Sidekick because merchants need around-the-clock access to expert-level guidance.

#### Results and impact

* **Millions of merchants** receive expert guidance 24/7
* Entrepreneurs reach **first sale in days rather than weeks**
* Non-developers build internal tools in **minutes rather than days**

### Lovable enables users to ship code 20x faster than manual development

[Lovable (opens in new tab)](https://www.claude.com/customers/lovable) aims to democratize software development by enabling anyone to code. But Lovable faced a technical challenge that had long stumped the industry: how do you help non-coders generate functional, well-architected software? How do you lower the barrier to creating software?

The challenge

Software development timelines blocking idea validation

Traditional software development remains inaccessible to most people, limiting who can ship digital products quickly. Lovable needed an AI solution that could transform conversational interactions into functional, well-architected software that non-technical users could build and technical users could accelerate.

The solution

Conversational interface delivers production-ready code 20x faster

After evaluating commercial and open-source AI models through rigorous quantitative evaluation, Lovable chose Claude for its superior code generation capabilities. By combining Claude's capabilities with their innovations in prompt engineering and system design, Lovable created a platform that delivers functional, production-ready code.

#### Results and impact

* **20x faster development** than writing code manually
* **$40 million ARR** within six months of launch
* **1 million+ active users** monthly building software products

## Startups

The barrier to building software has collapsed. Startups are being built in hours. Non-technical founders can prototype working products through conversations with AI agents. Teams of one can ship what once required significant engineering resources.

### Replit enables deployment in minutes from any device

[Replit (opens in new tab)](https://www.claude.com/customers/replit) is democratizing coding by making it faster and easier to build software. Their mission: empower the next billion software creators—not just developers, but anyone armed with an inspiring product idea. Despite recent AI advances, their mission to democratize access to the digital economy required an easier way to deploy applications for those lacking programming skills.

The challenge

Removing the barrier of learning to code

The time and resources it takes to learn programming remains a significant barrier, even with recent AI advancements. Non-developers needed a solution that could automate complex technical tasks while maintaining professional output.

The solution

Build and deploy applications in minutes without writing code

After evaluating multiple AI models, Replit selected Claude on Google Cloud's Vertex AI for its superior code generation capabilities and seamless cloud integration. Claude demonstrated unique strengths in creating interconnected files that form working applications and editing multiple files simultaneously while maintaining context across the entire codebase.

Running Claude on Vertex AI provided the enterprise-grade security and scalability Replit needed for their global user base. The platform maintains enterprise-grade performance while supporting development from any device, allowing users to go from idea to application in minutes without prior coding experience.

#### Results and impact

* Users build and **deploy apps in minutes**
* **Tens of thousands of applications** running on Google Cloud Run
* Non-technical teams across sales, operations, and marketing now building apps

### Parcha reduces customer due diligence from 3 months to 5 minutes

[Parcha (opens in new tab)](https://claude.com/customers/parcha) helps the world's leading fintechs and banks scale their customer due diligence processes with AI. The company serves clients including Airwallex, Pipe, Flutterwave, and Alloy—navigating complex regulatory requirements while maintaining rapid growth.

Every financial institution approaches compliance differently. Each monitors transactions and conducts customer due diligence their own way, creating a paradox for Parcha: how do you build flexible AI tools when every customer has unique requirements?

The challenge

Rigid workflows couldn't adapt across institutions

Parcha spent two years developing their own workflow engine but struggled to make it work flexibly across their customer base. Traditional approaches led the engineering team to build rigid workflows for specific customers that were nearly impossible to adapt for others.

Beyond these enterprise workflow challenges, compliance analysts at every institution spend hours conducting open-source research on businesses and individuals—work that's time-consuming, unauditable, and difficult to standardize.

The solution

Adaptive AI system compresses 3-month workflows into 5 minutes

Parcha's tools undergo some of the most rigorous compliance reviews in financial services. Their bank-grade compliance tools are built and certified using Claude models, passing some of the most challenging model governance evaluations in the industry.

After two years building in-house agents with Claude models, Parcha selected the Claude Agent SDK based on proven results and deep familiarity with its capabilities. The Agent SDK allowed Parcha's existing product to gain new flexibility—rather than building separate workflows for each customer's unique requirements, the Agent SDK enabled their product to adapt dynamically.

With the Agent SDK, Parcha developed a fully agentic open-source intelligence research product in just two weeks.

#### Results and impact

* Customer due diligence workflows reduced from **3 months to 5 minutes**
* AI tools pass rigorous **bank compliance certifications**
* **$1 million in new bookings** from platform licensing model

## Financial Services

Few industries face more stringent regulatory requirements than financial services, making it the ultimate test for enterprise AI. When banks and investment firms deploy agents at scale, they're proving AI can meet the highest standards for accuracy, auditability, and compliance.

### NBIM manages $1.7 trillion with 20% time savings

[Norges Bank Investment Management (NBIM) (opens in new tab)](https://www.claude.com/customers/nbim) manages Norway's Government Pension Fund Global, with the mandate to transform Norway's oil revenues into long-term financial wealth for future generations. With $1.7 trillion in assets, NBIM is one of the world's largest sovereign funds.

Managing $1.7 trillion across global stock markets, bonds, real estate, and renewable energy infrastructure requires processing massive amounts of information daily. NBIM's teams analyze research reports, market data, regulatory filings, and multilingual news to make investment decisions with enormous consequences.

The challenge

Finding an AI that the entire team could use

The organization struggled to find an AI-powered solution sophisticated enough for institutional investment analysis yet simple enough that everyone—from highly technical portfolio managers to non-technical compliance specialists—could use it.

Complex ESG reporting expectations compounded the challenge, requiring nuanced analysis and clear reporting for each of the 9,000 companies they invest in. They needed AI that was advanced enough for serious investment research and ESG analysis, straightforward enough for their whole team to use, and able to adhere to strict data protection and compliance regulations.

The solution

Human-supervised AI saves analysts 20% of their time weekly

NBIM evaluated multiple LLMs and built human-in-the-loop evaluations to test model capabilities in finance-specific domains. Claude consistently performed best on analysis and reasoning tasks, and in maintaining context over long analytical sessions involving multiple documents. For analysts managing large portfolios, these capabilities translate to 20% time savings every week.

Anthropic's focus on responsible AI development matched NBIM's values and transparency expectations as a public entity. The partnership approach was equally important—the two companies regularly consult on financial services capabilities, test new features, and exchange feedback on safety and enterprise controls.

#### Results and impact

* **Weekly 20% time savings** across all departments
* **600+ active users** within two months
* **300 daily Claude Code users,** now most-used AI tool on engineering team

### N26 achieves 70% automation across targeted processes in one year

[N26 (opens in new tab)](https://www.claude.com/customers/n26) is building the bank the world loves to use, serving diverse, digital-native customers across 24 European markets. As a fully licensed bank, N26 provides a 100% digital banking experience powered by advanced digital, data, and AI technologies.

As N26 rapidly scaled its customer base across multiple European markets, the company faced a critical challenge: ensuring service quality could keep pace with growth. Many essential processes remained manual, document-heavy, and time-consuming.

The challenge

Manual processes couldn't keep pace with rapid customer growth

The rising volume of customer interactions created bottlenecks that directly affected both customer experience and internal efficiency. Teams spent increasing time on document classification, information extraction, translation, and drafting materials based on complex multilingual sources.

The solution

15+ integrated AI applications achieve 70% automation in one year

N26 selected Claude for its advanced reasoning and multimodal capabilities, which proved essential for handling the sophisticated decision-making required in financial processes. Claude's availability through AWS Bedrock in Europe provided the regulatory compliance, security, and scalability that N26 required as a fully licensed bank.

Since beginning work with Claude in 2024, N26 has integrated the AI assistant into more than 15 internal applications. The deployments span the full customer service lifecycle: a customer-facing virtual assistant providing instant support in five languages around the clock, chargeback request processing that translates documentation and analyzes complex claims, and financial crime analysis where Claude assists analysts by synthesizing customer data and auto-drafting investigation reports.

#### Results and impact

* **70% automation** across targeted processes within one year
* **15+ AI applications** serving customer service teams and fraud analysts
* **1-2 weeks** from implementation to testing while meeting regulatory standards

## Cybersecurity

Cybersecurity teams face an asymmetric problem: attackers only need to be right once, defenders need to be right every time. AI agents are enabling security teams to analyze threats and respond to incidents at machine speed while maintaining the strategic judgment that only humans can provide.

### eSentire compresses threat analysis from 5 hours to 7 minutes

[eSentire (opens in new tab)](https://www.claude.com/customers/esentire) protects critical infrastructure organizations in 80+ countries as the authority in managed detection and response (MDR). Looking to expand into new markets and protect more customers, the company's security analysts were spending 5 hours on each threat investigation. Their expertise couldn't scale at the pace they needed.

The challenge

5-hour expert investigations needed to happen at scale

With their Atlas Platform successfully delivering complete threat resolution, the company set their sights on expanding to new markets while deepening customer engagement through enhanced security operations.

eSentire needed to deliver expert-level investigation precision at scale while enhancing transparency of threat resolution outcomes. The goal was enabling existing security experts to amplify their capabilities, protecting more customers while deepening threat analysis in every investigation. What previously required 5 hours of expert analysis needed to happen much faster without sacrificing quality or thoroughness.

The solution

Autonomous AI threat analysis achieves 95% expert alignment in minutes

eSentire evaluated multiple AI models across real-world security scenarios. Claude provided the highest performance for complex security reasoning, with continuous improvements across model versions. Claude's agentic capabilities excelled at orchestrating multi-tool workflows while maintaining investigative coherence—essential for their MDR approach, while its threat analysis aligned with their most senior security experts 95% of the time while delivering answers in 7 minutes instead of 5 hours.

Amazon Bedrock provided the enterprise-grade security and infrastructure eSentire needed for sensitive intelligence. Claude's intelligent tool selection mirrored expert analyst approaches to complex threat analysis, synthesizing evidence from multiple sources, correlating disparate security events, and incorporating findings into comprehensive conclusions.

eSentire conducted rigorous validation using 1,000 real-world investigations, comparing Claude's decisions against their most senior SOC (Security Operations Center) experts.

#### Results and impact

* Expert security analysis compressed from **5 hours to 7 minutes** with **95% alignment**
* **99.3%** threat suppression across critical infrastructure deployments
* **$1 million+** in new bookings from platform licensing

### Palo Alto Networks accelerates junior developer integration by 70%

[Palo Alto Networks (opens in new tab)](https://www.claude.com/customers/palo-alto-networks), the world's largest cybersecurity company, protects organizations globally with comprehensive security solutions. As threats evolve faster, the engineering team saw an opportunity to use AI to help their products stay ahead of competitors and bad actors.

The challenge

Accelerating development without compromising security

The engineering team mapped their software delivery process to identify where developers spent time and where errors mostly occurred. Their analysis revealed that while junior developers spent 30-35% of their time in initial development, this phase was also where the most critical issues emerged. And rushing developers through onboarding to ship features faster than competitors could open them up to unintentionally shipping vulnerabilities, too.

They needed to compress the months-long path it often took to get their engineers up-to-speed on their codebase and processes without creating the security debt that comes from moving too fast. Palo Alto Networks saw a powerful opportunity: using generative AI to stay ahead of both competitors and bad actors in the rapidly evolving cybersecurity landscape.

The solution

AI-powered development cuts junior developer onboarding time by 70%

After evaluating multiple AI solutions, the engineering team chose Claude on Google Cloud's Vertex AI for several key reasons. Claude consistently demonstrated superior performance in coding tasks while maintaining high accuracy and security standards.

Anthropic prioritized safety and security a lot more than other LLM providers, discussing security and safety implications in every meeting, a critical consideration for a cybersecurity leader.

Using Google Cloud's Vertex AI provided significant advantages, including granular usage-based pricing with flexible commitment periods and seamless SDK integration for provisioned throughput.

#### Results and impact

* Junior developers complete complex integrations **70% faster**
* New developers contribute meaningfully in **weeks instead of months**
* **20-30% increase** in feature development velocity

## Legal

Legal and professional services built their business models on expert knowledge and billable hours. AI agents are transforming this equation, making decades of expertise instantly accessible while freeing professionals to focus on client relationships rather than research and document review.

### Thomson Reuters delivers comprehensive legal analysis in minutes

[Thomson Reuters (opens in new tab)](https://www.claude.com/customers/thomson-reuters) is a global content and technology company serving legal, tax, accounting, and compliance professionals. With 3,000 domain experts and over 150 years of authoritative content, the company provides trusted intelligence to professionals who need accurate information to advise their clients.

As a result of their size and breadth of expertise, they faced a knowledge access crisis that directly impacted their users' ability to serve their clients. A lawyer researching a case precedent, for example, would have to manually search through thousands of documents, billing hours while hunting for relevant materials.

The challenge

150 years of legal expertise trapped in formats lawyers couldn't access quickly

Thomson Reuters needed an AI solution to leverage their vast professional knowledge base while meeting strict accuracy and reliability requirements. The risk of providing wrong advice is substantial, requiring extraordinarily high quality thresholds.

They needed technology to maintain their high standards while making expert knowledge more accessible. In professional services, response speed can directly determine who wins clients. But accuracy can't be sacrificed, as wrong advice can expose clients to regulatory liability and penalties.

The solution

AI platform delivers comprehensive legal analysis in minutes instead of hours

Thomson Reuters uses Claude in Amazon Bedrock as part of its strategy to power their AI platform, CoCounsel, helping legal and tax professionals synthesize expert knowledge and deliver comprehensive advice to clients.

After extensive evaluation against automated and human expert benchmarks, Thomson Reuters selected Claude. Their choice to deploy Claude in Amazon Bedrock emerged from three key factors: Anthropic's focus on safety aligning with their core values, Claude consistently meeting rigorous quality standards, and Amazon Bedrock providing significant enterprise advantages for rapid testing and deployment while maintaining strict security standards.

#### Results and impact

* **Minutes to search** 3,000+ domain experts and 150 years of case law
* Thomson Reuters tests AI models **the day they're released** via Amazon Bedrock
