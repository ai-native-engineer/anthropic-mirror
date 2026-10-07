<!-- source: https://claude.com/resources/articles/how-people-are-using-claude-cowork -->

When we released [Claude Code](https://claude.com/product/claude-code) in 2025, we were surprised at how many non-technical users started playing around with it. People who had never opened the terminal before were using it to create agents that organized folders, deduplicated files, and wrote spreadsheet formulas.

But for others, the terminal remained a slightly intimidating place—a literal “black box.” We built [Claude Cowork](https://www.anthropic.com/product/claude-cowork) to extend the agentic capabilities of Claude Code to the same chat interface people were already using to talk to Claude.

Since we launched Claude Cowork in January, it’s become an especially potent tool for those whose work is focused on the creation and exchange of information, what many call “knowledge work.” People are using it for a variety of tasks that aren’t necessarily the hallmark of a specific role, but instead represent the connective work around a role that moves projects forward and keeps businesses running. That means tasks like drafting a status update, building a slide deck, or condensing reams of research into a single report.

In this post, we share data from a sample of Claude Cowork sessions in May 2026, and explore what it tells us about how people are using AI in their day-to-day work, beyond the terminal.

## What the data shows

We sampled 1.2 million anonymized and aggregated Claude Cowork sessions from May 11–31, 2026 and classified them according to a taxonomy of 20 different categories of work. Among our findings, the largest category of use is for “business process and operations”—things like pulling scattered updates into a single report, building onboarding checklists, and reconciling spreadsheets—at 33.4%. This makes sense, because business operations tasks span many different roles: people in finance, HR, and administrative jobs, for example, are all likely to make use of Claude Cowork for these types of tasks.

Next was content creation and copywriting—synthesis-intensive business communications work like producing drafts, slide decks, posts, and proposals—at 16.4%. Staring down a blank page is often the first barrier to getting started, and Claude Cowork is a useful tool for threading thoughts and information into a rough draft. These types of tasks also cross roles: people in marketing, communications, business development, and project management, among others, are likely to collaborate with Claude Cowork on them.

The next top categories are software development, at 8.7%; DevOps and infrastructure, at 7%; research and intelligence, at 6.4%, data analysis and business intelligence, at 5.8%, document processing and extraction, at 4.1%, and sales and revenue operations, at 4%.

All other categories comprised less than 4% of the data set, including personal assistance at 3.8%, education at 2.4%, and meeting intelligence at 1.8%.

![](https://assets.claude.com/e7b48eac9654b3429ec6872b6a0dd63c4479d064.png)

In a recent study, business process and operations accounted for a third of sampled Claude Cowork sessions (33.4%), more than double the next-largest category, content creation and copywriting (16.4%).

## How knowledge workers are using AI

It’s telling that the two top usage categories—business process and operations, and content creation and copywriting—make up roughly half of all Claude Cowork usage. These categories are overwhelmingly connective in nature: spreadsheets pull disparate data points into a context where they can be read, compared, and tracked; decks convey an idea or decision to a broader audience with varying levels of context; and onboarding checklists help a new hire tap into institutional knowledge.

Our data suggests that people are using Claude Cowork to assemble and structure the information they can use to act on their expertise. A lawyer, for example, might use Claude Cowork to handle document formatting and filing, giving them more time to apply their legal judgment to challenging cases. A hiring manager might use Cowork to schedule meetings and synthesize interview feedback, allowing them to spend more time on candidate conversations and evaluating work samples. And a team lead might use Claude Cowork to produce the slide deck that explains a difficult decision, freeing them up to actually make those tough calls.

This usage pattern presents an interesting contrast to Claude Code, which is most often used by software developers for the key parts of their role: building, debugging, and shipping code. So it’s perhaps unsurprising that software development makes up such a small share of Claude Cowork use. Developers are much more likely to use Claude Code than Claude Cowork to write code, but the work they do in Claude Cowork is the connective, communications-focused work that surrounds every role, software engineering included.

## The rise of AI in knowledge work

While coding is still—understandably—one of the uses of AI that gets the most attention, the use of AI for everyday business work is on the rise, and the kinds of tasks they’re finding it most helpful for are coming into focus. People are turning to Claude Cowork to help with the tasks that help track and communicate information and ideas across teams: status reports, decks, trackers, and more.

This is just a single snapshot, and Claude Cowork is still new; its uses are evolving quickly. Our goal is to make this a reference point for people who are figuring out how to integrate AI products into their daily work, and to show where use is most concentrated. We plan to continue publishing data as usage grows and shifts, and we’ll report on what changes over time.

### Getting started with Cowork

Claude Cowork is available to all Claude users. [Learn more](http://anthropic.com/product/claude-cowork) or [take our Introduction to Claude Cowork course](https://anthropic.skilljar.com/introduction-to-claude-cowork) to get started.

++++

## Additional details about our research

See below for more information about how we conducted this Claude Cowork user survey.

### **How we measured**

This analysis draws on a sample of Claude Cowork sessions classified by an automated system into a 20-category taxonomy of work. The data was gathered using a privacy-preserving analysis tool that keeps all user information anonymous; no individual session was read by a human analyst, and we worked only with aggregate category-level statistics.

The sample is collected at a capped rate—a fixed maximum number of sessions per hour—rather than as a fixed percentage of traffic. As a result, every number in this report is a share of sampled sessions and not an absolute volume. Data was gathered between May 11 and 31, 2026, covering 1.2 million sampled sessions from more than 600,000 organizations.

### **Limitations**

* Taxonomy granularity: The taxonomy we used classifies sessions by the work being done, not by the job title of the person doing it. Several categories map cleanly onto recognizable knowledge-work functions, such as research and intelligence work (6.4% of sessions), data analysis and business intelligence (5.8%), sales and revenue operations (4%), and legal and compliance work (1.3%). Meeting and conversation intelligence (1.8%) and customer support (0.8%) appear as well. But there are limitations to what the taxonomy can split out. There are no standalone categories for marketing, finance, or HR—those functions are best represented by the “business process and operations” category, which is likely part of why it occupies a third of all usage.
* Shares versus volumes: Because the sample is rate-capped, the sampled session and organization counts do not reflect total Cowork usage or growth, and usage during busier hours of the day is somewhat underrepresented relative to usage during quieter hours.
* Window choice: We used three recent complete weeks rather than a longer time span because the category shares shifted around May 11, in a way that was consistent with a change in our labeling pipeline rather than in user behavior. The shares reported here were computed entirely after the change and are correct under either explanation.
* Mix of work and personal use: The sample covers use among external organizations, not individuals. But the Claude Cowork sessions sampled include some personal, non-work use (personal assistance, hobbies, and companionship-style conversations together account for roughly 5% of sessions), so the sample doesn’t purely represent workplace activity.
* Automated classification: Category labels were applied by an automated system, not by a human reviewer, and any classifier could have errors. Where sessions could plausibly fit multiple categories, the results depended on the definitions included in our taxonomy; we've noted in the “taxonomy granularity” bullet above where those definitions most affect interpretation.

‍

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
