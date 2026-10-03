<!-- source: https://www.anthropic.com/transparency/voluntary-commitments -->

# Anthropic’s Transparency Hub

A look at Anthropic's key processes, programs, and practices for responsible AI development.

[01Model Report](https://www.anthropic.com/transparency/model-report)[02System Trust and Reporting](https://www.anthropic.com/transparency/system-trust-reporting)[03Voluntary Commitments](https://www.anthropic.com/transparency/voluntary-commitments)

03Voluntary Commitments

[01Model Report](https://www.anthropic.com/transparency/model-report)

[02System Trust and Reporting](https://www.anthropic.com/transparency/system-trust-reporting)

[03Voluntary Commitments](https://www.anthropic.com/transparency/voluntary-commitments)

## Executive Summary

Last updated July 23, 2026

Below is information about how we are meeting and working towards our [voluntary commitments](#list-of-voluntary-commitments). Our experience with multiple voluntary frameworks has revealed consistent themes, as well as considerable overlap in their core requirements around safety, security, and responsible development. We are providing an overview organized by key areas of focus. We [welcome feedback](mailto:transparency@anthropic.com) from the AI community and policymakers to inform our future work.

## Risk Assessment and Mitigation

Responsible Scaling Policy and Frontier Compliance FrameworkIn September 2023, we published the first version of our [Responsible Scaling Policy](https://www-cdn.anthropic.com/1adf000c8f675958c2ee23805d91aaade1cd4613/responsible-scaling-policy.pdf) (RSP), our framework for managing potential catastrophic risks from models.

The policy is centered around implementing safeguards which are proportional to the identified risks. As AI models become more powerful, they require stronger protections. When models reach certain capability thresholds, we will implement additional safeguards around security and deployment.

The RSP is designed to evolve as our understanding of AI risks improves, while maintaining this fundamental commitment to safety. In February 2026, we [updated the RSP](https://www.anthropic.com/news/responsible-scaling-policy-v3) to reflect our current understanding of AI and mitigating catastrophic risk. It serves both as our internal guidebook and as a model for industry-wide safety standards.

In December 2025, we published the [Frontier Compliance Framework.](https://trust.anthropic.com/resources?s=eorilovp4wxk38nxbi7k3&name=anthropic-frontier-compliance-framework) Our FCF describes how we assess and mitigate cyber offense, chemical, biological, radiological, and nuclear threats, as well as the risks of AI sabotage and loss of control, and harmful manipulation, for our frontier models. The framework also lays out our tiered system for evaluating model capabilities against these risk categories and explains our approach to mitigations. It also covers how we protect model weights and respond to safety incidents. The FCF serves as our compliance framework for SB 53 and other regulatory requirements. The RSP remains our voluntary safety policy, reflecting what we believe best practices should be as the AI landscape evolves, even when that goes beyond or otherwise differs from current regulatory requirements.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; AI Seoul Summit's Frontier AI Safety Commitments; Seoul AI Business Pledge

### Risk Identification

Anthropic works to identify a wide spectrum of potential risks from AI systems:

* For catastrophic risks addressed in our [Responsible Scaling Policy](https://www.anthropic.com/news/responsible-scaling-policy-v3) (RSP), we have identified capability and usage thresholds that map to required security and deployment mitigations. These thresholds currently cover chemical and biological weapons production, misaligned AI systems in high-stakes settings, and automated R&D in key domains such as AI development. Our Frontier Compliance Framework assesses cyber offense, chemical, biological, radiological, and nuclear threats, as well as the risks of AI sabotage and loss of control and harmful manipulation, for our frontier models.
* We also study and assess risks in other domains, including [cybersecurity](https://red.anthropic.com/2026/exploit-evals/); [autonomous capabilities](https://www.anthropic.com/institute/recursive-self-improvement); societal impacts like [representation](https://www.anthropic.com/research/towards-measuring-the-representation-of-subjective-global-opinions-in-language-models) and [discrimination](https://arxiv.org/abs/2312.03689); and [child safety](https://www.anthropic.com/news/child-safety-principles) and [election integrity](https://www.anthropic.com/news/election-safeguards-update).

This system is dynamic and evolving. We also regularly update our [Usage Policy](https://www.anthropic.com/legal/aup) to reflect new insights into how our models are being used and adjust our risk identification and assessment strategies accordingly.

[Related Commitments](#list-of-voluntary-commitments): AI Seoul Summit's Frontier AI Safety Commitments

### Internal and External Risk Assessments

Anthropic employs a multi-faceted approach to assessing and mitigating catastrophic and non-catastrophic risks across the AI lifecycle. For example, we may employ the following techniques:

1. **Regular evaluations:** We conduct systematic evaluations at defined intervals to detect warning signs of increased catastrophic risks.
2. **Threat modeling:** We collaborate with external experts to develop detailed threat models, particularly in high-risk areas as outlined in our RSP.
3. **Red team testing:** We employ both internal and external red teaming to proactively identify vulnerabilities and potential misuse scenarios. This includes testing for issues like deception, jailbreaking, emergent capabilities, as well as potential misuse scenarios for risks covered under our [Usage Policy](https://www.anthropic.com/legal/aup), such as engaging in fraud or inciting violence.
4. **Expert consultations**: We integrate feedback from external subject matter experts to ensure our risk identification processes are robust.
5. **External evaluations:** We have worked with a variety of independent organizations to conduct additional testing and evaluation of our models, including the UK AI Security Institute (UK AISI), the US Center for AI Standards and Innovation (US CAISI), and Model Evaluation and Threat Research (METR).
6. **Research on emergent risks:** Our research teams actively investigate potential future risks, such as autonomous AI R&D. We share some of these research findings on our Frontier Red Team’s blog, [red.anthropic.com](http://red.anthropic.com), and our Alignment Science Team’s blog, [alignment.anthropic.com](http://alignment.anthropic.com).
7. **Policy vulnerability testing (PVT):** Our Safeguards team conducts in-depth testing with external experts on a variety of policy topics covered under our [Usage Policy](https://www.anthropic.com/legal/aup).
8. **Pre-deployment testing:** Before releasing new models, we conduct thorough testing to identify potential risks.
9. **External certifications:** Our compliance team works to achieve accredited certifications that provide independent validation of our risk frameworks. We achieved the [ISO/IEC 42001:2023 standard](https://www.iso.org/standard/81230.html) for our AI management system, which is the first international standard outlining requirements for AI governance and helps ensure AI systems are developed and used responsibly.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; AI Seoul Summit's Frontier AI Safety Commitments; Seoul AI Business Pledge; Trusted Tech Alliance

### Post-Deployment Monitoring

We regularly update our [Usage Policy](https://www.anthropic.com/legal/aup) and our detection methods, including classifiers, based on how our models are being used in practice. Additionally, Anthropic has also established multiple mechanisms for receiving reports of potential security vulnerabilities and other safety issues from third parties:

1. **Responsible Disclosure Policy:** We have a publicly accessible [Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy) on our website with a reporting form for security-related vulnerabilities.
2. **Bug Bounty Program:** We operate bug bounty programs through HackerOne, including programs for identifying vulnerabilities in our [classifier systems](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program) and [security vulnerabilities](https://hackerone.com/anthropic).
3. **Safety Issue Reporting**: Users of Anthropic services can report safety issues, “jailbreaks”, and similar concerns at usersafety@anthropic.com.
4. **Engagement with Research Community**: We maintain open channels of communication with the broader AI research community, allowing for informal reporting of potential issues or concerns.

**Whistleblowing and Anti-retaliation Policy:** Anthropic employees can report AI safety-related concerns through three main channels: an emergency alerting and response system for incidents involving potential harmful uses of our services, a general concern sharing forum for suggesting safety improvements, and an anonymous channel specifically for [reporting potential violations of our AI safety commitments under the Responsible Scaling Policy](https://www.anthropic.com/news/responsible-scaling-policy-v3). These channels ensure staff can escalate everything from immediate concerns to long-term safety risks, with confidentiality protections in place so that employees can raise concerns without fear of retaliation.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Trusted Tech Alliance

### Information Sharing on Risks

1. We are a founding member of the [Frontier Model Forum (FMF)](https://www.frontiermodelforum.org/), an industry organization developing safety research, standards, and evaluations for AI safety and responsibility. The Frontier Model Forum [in 2026 announced](https://www.frontiermodelforum.org/updates/progress-update-fmf-information-sharing-of-frontier-ai-threats-and-vulnerabilities/) plans to expand its info-sharing capabilities beyond its formal members, to include a broader range of third party actors.
2. We collaborate with government organizations like the UK AI Security Institute and US Center for AI Standards and Innovation (CAISI) for independent testing.
3. We partner with academic researchers and may fund third-party evaluations to advance the science of AI safety and evaluation.
4. We work with domain experts to improve our risk assessments in specific areas.
5. We engage globally on topics such as child safety and election integrity, collaborating with civil society, industry, and governments to share research and gain insights.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; AI Seoul Summit's Frontier AI Safety Commitments; Seoul AI Business Pledge

## Cybersecurity & Privacy

### Cybersecurity Safeguards

Anthropic implements a number of cybersecurity initiatives, products and best practices, including:

1. **Cyber Verification Program:** Our cybersecurity safeguards restrict activities ranging from prohibited uses with little to no legitimate defensive application (such as ransomware development) to high-risk dual-use activities like vulnerability discovery. Cybersecurity professionals can apply through our [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude) to seek access for legitimate use cases on select models. To support this, we launched [Project Glasswing](https://www.anthropic.com/news/project-glasswing) to allow launch partners to use Mythos Preview as part of their defensive security work. We also extended access to a group of over 40 additional organizations that build or maintain critical software infrastructure so they can use the model to scan and secure both first-party and open-source systems.
2. **Claude Security:** We offer [Claude Security](https://claude.com/product/claude-security), which scans codebases for security vulnerabilities and suggests targeted patches for human review.
3. **Cybersecurity Controls:** We implement a [comprehensive cybersecurity program](https://trust.anthropic.com/) and cybersecurity safeguards specifically tailored for AI model development.
4. **Third-Party Evaluations:** We engage independent assessors to evaluate the effectiveness of our cybersecurity measures and participate periodically in third-party test and evaluation schemes. We make these attestation and compliance artifacts available on our [Trust Center](https://trust.anthropic.com/).
5. **Regular Threat Modeling:** We perform regular reviews and updates to our threat models to account for tactics, techniques, and procedures used by sophisticated threat actors.
6. **AI-Specific Risk Mitigation:** We conduct research on improving model resistance to prompt injection and other [adversarial "jailbreaking" techniques](https://www.anthropic.com/research/many-shot-jailbreaking). We also use red teaming to evaluate model vulnerabilities and implement mitigations.
7. **Supply Chain Security:** We maintain structured oversight of our third-party and supplier relationships. Suppliers must comply with our Vendor Code of Conduct, which sets requirements on legal and regulatory compliance, labor and human rights, responsible sourcing, and data protection and privacy, and must apply equivalent standards across their own supply chains. Vendors that store, process, or host Anthropic data or infrastructure are subject to additional contractual security terms, including maintaining a documented security program, undergoing independent security audits, and holding recognized certifications.
8. **Enterprise Customers:** We offer enterprise-grade security features designed to give organizations visibility and control over how their data is handled, including [SSO, SCIM, audit logs, and role-based permissions](https://support.anthropic.com/en/collections/10351014-enterprise-plan-features). See more in our [Help Center](https://support.anthropic.com/en/articles/9797531-what-is-the-claude-enterprise-plan).

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Trusted Tech Alliance

### Cybersecurity During External Testing

We protect the security of our model environments, including during evaluations:

* Models are protected by two-party controls, with explicit per-user access validation and multifactor authentication.
* Internal model evaluations are performed within our own infrastructure, while external evaluations use API access with ‘zero data retention’ settings when eligible to prevent content storage.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct

### Protections for Personal Data and IP Rights

We respect privacy rights and comply with relevant data protection laws, including through detailed disclosures about personal data use and processing, and user controls. We also implement a number of transparency and technical measures to help ensure that we advance the field of responsible AI development and provide site owners the ability to communicate their preferences:

* Per our Commercial and Consumer Terms of Service, customers retain all rights to their inputs and own their outputs, customer content is treated as confidential, and customers can choose to opt-out of model training through their account settings;
* Customers can [export their data and memory](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude) in portable formats for backup or migration.
* We identify our web crawler’s activities openly and transparently and respect industry-standard technical signals that site owners use to communicate their preferences, robots.txt.

More details can be found in our [Privacy Center](https://privacy.anthropic.com/en/), [Help Center](https://support.anthropic.com/en/articles/7996866-how-long-do-you-store-personal-data), and our [Privacy Policy](https://www.anthropic.com/legal/consumer-terms#privacy).

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Trusted Tech Alliance

## Public Awareness

### Corporate Governance and Financing Transparency

Anthropic is a public benefit corporation (PBC) headquartered in San Francisco, California. As a U.S.headquartered company, Anthropic operates within established and transparent legal frameworks and is subject to independent regulatory oversight — including U.S. federal and state authorities and we adhere to international agreements and frameworks such as the G7 Hiroshima Process International Code of Conduct. For more information on our regulatory compliance please see our [Trust Center](https://trust.anthropic.com/).

Our governance is further anchored by the [Long-Term Benefit Trust](https://www.anthropic.com/news/the-long-term-benefit-trust) (LTBT), an independent body of financially disinterested trustees selected for their expertise in fields such as AI safety, national security, public policy, and social enterprise. The Trust holds the authority to elect — and over time to appoint a majority of — the members of our Board of Directors, helping ensure our mission is insulated from short-term commercial and shareholder pressures.

We maintain transparency in our financing and corporate practices, competing openly for capital and talent and publicly disclosing our [funding rounds](https://www.anthropic.com/news/series-h), including the participating investors and our post-money valuation.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Seoul AI Business Pledge; Trusted Tech Alliance

### Advancements of Global Technical Standards

Anthropic contributes to the development of international technical standards and best practices:

* We work with NIST to strengthen its AI Risk Management Framework, contributing insights from our technical safety research to the companion [playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook) and responding to its requests for information, such as the [RFI on Security Considerations for AI Agents](https://www-cdn.anthropic.com/43ec7e770925deabc3f0bc1dbf0133769fd03812.pdf).
* We co-founded and are an active member in the [Frontier Model Forum (FMF)](https://www.frontiermodelforum.org/), which, among other aims, seeks to advance AI safety research, standards and evaluations.
* We are a founding member of [CoSAI](https://www.coalitionforsecureai.org/) and serve on the Executive and Technical Steering Committees and on several working groups.
* We collaborate with the [Cloud Security Alliance](https://cloudsecurityalliance.org/) (CSA) on the development of controls applicable to the AI industry and assist in the development of diligence efforts that could take place based on those controls.
* We are actively contributing to the development of [standards for evaluating models](https://www.anthropic.com/news/a-new-initiative-for-developing-third-party-model-evaluations) and [third-party testing](https://www.anthropic.com/news/third-party-testing), by launching an initiative to fund evaluations developed by third-party organizations that can effectively measure advanced capabilities in AI models and by proposing a third-party testing regime.
* We created the Model Context Protocol (MCP) as an open source project in 2024. We have since donated MCP to the newly created [Agentic AI Foundation (AAIF)](https://aaif.io/), a directed fund under the Linux Foundation. We co-founded the AAIF with other industry partners to support the development of open technical standards for agentic AI systems.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Seoul AI Business Pledge; Trusted Tech Alliance

### Public Report on AI Systems

Anthropic publishes and maintains detailed information on our models and practices:

1. **[System Cards](https://www.anthropic.com/system-cards):** With each new model family release, we publish a detailed model documentation in a model or system card or addendum. These cards provide information about model capabilities and performance across various benchmarks; known limitations and potential risks; results of safety evaluations and red teaming; information on model training; and more.
2. **[Risk Reports](https://www-cdn.anthropic.com/08eca2757081e850ed2ad490e5253e940240ca4f.pdf):** We publish Risk Reports discussing the risks of our AI systems and our determinations about whether to continue AI development and deployment in light of those risks. These reports go beyond model capabilities to address threat models, active risk mitigations, and an overall assessment of risk level. Risk Reports are published every 3–6 months, shared with our Board and Long-Term Benefit Trust, and subject to review by independent external parties.
3. AI Safety Frameworks (**[Responsible Scaling Policy (RSP) and Frontier Compliance Framework (FCF)](https://www.anthropic.com/news/responsible-scaling-policy-v3) :** We share our RSP and FCF publicly, which outlines our frameworks for evaluating and mitigating potential catastrophic risks posed by AI systems.
4. **[Research](https://www.anthropic.com/research):** We regularly publish research on cutting edge safety, [interpretability](https://transformer-circuits.pub/), economic and [societal impacts](https://www.anthropic.com/news/measuring-model-persuasiveness), [alignment](https://alignment.anthropic.com/), and [frontier red teaming](https://red.anthropic.com/).
5. **[Usage Policy](https://www.anthropic.com/legal/aup):** Our Usage Policy is intended to help our users stay safe and help ensure our products and services are being used responsibly. Our [Safeguards Help Center](https://support.anthropic.com/en/collections/4078535-safeguards) provides additional best practices and recommendations.
6. **[User Guides](https://docs.anthropic.com/en/home):** We publish a suite of reference documents for users to learn more about Claude’s capabilities and appropriate uses including a [Prompt Library](https://docs.anthropic.com/en/prompt-library/library), [Prompt Engineering Guidelines](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview), [Release Notes](https://docs.anthropic.com/en/release-notes/overview), and [System Prompt](https://docs.anthropic.com/en/release-notes/system-prompts) updates.
7. **[Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy):** We review remote MCP servers included in our connections directory to ensure they meet our standards for safety, security, and compatibility with other servers as outlined in our MCP Directory Policy.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; AI Seoul Summit's Frontier AI Safety Commitments; Seoul AI Business Pledge

### Transparency of AI Generation

Claude currently has multimodal input capabilities and text-based outputs, including text-based artifacts and text-to-speech voice output. We have worked across industry and academia to explore and stay abreast of technological developments for watermarking and are preparing for compliance with applicable laws by the relevant legal deadlines.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Seoul AI Business Pledge

## Societal Impact

### Public Benefit Research and Support

We support a range of partnerships and programs designed to extend the benefits of AI to the public good, including in global health, scientific research, education, and economic mobility:

* We formed a [$200 million partnership with the Gates Foundation](https://www.anthropic.com/news/gates-foundation-partnership), committing grant funding, Claude credits, and technical support over four years to programs in global health, life sciences, education, and economic mobility — including accelerating vaccine and therapy research for diseases like polio, HPV, and preeclampsia, co-developing K-12 education tools in the US, sub-Saharan Africa, and India, and supporting smallholder farmers and workforce mobility.
* We partnered with [the Allen Institute and Howard Hughes Medical Institute](https://www.anthropic.com/news/anthropic-partners-with-allen-institute-and-howard-hughes-medical-institute) as founding life sciences partners to accelerate scientific discovery, developing specialized AI agents and multi-agent systems that help researchers synthesize knowledge, generate hypotheses, and interpret complex biological data.
* We launched [Claude Corps](https://www.anthropic.com/news/claude-corps), a national fellowship program backed by an initial $150 million commitment that will train 1,000 fellows early in their careers, place them full-time with nonprofits across America for a year, and pay them to help host organizations advance their missions while building AI skills of their own.

Many of our enterprise customers also leverage Claude to increase public health, education, environmental sustainability, and economic development. We have launched specific programs to support Claude for public benefit.

* We launched [Claude for Life Sciences](https://www.anthropic.com/news/claude-for-life-sciences) to support researchers, clinical coordinators, and regulatory affairs managers across the drug discovery and development process. The product introduces new connectors to scientific platforms like [Benchling](https://www.benchling.com/), [BioRender](https://www.biorender.com/), and [PubMed](https://pubmed.ncbi.nlm.nih.gov/), along with purpose-built Agent Skills for tasks like single-cell RNA sequencing quality control and a dedicated prompt library to help life sciences teams accelerate research from early discovery through commercialization.
* We launched [Claude for Education](https://www.anthropic.com/education) to help universities maintain academic integrity while incorporating AI tools in education. We also partnered with [Teach For All](https://www.anthropic.com/news/anthropic-teach-for-all) to launch the AI Literacy & Creator Collective, bringing AI tools and training to more than 100,000 educators across 63 countries who serve over 1.5 million students in under-resourced schools, positioning teachers as co-architects shaping how AI develops in the classroom.
* We launched [Claude for Nonprofits](https://www.anthropic.com/news/claude-for-nonprofits) in partnership with [Giving Tuesday](https://www.givingtuesday.org/), offering discounts of up to 75% on Team and Enterprise plans for verified 501(c)(3) organizations, new connectors to nonprofit platforms like [Blackbaud](https://www.blackbaud.com/), [Candid](https://candid.org/), and [Benevity](https://benevity.com/), and a free [AI Fluency for Nonprofits](https://anthropic.skilljar.com/ai-fluency-for-nonprofits) course to help mission-driven organizations adopt AI responsibly and effectively.
* We launched [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business), a package of connectors and ready-to-run workflows that put Claude inside the tools small businesses already use — such as QuickBooks, PayPal, HubSpot, and Canva — to handle work like payroll planning, month-end close, and invoice chasing, alongside a free AI Fluency for Small Business course, a multi-city AI fluency tour, and partnerships with small business–focused nonprofits and CDFIs.
* Read more about how our customers use Claude for societal good [here](https://www.anthropic.com/customers).

We also have [researcher access programs](https://support.anthropic.com/en/articles/9125743-what-is-the-external-researcher-access-program) to provide free Claude credits for researchers advancing AI research. And we support critical infrastructure research through [a contribution to Carnegie Mellon University](https://www.anthropic.com/news/investing-in-energy-to-secure-america-s-ai-future) to advance AI-powered energy solutions and build the cybersecurity workforce needed to protect America’s energy infrastructure.

Anthropic also conducts research on [discriminatory](https://arxiv.org/abs/2312.03689) model outputs, [emotional impacts of AI](https://www.anthropic.com/news/how-people-use-claude-for-support-advice-and-companionship), [political evenhandedness](https://www.anthropic.com/news/political-even-handedness), [education](https://www.anthropic.com/news/anthropic-education-report-how-educators-use-claude), and more. We have also published [Claude’s Constitution](https://www.anthropic.com/constitution) in an effort to be transparent about how we describe the values, knowledge, and behaviors we want Claude to have. This builds off of our earlier [Constitutional AI](https://www.anthropic.com/news/claudes-constitution) methods of aligning models with human values, which we published in 2022.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; Seoul AI Business Pledge

### Economic Impact Research

In February 2025, we launched the first [Anthropic Economic Index](https://www.anthropic.com/economic-index), an initiative aimed at understanding AI's effects on labor markets and the economy over time. So far, we have published 6 indexes, tracking how AI use patterns are evolving across the economy. Each index provides analysis based on millions of anonymized Claude conversations, offering insights into how AI is being incorporated into real-world tasks across the modern economy. As part of this effort, we are open sourcing the dataset underpinning our analysis and inviting economists, policy experts, and researchers to provide input on the Index. We also conduct the [Economic Index Survey](https://www.anthropic.com/research/economic-index-survey-announcement), where we gather qualitative insights from Claude users about how AI is changing their work.

We launched our [Economic Futures Program](https://www.anthropic.com/news/introducing-the-anthropic-economic-futures-program), a multidisciplinary program funding research grants, policy development, and data infrastructure to help society understand and navigate AI's economic transformation in June 2025. Over the first year of the program, we have offered grants between $10,000 and $50,000 for empirical research on AI’s economic impacts. In June 2026, we announced a $200 million commitment to an Economic Futures Research Fund, an evolution to our Economic Futures Program, which will fund major research trials and program evaluation on promising public policies.

[Related Commitments](#list-of-voluntary-commitments): G7 Hiroshima Process International Code of Conduct; New Delhi Frontier AI Impact; Seoul AI Business Pledge

### AI Education and Professional Development

Anthropic enables organizations and professionals to learn and work with AI tools:

1. We partnered with [CodePath](https://www.anthropic.com/news/anthropic-codepath-partnership), the United States’ largest provider of collegiate computer science education, to put Claude and Claude Code at the center of its courses and career programs — giving more than 20,000 students at community colleges, state schools, and HBCUs access to frontier AI tools, with over 40% of CodePath students coming from families earning under $50,000 a year.
2. As part of our [Anthropic Academy](https://www.anthropic.com/learn), which provides learning resources from API development guides to enterprise best practices, we also created an [AI Fluency Course](https://www.anthropic.com/ai-fluency). This course is a foundational resource to provide individuals everywhere with advice on effective, efficient, ethical, and safe human-AI collaboration.
3. We launched [Claude for Enterprise](https://www.anthropic.com/news/claude-for-enterprise), which helps organizations securely collaborate using internal knowledge in our AI chatbot.
4. Our [Prompt Library](https://docs.anthropic.com/en/prompt-library/library) provides a library of optimized prompts for business and personal tasks.
5. We maintain academic partnerships and created an [External Researcher Access](https://support.anthropic.com/en/articles/9125743-what-is-the-external-researcher-access-program) program to foster collaboration between industry and academia.
6. As part of the [White House's Pledge to America's Youth](https://www.whitehouse.gov/edai/) initiative, we are investing in AI cybersecurity education for K-12 students and educators while supporting programs that prepare young Americans to become the next generation of leaders in these critical fields.

[Related Commitments](#list-of-voluntary-commitments): Seoul AI Business Pledge

### Democratizing Model Access

We also support an open and interoperable technology ecosystem. Our models are available through Anthropic's own [API](https://www.anthropic.com/api) and through [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), [Google Cloud Vertex AI](https://cloud.google.com/vertex-ai), and [Microsoft Foundry on Azure](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude?tabs=python), so organizations can adopt Claude through the cloud provider they already use. This is reinforced by deliberately diversified compute partnerships spanning Amazon, Google Cloud, and Microsoft Azure.

Claude is available in [over 170 countries](https://www.anthropic.com/supported-countries). We evaluate Claude's capabilities and behavior across many languages and cultural contexts. Multilingual benchmark results are published in our [system cards](https://www.anthropic.com/system-cards) and our evaluations increasingly use natively authored prompts, native-speaker judgment, and culturally grounded tasks so that performance and safety are assessed in realistic local contexts. We collaborate with governments on the science of AI evaluation — including the UK AI Security Institute and the US Center for AI Standards and Innovation and we engage with emerging AI safety institutes and local research ecosystems to support evaluations for languages and cultural contexts that are under-represented in existing benchmarks. We will continue to invest and grow our efforts to internationalize our products in an inclusive and localized way.

We support the National AI Research Resource (NAIRR), which is a public-private partnership through the National Science Foundation that connects U.S. researchers to computational, data, software, model and training resources to enable increased AI research and education.

We endorsed the [CREATE AI Act](https://www.congress.gov/bill/118th-congress/senate-bill/2714) to authorize the NAIRR and are participating in the [NAIRR pilot at the National Science Foundation](https://new.nsf.gov/focus-areas/artificial-intelligence/nairr).

[Related Commitments](#list-of-voluntary-commitments): New Delhi Frontier AI Impact, Seoul AI Business Pledge; Trusted Tech Alliance

### Protect Consumers from Data Center Costs

We are committed to [covering electricity price increases](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure) consumers may face from our data centers. We are paying for 100% of the grid upgrades needed to interconnect them, working to bring net-new generation online and cover demand-driven price effects, and investing in curtailment and grid-optimization tools to ease strain on the grid.

## System Safeguard Commitments

In the following sections, we'll focus specifically on how we address three critical areas that have their own dedicated sets of commitments: Image-Based Sexual Abuse, Election Integrity, and Terrorist and Extremist Content.

### Policy Prohibitions

At the foundation of our Safeguards work is our [Usage Policy](https://www.anthropic.com/legal/aup), which sets standards for how our products and services can be used, including prohibitions on activities associated with terrorism and violent extremism, child exploitation content, and disruptive and deceptive activities related to elections. We have a suite of tools to detect harm and enforce our Usage Policy. These include:

* Classifier systems, including AI-powered scanners that examine, sort, and categorize data to detect potential violations of our Usage Policy and user safety and security concerns such as prompt injections.
* [Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers), safeguards trained on synthetic data generated from a "constitution" of natural language rules, which monitor model inputs and outputs to block potentially harmful content such as attempted jailbreaks. Our [next-generation system](https://www.anthropic.com/research/next-generation-constitutional-classifiers) adds probes of the model's internal activations, and no universal jailbreak has yet been discovered against it.
* Investigations to understand the scale and scope of abusive activity that may occur across multiple accounts or actors. For example, the Threat Intelligence team works to identify sophisticated cases of misuse, including by correlating observed usage patterns with external threat data, and collaborates within our Safeguards organization to improve defenses against such activity.
* Response steering technology that can steer model outputs if they might lead to harmful responses.
* A range of enforcement or intervention actions we can take in real-time if a violation or safety concern is detected, including placing restrictions on accounts, removing them altogether, or [directing users](https://www.anthropic.com/news/protecting-well-being-of-users) to additional resources.

[Related Commitments](#list-of-voluntary-commitments): Thorn’s Safety by Design for Generative AI; Munich Accord on Elections; Christchurch Call Commitments

## Child Safety & Image-Based Sexual Abuse

[Claude.ai](http://claude.ai/redirect/website.v1.31590fb4-7d02-4138-855c-296d37f6008e) is 18+. Our Consumer Terms of Service require individuals to be at least 18 years old to use our services. When we detect signals that an account may belong to someone under 18, we disable the account and offer the user an opportunity to [verify their age through Yoti, a third-party age verification provider](https://support.claude.com/en/articles/15171100-age-assurance-on-claude), before reinstating access. Additionally, organizations building tools that serve minors (such as educational resources) that incorporate our API(s) must comply with the additional guidelines outlined in our [Help Center article](https://support.anthropic.com/en/articles/9307344-responsible-use-of-anthropic-s-models-guidelines-for-organizations-serving-minors).

### Detection and Prevention Systems

Claude currently does not generate image or video outputs of people, and is therefore incapable of generating image-based child sexual abuse material (CSAM) or non-consensual intimate images (NCII). Abuse can occur directly through CSAM uploads, sexualized content generation involving minors, and indirect or technical abuse such as using Claude's code generation capabilities to build tooling.
We address this full range through a multi-layered approach spanning proactive protections and reactive controls across policy, detection, model training, and enforcement. For example, we may employ the following techniques:

* On our first-party services, we employ hash-matching technology across all surfaces and novel CSAM classifiers on Claude.ai to [detect and report known and novel CSAM](https://support.anthropic.com/en/articles/9020328-csam-detection-and-reporting) to the National Center for Missing and Exploited Children (NCMEC). We continue to expand scanning coverage across new surfaces and products, and are implementing similar technologies for detecting NCII. Our third-party partners maintain their own screening and detection systems.
* We run safety classifiers across a range of child safety harm areas, including risk of imminent harm to minors, and continue to improve upon these and expand coverage across harm areas.
* If user inputs violate our [Usage Policy](https://www.anthropic.com/legal/aup), we may take action such as automatically modifying the request, issuing warnings or strikes, removing content, or in serious cases, conducting user suspensions or bans.
* We have incorporated targeted prevention messaging for users who exhibit signs of sexual interest in minors, directing them to anonymous helpline resources to prevent harm to minors before it occurs.
* We undertake various data preparation and cleaning processes to ensure that training data is of sufficient quality and appropriateness. We apply CSAM and other safety filters to some of our datasets that proactively detect, report, and prevent CSAM from being used for training our models, and report to NCMEC when identified.
* Additionally, we provide [guidance](https://support.claude.com/en/articles/15591275-child-safety-guidance-for-developers) to developers building on Claude to support their own child safety programs, including Usage Policy obligations and detection and reporting resources.

### Model & Product Testing

We integrate external testing for violations of our [Usage Policy](https://www.anthropic.com/legal/aup). We commission testing from outside subject matter experts to ensure that our evaluations are robust and reflect new trends in abuse. Results from red teaming are provided to our model finetuning and safeguards teams to assess for integration back into model training, model development, and deployment of safety and enforcement strategies. For example, we used feedback from child safety experts at Thorn around signals often seen in child grooming to update our classifiers, enhance our Usage Policy, fine-tune our models, and incorporate these signals into testing of future models.
Additionally, we use a phased deployment approach that ensures thorough testing and limits access before wider release. Our deployment phases typically include: (1) Internal testing with employees only; (2) Limited early access with select customers; and (3) Graduated general availability.

### Monitoring & Reporting

We also take a layered approach to monitoring and reporting. Users can flag concerning content or model behavior directly through our [reporting flows](https://support.anthropic.com/en/articles/7996906-reporting-harmful-or-illegal-content), while our in-house Safeguards experts proactively monitor public forums and analyze emerging abuse patterns. We also work with a third-party vendor to perform Open-Source Intelligence (OSINT) and send our internal team alerts related to general platform abuse. Web Search capabilities integrated into claude.ai incorporate standard CSAM mitigation tactics, such as URL blocking.

We regularly update our [Transparency Hub](https://www.anthropic.com/transparency/) including our [System Trust and Reporting page](https://www.anthropic.com/transparency/system-trust-reporting), our [Voluntary Commitments](https://www.anthropic.com/transparency/voluntary-commitments) page , and child safety testing information in our [model documentation](https://www.anthropic.com/system-cards). These updates reflect our ongoing commitment to responsible development, deployment, and maintenance of model safety consistent with [our commitments](https://www.anthropic.com/news/child-safety-principles) under [Thorn's Safety by Design for Generative AI initiative](https://www.thorn.org/blog/generative-ai-principles/?ref=safer.io).

### Law Enforcement Requests

Law enforcement agencies investigating harm to minors, CSAM, or other image-based sexual abuse may submit formal requests for account records through our legal process intake: [Law Enforcement Requests](https://support.claude.com/en/articles/9035075-law-enforcement-requests). Requests must include the required legal documentation (subpoena, warrant, or other valid process) and, where applicable, the associated NCMEC Report Identifier.

[Related Commitments](#list-of-voluntary-commitments): Thorn’s Safety by Design for Generative AI; White House's commitments to combat Image-Based Sexual Abuse

## Election Integrity

### Evaluation and Testing

We take a multi-pronged approach to evaluating risks related to election related misuse and abuse:

* Our Policy Vulnerability Testing (PVT) program, conducted in collaboration with external subject matter experts, examines potential [election-specific risks](https://huggingface.co/datasets/Anthropic/election_questions) related to misinformation, bias, and adversarial abuse.
* We also employ advanced monitoring techniques such as our Claude insights and observations [tooling](https://www.anthropic.com/research/clio) to detect and respond to the misuse of our AI systems in elections.

### Mitigations and Industry Collaboration

We collaborate with stakeholders across sectors to share threat intelligence and develop election integrity best practices. Since our models are not trained frequently enough to provide real-time election information (unless the [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) is used), we've implemented several measures to ensure users can access accurate, up-to-date information.

* We implement an elections banner on Claude.ai when appropriate in select countries to redirect users to authoritative election resources if they ask for voting information. For example, in the U.S. we partnered with Democracy Works to direct users to authoritative election information during the relevant timeframe.
* Claude.ai’s system prompt includes a clear reference to its knowledge cutoff date (the date up to which Claude’s training data extends).
* We have developed evaluations to ensure that web search triggers when a user prompts Claude for time-sensitive election-related queries
* We also deploy a multi-pronged detection strategy that combines leveraging classifiers and human review to address Election Integrity harms such as election misinformation, deceptive campaigning, and election fraud. In addition, we leverage our Threat Intelligence team to stay abreast of novel tactics that malicious actors attempt to use in election contexts.

To help others improve their own election integrity efforts and drive better safety outcomes across the industry, we have released some of our [automated evaluations](https://huggingface.co/datasets/Anthropic/election_questions) and have published multiple [blog posts](https://www.anthropic.com/news/election-safeguards-update) outlining our approach to this work. We have also open-sourced our [political evenhandedness evaluation](https://www.anthropic.com/news/political-even-handedness).

[Related Commitments](#list-of-voluntary-commitments): Munich Accord on Elections

## Terrorist and Violent Extremist Content

### Risk Assessment and Mitigation

We conduct pre-launch assessments and rigorous testing, informed by staff expertise and civil society, to mitigate extremist content risks. Our specialized evaluation sets are continuously updated with external insights to address evolving threats.

### Transparency and Collaboration

We engage with external experts on combating extremist content through safety briefings, usage standards consultation, and Policy Vulnerability Testing. We have partnered with the Global Project Against Hate & Extremism, the Polarization and Extremism Research Lab at American University, and the Middlebury Center on Terrorism, Extremism, and Counterterrorism to validate model performance on extremism and will continue to invest in similar partnerships. We have also joined the Global Internet Forum to Counter Terrorrism (GIFCT) to help strengthen our ability to detect potential risks early, and participate in their AI working group. We will comply with requests for data in response to valid legal requests (e.g. a subpoena or a warrant).

**Monitoring and Reporting**

We maintain multiple channels for identifying and reporting potentially violative content. Our in-house Safeguards experts monitor public events and analyze emerging abuse patterns.

We have developed crisis response protocols to guide our actions in the event of a publicly reported act of violence or terrorism, including following the Christchurch Call Foundation Crisis Response Protocol. Pursuant to these protocols, we review for any potential harmful Claude outputs related to the incident, monitor public reporting for emerging details such as perpetrator identification, and coordinate with cross-industry partners to inform the appropriate response measures. These activations ensure rapid detection of policy-violating content and align Anthropic's response with broader industry efforts to limit the viral spread of violent content.

[Related Commitments](#list-of-voluntary-commitments): Christchurch Call Commitments

## List of Voluntary Commitments

Below, you'll find a summary of our voluntary commitments. While we've highlighted the core aims of each commitment, we encourage you to review the complete commitment documents (linked) to fully understand their scope and context.

01G7 Hiroshima Process International Code of Conduct

The [Hiroshima AI commitments](https://www.mofa.go.jp/ecm/ec/page5e_000076.html) were announced in October 2023 at the G7 Summit. They aim to promote safe, secure, and trustworthy AI worldwide and provide voluntary guidance for actions by organizations developing the most advanced AI systems, with an emphasis on taking a risk-based approach. Below are the aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Risk assessment and mitigation throughout the AI lifecycle.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
2. Post-deployment vulnerability monitoring and response.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
3. Public reporting of AI systems capabilities and limitations.
   [See: Public Awareness](#public-awareness)
4. Information sharing across industry and government.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
5. AI governance and risk management policy implementation.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
6. Security controls across physical, cyber, and insider threats.
   [See: Security & Privacy](#security-privacy)
7. AI content authentication, for example, through watermarking.
   [See: Public Awareness](#public-awareness)
8. Research on safety and societal risks.
   See: [Risk Assessment and Mitigation](#risk-assessment-and-mitigation), [Societal Impact](#societal-impact)
9. AI development for global challenges.
   [See: Societal Impact](#societal-impact)
10. International technical standards development.
    [See: Public Awareness](#public-awareness)
11. Data protection for personal data and intellectual property.
    [See: Security & Privacy](#security-privacy)

02AI Seoul Summit's Frontier AI Safety Commitments

The [2023 AI Safety Summit in Seoul produced voluntary commitments](https://www.gov.uk/government/publications/frontier-ai-safety-commitments-ai-seoul-summit-2024/frontier-ai-safety-commitments-ai-seoul-summit-2024) for leading AI companies to develop and deploy their frontier AI models and systems responsibly. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Risk assessment across the AI model lifecycle.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
2. Setting and monitoring clear risk thresholds.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
3. Implementation plan for keeping risks below thresholds.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
4. Processes for threshold-exceeding risks.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
5. Continuous improvement of risk assessment capabilities.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
6. Internal governance framework and accountability.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
7. Public transparency on risk management implementation.
   See: [Risk Assessment and Mitigation](#risk-assessment-and-mitigation), [Public Awareness](#public-awareness)
8. External stakeholder involvement in safety assessments.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)

03Seoul AI Business Pledge

At the 2023 AI Safety Summit, major AI companies also signed a voluntary [business pledge](https://aiseoulsummit.kr/press/?mod=document&uid=43) committing to responsible development of AI systems. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Research advancement for AI safety.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
2. Internal governance for risk management.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
3. Collaboration with government, industry, and civil society on AI safety standards.
   [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
4. Earning and upholding public trust through safe development and content authentication.
   See: [Risk Assessment and Mitigation](#risk-assessment-and-mitigation), [Public Awareness](#public-awareness)
5. Investment in beneficial AI development.
   [See: Societal Impact](#societal-impact)
6. Ecosystem support for AI R&D and industry partnerships with SMEs and startups.
   [See: Societal Impact](#societal-impact)
7. Professional talent development and academic collaboration.
   [See: Societal Impact](#societal-impact)
8. Support for equitable access to AI infrastructure.
   [See: Societal Impact](#societal-impact)
9. Inclusive AI development for underserved communities and marginalized regions.
   [See: Societal Impact](#societal-impact)

04White House's Voluntary Commitments for Safe, Secure, and Trustworthy AI

In July 2023, the Biden-Harris administration established voluntary AI commitments which "underscore three principles that must be fundamental to the future of AI: safety, security, and trust." Below are the core aims of the commitments. Though these specific commitments are no longer formally maintained under the Trump administration, our organization continues to uphold all these principles. These commitments address:

1. Security testing before model release. [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
2. Information sharing on managing AI risks across industry and government. [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
3. Cybersecurity protection of model weights. [See: Security & Privacy](#security-privacy)
4. Third-party vulnerability reporting systems. [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
5. Technical watermarking of AI-generated content. [See: Public Awareness](#public-awareness)
6. Public reporting of AI capabilities and limitations. [See: Public Awareness](#public-awareness)
7. Research on bias, discrimination, and privacy risks. [See: Risk Assessment and Mitigation](#risk-assessment-and-mitigation)**,** [Societal Impact](#societal-impact)
8. AI deployment for major societal challenges. [See: Societal Impact](#societal-impact)

05Munich AI Elections Accord

The [2024 Munich AI Elections Accord](https://securityconference.org/en/aielectionsaccord/accord/) establishes voluntary commitments for tech companies and governments to safeguard electoral processes from AI-enabled interference and misinformation. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Developing technology to mitigate risks related to deceptive AI election content (for example content provenance or watermarking).
   [See: Public Awareness](#public-awareness)
2. Risk assessment for deceptive election content.
   [See: Election Integrity](#election-integrity)
3. Cross-industry collaboration on election integrity.
   [See: Election Integrity](#election-integrity)
4. Public transparency on election content policies.
   See: [Election Integrity](#election-integrity), [Trust and Safety](#trust-and-safety)
5. Engagement with experts on global risk assessment.
   [See: Election Integrity](#election-integrity)
6. Public education on AI election content risks.
   [See: Election Integrity](#election-integrity)

06Thorn’s Safety by Design for Generative AI: Preventing Child Sexual Abuse

The [Thorn Child Safety Commitments](https://www.anthropic.com/news/child-safety-principles) establish voluntary guidelines for AI companies to work toward protecting children from technology-facilitated abuse, emphasizing prevention and safety by design. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Responsibly source our training data: avoid ingesting data into training that has a known risk - as identified by relevant experts in the space - of containing CSAM and CSEM.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
2. Detect, remove, and report CSAM and CSEM from our training data at ingestion.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
3. Conduct red teaming, incorporating structured, scalable, and consistent stress testing of our models for AIG-CSAM and CSEM.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
4. Include content provenance on image and video outputs.
   [See: Public Awareness](#public-awareness)
5. Define specific training data and model development policies.
   See: [Security & Privacy](#security-privacy), [Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
6. Prohibit customer use of our models to further sexual harms against children.
   [See: Trust and Safety](#trust-and-safety)
7. Detect abusive content (CSAM, AIG-CSAM, and CSEM) in inputs and outputs.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
8. Include user reporting, feedback, or flagging options.
   See: [Image-Based Sexual Abuse](#image-based-sexual-abuse), [Risk Assessment and Mitigation](#risk-assessment-and-mitigation)
9. Include an enforcement mechanism.
   [See: Trust and Safety](#trust-and-safety)
10. Include prevention messaging for CSAM solicitation using available tools.
    [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
11. Incorporate phased deployment, monitoring for abuse in early stages before launching broadly.
    [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
12. Incorporate a child safety section into our model cards.
    [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
13. When reporting to NCMEC, use the Generative AI File Annotation.
14. Detect, report, remove, and prevent CSAM, AIG-CSAM and CSEM.
    [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
15. Invest in tools to protect content from AI-generated manipulation.
    [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
16. Maintain the quality of our mitigations.
    See: [Image-Based Sexual Abuse](#image-based-sexual-abuse), [Trust and Safety](#trust-and-safety)
17. Disallow the use of generative AI to deceive others for the purpose of sexually harming children.
    [See: Trust and Safety](#trust-and-safety)
18. Leverage Open Source Intelligence (OSINT) capabilities to understand how our platforms, products and models are potentially being abused by bad actors.

07White House’s Image-Based Sexual Abuse Commitments

In September 2024, the Biden-Harris Administration announced [voluntary commitments](https://bidenwhitehouse.archives.gov/ostp/news-updates/2024/09/12/white-house-announces-new-private-sector-voluntary-commitments-to-combat-image-based-sexual-abuse/#:~:text=Today%2C%20following%20the%20White%20House,abuse%20will%20continue%20to%20evolve.) from AI model developers and data providers to reduce AI-generated image-based sexual abuse. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Responsible dataset sourcing to prevent image-based sexual abuse.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
2. Feedback loops and stress testing against image-based sexual abuse.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)
3. When appropriate, nude image removal from training datasets.
   [See: Image-Based Sexual Abuse](#image-based-sexual-abuse)

08Christchurch Call Commitments

[The Christchurch Call](https://www.christchurchcall.org/the-christchurch-call-commitments/), established in 2019, unites governments and technology companies in voluntary commitments to prevent the spread of terrorist and violent extremist content online, including through AI systems. Below are the core aims of the commitments for online service providers. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Transparency in terrorist and violent extremist content policies.
   [See: Trust and Safety](#trust-and-safety)
2. Human rights-aligned enforcement of content standards.
   [See: Trust and Safety](#trust-and-safety)
3. Cross-industry coordination on terrorist and violent extremist content.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)
4. Work with civil society to counter extremism.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)
5. Enabling lawful cooperation with enforcement agencies while protecting human rights.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)
6. Respect for human rights.
   [See: Societal Impact](#societal-impact)
7. Recognizing civil society's role in implementation, transparency, and user support.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)
8. Continued collaboration and building wider support for the call.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)
9. Developing practical, non-redundant initiatives to deliver on these commitments.
   [See: Terrorist and Extremist Violent Content](#terrorist-and-violent-extremist-content)

09New Delhi Frontier AI Commitments

The [New Delhi Frontier AI Impact Commitments](https://d19ob9sqegt2wc.cloudfront.net/stage/uploads/New_Delhi_Frontier_AI_Impact_Commitments_f81b331b93.pdf) were announced in February 2026 at the India AI Impact Summit in New Delhi, committing frontier AI developers to promote greater understanding of AI usage and its impacts and to broaden access to AI's benefits across languages, cultures, and use cases. Below are the core aims of the commitments. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Advancing analysis of real-world AI usage to shed light on the future of work and support evidence-based policymaking.
   [See: Societal Impact](#societal-impact)
2. Publishing statistical insights derived from anonymised, aggregated, and taxonomized usage data by the next AI Summit.
   [See: Societal Impact](#societal-impact)
3. Evaluating multilingual capabilities across a subset of languages and cultural contexts.
   [See: Societal Impact](#societal-impact), [Public Awareness](#public-awareness)
4. Collaborating with local ecosystems to develop and apply evaluations for under-represented languages and cultural contexts.
   [See: Societal Impact](#societal-impact)

010Trusted Tech Alliance

The [Trusted Tech Alliance](https://www.trustedtechalliance.com/our-principles/), launched in February 2026, is a coalition of leading global technology providers committed to trusted, secure, and reliable technology development across the full stack. Below are the core principles of the alliance. Please review the commitment documents (linked) to fully understand their scope and context. Commitments toward:

1. Transparent corporate governance and ethical conduct, including transparent financing and independent regulatory oversight.
   [See: Public Awareness](#public-awareness)
2. Operational transparency, secure development, and independent assessment, including vulnerability disclosure programs and internationally recognized certifications.
   See: [Risk Assessment and Mitigation](#risk-assessment-and-mitigation), [Security & Privacy](#security-privacy)
3. Robust supply chain and security oversight, with contractually binding security and quality assurances from suppliers.
   See: [Security & Privacy](#security-privacy)
4. An open, cooperative, inclusive, and resilient digital ecosystem, including open standards and cross-border innovation.
   [See: Public Awareness](#public-awareness), [Societal Impact](#societal-impact)
5. Respect for the rule of law and data protection, evidenced through independent regulatory oversight and transparent legal frameworks.
   [See: Public Awareness](#public-awareness), [Security & Privacy](#security-privacy)

[![Open book with turning page, positioned against textured background](https://www-cdn.anthropic.com/images/4zrzovbb/website/71800a27b08a18e808de684513bb852c37b8a334-1000x1000.svg)

### Archived content from January - June 2025

View PDF](https://www-cdn.anthropic.com/50384a465da97cce5cbd3abfa752f5b39d7b7f65.pdf)

[![Open book with turning page, positioned against textured background](https://www-cdn.anthropic.com/images/4zrzovbb/website/71800a27b08a18e808de684513bb852c37b8a334-1000x1000.svg)

### Archived content from July - December 2025

Archived content from July to December 2025](https://www-cdn.anthropic.com/5fb26a6974468f83ce87b4799a7ac957ce9d8f96.pdf)

[![Open book with turning page, positioned against textured background](https://www-cdn.anthropic.com/images/4zrzovbb/website/71800a27b08a18e808de684513bb852c37b8a334-1000x1000.svg)

### Archived content from January - June 2026

Archived content from July to December 2025](https://www-cdn.anthropic.com/5fb26a6974468f83ce87b4799a7ac957ce9d8f96.pdf)

### RSP Updates

Overview of past capability and safeguard assessments, future plans, and other program updates.

[Read more](https://www.anthropic.com/rsp-updates)

### Privacy Center

A central hub for information related to data privacy at Anthropic.

[Read more](https://privacy.anthropic.com/en/)

### Trust center

This page acts as an overview to demonstrate our commitment to compliance and security.

[Read more](https://trust.anthropic.com/)

### Developer Documentation

Learn how to get started with the Anthropic API and Claude with our user guides, release notes, and system prompts.

[Read more](https://docs.anthropic.com/en/home)
