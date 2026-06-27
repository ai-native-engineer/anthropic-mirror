---
title: "Evaluate prompts in the Anthropic Console"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=KIGBsQqZcNA
youtube_id: KIGBsQqZcNA
published: 2024-07-09
duration: "3:20"
captions: en
---

# Evaluate prompts in the Anthropic Console

[![Evaluate prompts in the Anthropic Console](https://img.youtube.com/vi/KIGBsQqZcNA/hqdefault.jpg)](https://www.youtube.com/watch?v=KIGBsQqZcNA)

<details>
<summary>자막: Evaluate prompts in the Anthropic Console (3:20)</summary>

[00:00]
We've recently made a number of improvements to the Anthropic Workbench
that make it easier to develop and deploy high-quality prompts for Claude.
Let's see how it works by taking a look at our recently updated prompt generator.
You can use the prompt generator to take a high-level description of a task and convert
it into a detailed prompt template using Claude 3.5 Sonnet.
In this case, let's imagine we need to triage customer support requests.
As you can see, Claude immediately starts writing a prompt based off of our task.
It's detailed and specific and looks like it should work.
But, before we deploy it to production, we should really test to see how it performs
with realistic customer data.
Coming up with realistic test data can be time-consuming and it can take longer than
writing the prompt itself.
You can now use Claude to automatically generate realistic input data based off of your prompt.
In this case, we can generate a customer support request.
This one looks good, so let's see how the prompt works with this particular support request

[00:01]
This seems pretty good.
It's providing a justification and a triage decision.
But how do we know that we didn't get lucky?
How do we know that this prompt is actually going to work in a broad range of scenarios?
That's where the new Evaluate feature comes in.
You can use the Evaluate page to set up as many test cases as you want.
Let's keep generating a broad range of representative test cases.
You can also upload test cases from a CSV if you happen to have the test data in it.
Test case generation logic is highly customizable and adapts to your existing test set.
If you have highly specific requirements, you can directly edit the generation logic
yourself.
Once you have enough test cases ready, you can generate results for your new test suite.
Alright, these results look pretty good, so let's go and grade their quality.

[00:02]
Maybe we decide when we're evaluating them that we actually felt that the justifications
were a little brief.
We'd like them to be a bit longer.
Well, we can go back to the prompt and find the section where it specified a one sentence
justification and update it to a two sentence justification.
We can rerun the prompt, and just as we'd hope, we're seeing a two sentence justification.
So let's go back to the evaluate tab, and thankfully, our test suite is still there.
So it can rerun the new prompt against the old test set data.
And just as we hoped, they're all just a little bit longer.
We can go and grade these new outputs.
We're happier with these ones.
But just to be sure, we can actually compare these new results against the old results.

[00:03]
And here we can see, side by side, the results are longer.
We're still getting similar triage decisions, but our grading, on average, is better.

</details>
