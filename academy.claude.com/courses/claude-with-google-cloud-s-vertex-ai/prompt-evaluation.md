<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/prompt-evaluation -->

Lesson 10 of 66 · Claude with Google Cloud's Vertex AIPrompt evaluation

When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques to write better prompts, while prompt evaluation helps you measure how well those prompts actually work.

![](https://academy.claude.com/assets/media/c1b0e1164b44e2de255137a6950d9a3795f2ab17eaa22cae93abba5aa021b66e.png)

## Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for writing and improving prompts. It's a set of best practices that help Claude understand exactly what you're asking for and how you want it to respond. Think of it as the craft of prompt writing - techniques like multishot prompting, structuring with XML tags, and many other approaches we'll explore.

Prompt evaluation, on the other hand, is about measurement. It's automated testing that gives you objective metrics on whether your prompts are actually effective. Instead of guessing if your prompt works well, evaluation lets you:

* Test against expected answers
* Compare different versions of the same prompt
* Review outputs for errors

## The Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

![](https://academy.claude.com/assets/media/332ba59ed8712471e1810909958b12131598e00e5640618a75b9b4ed2b0bdb3e.png)

**Option 1:** Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

**Option 2:** Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

**Option 3:** Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective data. This requires more work and cost upfront, but gives you much more confidence in your prompt's reliability.

## Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are traps that all engineers fall into - myself included. It's natural to write a prompt, test it a couple times with your own inputs, and think "this looks good enough." But when you're building serious applications, this approach often leads to problems in production.

The issue is that you can't predict all the ways users will interact with your prompt. What seems to work perfectly in your limited testing might fail completely when faced with real-world usage patterns.

## The Value of Systematic Evaluation

Option 3 - running your prompt through an evaluation pipeline - gives you objective data about performance. Instead of relying on gut feelings or limited manual testing, you get measurable scores that tell you how well your prompt handles a variety of inputs.

This approach lets you iterate confidently. You can make changes to your prompt and immediately see whether those changes improve or hurt performance. It's the difference between guessing and knowing whether your prompt improvements actually work.

While evaluation requires more upfront investment in time and resources, it pays dividends when you need reliable, production-ready prompts that work consistently across diverse user inputs.
