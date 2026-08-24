<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/overview-of-claude-models -->

Lesson 1 of 65 · Claude with Amazon BedrockOverview of Claude Models

Claude offers three distinct model families, each optimized for different priorities. All three models share Claude's core capabilities - they can handle text generation, coding, image analysis, and other tasks. The key difference is how they balance intelligence, speed, and cost. The examples in this course use Claude Haiku 4.5.

![](https://academy.claude.com/assets/media/d87ca18bfca0fadd839a95aa8eecb912a4b3cf1dbb1400081f2324be879509a9.png)

## Claude Opus

Opus delivers Claude's highest level of intelligence. It's designed for complex scenarios that require sophisticated reasoning and planning capabilities.

Opus excels at working independently on complex projects for extended periods. It can manage multi-step processes and navigate different requirements without much human intervention. The model supports reasoning, meaning it can provide quick responses for simple tasks or spend time thinking through more complex problems.

The trade-off is moderate latency and higher cost. You're paying more and waiting longer for that extra intelligence.

## Claude Sonnet

Sonnet sits in the sweet spot of Claude's lineup, offering a balanced combination of intelligence, speed, and cost that works well for most practical applications.

What makes Sonnet particularly valuable is its strong coding ability combined with fast text generation. Many developers appreciate its ability to make precise edits to complex codebases without breaking existing functionality.

## Claude Haiku

Haiku is Claude's fastest model, built specifically for applications where response time is critical. It's optimized for speed and cost efficiency rather than maximum intelligence.

Haiku does support reasoning: Claude Haiku 4.5 can think through harder problems when you enable extended thinking with a token budget. The difference from Opus and Sonnet is that Haiku won't decide on its own how much reasoning a request needs. In practice, it's ideal for user-facing applications that need real-time interactions, with extended thinking in reserve for the occasional harder task.

## Choosing the Right Model

![](https://academy.claude.com/assets/media/6aad8c72323f0bce9bd4ab382bdaefdb0f3c387cc58446a2732184687afdee7d.png)

Model selection comes down to understanding the trade-offs between intelligence and cost/speed. Here's how to decide:

* **Choose Opus** when intelligence is your top priority. If you have complex tasks requiring strong reasoning capabilities, you're choosing quality over speed and cost.
* **Choose Haiku** when speed matters most. For real-time user interactions or high-volume processing where you need the fastest possible responses.
* **Choose Sonnet** when you need balance. Most applications benefit from Sonnet's combination of intelligence, speed, and reasonable cost.

## Using Multiple Models

Many teams don't stick to just one model. Instead, they use different models for different parts of the same application:

* Haiku for user-facing interactions where speed is crucial
* Sonnet for main business logic
* Opus for complex tasks requiring deeper reasoning

This approach lets you optimize each part of your application for its specific requirements while managing overall costs and performance.
