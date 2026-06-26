<!-- source: https://claude.com/blog/opus-4-6-finance -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

# Advancing finance with Claude Opus 4.6

With Claude Opus 4.6, finance teams get better reasoning on complex analyses, cleaner first-pass deliverables, and new tools built for where analysts actually spend their time.

  [Enterprise AI](https://claude.com/blog/category/enterprise-ai)
* Product

  Claude apps
* Date

  February 5, 2026
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/opus-4-6-finance

[Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6) marks a step forward in AI for finance. It can be used to help professionals make decisions based on accurate information and clear analysis, and it produces deliverables with real polish. The model is substantially better than others in the market at financial reasoning, multitasking, and maintaining focus over longer multi-step tasks.

Alongside Claude Opus 4.6, we’re updating some of our existing products—and introducing a new one—to put these capabilities where analysts spend the majority of their time. [Cowork](https://claude.com/product/cowork) now delivers more polished outputs, such as financial models and presentations, on the first pass. [Claude in Excel](https://claude.com/claude-in-excel) is now better at handling long-running tasks, with Claude Opus 4.6 staying focused and accurate as financial models become more complex. And we’re releasing [Claude in PowerPoint](https://claude.com/claude-in-powerpoint) as a research preview in beta for natively building and iterating on decks and presentations.

Our internal Real-World Finance evaluation measures Claude’s performance on ~50 investment and financial analysis use cases spanning spreadsheets, slide decks, and word document generation and review. These are tasks commonly performed by analysts across investment banking, private equity, public investing, and corporate finance. Claude Opus 4.6 improves by over 23 percentage points on Claude Sonnet 4.5, our state-of-the-art model just a few months ago.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6984b66b95b2a1a24ab26f64_Opus-4-6-Chart-Real-world-finance-no-subtext%402x%20(1).png)

*This eval tests a combination of code execution and tool use agentic harnesses, and was scored based on a combination of rubrics and preferences that gauge finance domain knowledge, task completeness and accuracy, and presentation quality.*

Together, these updates make Claude a much stronger partner for those across financial services and corporate finance.

## Research, analyze, create

Financial professionals use AI to research effectively across multiple data sources, support financial analyses, and create deliverables that their teams and customers can act on. Claude Opus 4.6 is best in class across all three dimensions.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6984ad0f7e9fc5edd808036e_Opus_4-6_Finance-Tasks-Benchmark.png)

On research, Claude Opus 4.6 improves on both BrowseComp and DeepSearchQA, two benchmarks that test a model’s ability to extract specific information from large, unstructured data sources. In practice, this means that users can hand Claude a dense set of documents and receive a specific, focused answer, rather than a simple summary.

On analysis, Claude Opus 4.6 is state-of-the-art at 60.7% (achieving a 5.47% improvement from Opus 4.5) on [Finance Agent](https://www.vals.ai/benchmarks/finance_agent), an external benchmark from Vals AI that evaluates models on research of SEC filings of public companies. Opus 4.6 is also state-of-the-art on the [TaxEval](https://www.vals.ai/benchmarks/tax_eval_v2) by Vals AI at 76.0%.

On creation, we use GDPval-AA to measure Claude’s performance on complex knowledge work, in addition to our Real-World Finance evaluation. With Claude Opus 4.6, structured outputs like spreadsheets and presentations come out right more often on the first pass. The side-by-side outputs below show how output quality has improved from Claude Opus 4.5 to Opus 4.6. These are examples of Claude’s first-pass performance on a commercial due diligence task (evaluating a potential acquisition)—the kind of work that would typically take a senior analyst two to three weeks to complete.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69860def3cf544958f0a7c43_Opus-46-Blog-Comparison-Excel%20(1).png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69860e00c073500bc2eb26f4_Opus-46-Blog-Comparison-PowerPoint%20(1).png)

> “With Claude Opus 4.6, creating financial PowerPoints that used to take hours now takes minutes. We're seeing tangible improvements in attention to detail, spatial layout, and content structuring.” - **Aabhas Sharma, CTO, Hebbia**

> “The performance jump with Claude Opus 4.6 feels almost unbelievable. Real-world tasks that were challenging for Opus [4.5] suddenly became easy. This feels like a watershed moment for spreadsheet agents on Shortcut.” - **Nico Christie, Co-Founder & CTO, Shortcut AI**

## Better multitasking and first drafts

