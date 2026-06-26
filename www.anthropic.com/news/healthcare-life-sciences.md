<!-- source: https://www.anthropic.com/news/healthcare-life-sciences -->

# Advancing Claude in healthcare and the life sciences
2026년 1월 11일
[Watch on-demand](https://anthropic.com/events/the-briefing-healthcare-and-life-sciences-virtual-event)
![Advancing Claude in healthcare and the life sciences](https://www-cdn.anthropic.com/images/4zrzovbb/website/a5be087781bd5c60788beba7d8148d147bc4d0ed-1000x1000.svg)
Getting started
  * Introducing Claude for Healthcare
  * Expanding Claude for Life Sciences
  * Getting started

In October, we announced [Claude for Life Sciences](https://www.anthropic.com/news/claude-for-life-sciences), our latest step in making Claude a productive research partner for scientists and clinicians, and in helping Claude to support those in industry bringing new scientific advancements to the public.
Now, we’re expanding that feature set in two ways. First, we’re introducing [Claude for Healthcare](https://claude.com/solutions/healthcare), a complementary set of tools and resources that allow healthcare providers, payers, and health tech companies and startups to use Claude for medical purposes through HIPAA-ready products. We're also introducing tools to help individuals understand and navigate their personal health data. Second, we’re adding new capabilities for life sciences: connecting Claude to more scientific platforms, and helping it provide greater support in areas ranging from clinical trial management to regulatory operations.
These features build on top of major recent improvements we’ve made to Claude’s general intelligence. These improvements are best captured by evaluations of Claude’s agentic performance on detailed simulations of medical and scientific tasks, since this correlates most closely to real-world usefulness. Here, Claude Opus 4.5, our latest model, represents a major forward step:
Medical benchmark performanceKey life sciences tasksSpatialBench: Spatial biology analysis by LatchBio
![Medical benchmarket performance](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F351d4c302f534df54f68ade366e423cd037cbf17-1920x1080.png&w=3840&q=75)
  * _*Claude 4.5 models evaluated with extended thinking (64k tokens) and native tool use_
  * _MedCalc: Medical calculation accuracy (with Python code execution)_
  * _MedAgentBench: Medical agent task completion ([Stanford](https://ai.nejm.org/doi/pdf/10.1056/AIdbp2500144))_

![Spatial biology analysis](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe0c2419a2d241cb88327244ddc34abd7a067f91e-1920x1080.png&w=3840&q=75)_Opus 4.5 model shows improvement in accuracy against our internal evaluation of key life sciences tasks (scientific figure interpretation, computational biology, and protein understanding)_
![SpatailBench: Spatial biology analysis by LatchBio](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F870ba1c53ad1135cf7f9a5c57c30a9631a946787-1920x1080.png&w=3840&q=75)_Source:[LatchBio SpatialBench](https://blog.latch.bio/p/spatialbench-can-agents-analyze-real) (Dec 2025) - 146 verifiable problems across 5 spatial problems and 7 task categories_
In addition, Opus 4.5 with extended thinking improves on earlier Claude models in producing correct answers on our suite of honesty evaluations, reflecting the progress we’ve made on factual hallucinations.1
With these model improvements and our new tools, Claude is now dramatically more useful for real-world healthcare and life sciences tasks. Ultimately, it’s those real-world outcomes that have motivated our work: these tools can be used to speed up prior authorization requests so that patients can get life saving care more quickly, can help with patient care coordination to reduce the pressures on clinicians' time, and help with regulatory submissions so that more life saving drugs can come to market faster. We discuss the practical ways that Claude can be used across these industries in more detail below.
## **Introducing Claude for Healthcare**
#### **What’s new**
[Connectors](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6/settings/connectors) are tools that allow users to give Claude access to other platforms directly. For payers and providers, we’ve added several connectors that make healthcare information easier to find, access, and understand. These allow Claude to pull information from industry-standard systems and databases, meaning that clinicians and administrators can save significant time finding the data and generating the reports they need.
Claude can now connect to:
  * The **Centers for Medicare & Medicaid Services (CMS) Coverage Database**, including both Local and National Coverage Determinations. This enables Claude to verify locally-accurate coverage requirements, support prior authorization checks, and help build stronger claims appeals. This connector is designed to help revenue cycle, compliance, and patient-facing teams work more efficiently with Medicare policy.
  * The **International Classification of Diseases, 10th Revision (ICD-10).** Claude can look up both diagnosis and procedure codes to support medical coding, billing accuracy, and claims management. This data is provided by the CMS and the Centers for Disease Control and Prevention (CDC).
  * The **National Provider Identifier Registry** , which allows Claude to help with provider verification, credentialing, networking directory management, and claims validation.

Since HIPAA-compliant organizations can now use Claude for Enterprise, they can also access existing healthcare-related connectors, including **PubMed** , which provides access to more than 35 million pieces of biomedical literature and allows Claude to quickly surface the latest research, and produce up-to-date literature reviews.
Finally, we’ve added two new [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): **FHIR development** and a sample**prior authorization review** skill. FHIR is the modern standard for exchanging data between healthcare systems, and this skill helps to improve interoperability by enabling developers to connect them faster and with fewer errors.
The prior authorization skill**** provides a template that can be customized to organizations’ policies and work patterns, helping with cross-referencing between coverage requirements, clinical guidelines, patient records, and appeal documents.
#### **Using Claude for healthcare tasks**
With these new tools, Claude can provide meaningful support for healthcare startups building new products, and for large enterprises looking to integrate AI more deeply into their operations. For example, Claude can:
**Speed up reviews of prior authorization requests**. These requests can take hours to review, slowing patients’ access to care they need and frustrating payers and providers alike. Reviews require working across various fragmented sources of information, including coverage requirements, clinical guidelines, patient records, and appeal documents. Now, Claude can pull coverage requirements from CMS or custom policies, check clinical criteria against patient records in a HIPAA-ready manner, and then propose a determination with supporting materials for the payer’s review.
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F249b312cf875a6daa78a7d42497d58bf457b8099-3418x1914.png&w=3840&q=75)
**Support claims appeals**. Denied claims cost time and money for all parties. By pulling together the necessary information from patient records, coverage policies, clinical guidelines and prior documentation, Claude helps providers build stronger appeals, and helps payers to process them more quickly.
**Coordinate care and triage patient messages.** Claude can support care teams in navigating a large volume of patient portal messages, referrals, and handoffs. It can sort through these to identify what needs immediate attention, and to ensure that nothing gets inadvertently forgotten.
**Support healthcare startups developing new ideas.** On the Claude Developer Platform, startups can build new products that use Claude to reduce the time burden of healthcare administration—such as ambient scribing for clinical documentation, or tools to support chart reviews and clinical decisions.
#### **Connecting personal health data**
We’re also introducing integrations designed to make it easier for individuals to understand their health information and prepare for important medical conversations with clinicians.
In the US, Claude Pro and Max plan subscribers can choose to give Claude secure access to their lab results and health records. New **HealthEx** and **Function** connectors are available in beta today, while **Apple Health** and **Android Health Connect** integrations**** are**** rolling out in beta this week via the Claude [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude&hl=en_GB&pli=1) apps.
When connected, Claude can summarize users’ medical history, explain test results in plain language, detect patterns across fitness and health metrics, and prepare questions for appointments. The aim is to make patients' conversations with doctors more productive, and to help users stay well-informed about their health.
These integrations are private by design. Users can choose exactly the information they share with Claude, must explicitly opt-in to enable access, and can disconnect or edit Claude’s permissions at any time. We do not use users’ health data to train models.
Claude is designed to include contextual disclaimers, acknowledge its uncertainty, and direct users to healthcare professionals for personalized guidance.
## **Expanding Claude for Life Sciences**
#### **What’s new**
In our initial release, we focused on making Claude more powerful for preclinical research and development (including bioinformatics, and generating hypotheses and protocols). Now, we’re expanding our focus to the clinical trial operations and regulatory stages of the development chain. We’re adding connectors to:
  * **Medidata** , a leading provider of clinical trial solutions to the life sciences industry. Enabled Medidata Study Feasibility customers can use Claude to securely access Medidata's historical trial enrollment information as well as information about site performance.
  * **ClinicalTrials.gov** , the US clinical trials registry. This provides Claude with information on drug and device development pipelines, as well as patient recruitment planning, site selection, and protocol design.
  * **ToolUniverse** , which allows scientists to use a library of over 600 vetted scientific tools to rapidly test hypotheses, compare approaches, and refine their analyses.
  * **bioRxiv & medRxiv**, the life sciences preprint servers. When connected to bioRxiv & medRxiv, Claude can access the latest research before it’s formally published.
  * **Open Targets** , which supports the systematic identification and prioritization of potential therapeutic drug targets.
  * **ChEMBL** , the bioactive compound and drug database, which will help Claude support early discovery work.
  * **Owkin,** whose**** Pathology Explorer agent analyzes tissue images to detect cells and map tumors, designed to accelerate drug discovery and development.

These join our existing Life Sciences connectors to **Benchling** , **10x Genomics** , **PubMed** , **BioRender** , **Synapse.org** , and **Wiley Scholar Gateway**. Our Benchling connector is now also available via Claude.ai on the web (in addition to the Claude desktop app), with secure access via SSO.
Finally, we’re adding new Agent Skills for **scientific problem selection** , converting **instrument data to Allotrope** , and supporting bioinformatics work with skills bundles for **scVI-tools** and **Nextflow deployment**. We’re also adding a sample skill for **clinical trial protocol draft generation**. These drafts include endpoint recommendations and account for regulatory pathways, the competitive landscape, and relevant FDA guidelines.
See the clinical trial skill in action, below:
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F842ab2275159eeb8f8f4a7d7f5a14050a4e77b93-2982x1632.png&w=3840&q=75)
#### **Using Claude in life sciences**
With this new package of tools, Claude can support:
**Drafting clinical trial protocols.** Claude can create a draft of a clinical trial protocol that takes FDA and NIH requirements into account and uses your organization’s preferred templates, policies, and datasets.
**Clinical trial operations.** Using Medidata trial data, Claude can track important indicators—like enrollment and site performance—that allow it to surface issues before they begin to affect a trial’s timeline.
**Preparing regulatory submissions.** Claude can identify gaps in existing regulatory documents, draft responses to agencies’ queries, and navigate FDA guidelines.
#### **Our customers and partners**
We’re working with a number of organizations in healthcare and the life sciences. A selection of our partners describe their experiences using Claude below:
![Banner Health logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2b0c94b75aa81c160289105e777a25eecc8fcdd0-2145x276.png&w=256&q=75)
> We were drawn to [Anthropic's focus on AI safety](https://claude.com/customers/banner-health) and Claude's Constitutional AI approach to creating more helpful, harmless, and honest AI systems.
> Mike Reagin  
> Chief Technology Officer, Banner Health
![Novo Nordisk logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5080602ba328ac22c4a32d3cd348ba234320900a-800x565.png&w=256&q=75)
> We've consistently been one of the first movers when it comes to document and content automation in pharma development. [Our work with Anthropic and Claude](https://claude.com/customers/novo-nordisk) has set a new standard — we're not just automating tasks, we're transforming how medicines get from discovery to the patients who need them.
> Louise Lind Skov  
> Director Content Digitalisation, Novo Nordisk
![Qualified Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/220d794f1916851d190771cbf1e5d0c967372f5b-231x32.svg)
> Safety is non-negotiable in healthcare. [Anthropic has been a clear leader](https://claude.com/customers/qualified-health) in building models with strong safety foundations.
> Justin Norden  
> MD and co-founder, Qualified Health
![Genmab logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffe19dca89482cda5712ddb7d40d0b0e5db73f2a6-1301x380.png&w=256&q=75)
> By reducing manual burden, our partnership with Anthropic will empower our teams to focus more time on high-value scientific and strategic work, accelerating our path to patient impact.
> Hisham Hamadeh  
> Senior Vice President, Global Head of Data, Digital & AI, Genmab
![Sanofi logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffa1c08cc48fde9dd5c5a5638c661ba0848cfa76a-2000x922.png&w=256&q=75)
> Claude is integral to Sanofi's AI transformation and is used by most Sanofians daily. We're seeing efficiency gains across the value-chain. This collaboration with Anthropic augments human expertise to deliver life-changing medicines faster and more efficiently to patients worldwide.
> Emmanuel Frenehard  
> Chief Digital Officer, Sanofi
![Elation Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d64b1f0e2f15cc9edfaa844e12d13916c7f83018-2047x820.svg)
> We chose Claude, powered by Anthropic, for the strength of its model and [its reputation for responsible AI](https://claude.com/customers/elation-health). That balance of performance plus trust was a decisive factor.
> Kyna Fong  
> CEO & Co-Founder, Elation Health
![Edison Scientific  logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3f900ef1d51813290d22ccaf5ef96390baa9f2bc-116x28.svg)
> Opus 4.5 is an incredible model and a great choice for computational biology. The model is excellent at coding, reasoning about biology, and understanding scientific figures.
> Andrew White  
> CTO, Edison Scientific 
![Viz.ai logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1f2ac3aa8f9d8171e56f1a71fd5c57f550fe4352-6144x3190.png&w=256&q=75)
> Anthropic's models are unmatched in their reasoning capabilities and safety design.
> Chris Mansi  
> MD, CEO & Co-founder, Viz.ai
![Flatiron Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3cacb2a412f094d7793f89666a25557dd976a797-476x144.svg)
> Claude has fundamentally changed what's possible in evidence generation. For the first time, our researchers can truly converse with our datasets.
> Allison Candido  
> Chief Technology Officer, Flatiron Health
![Veeva AI logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/522b19dda39de3a0cd89f858f4e6407259b1a6bb-354x115.svg)
> Veeva AI is industry-specific agentic AI that leverages Veeva's deep applications, data, domain expertise, and Anthropic’s Claude. This unique combination allows us to bring the transformative promise of AI to life sciences at scale.
> Andy Han  
> Senior Vice President, Veeva AI
![Heidi Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/dc06aadb4792a8de3c9c9d2173310e43d63b9111-198x226.svg)
> Claude's Agent SDK has unlocked a step-change in how we operate—converting rigid research processes into adaptive, compliant agents.
> Dr. Thomas Kelly  
> Co-Founder and CEO, Heidi Health
![Schrödinger logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb463e00f9945da22059fbb8216e3af714f58fd62-1238x362.png&w=256&q=75)
> Claude Code has become a powerful accelerator for us at Schrödinger. For the projects where it fits best, Claude Code allows us to turn ideas into working code in minutes instead of hours, enabling us to move up to 10x faster in some cases. As we continue to work with Claude, we are excited to see how we can further transform the way we build and customize our software.
> Pat Lorton  
> EVP, Chief Technology Officer, and Chief Operating Officer, Schrödinger
![Premier  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd60f9669eac6ad0a11dc87fd8ac559f6822e0b62-2247x454.png&w=256&q=75)
> Claude handles the complex healthcare workflows our teams deal with daily—accurately and securely. Our engineers are shipping faster, our consultants are delivering insights with unprecedented speed. When you're serving 4,400+ healthcare organizations, that combination of capability and velocity is critical.
> David Zito  
> President Performance Services, Premier 
![Commure logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e409cc084939de75e85575594b8cb918ba007653-113x40.svg)
> For Commure’s Ambient AI, precision is the prerequisite for trust. Scaling to tens of millions of appointments requires exceptional performance and contextual understanding. With Claude’s suite of LLMs, we deliver the quality to automate clinical documentation at scale, saving clinicians millions of hours annually and returning their focus to patient care.
> Dhruv Parthasarathy  
> Chief Technology Officer, Commure
![Carta Healthcare  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd98996a63d8d455b163cb8d111d965a8558d3f63-2000x827.png&w=256&q=75)
> Carta Healthcare's implementation of [Anthropic models via Amazon Bedrock](https://claude.com/customers/carta-healthcare) has allowed for rapid and secure deployment of the newest models. Unlocking our hybrid intelligence AI system that is turning into a complete re-invention of understanding a patient’s medical record for clinical data abstraction.
> Andrew Crowder  
> VP of Engineering, Carta Healthcare 
![Brellium  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0a0504e322bd7039208046f9812c0f849f20c5f0-750x165.png&w=256&q=75)
> Claude lets us punch way above our weight in healthcare AI. It powers our clinical extraction engine, cuts implementation timelines, and gives our GTM team dev-level capabilities. The faster we build, the faster clinics get out of manual chart review and back to patients.
> Zach Rosen  
> CEO & Co-Founder, Brellium 
01 / 16
Claude is the only frontier model available on all three leading cloud services: AWS, Google Cloud, and Microsoft.
We’re also partnering with companies who specialize in helping organizations adopt AI for specialist work, including Accenture, Blank Metal, Caylent, Deloitte, Deepsense.ai, Firemind, KPMG, Provectus, PwC, OWT, Quantium, Slalom, Tribe AI, and Turing.
## **Getting started**
To learn more about Claude for Healthcare, see [here](http://claude.com/solutions/healthcare), or see our tutorial guides [here](https://claude.com/resources/tutorials-category/healthcare). For more detail on the expanded Claude for Life Sciences capabilities, see [here](https://claude.com/solutions/life-sciences), and our tutorial guides [here](https://claude.com/resources/tutorials-category/life-sciences).
Our new connectors and Agent Skills are generally available to all Claude subscribers, including Claude Pro, Max, Teams, and Enterprise.
You can also [contact our sales team](https://www.claude.com/contact-sales%20) to discuss bringing Claude to your organization.
#### Footnotes
_1: See the[Claude Opus 4.5 system card](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf), pages 48-49._
**Changelog:**
February 7, 2026: _Edited the introductory paragraph to clarify that HIPAA-ready products are specific to healthcare providers and payers. The personal health integrations for individual users are covered in the "Connecting personal health data" section._
[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/healthcare-life-sciences)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/healthcare-life-sciences)
Announcements
# Advancing Claude in healthcare and the life sciences
2026년 1월 11일
[Watch on-demand](https://anthropic.com/events/the-briefing-healthcare-and-life-sciences-virtual-event)
![Advancing Claude in healthcare and the life sciences](https://www-cdn.anthropic.com/images/4zrzovbb/website/a5be087781bd5c60788beba7d8148d147bc4d0ed-1000x1000.svg)
Getting started
  * Introducing Claude for Healthcare
  * Expanding Claude for Life Sciences
  * Getting started

In October, we announced [Claude for Life Sciences](https://www.anthropic.com/news/claude-for-life-sciences), our latest step in making Claude a productive research partner for scientists and clinicians, and in helping Claude to support those in industry bringing new scientific advancements to the public.
Now, we’re expanding that feature set in two ways. First, we’re introducing [Claude for Healthcare](https://claude.com/solutions/healthcare), a complementary set of tools and resources that allow healthcare providers, payers, and health tech companies and startups to use Claude for medical purposes through HIPAA-ready products. We're also introducing tools to help individuals understand and navigate their personal health data. Second, we’re adding new capabilities for life sciences: connecting Claude to more scientific platforms, and helping it provide greater support in areas ranging from clinical trial management to regulatory operations.
These features build on top of major recent improvements we’ve made to Claude’s general intelligence. These improvements are best captured by evaluations of Claude’s agentic performance on detailed simulations of medical and scientific tasks, since this correlates most closely to real-world usefulness. Here, Claude Opus 4.5, our latest model, represents a major forward step:
Medical benchmark performanceKey life sciences tasksSpatialBench: Spatial biology analysis by LatchBio
![Medical benchmarket performance](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F351d4c302f534df54f68ade366e423cd037cbf17-1920x1080.png&w=3840&q=75)
  * _*Claude 4.5 models evaluated with extended thinking (64k tokens) and native tool use_
  * _MedCalc: Medical calculation accuracy (with Python code execution)_
  * _MedAgentBench: Medical agent task completion ([Stanford](https://ai.nejm.org/doi/pdf/10.1056/AIdbp2500144))_

![Spatial biology analysis](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe0c2419a2d241cb88327244ddc34abd7a067f91e-1920x1080.png&w=3840&q=75)_Opus 4.5 model shows improvement in accuracy against our internal evaluation of key life sciences tasks (scientific figure interpretation, computational biology, and protein understanding)_
![SpatailBench: Spatial biology analysis by LatchBio](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F870ba1c53ad1135cf7f9a5c57c30a9631a946787-1920x1080.png&w=3840&q=75)_Source:[LatchBio SpatialBench](https://blog.latch.bio/p/spatialbench-can-agents-analyze-real) (Dec 2025) - 146 verifiable problems across 5 spatial problems and 7 task categories_
In addition, Opus 4.5 with extended thinking improves on earlier Claude models in producing correct answers on our suite of honesty evaluations, reflecting the progress we’ve made on factual hallucinations.1
With these model improvements and our new tools, Claude is now dramatically more useful for real-world healthcare and life sciences tasks. Ultimately, it’s those real-world outcomes that have motivated our work: these tools can be used to speed up prior authorization requests so that patients can get life saving care more quickly, can help with patient care coordination to reduce the pressures on clinicians' time, and help with regulatory submissions so that more life saving drugs can come to market faster. We discuss the practical ways that Claude can be used across these industries in more detail below.
## **Introducing Claude for Healthcare**
#### **What’s new**
[Connectors](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6/settings/connectors) are tools that allow users to give Claude access to other platforms directly. For payers and providers, we’ve added several connectors that make healthcare information easier to find, access, and understand. These allow Claude to pull information from industry-standard systems and databases, meaning that clinicians and administrators can save significant time finding the data and generating the reports they need.
Claude can now connect to:
  * The **Centers for Medicare & Medicaid Services (CMS) Coverage Database**, including both Local and National Coverage Determinations. This enables Claude to verify locally-accurate coverage requirements, support prior authorization checks, and help build stronger claims appeals. This connector is designed to help revenue cycle, compliance, and patient-facing teams work more efficiently with Medicare policy.
  * The **International Classification of Diseases, 10th Revision (ICD-10).** Claude can look up both diagnosis and procedure codes to support medical coding, billing accuracy, and claims management. This data is provided by the CMS and the Centers for Disease Control and Prevention (CDC).
  * The **National Provider Identifier Registry** , which allows Claude to help with provider verification, credentialing, networking directory management, and claims validation.

Since HIPAA-compliant organizations can now use Claude for Enterprise, they can also access existing healthcare-related connectors, including **PubMed** , which provides access to more than 35 million pieces of biomedical literature and allows Claude to quickly surface the latest research, and produce up-to-date literature reviews.
Finally, we’ve added two new [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): **FHIR development** and a sample**prior authorization review** skill. FHIR is the modern standard for exchanging data between healthcare systems, and this skill helps to improve interoperability by enabling developers to connect them faster and with fewer errors.
The prior authorization skill**** provides a template that can be customized to organizations’ policies and work patterns, helping with cross-referencing between coverage requirements, clinical guidelines, patient records, and appeal documents.
#### **Using Claude for healthcare tasks**
With these new tools, Claude can provide meaningful support for healthcare startups building new products, and for large enterprises looking to integrate AI more deeply into their operations. For example, Claude can:
**Speed up reviews of prior authorization requests**. These requests can take hours to review, slowing patients’ access to care they need and frustrating payers and providers alike. Reviews require working across various fragmented sources of information, including coverage requirements, clinical guidelines, patient records, and appeal documents. Now, Claude can pull coverage requirements from CMS or custom policies, check clinical criteria against patient records in a HIPAA-ready manner, and then propose a determination with supporting materials for the payer’s review.
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F249b312cf875a6daa78a7d42497d58bf457b8099-3418x1914.png&w=3840&q=75)
**Support claims appeals**. Denied claims cost time and money for all parties. By pulling together the necessary information from patient records, coverage policies, clinical guidelines and prior documentation, Claude helps providers build stronger appeals, and helps payers to process them more quickly.
**Coordinate care and triage patient messages.** Claude can support care teams in navigating a large volume of patient portal messages, referrals, and handoffs. It can sort through these to identify what needs immediate attention, and to ensure that nothing gets inadvertently forgotten.
**Support healthcare startups developing new ideas.** On the Claude Developer Platform, startups can build new products that use Claude to reduce the time burden of healthcare administration—such as ambient scribing for clinical documentation, or tools to support chart reviews and clinical decisions.
#### **Connecting personal health data**
We’re also introducing integrations designed to make it easier for individuals to understand their health information and prepare for important medical conversations with clinicians.
In the US, Claude Pro and Max plan subscribers can choose to give Claude secure access to their lab results and health records. New **HealthEx** and **Function** connectors are available in beta today, while **Apple Health** and **Android Health Connect** integrations**** are**** rolling out in beta this week via the Claude [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude&hl=en_GB&pli=1) apps.
When connected, Claude can summarize users’ medical history, explain test results in plain language, detect patterns across fitness and health metrics, and prepare questions for appointments. The aim is to make patients' conversations with doctors more productive, and to help users stay well-informed about their health.
These integrations are private by design. Users can choose exactly the information they share with Claude, must explicitly opt-in to enable access, and can disconnect or edit Claude’s permissions at any time. We do not use users’ health data to train models.
Claude is designed to include contextual disclaimers, acknowledge its uncertainty, and direct users to healthcare professionals for personalized guidance.
## **Expanding Claude for Life Sciences**
#### **What’s new**
In our initial release, we focused on making Claude more powerful for preclinical research and development (including bioinformatics, and generating hypotheses and protocols). Now, we’re expanding our focus to the clinical trial operations and regulatory stages of the development chain. We’re adding connectors to:
  * **Medidata** , a leading provider of clinical trial solutions to the life sciences industry. Enabled Medidata Study Feasibility customers can use Claude to securely access Medidata's historical trial enrollment information as well as information about site performance.
  * **ClinicalTrials.gov** , the US clinical trials registry. This provides Claude with information on drug and device development pipelines, as well as patient recruitment planning, site selection, and protocol design.
  * **ToolUniverse** , which allows scientists to use a library of over 600 vetted scientific tools to rapidly test hypotheses, compare approaches, and refine their analyses.
  * **bioRxiv & medRxiv**, the life sciences preprint servers. When connected to bioRxiv & medRxiv, Claude can access the latest research before it’s formally published.
  * **Open Targets** , which supports the systematic identification and prioritization of potential therapeutic drug targets.
  * **ChEMBL** , the bioactive compound and drug database, which will help Claude support early discovery work.
  * **Owkin,** whose**** Pathology Explorer agent analyzes tissue images to detect cells and map tumors, designed to accelerate drug discovery and development.

These join our existing Life Sciences connectors to **Benchling** , **10x Genomics** , **PubMed** , **BioRender** , **Synapse.org** , and **Wiley Scholar Gateway**. Our Benchling connector is now also available via Claude.ai on the web (in addition to the Claude desktop app), with secure access via SSO.
Finally, we’re adding new Agent Skills for **scientific problem selection** , converting **instrument data to Allotrope** , and supporting bioinformatics work with skills bundles for **scVI-tools** and **Nextflow deployment**. We’re also adding a sample skill for **clinical trial protocol draft generation**. These drafts include endpoint recommendations and account for regulatory pathways, the competitive landscape, and relevant FDA guidelines.
See the clinical trial skill in action, below:
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F842ab2275159eeb8f8f4a7d7f5a14050a4e77b93-2982x1632.png&w=3840&q=75)
#### **Using Claude in life sciences**
With this new package of tools, Claude can support:
**Drafting clinical trial protocols.** Claude can create a draft of a clinical trial protocol that takes FDA and NIH requirements into account and uses your organization’s preferred templates, policies, and datasets.
**Clinical trial operations.** Using Medidata trial data, Claude can track important indicators—like enrollment and site performance—that allow it to surface issues before they begin to affect a trial’s timeline.
**Preparing regulatory submissions.** Claude can identify gaps in existing regulatory documents, draft responses to agencies’ queries, and navigate FDA guidelines.
#### **Our customers and partners**
We’re working with a number of organizations in healthcare and the life sciences. A selection of our partners describe their experiences using Claude below:
![Banner Health logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2b0c94b75aa81c160289105e777a25eecc8fcdd0-2145x276.png&w=256&q=75)
> We were drawn to [Anthropic's focus on AI safety](https://claude.com/customers/banner-health) and Claude's Constitutional AI approach to creating more helpful, harmless, and honest AI systems.
> Mike Reagin  
> Chief Technology Officer, Banner Health
![Novo Nordisk logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5080602ba328ac22c4a32d3cd348ba234320900a-800x565.png&w=256&q=75)
> We've consistently been one of the first movers when it comes to document and content automation in pharma development. [Our work with Anthropic and Claude](https://claude.com/customers/novo-nordisk) has set a new standard — we're not just automating tasks, we're transforming how medicines get from discovery to the patients who need them.
> Louise Lind Skov  
> Director Content Digitalisation, Novo Nordisk
![Qualified Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/220d794f1916851d190771cbf1e5d0c967372f5b-231x32.svg)
> Safety is non-negotiable in healthcare. [Anthropic has been a clear leader](https://claude.com/customers/qualified-health) in building models with strong safety foundations.
> Justin Norden  
> MD and co-founder, Qualified Health
![Genmab logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffe19dca89482cda5712ddb7d40d0b0e5db73f2a6-1301x380.png&w=256&q=75)
> By reducing manual burden, our partnership with Anthropic will empower our teams to focus more time on high-value scientific and strategic work, accelerating our path to patient impact.
> Hisham Hamadeh  
> Senior Vice President, Global Head of Data, Digital & AI, Genmab
![Sanofi logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffa1c08cc48fde9dd5c5a5638c661ba0848cfa76a-2000x922.png&w=256&q=75)
> Claude is integral to Sanofi's AI transformation and is used by most Sanofians daily. We're seeing efficiency gains across the value-chain. This collaboration with Anthropic augments human expertise to deliver life-changing medicines faster and more efficiently to patients worldwide.
> Emmanuel Frenehard  
> Chief Digital Officer, Sanofi
![Elation Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d64b1f0e2f15cc9edfaa844e12d13916c7f83018-2047x820.svg)
> We chose Claude, powered by Anthropic, for the strength of its model and [its reputation for responsible AI](https://claude.com/customers/elation-health). That balance of performance plus trust was a decisive factor.
> Kyna Fong  
> CEO & Co-Founder, Elation Health
![Edison Scientific  logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3f900ef1d51813290d22ccaf5ef96390baa9f2bc-116x28.svg)
> Opus 4.5 is an incredible model and a great choice for computational biology. The model is excellent at coding, reasoning about biology, and understanding scientific figures.
> Andrew White  
> CTO, Edison Scientific 
![Viz.ai logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1f2ac3aa8f9d8171e56f1a71fd5c57f550fe4352-6144x3190.png&w=256&q=75)
> Anthropic's models are unmatched in their reasoning capabilities and safety design.
> Chris Mansi  
> MD, CEO & Co-founder, Viz.ai
![Flatiron Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3cacb2a412f094d7793f89666a25557dd976a797-476x144.svg)
> Claude has fundamentally changed what's possible in evidence generation. For the first time, our researchers can truly converse with our datasets.
> Allison Candido  
> Chief Technology Officer, Flatiron Health
![Veeva AI logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/522b19dda39de3a0cd89f858f4e6407259b1a6bb-354x115.svg)
> Veeva AI is industry-specific agentic AI that leverages Veeva's deep applications, data, domain expertise, and Anthropic’s Claude. This unique combination allows us to bring the transformative promise of AI to life sciences at scale.
> Andy Han  
> Senior Vice President, Veeva AI
![Heidi Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/dc06aadb4792a8de3c9c9d2173310e43d63b9111-198x226.svg)
> Claude's Agent SDK has unlocked a step-change in how we operate—converting rigid research processes into adaptive, compliant agents.
> Dr. Thomas Kelly  
> Co-Founder and CEO, Heidi Health
![Schrödinger logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb463e00f9945da22059fbb8216e3af714f58fd62-1238x362.png&w=256&q=75)
> Claude Code has become a powerful accelerator for us at Schrödinger. For the projects where it fits best, Claude Code allows us to turn ideas into working code in minutes instead of hours, enabling us to move up to 10x faster in some cases. As we continue to work with Claude, we are excited to see how we can further transform the way we build and customize our software.
> Pat Lorton  
> EVP, Chief Technology Officer, and Chief Operating Officer, Schrödinger
![Premier  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd60f9669eac6ad0a11dc87fd8ac559f6822e0b62-2247x454.png&w=256&q=75)
> Claude handles the complex healthcare workflows our teams deal with daily—accurately and securely. Our engineers are shipping faster, our consultants are delivering insights with unprecedented speed. When you're serving 4,400+ healthcare organizations, that combination of capability and velocity is critical.
> David Zito  
> President Performance Services, Premier 
![Commure logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e409cc084939de75e85575594b8cb918ba007653-113x40.svg)
> For Commure’s Ambient AI, precision is the prerequisite for trust. Scaling to tens of millions of appointments requires exceptional performance and contextual understanding. With Claude’s suite of LLMs, we deliver the quality to automate clinical documentation at scale, saving clinicians millions of hours annually and returning their focus to patient care.
> Dhruv Parthasarathy  
> Chief Technology Officer, Commure
![Carta Healthcare  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd98996a63d8d455b163cb8d111d965a8558d3f63-2000x827.png&w=256&q=75)
> Carta Healthcare's implementation of [Anthropic models via Amazon Bedrock](https://claude.com/customers/carta-healthcare) has allowed for rapid and secure deployment of the newest models. Unlocking our hybrid intelligence AI system that is turning into a complete re-invention of understanding a patient’s medical record for clinical data abstraction.
> Andrew Crowder  
> VP of Engineering, Carta Healthcare 
![Brellium  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0a0504e322bd7039208046f9812c0f849f20c5f0-750x165.png&w=256&q=75)
> Claude lets us punch way above our weight in healthcare AI. It powers our clinical extraction engine, cuts implementation timelines, and gives our GTM team dev-level capabilities. The faster we build, the faster clinics get out of manual chart review and back to patients.
> Zach Rosen  
> CEO & Co-Founder, Brellium 
01 / 16
Claude is the only frontier model available on all three leading cloud services: AWS, Google Cloud, and Microsoft.
We’re also partnering with companies who specialize in helping organizations adopt AI for specialist work, including Accenture, Blank Metal, Caylent, Deloitte, Deepsense.ai, Firemind, KPMG, Provectus, PwC, OWT, Quantium, Slalom, Tribe AI, and Turing.
## **Getting started**
To learn more about Claude for Healthcare, see [here](http://claude.com/solutions/healthcare), or see our tutorial guides [here](https://claude.com/resources/tutorials-category/healthcare). For more detail on the expanded Claude for Life Sciences capabilities, see [here](https://claude.com/solutions/life-sciences), and our tutorial guides [here](https://claude.com/resources/tutorials-category/life-sciences).
Our new connectors and Agent Skills are generally available to all Claude subscribers, including Claude Pro, Max, Teams, and Enterprise.
You can also [contact our sales team](https://www.claude.com/contact-sales%20) to discuss bringing Claude to your organization.
#### Footnotes
_1: See the[Claude Opus 4.5 system card](https://assets.anthropic.com/m/64823ba7485345a7/Claude-Opus-4-5-System-Card.pdf), pages 48-49._
**Changelog:**
February 7, 2026: _Edited the introductory paragraph to clarify that HIPAA-ready products are specific to healthcare providers and payers. The personal health integrations for individual users are covered in the "Connecting personal health data" section._
[](https://twitter.com/intent/tweet?text=https://www.anthropic.com/news/healthcare-life-sciences)[](https://www.linkedin.com/shareArticle?mini=true&url=https://www.anthropic.com/news/healthcare-life-sciences)
Getting started
  * Introducing Claude for Healthcare
  * Expanding Claude for Life Sciences
  * Getting started

In October, we announced [Claude for Life Sciences](https://www.anthropic.com/news/claude-for-life-sciences), our latest step in making Claude a productive research partner for scientists and clinicians, and in helping Claude to support those in industry bringing new scientific advancements to the public.
Now, we’re expanding that feature set in two ways. First, we’re introducing [Claude for Healthcare](https://claude.com/solutions/healthcare), a complementary set of tools and resources that allow healthcare providers, payers, and health tech companies and startups to use Claude for medical purposes through HIPAA-ready products. We're also introducing tools to help individuals understand and navigate their personal health data. Second, we’re adding new capabilities for life sciences: connecting Claude to more scientific platforms, and helping it provide greater support in areas ranging from clinical trial management to regulatory operations.
These features build on top of major recent improvements we’ve made to Claude’s general intelligence. These improvements are best captured by evaluations of Claude’s agentic performance on detailed simulations of medical and scientific tasks, since this correlates most closely to real-world usefulness. Here, Claude Opus 4.5, our latest model, represents a major forward step:
Medical benchmark performanceKey life sciences tasksSpatialBench: Spatial biology analysis by LatchBio
![Medical benchmarket performance](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F351d4c302f534df54f68ade366e423cd037cbf17-1920x1080.png&w=3840&q=75)
  * _*Claude 4.5 models evaluated with extended thinking (64k tokens) and native tool use_
  * _MedCalc: Medical calculation accuracy (with Python code execution)_
  * _MedAgentBench: Medical agent task completion ([Stanford](https://ai.nejm.org/doi/pdf/10.1056/AIdbp2500144))_

![Spatial biology analysis](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fe0c2419a2d241cb88327244ddc34abd7a067f91e-1920x1080.png&w=3840&q=75)_Opus 4.5 model shows improvement in accuracy against our internal evaluation of key life sciences tasks (scientific figure interpretation, computational biology, and protein understanding)_
![SpatailBench: Spatial biology analysis by LatchBio](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F870ba1c53ad1135cf7f9a5c57c30a9631a946787-1920x1080.png&w=3840&q=75)_Source:[LatchBio SpatialBench](https://blog.latch.bio/p/spatialbench-can-agents-analyze-real) (Dec 2025) - 146 verifiable problems across 5 spatial problems and 7 task categories_
In addition, Opus 4.5 with extended thinking improves on earlier Claude models in producing correct answers on our suite of honesty evaluations, reflecting the progress we’ve made on factual hallucinations.1
With these model improvements and our new tools, Claude is now dramatically more useful for real-world healthcare and life sciences tasks. Ultimately, it’s those real-world outcomes that have motivated our work: these tools can be used to speed up prior authorization requests so that patients can get life saving care more quickly, can help with patient care coordination to reduce the pressures on clinicians' time, and help with regulatory submissions so that more life saving drugs can come to market faster. We discuss the practical ways that Claude can be used across these industries in more detail below.
## **Introducing Claude for Healthcare**
#### **What’s new**
[Connectors](https://claude.ai/redirect/website.v1.0e3a6f32-5f88-4168-82b2-642763282fa6/settings/connectors) are tools that allow users to give Claude access to other platforms directly. For payers and providers, we’ve added several connectors that make healthcare information easier to find, access, and understand. These allow Claude to pull information from industry-standard systems and databases, meaning that clinicians and administrators can save significant time finding the data and generating the reports they need.
Claude can now connect to:
  * The **Centers for Medicare & Medicaid Services (CMS) Coverage Database**, including both Local and National Coverage Determinations. This enables Claude to verify locally-accurate coverage requirements, support prior authorization checks, and help build stronger claims appeals. This connector is designed to help revenue cycle, compliance, and patient-facing teams work more efficiently with Medicare policy.
  * The **International Classification of Diseases, 10th Revision (ICD-10).** Claude can look up both diagnosis and procedure codes to support medical coding, billing accuracy, and claims management. This data is provided by the CMS and the Centers for Disease Control and Prevention (CDC).
  * The **National Provider Identifier Registry** , which allows Claude to help with provider verification, credentialing, networking directory management, and claims validation.

Since HIPAA-compliant organizations can now use Claude for Enterprise, they can also access existing healthcare-related connectors, including **PubMed** , which provides access to more than 35 million pieces of biomedical literature and allows Claude to quickly surface the latest research, and produce up-to-date literature reviews.
Finally, we’ve added two new [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): **FHIR development** and a sample**prior authorization review** skill. FHIR is the modern standard for exchanging data between healthcare systems, and this skill helps to improve interoperability by enabling developers to connect them faster and with fewer errors.
The prior authorization skill**** provides a template that can be customized to organizations’ policies and work patterns, helping with cross-referencing between coverage requirements, clinical guidelines, patient records, and appeal documents.
#### **Using Claude for healthcare tasks**
With these new tools, Claude can provide meaningful support for healthcare startups building new products, and for large enterprises looking to integrate AI more deeply into their operations. For example, Claude can:
**Speed up reviews of prior authorization requests**. These requests can take hours to review, slowing patients’ access to care they need and frustrating payers and providers alike. Reviews require working across various fragmented sources of information, including coverage requirements, clinical guidelines, patient records, and appeal documents. Now, Claude can pull coverage requirements from CMS or custom policies, check clinical criteria against patient records in a HIPAA-ready manner, and then propose a determination with supporting materials for the payer’s review.
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F249b312cf875a6daa78a7d42497d58bf457b8099-3418x1914.png&w=3840&q=75)
**Support claims appeals**. Denied claims cost time and money for all parties. By pulling together the necessary information from patient records, coverage policies, clinical guidelines and prior documentation, Claude helps providers build stronger appeals, and helps payers to process them more quickly.
**Coordinate care and triage patient messages.** Claude can support care teams in navigating a large volume of patient portal messages, referrals, and handoffs. It can sort through these to identify what needs immediate attention, and to ensure that nothing gets inadvertently forgotten.
**Support healthcare startups developing new ideas.** On the Claude Developer Platform, startups can build new products that use Claude to reduce the time burden of healthcare administration—such as ambient scribing for clinical documentation, or tools to support chart reviews and clinical decisions.
#### **Connecting personal health data**
We’re also introducing integrations designed to make it easier for individuals to understand their health information and prepare for important medical conversations with clinicians.
In the US, Claude Pro and Max plan subscribers can choose to give Claude secure access to their lab results and health records. New **HealthEx** and **Function** connectors are available in beta today, while **Apple Health** and **Android Health Connect** integrations**** are**** rolling out in beta this week via the Claude [iOS](https://apps.apple.com/us/app/claude-by-anthropic/id6473753684) and [Android](https://play.google.com/store/apps/details?id=com.anthropic.claude&hl=en_GB&pli=1) apps.
When connected, Claude can summarize users’ medical history, explain test results in plain language, detect patterns across fitness and health metrics, and prepare questions for appointments. The aim is to make patients' conversations with doctors more productive, and to help users stay well-informed about their health.
These integrations are private by design. Users can choose exactly the information they share with Claude, must explicitly opt-in to enable access, and can disconnect or edit Claude’s permissions at any time. We do not use users’ health data to train models.
Claude is designed to include contextual disclaimers, acknowledge its uncertainty, and direct users to healthcare professionals for personalized guidance.
## **Expanding Claude for Life Sciences**
#### **What’s new**
In our initial release, we focused on making Claude more powerful for preclinical research and development (including bioinformatics, and generating hypotheses and protocols). Now, we’re expanding our focus to the clinical trial operations and regulatory stages of the development chain. We’re adding connectors to:
  * **Medidata** , a leading provider of clinical trial solutions to the life sciences industry. Enabled Medidata Study Feasibility customers can use Claude to securely access Medidata's historical trial enrollment information as well as information about site performance.
  * **ClinicalTrials.gov** , the US clinical trials registry. This provides Claude with information on drug and device development pipelines, as well as patient recruitment planning, site selection, and protocol design.
  * **ToolUniverse** , which allows scientists to use a library of over 600 vetted scientific tools to rapidly test hypotheses, compare approaches, and refine their analyses.
  * **bioRxiv & medRxiv**, the life sciences preprint servers. When connected to bioRxiv & medRxiv, Claude can access the latest research before it’s formally published.
  * **Open Targets** , which supports the systematic identification and prioritization of potential therapeutic drug targets.
  * **ChEMBL** , the bioactive compound and drug database, which will help Claude support early discovery work.
  * **Owkin,** whose**** Pathology Explorer agent analyzes tissue images to detect cells and map tumors, designed to accelerate drug discovery and development.

These join our existing Life Sciences connectors to **Benchling** , **10x Genomics** , **PubMed** , **BioRender** , **Synapse.org** , and **Wiley Scholar Gateway**. Our Benchling connector is now also available via Claude.ai on the web (in addition to the Claude desktop app), with secure access via SSO.
Finally, we’re adding new Agent Skills for **scientific problem selection** , converting **instrument data to Allotrope** , and supporting bioinformatics work with skills bundles for **scVI-tools** and **Nextflow deployment**. We’re also adding a sample skill for **clinical trial protocol draft generation**. These drafts include endpoint recommendations and account for regulatory pathways, the competitive landscape, and relevant FDA guidelines.
See the clinical trial skill in action, below:
![Video thumbnail](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F4zrzovbb%2Fwebsite%2F842ab2275159eeb8f8f4a7d7f5a14050a4e77b93-2982x1632.png&w=3840&q=75)
#### **Using Claude in life sciences**
With this new package of tools, Claude can support:
**Drafting clinical trial protocols.** Claude can create a draft of a clinical trial protocol that takes FDA and NIH requirements into account and uses your organization’s preferred templates, policies, and datasets.
**Clinical trial operations.** Using Medidata trial data, Claude can track important indicators—like enrollment and site performance—that allow it to surface issues before they begin to affect a trial’s timeline.
**Preparing regulatory submissions.** Claude can identify gaps in existing regulatory documents, draft responses to agencies’ queries, and navigate FDA guidelines.
#### **Our customers and partners**
We’re working with a number of organizations in healthcare and the life sciences. A selection of our partners describe their experiences using Claude below:
![Banner Health logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F2b0c94b75aa81c160289105e777a25eecc8fcdd0-2145x276.png&w=256&q=75)
> We were drawn to [Anthropic's focus on AI safety](https://claude.com/customers/banner-health) and Claude's Constitutional AI approach to creating more helpful, harmless, and honest AI systems.
> Mike Reagin  
> Chief Technology Officer, Banner Health
![Novo Nordisk logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F5080602ba328ac22c4a32d3cd348ba234320900a-800x565.png&w=256&q=75)
> We've consistently been one of the first movers when it comes to document and content automation in pharma development. [Our work with Anthropic and Claude](https://claude.com/customers/novo-nordisk) has set a new standard — we're not just automating tasks, we're transforming how medicines get from discovery to the patients who need them.
> Louise Lind Skov  
> Director Content Digitalisation, Novo Nordisk
![Qualified Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/220d794f1916851d190771cbf1e5d0c967372f5b-231x32.svg)
> Safety is non-negotiable in healthcare. [Anthropic has been a clear leader](https://claude.com/customers/qualified-health) in building models with strong safety foundations.
> Justin Norden  
> MD and co-founder, Qualified Health
![Genmab logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffe19dca89482cda5712ddb7d40d0b0e5db73f2a6-1301x380.png&w=256&q=75)
> By reducing manual burden, our partnership with Anthropic will empower our teams to focus more time on high-value scientific and strategic work, accelerating our path to patient impact.
> Hisham Hamadeh  
> Senior Vice President, Global Head of Data, Digital & AI, Genmab
![Sanofi logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ffa1c08cc48fde9dd5c5a5638c661ba0848cfa76a-2000x922.png&w=256&q=75)
> Claude is integral to Sanofi's AI transformation and is used by most Sanofians daily. We're seeing efficiency gains across the value-chain. This collaboration with Anthropic augments human expertise to deliver life-changing medicines faster and more efficiently to patients worldwide.
> Emmanuel Frenehard  
> Chief Digital Officer, Sanofi
![Elation Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/d64b1f0e2f15cc9edfaa844e12d13916c7f83018-2047x820.svg)
> We chose Claude, powered by Anthropic, for the strength of its model and [its reputation for responsible AI](https://claude.com/customers/elation-health). That balance of performance plus trust was a decisive factor.
> Kyna Fong  
> CEO & Co-Founder, Elation Health
![Edison Scientific  logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3f900ef1d51813290d22ccaf5ef96390baa9f2bc-116x28.svg)
> Opus 4.5 is an incredible model and a great choice for computational biology. The model is excellent at coding, reasoning about biology, and understanding scientific figures.
> Andrew White  
> CTO, Edison Scientific 
![Viz.ai logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F1f2ac3aa8f9d8171e56f1a71fd5c57f550fe4352-6144x3190.png&w=256&q=75)
> Anthropic's models are unmatched in their reasoning capabilities and safety design.
> Chris Mansi  
> MD, CEO & Co-founder, Viz.ai
![Flatiron Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/3cacb2a412f094d7793f89666a25557dd976a797-476x144.svg)
> Claude has fundamentally changed what's possible in evidence generation. For the first time, our researchers can truly converse with our datasets.
> Allison Candido  
> Chief Technology Officer, Flatiron Health
![Veeva AI logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/522b19dda39de3a0cd89f858f4e6407259b1a6bb-354x115.svg)
> Veeva AI is industry-specific agentic AI that leverages Veeva's deep applications, data, domain expertise, and Anthropic’s Claude. This unique combination allows us to bring the transformative promise of AI to life sciences at scale.
> Andy Han  
> Senior Vice President, Veeva AI
![Heidi Health logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/dc06aadb4792a8de3c9c9d2173310e43d63b9111-198x226.svg)
> Claude's Agent SDK has unlocked a step-change in how we operate—converting rigid research processes into adaptive, compliant agents.
> Dr. Thomas Kelly  
> Co-Founder and CEO, Heidi Health
![Schrödinger logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fb463e00f9945da22059fbb8216e3af714f58fd62-1238x362.png&w=256&q=75)
> Claude Code has become a powerful accelerator for us at Schrödinger. For the projects where it fits best, Claude Code allows us to turn ideas into working code in minutes instead of hours, enabling us to move up to 10x faster in some cases. As we continue to work with Claude, we are excited to see how we can further transform the way we build and customize our software.
> Pat Lorton  
> EVP, Chief Technology Officer, and Chief Operating Officer, Schrödinger
![Premier  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd60f9669eac6ad0a11dc87fd8ac559f6822e0b62-2247x454.png&w=256&q=75)
> Claude handles the complex healthcare workflows our teams deal with daily—accurately and securely. Our engineers are shipping faster, our consultants are delivering insights with unprecedented speed. When you're serving 4,400+ healthcare organizations, that combination of capability and velocity is critical.
> David Zito  
> President Performance Services, Premier 
![Commure logo](https://www-cdn.anthropic.com/images/4zrzovbb/website/e409cc084939de75e85575594b8cb918ba007653-113x40.svg)
> For Commure’s Ambient AI, precision is the prerequisite for trust. Scaling to tens of millions of appointments requires exceptional performance and contextual understanding. With Claude’s suite of LLMs, we deliver the quality to automate clinical documentation at scale, saving clinicians millions of hours annually and returning their focus to patient care.
> Dhruv Parthasarathy  
> Chief Technology Officer, Commure
![Carta Healthcare  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Fd98996a63d8d455b163cb8d111d965a8558d3f63-2000x827.png&w=256&q=75)
> Carta Healthcare's implementation of [Anthropic models via Amazon Bedrock](https://claude.com/customers/carta-healthcare) has allowed for rapid and secure deployment of the newest models. Unlocking our hybrid intelligence AI system that is turning into a complete re-invention of understanding a patient’s medical record for clinical data abstraction.
> Andrew Crowder  
> VP of Engineering, Carta Healthcare 
![Brellium  logo](https://www.anthropic.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F0a0504e322bd7039208046f9812c0f849f20c5f0-750x165.png&w=256&q=75)
> Claude lets us punch way above our weight in healthcare AI. It powers our clinical extraction engine, cuts implementation timelines, and gives our GTM team dev-level capabilities. The faster we build, the faster clinics get out of manual chart review and back to patients.
> Zach Rosen  
> CEO & Co-Founder, Brellium 
01 / 16
Claude is the only frontier model available on all three leading cloud services: AWS, Google Cloud, and Microsoft.
We’re also partnering with companies who specialize in helping organizations adopt AI for specialist work, including Accenture, Blank Metal, Caylent, Deloitte, Deepsense.ai, Firemind, KPMG, Provectus, PwC, OWT, Quantium, Slalom, Tribe AI, and Turing.
## **Getting started**
To learn more about Claude for Healthcare, see [here](http://claude.com/solutions/healthcare), or see our tutorial guides [here](https://claude.com/resources/tutorials-category/healthcare). For more detail on the expanded Claude for Life Sciences capabilities, see [here](https://claude.com/solutions/life-sciences), and our tutorial guides [here](https://claude.com/resources/tutorials-category/life-sciences).
Our new connectors and Agent Skills are generally available to all Claude subscribers, including Claude Pro, Max, Teams, and Enterprise.
You can also [contact our sales team](https://www.claude.com/contact-sales%20) to discuss bringing Claude to your organization.
