<!-- source: https://claude.com/resources/articles/trainium2-and-distillation -->

As part of our expanded [collaboration with AWS](https://www.anthropic.com/news/anthropic-amazon-trainium), we’ve begun optimizing Claude models to run on [AWS Trainium2](https://aws.amazon.com/ai/machine-learning/trainium/), their most advanced AI chip.

To preview what’s possible with Trainium2, Claude 3.5 Haiku now supports latency-optimized inference in [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), making the model significantly faster without compromising accuracy.

We’re also adding support for model distillation in Amazon Bedrock, bringing the intelligence of larger Claude models to our faster and more cost-effective models.

### Next-gen models on Trainium2

We are collaborating with AWS to build Project Rainier—an EC2 UltraCluster of Trn2 UltraServers containing hundreds of thousands of Trainium2 chips. This cluster will deliver more than five times the computing power (in exaflops) used to train our current generation of leading AI models.

Trainium2 enables us to offer faster models in Amazon Bedrock, starting with Claude 3.5 Haiku which now supports latency-optimized inference in public preview. By enabling latency optimization, Claude 3.5 Haiku can deliver up to 60% faster inference speed—making it the ideal choice for use cases ranging from code completions to real-time content moderation and chatbots.

This faster version of Claude 3.5 Haiku, powered by Trainium2, is available in the US East (Ohio) Region via [cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) and is offered at $1 per million input tokens and $5 per million output tokens.

### Amazon Bedrock Model Distillation

We’re also enabling customers to get frontier performance from Claude 3 Haiku—our most cost-effective model from the last generation. With distillation, Claude 3 Haiku can now achieve significant performance gains, reaching Claude 3.5 Sonnet-like accuracy for specific tasks—at the same price and speed of our most cost-effective model.

This technique transfers knowledge from the "teacher" (Claude 3.5 Sonnet) to the "student" (Claude 3 Haiku), enabling customers to run sophisticated tasks like retrieval augmented generation (RAG) and data analysis at a fraction of the cost.

Unlike traditional fine-tuning, which requires developers to manually craft training examples and continuously adjust parameters, Amazon Bedrock Model Distillation automates the entire process by:

1. **Generating synthetic training data** from Claude 3.5 Sonnet
2. **Training and evaluating** Claude 3 Haiku
3. **Hosting** the final distilled model for inference

Amazon Bedrock Model Distillation automatically applies different data synthesis methods—from generating similar prompts to creating new high-quality responses based on your example prompt-response pairs.

Distillation for Claude 3 Haiku in Amazon Bedrock is now available in preview. Learn more in the AWS [launch blog](https://aws.amazon.com/blogs/aws/build-faster-more-cost-efficient-highly-accurate-models-with-amazon-bedrock-model-distillation-preview/) and [documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-distillation.html).

### Lower prices for Claude 3.5 Haiku

In addition to offering a faster version on Trainium2, customers can continue to access [Claude 3.5 Haiku](https://www.anthropic.com/claude/haiku) on the [Anthropic API](https://console.anthropic.com/workbench), [Amazon Bedrock](https://aws.amazon.com/bedrock/claude/), and [Google Cloud’s Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude).

To make this model even more accessible for a wide range of use cases, we’re lowering the price of Claude 3.5 Haiku to $0.80 per million input tokens and $4 per million output tokens across all platforms.

### Get started

Starting today, model distillation and the faster Claude 3.5 Haiku are available in preview in Amazon Bedrock. For developers seeking the optimal balance of price, performance, and speed, you now have expanded model options with Claude:

* Claude 3.5 Haiku with latency optimization, powered by Trainium2, for general use cases
* Claude 3 Haiku, distilled with frontier performance, for high-volume, repetitive use cases

To get started, visit the [Amazon Bedrock console](https://signin.aws.amazon.com/signup?request_type=register). We can’t wait to see what you build.

[ArticleOct 1, 2026

### Customize Claude Code with mods

Change how Claude Code behaves and looks with a few lines of TypeScript.

Claude Code](https://claude.com/resources/articles/claude-code-mods)[ArticleSep 30, 2026

### Claude for Government is now generally available

Claude Code CLI and Claude for Microsoft 365 also now available in early access.](https://claude.com/resources/articles/claude-for-government-is-now-generally-available)[ArticleSep 25, 2026

### Build plugins for Claude

You can now submit plugins to the Claude directory through a new developer portal, track them through review, and see usage analytics once they’re live.

Claude apps](https://claude.com/resources/articles/build-plugins-for-claude)[ArticleSep 24, 2026

### Claude Tag now supports personal connectors in channels

Claude Tag can now use your connectors for requests you make in a channel. Nobody else can use them, and you're in control of how to present the output.

Claude Tag](https://claude.com/resources/articles/claude-tag-now-supports-personal-connectors-in-channels)

## Transform how your organization operates with Claude

[See pricing](https://claude.com/pricing#api)[Contact sales](https://claude.com/contact-sales)

### Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.