The finance capabilities of Claude Opus 4.6 are easy to access with Cowork, a [new way to use Claude](https://claude.com/blog/cowork-research-preview) in our desktop app.

In Cowork, you give Claude access to a desktop folder of your choosing. Claude is able to read, edit, and create new files directly in that folder. For finance teams, this means you can kick off several analyses at once, while steering Claude’s thought process as it creates each deliverable to meet your standard.

Cowork can also be customized [with plugins](https://claude.com/blog/cowork-plugins)—bundles of skills (which specify how to complete a task) and connectors to data on other platforms. With [our corporate finance plugin](https://claude.com/plugins/finance), for example, Claude immediately knows how to complete common workflows like journal entries, variance analyses, and reconciliation. You can also [build your own plugins](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) to match how you like to work.

Cowork is [available](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) as a desktop-only research preview in beta on all paid Claude plans1.

## Go deeper without leaving your spreadsheet

Claude in Excel brings Claude Opus 4.6 directly to your spreadsheets.  We’ve now made it better at planning and clarifying assumptions with users, especially as the task becomes more complex. It also now supports pivot table editing, chart modifications, conditional formatting, sorting and filtering, data validation, and finance-grade formatting.

Finally, we’ve added usability improvements, including auto-compaction for long conversations and drag-and-drop multi-file support. This means you’ll need to do much less copying and pasting between tabs. You can work with Claude on everything from financial models to client-ready workbooks, all in one place.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6984ae18765ce9ada0768cfc_ClaudeExcel-Blog-Hero-Desktop.png)

> “Claude in Excel powered by Claude Opus 4.6 represents a significant leap forward. From due diligence to financial modeling, it’s proving to be a remarkably powerful tool for our team - taking unstructured data and intelligently working with minimal prompting to meaningfully automate complex analysis. It’s an excellent example of AI augmenting investment professionals’ capabilities in tangible, time-saving ways.” - **Lloyd Hilton, Head of Hg Catalyst**

> “As one of Canada’s largest institutional investors, we’re constantly innovating and see AI at the forefront of shaping our future. Claude Opus 4.6's enhanced speed, precision, and capacity for complex tasks, like multi-tab analysis in Claude in Excel, unlock exciting possibilities for how we work.” - **Ben Letalik, Sr. Director, Digital Transformation & Innovation, BCI**

## Refine your presentations directly with Claude

We’re also launching Claude in PowerPoint as a research preview in beta. Just like Claude in Excel, this brings Claude into your PowerPoint sidebar, letting it read your existing layouts, fonts, and masters before then creating new work in-line. Claude can build decks from client templates, make targeted edits to existing slides, and generate a great first-pass presentation from scratch.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6984ae4566ef8dcf3a381733_ClaudePPT-Blog-Hero-Desktop.png)

Claude in PowerPoint is now available as a research preview for all users on a Max, Team, or Enterprise plan.

## Getting started

Claude Opus 4.6 and our latest product updates make a whole range of new tasks possible. But AI for finance remains an active frontier. Users should continue to review Claude’s outputs to ensure it meets their specifications; particularly for high-stakes work, human judgment remains essential. As we continue to improve Claude’s capabilities, our aim is to equip finance industry professionals with ever-more powerful tools for research and analysis, and to help them focus on their most important work.

Claude Opus 4.6, Cowork, and Claude in Excel are available on all paid Claude plans. To learn more about Claude in Excel, explore our [guide](https://support.claude.com/en/articles/12650343-claude-in-excel) and [video tutorial](https://claude.com/resources/tutorials/getting-started-with-claude-in-excel), and [get started here](https://claude.com/claude-in-excel). Claude in PowerPoint is available in research preview for all Max, Team, and Enterprise users, and you can [get started here](https://claude.com/claude-in-powerpoint).

To see how organizations are using these new features in action, [register for our webinar](https://anthropic.com/webinars/claude-in-excel-and-powerpoint).

‍

###### *Cowork is* [*available*](https://support.claude.com/en/articles/13345190-getting-started-with-cowork) *as a desktop-only research preview on all paid Claude plans, starting with Mac (Windows coming soon).*

‍

‍

‍

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

Jun 24, 2026

### Building effective human-agent teams

Enterprise AI

[Building effective human-agent teams](#)Building effective human-agent teams

[Building effective human-agent teams](/blog/building-effective-human-agent-teams)Building effective human-agent teams

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

Jun 22, 2026

### The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

Enterprise AI

[The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](#)The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

[The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry)The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

Mar 13, 2026

### 1M context is now generally available for Opus 4.6 and Sonnet 4.6

Product announcements

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](#)1M context is now generally available for Opus 4.6 and Sonnet 4.6

[1M context is now generally available for Opus 4.6 and Sonnet 4.6](/blog/1m-context-ga)1M context is now generally available for Opus 4.6 and Sonnet 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

Jul 24, 2025

### How Anthropic teams use Claude Code

Enterprise AI

[How Anthropic teams use Claude Code](#)How Anthropic teams use Claude Code

[How Anthropic teams use Claude Code](/blog/how-anthropic-teams-use-claude-code)How Anthropic teams use Claude Code

## Transform how your organization operates with Claude

See pricing

[See pricing](https://claude.com/pricing#api)See pricing

Contact sales

[Contact sales](https://claude.com/contact-sales)Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Thank you! You’re subscribed.

Sorry, there was a problem with your submission, please try again later.

    

    

    

    

    

    

    

    

    

    

Claude apps
