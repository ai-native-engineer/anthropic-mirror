<!-- source: https://claude.com/blog/prompt-improver -->

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23073f253139349bf60_71800a27b08a18e808de684513bb852c37b8a334-1000x1000.svg)

# Improve your prompts in the developer console

Claude can now automatically refine prompts in the developer console using techniques like chain-of-thought reasoning and example enrichment.

‍

  [Product announcements](https://claude.com/blog/category/announcements)
* Product

* Date

  October 14, 2024
* Reading time

  5

  min
* Share

  [Copy link](#)

  https://claude.com/blog/prompt-improver

Today, we're introducing the ability to improve prompts and manage examples directly in the [Anthropic Console](https://console.anthropic.com/). These features make it easier to leverage prompt engineering best practices and build more reliable AI applications.

## Better prompts for better completions

Prompt quality plays a significant role in how successful a model's responses are for a given task. However, prompting best practices take time to implement and often vary across model providers.

The prompt improver allows developers to take existing prompts and leverage Claude to automatically refine them using advanced prompt engineering techniques. This is ideal for adapting prompts that were originally written for other AI models, as well as for optimizing hand-written prompts.

[](https://cdn.sanity.io/files/4zrzovbb/website/fb1afd8b4dd4831fd1e700ad23affda9cf70d666.mp4)

The prompt improver strengthens existing prompts via the following methods:

1. **Chain-of-thought reasoning:** Adds a dedicated section for Claude to think through problems systematically before responding to improve accuracy and reliability.
2. **Example standardization:** Converts examples into a consistent XML format for improved clarity and processing.
3. **Example enrichment:** Augments existing examples with chain-of-thought reasoning that aligns with the newly structured prompt.
4. **Rewriting:** Rewrites the prompt to clarify structure and correct any minor grammatical or spelling issues.
5. **Prefill addition:** Prefills the Assistant message to direct Claude’s actions and enforce output formats.

Once the new prompt is generated, you can provide feedback for Claude about what is and isn’t working to further improve the prompt.

**Our testing shows that the prompt improver increased accuracy by 30% for a multilabel classification test1 and brought word count adherence up to 100% for a summarization task.2**

# Manage multi-shot examples

Adding examples to prompts is one of the most effective ways to improve model response quality, especially when it comes to getting Claude to precisely follow a specific format in the output. You can now manage examples in a structured format directly in the Workbench. This makes it easier to add new examples with clear input/output pairs or edit existing examples to refine response quality.

![A visual of the Anthropic Console showing examples for a prompt.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d939bfbe47c603d7aae_57c9898911ae729e6745f4d5cc5d9c1e0e4b18df-3840x2160.jpeg)

If your prompt doesn’t have examples, you can add them with Claude-driven example generation. Claude can automatically create synthetic example inputs and draft outputs for you to streamline this process.

Adding examples contributes to increased:

* **Accuracy:** Reduces misinterpretation of instructions.
* **Consistency:** Ensures desired output formatting.
* **Performance:** Boosts Claude’s ability to handle complex tasks.

## Evaluate prompts with ideal outputs

Our [prompt evaluator](https://www.anthropic.com/news/evaluate-prompts) allows you to test your prompts under various scenarios. To help benchmark and improve prompt performance, we've added an optional "ideal output" column in the Evaluations tab. This column helps users effectively and consistently grade model outputs on a 5-point scale.

After testing your new prompt, you can give Claude additional feedback in the prompt improver on what’s still not working and repeat this process until you’re satisfied with the result. The prompt improver can also modify the prompt and examples based on arbitrary requests. For example you can ask Claude to change the prompt and examples to have JSON-formatted outputs instead of XML-formatted outputs.

## Customer spotlight: Kapa.ai

[Kapa.ai](https://www.kapa.ai/), a technology company that turns your technical knowledge base into a production-ready AI assistant, used the prompt improver to migrate multiple critical AI workflows to Claude.

"Anthropic's prompt improver streamlined our migration to Claude 3.5 Sonnet and enabled us to get to production faster," said Finn Bauer, Co-Founder at Kapa.ai.

## Getting started

The prompt improver, example management, and ideal outputs are available to all users in the [Anthropic Console](https://console.anthropic.com/).

To learn more about how to improve and evaluate prompts with Claude, check out our [docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver).

#### Footnotes

[1] Given 500 Wikipedia articles and titles, we tested Claude 3 Haiku’s ability to match article titles to a sentence pulled from an article at random. Claude 3 Haiku’s accuracy increased by 30% in comparison to the original prompt.

[2] Given ten Wikipedia articles, Claude’s adherence to an instruction to write summaries within a specific word count range was 100% after running through the prompt improver.

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

    

    

    

    

    

    

    

    

    

    

Coding
