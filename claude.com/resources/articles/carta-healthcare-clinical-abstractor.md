<!-- source: https://claude.com/resources/articles/carta-healthcare-clinical-abstractor -->

*In our new series, **How startups build with Claude**, we highlight how hypergrowth organizations are transforming their industries with AI. In this article, we share engineering lessons learned behind the creation of Lighthouse, Carta Healthcare's clinical data abstraction platform, and why context engineering matters as much as model capability when you’re building AI-powered systems at scale.*

| The quick pitch |
| --- |
| Name | Carta Healthcare |
| Founded | 2017 |
| CEO | Brent Dover |
| Stack | Claude in Amazon Bedrock |
| Growth | 10x growth in the last 3 years, supporting 125+ hospitals |

Clinical registries collect standardized data on patients who share a common diagnosis, procedure, or condition. Hospitals submit to registries to benchmark outcomes, identify gaps in care, and drive quality improvement, but registries are only as valuable as the data that feeds them, and producing that data is harder than it looks.

Turning patient records into registry-ready data is called clinical data abstraction. Trained abstractors read through charts, interpret physician notes, reconcile conflicting documentation, and apply clinical judgment where the record isn't clear. A routine case can take 60 minutes; a complex one can take five or six hours. For a large health system, that adds up to more than [11,000 hours of skilled labor annually](https://claude.com/customers/carta-healthcare) for a single registry program.

Traditional automation tools haven't been able to close the gap. Rules-based systems and NLP can handle predictable documentation, but clinical language rarely is. The same finding might appear as a structured field at one hospital and buried free-text at another. Edge cases multiply, context matters, and the cost of getting it wrong isn't a bad recommendation—it's flawed quality data that undermines the registry entirely.

