<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/being-specific -->

Lesson 18 of 65 · Claude with Amazon BedrockBeing specific

When working with Claude, one of the most effective ways to improve your results is to be specific about what you want. Instead of leaving everything up to the model's interpretation, you can provide clear guidelines or steps that direct Claude toward the kind of output you're looking for.

![](https://academy.claude.com/assets/media/369e6e634eb42154aaf3f7556b6a44d2a40762bf7e657cf5798953211f0236c3.png)

Think about it this way: if you ask Claude to "write a short story about a character who discovers a hidden talent," the model could go in countless directions. It might write 200 words or 2,000 words. It could focus on one character or introduce five. The story structure could vary wildly.

But if you add specific guidelines, you can shape the output to match your needs much more closely.

## Two Types of Guidelines

There are two main approaches to being specific in your prompts, and you'll often see both used together in professional applications.

![](https://academy.claude.com/assets/media/559eb8d6c6972037d53b153f4d4982147cd2500c28b50a44607ba101d31a0afa.png)

### Quality Guidelines

The first type focuses on listing qualities that your output should have. These guidelines control attributes like:

* Length constraints (keep under 1,000 words)
* Structural requirements (include a clear action that reveals the character's talent)
* Content specifications (include at least one supporting character)

### Process Steps

The second type provides specific steps for the model to follow. This approach makes Claude think through the problem systematically:

1. Brainstorm 3 talents that would create dramatic tension
2. Pick the most interesting talent
3. Outline a pivotal scene that reveals the talent
4. Brainstorm 3 supporting character types that could increase the impact of this discovery

Quality guidelines control what the output looks like, while process steps control how Claude arrives at that output.

## Real-World Testing

Let's look at how this works in practice. Here's a prompt for generating meal plans that incorporates specific guidelines:

```
Generate a one-day meal plan for an athlete that meets their dietary restrictions.

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}

Guidelines:
1. Include accurate daily calorie amount
2. Show protein, fat, and carb amounts
3. Specify when to eat each meal
4. Use only foods that fit restrictions
5. List all portion sizes in grams
6. Keep budget-friendly if mentioned
```



When tested against a baseline prompt without guidelines, this approach improved the evaluation score from 3.92 to 7.86 - more than doubling the quality.

Testing the process steps approach (telling Claude to calculate calories first, then figure out macros, then plan timing, etc.) also showed significant improvement, scoring 7.3.

## When to Provide Steps

While quality guidelines work well for most prompts, you should consider adding process steps when you're dealing with:

* Troubleshooting hard problems
* Decision making
* Critical thinking
* Anytime you want to force Claude to consider a "wider" view

![](https://academy.claude.com/assets/media/b2d486f7abc21edf5eff45f496e925048b9576561ce269c6a8befdf89fd3254c.png)

For example, if you're asking Claude to analyze why a sales team's numbers dropped 30% last quarter, you might want to provide steps that ensure it considers multiple angles - market conditions, individual performance, organizational changes, and customer feedback - rather than jumping to the first obvious explanation.

The key insight is that being specific helps you get consistent, high-quality results instead of leaving everything to chance. Whether you use quality guidelines, process steps, or both, you're giving Claude a clear framework to work within.
