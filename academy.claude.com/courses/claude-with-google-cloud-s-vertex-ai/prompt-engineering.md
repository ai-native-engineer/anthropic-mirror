<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-engineering -->

Lesson 16 of 66 · Claude with Google Cloud's Vertex AIPrompt engineering

Prompt engineering is about taking a prompt you've written and improving it to get more reliable, higher-quality outputs. This process involves iterative refinement - starting with a basic prompt, evaluating its performance, then systematically applying engineering techniques to improve it.

![](https://academy.claude.com/assets/media/135340165a55b554a968a55352c565b5d180ee9d685cc339021feb685f620efa.png)

## The Iterative Improvement Process

The approach follows a clear cycle that you can repeat until you achieve your desired results:

![](https://academy.claude.com/assets/media/c932d83fda9997cf44eedfc316055d33807ac4050bf2818a482afb1bc4f96693.png)

1. **Set a goal** - Define what you want your prompt to accomplish
2. **Write an initial prompt** - Create a basic first attempt
3. **Evaluate the prompt** - Test it against your criteria
4. **Apply prompt engineering techniques** - Use specific methods to improve performance
5. **Re-evaluate** - Verify that your changes actually improved the results

You repeat the last two steps until you're satisfied with the performance. Each iteration should show measurable improvement in your evaluation scores.

## Example: Meal Planning for Athletes

Let's walk through a practical example. The goal is to create a prompt that generates a one-day meal plan for athletes based on their physical characteristics and requirements.

![](https://academy.claude.com/assets/media/38a6bdc804f9e639fe11c3770baccc08aa7669075905278386f1f01cbd413ffe.png)

The prompt takes these inputs and should produce a comprehensive meal plan with caloric totals, macronutrient breakdowns, and specific meal details with portions and timing.

## Setting Up the Evaluation Framework

To measure improvement systematically, you need a robust evaluation setup. The framework includes:

* **Dataset generation** - Create test cases that represent real-world scenarios
* **Automated scoring** - Use consistent criteria to evaluate outputs
* **Performance tracking** - Monitor improvements across iterations

When setting up your evaluator, be mindful of API rate limits. Start with low concurrency (1-3 concurrent requests) and only increase if you don't encounter rate limiting errors.

## Creating Your Initial Prompt

Start with something simple, even if you know it's not great. Here's an example of a basic first attempt:

```
What should this person eat?

- Height: {prompt_inputs["height"]}
- Weight: {prompt_inputs["weight"]}
- Goal: {prompt_inputs["goal"]}
- Dietary restrictions: {prompt_inputs["restrictions"]}
```



This prompt is intentionally basic and will likely produce poor results. That's exactly what you want - a clear baseline to improve from.

## Establishing Evaluation Criteria

Define specific criteria that your prompt should meet. For the meal planning example, good output should include:

* Daily caloric total
* Macronutrient breakdown
* Meals with exact foods, portions, and timing

These criteria help the evaluation model grade outputs consistently and give you clear targets for improvement.

## Measuring Baseline Performance

Run your initial prompt through the evaluation framework. Don't be discouraged by low scores - a score of 2.3 out of 10 is actually perfect for a starting point. It gives you plenty of room to demonstrate improvement.

![](https://academy.claude.com/assets/media/2fd0f9ee259eec89733058334e131c87c93a044ab903477ced9e647b681c7a42.png)

## Analyzing Results

Most evaluation frameworks generate detailed reports showing how each test case performed. These reports typically include:

![](https://academy.claude.com/assets/media/5c83046a90e65b8d86f42b83334b201c7b01071c9c7f88803dc2568a65ed45c5.png)

* **Individual test case results** - See exactly what the model produced
* **Scoring breakdown** - Understand why certain outputs scored poorly
* **Reasoning** - Get feedback on what's missing or incorrect

Use this detailed feedback to identify specific areas where your prompt needs improvement. Look for patterns across multiple test cases to understand systematic issues rather than one-off problems.

## Next Steps

With your baseline established and evaluation framework in place, you're ready to start applying specific prompt engineering techniques. Each technique you apply should result in measurable improvement in your evaluation scores, moving you closer to your ideal output quality.

The key is to make one change at a time, evaluate the impact, then decide whether to keep the change or try a different approach. This systematic process ensures you understand which techniques work best for your specific use case.