That gap is exactly what [Carta Healthcare](https://www.carta.healthcare/), a clinical data management solution, built software to close at scale. Their platform, [Lighthouse](https://www.carta.healthcare/clinical-data-management/clinical-data-abstraction/), uses Claude to reason across clinical documentation the way a trained abstractor would.

What they discovered in the process reshaped their approach and offered a blueprint for any team trying to get AI from pilot to production.

## **From rules-based extraction to clinical reasoning**

The questions registry abstractors answer aren't simple lookups in a database.

For example, answering the question *"what was the most recent glucose before the procedure?"* requires knowing the exact procedure start time, then finding a lab value that precedes it. *"Was aspirin prescribed at discharge?"* requires distinguishing between a medication ordered for a patient to take home versus one administered during their stay.

The obvious approach is to automate those judgments with rules: map how clinicians document specific findings, build extraction logic around those patterns, and scale from there. But clinical documentation isn't consistent enough for that approach to work. The same clinical finding gets documented in a structured field at one hospital and as free-text in a clinical note at another.

Carta Healthcare’s early systems used natural language processing (NLP) to extract registry data automatically. Pattern recognition, it turned out, can't replicate clinical judgment.

"That's where Carta Healthcare started years ago with NLP, and it's exactly why we moved to LLMs," says Hannah Glaser, Applied AI Applications Manager at Carta Healthcare.

Getting reasoning right is critical as three abstractors can review the same cardiac case and reach different but defensible answers. Physician notes point one way, imaging studies another. The right answer requires weighing both, and that's not a problem you can rule your way out of.

"What an AI system needs to understand is what a trained clinical abstractor understands: how to read clinical language in context, weigh conflicting evidence across documents, apply temporal logic relative to specific procedure dates, and handle ambiguity," Glaser says. "If weight was assessed after the procedure, a skilled abstractor knows that doesn't count as a pre-procedure weight, and the system needs to know that too.”

Carta Healthcare evaluated several models before settling on Claude.

“No other model we evaluated showed the same capability for understanding and interpreting clinical documentation,” says Glaser.

eBook

### The Enterprise AI Transformation Guide for Healthcare and Life Sciences

Accelerate your enterprise AI transformation with proven strategies from Anthropic's customers in HCLS.

[Read the guide](https://resources.anthropic.com/hcls-transformation-guide)

![](https://assets.claude.com/29d8142c0cc732871194b2e7397a2564c3fb7e39.png)

## **Building the right context**

Every data point Lighthouse extracts needs different source documents, a different time window, and a different amount of context to answer correctly.

This is the core challenge of context engineering: an AI agent's performance isn't determined solely by the model. It's determined by what the model is given to work with. The best prompt in the world underperforms if it's fed incomplete, unordered, or poorly scoped information. Getting context right—what to include, what to exclude, and in what sequence—is the engineering work that separates a prototype from a production system.

Take pre-procedure weight. The requirement isn't *"find a weight in the record."* It's *"find a weight documented before a specific procedure start time."* The most recent weight may have been recorded two days after the operation. That value is inadmissible.

Carta Healthcare’s system incorporates patient-specific context at runtime so Claude has a precise time boundary for each question. The prompt for pre-procedure glucose specifies the procedure start time and asks for the most recent glucose before that moment. Without that specificity, even a strong model is working from incomplete information that any trained abstractor would catch immediately.

“The hardest problems we solved weren't about building a perfect prompt, they were about context construction,” says Matthew Mazzanti, Software Engineering Manager at Carta Healthcare. For Carta Healthcare’s team, the hard work was building the pipeline that assembles the right information at runtime—the right documentation, the right timeframe, the right priority order.

“Integrating, organizing, and surfacing the right data at the right time is the real work. A perfectly written prompt with bad context gives bad answers. A straightforward prompt with the right context delivers the results you need," says Mazzanti.

Glaser's advice for teams in the same position? Start by asking whether you're giving the model what it needs to reason, or asking it to figure things out from whatever's available.

"When something underperforms, you can trace it back to a specific prompt, a context issue, or a retrieval gap rather than staring at an aggregate score wondering what went wrong," says Mazzanti. "Build your evaluation framework early, make it granular, and design it to isolate variables. Skip this, and you'll spend more time debugging than building."

At one large health system, Lighthouse processed over 22,000 surgical cases annually across 14 hospitals, with [inter-rater reliability reaching 98-99%](https://claude.com/customers/carta-healthcare), the industry's standard measure of abstraction accuracy.

## **Keeping clinical expertise in the loop**

Once context construction is solid, the people who understand clinical documentation best can start shaping how the system behaves.

Building trust with abstractors came down to transparency. Lighthouse isn't a black box. For every data point it extracts, abstractors see the supporting evidence and Claude's rationale. They can validate findings and exercise clinical judgment rather than accepting outputs.

From there, prompting becomes the mechanism through which clinical expertise directly shapes how Claude reasons. When an abstractor finds that a specific registry data point isn't being extracted correctly, her explanation of why—the edge cases, the documentation patterns, what the prompt is missing—becomes a direct input to how Claude handles that field.

By prioritizing context engineering early on, Carta Healthcare turns that explanation into a revised prompt and ships it the same day.

"Our clinical abstractors regularly hand us long explanations of how a specific data point works in practice," Glaser says. "Instead of spending weeks translating that into data science models and custom code, we use that feedback directly in the prompts. What used to take months of engineering and QA per registry now ships in a week."

As one of Carta Healthcare’s abstractors put it: "Lighthouse doesn't replace my judgment. It enhances it."

***To learn more, read [Carta Healthcare's full story](https://claude.com/customers/carta-healthcare)*. *‍***

[ArticleSep 30, 2026

### How Anthropic's sales team rebuilt inbound with Claude Managed Agents

Carl Johnson, a sales development leader at Anthropic, shares how a Claude-powered buying agent now answers most inbound customers, and how that changed the way our sales team works.

Claude Platform](https://claude.com/resources/articles/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents)[ArticleSep 23, 2026

### How to prepare for AI-driven code modernization projects

How to organize AI-driven modernization projects for critical systems and regulated enterprises.

Claude Code](https://claude.com/resources/articles/how-to-prepare-for-ai-driven-code-modernization-projects)[ArticleSep 23, 2026

### How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace

CodeRabbit expanded its Vercel plan through Claude Marketplace, and Power Digital and ThoughtSpot expanded their Snowflake capacity using their existing Anthropic commitment.

Claude Platform](https://claude.com/resources/articles/how-coderabbit-power-digital-and-thoughtspot-scale-with-snowflake-and-vercel-on-claude-marketplace)[ArticleSep 17, 2026

### Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5

Balyasny Asset Management (BAM) Chief AI Officer Charlie Flanagan on why the firm uses Claude Fable 5 and the role of safeguards in deploying frontier intelligence safely and reliably across the organization.
‍

Claude PlatformClaude Code](https://claude.com/resources/articles/working-at-the-frontier-how-balyasny-asset-management-evaluates-and-governs-claude-fable-5)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

How Carta Healthcare built clinical AI with Claude | Claude by Anthropic
