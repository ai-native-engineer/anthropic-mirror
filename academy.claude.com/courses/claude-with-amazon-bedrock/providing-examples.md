<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/providing-examples -->

Lesson 20 of 65 · Claude with Amazon BedrockProviding examples

Providing examples in your prompts is one of the most effective prompt engineering techniques you'll use. This approach, known as "one-shot" or "multi-shot" prompting, involves giving Claude sample input/output pairs to guide its responses.

## How Examples Work

Let's look at a sentiment analysis example. Say you want Claude to categorize whether a tweet is positive or negative:

![](https://academy.claude.com/assets/media/07550ea11708a358f557446c0e1d64478b7bf9bcaf6acb1fa9b1fb1795ad7d3c.png)

The challenge here is sarcasm. A tweet like "Yeah, sure, that was the best movie I've seen since 'Plan 9 from Outer Space'" appears positive on the surface, but it's actually sarcastic and negative (Plan 9 from Outer Space is famously terrible).

## Adding Examples to Your Prompt

To handle this, you can add examples that show Claude exactly how to respond:

![](https://academy.claude.com/assets/media/d9149d7ef35a29ea692ee8fb875c5da77a86c357a87aa2cb7f173fd143fa7ef2.png)

The key elements are:

* Clear introduction: "Here is a example input with an ideal response"
* XML tags for structure: `<sample_input>` and `<ideal_output>`
* Concrete examples that demonstrate the desired behavior

## Handling Corner Cases

For tricky scenarios like sarcasm, you can provide multiple examples (multi-shot prompting). Add context to highlight what Claude should watch for:

```
Be especially careful with tweets that contain sarcasm.
For example:
<sample_input>
Oh yeah, I really needed a flight delay tonight! Excellent!
</sample_input>
<ideal_output>
Negative
</ideal_output>
```



## When to Use Examples

Examples are particularly useful for:

* Capturing corner cases or edge scenarios
* Defining complex output formats (like specific JSON structures)
* Showing Claude exactly what "good" output looks like

## Finding Good Examples from Evaluations

When running prompt evaluations, look for your highest-scoring outputs in the HTML report. These make excellent examples to include in your prompt.

![](https://academy.claude.com/assets/media/fd159d6bcdc25f88c8a4617225a19ac38d830f70042fd53f7aa8236ec416042b.png)

Find a response that scored well (ideally a 10, or your highest score), then copy both the input and output to use as your example.

## Adding Context to Examples

You can make examples even more effective by explaining why they're good. After your example output, add a brief explanation:

```
<ideal_output>
[Your example output here]
</ideal_output>

This example meal plan is well-structured, provides detailed information on food choices and quantities, and aligns with the athlete's goals and restrictions.
```



This helps Claude understand not just what to produce, but why that output is considered ideal.

## Best Practices

* **Use XML tags** to clearly structure your examples
* **Be explicit** about what you're showing Claude
* **Choose representative examples** that cover your most important use cases
* **Include corner cases** that might trip up the model
* **Explain why examples are good** when it's not obvious

One-shot and multi-shot prompting will quickly become essential tools in your prompt engineering toolkit, especially when you need consistent, well-formatted outputs or want to handle tricky edge cases reliably.
