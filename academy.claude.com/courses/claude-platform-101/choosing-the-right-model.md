<!-- source: https://academy.claude.com/courses/claude-platform-101/choosing-the-right-model -->

Lesson 3 of 13 · Claude Platform 101Choosing the right model

Loading

Choosing the right model

You're shipping an app with Claude. Which model do you pick? If you default
to the smartest one, your API bill will surprise you. Pick the cheapest one,
and the output might not hold up. Each model has different trade-offs, and
picking the right one affects both **quality** and **cost**.

## The model tiers

Anthropic currently offers four model tiers, and you choose between them with the `model` parameter in your API call.



*Note that Claude Fable 5 has been generally available since June 9, 2026,
but is not reflected in the video above. Learn more about Claude
Fable and Claude Mythos
[here(opens in new tab)](https://www.anthropic.com/news/claude-fable-5-mythos-5). The video and
terminal screenshot in this lesson were recorded with earlier models (Claude
Opus 4.7 and Claude Sonnet 4.6). The code below uses the current model IDs;
your latency and token numbers will differ.*

* **Claude Fable** is our most capable model yet — a new tier that sits above Opus, built for your toughest challenges. It comes at a significantly higher cost than Opus, so reserve it for work where that extra capability is worth paying for. The current Fable model is Claude Fable 5 (`claude-fable-5`).
* **Claude Opus** is the most capable of the three core model families, but also the slowest and highest cost of the three. Use it for deep reasoning, complex analysis, multi-step coding, and nuanced writing. The current Opus model is Claude Opus 5 (`claude-opus-5`).
* **Claude Haiku** is the fastest and lowest cost, optimized for speed and cost efficiency rather than maximum intelligence. Use it for high-volume, low-complexity work like classification, extraction, and routing. The current Haiku model is Claude Haiku 4.5 (`claude-haiku-4-5`).
* **Claude Sonnet** sits in the sweet spot: a balanced combination of intelligence, speed, and cost that works well for most production work. The current Sonnet model is Claude Sonnet 5 (`claude-sonnet-5`).

![Three cards comparing the Claude model tiers: Haiku (fastest, lowest cost, for classification and routing), Sonnet (capable and fast, for most production work), and Opus (most intelligent, highest cost, for deep reasoning and complex analysis)](https://academy.claude.com/assets/media/ee696666d9ca0b3bb8944eb4764fc2c9c97ec6eec6ad632e462e97459d16f9a2.png)

## Start with a simple evaluation

Before you write production code, set up a simple **evaluation**: a set of example inputs that you run through each model and score against what good output means for your use case. You don't need anything fancy — 20 or 30 representative examples from your actual workload is enough to start.

Then work your way up the tiers:

1. Run your examples through **Haiku** first. If the quality holds, you're done — and you just saved a lot of money.
2. If it doesn't, step up to **Sonnet**.
3. Only reach for **Opus** when the task needs it.

## Comparing the tiers side by side

Let's see the difference between the tiers, not just talk about it. We'll send the same prompt through all three models and watch the latency and token counts:

python

```
models = ["claude-haiku-4-5", "claude-sonnet-5", "claude-opus-5"]

for model in models:
    response = client.messages.create(
        model=model,
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    print(model, response.usage)
```

Two things are going on here:

* The loop swaps the `model` field on each request. Same prompt, same max tokens — only the model changes.
* `response.usage` gives you the input and output tokens straight back from the API, which is what your bill is calculated on.

![Terminal output from running the same prompt through Opus, Sonnet, and Haiku, showing each model's latency and input/output token counts](https://academy.claude.com/assets/media/f2fcad36116d737b93f677526df1b0af5c4be6477b87b4797e8700751c97ac56.png)

Run it and you'll see three models and three sets of numbers. **Opus** takes the longest and reads the most polished — but for a two-sentence definition, that polish is wasted. **Sonnet** tightens the writing up a little. And **Haiku** comes back, often in under a second, with a very competent two-sentence answer. It's honestly perfect for this kind of scenario.

And that's the whole point: **the right model is the cheapest one whose output you'd actually ship.** For a definition, Haiku is plenty. For drafting a regulatory response, you'd run the same comparison and probably end up on Opus. The eval is the same shape every single time.

## Routing different work to different models

In a real app, you'd route different kinds of work to different models inside the same endpoint. Take an operations dashboard with a document processing route:

* Every incoming file gets **classified with Haiku**.
* Client updates get **drafted with Sonnet**.
* Only RFP responses **reach for Opus**.

One queue, three models, picked per task.

## Recap

* Anthropic offers four model tiers: **Fable** for the highest available capability, **Opus** for hard problems, **Sonnet** for daily work, and **Haiku** for volume.
* Set up a simple evaluation — 20 or 30 representative examples from your real workload — before writing production code.
* Run the eval from Haiku upward and stop at the cheapest model whose output you'd actually ship.
* `response.usage` reports input and output tokens, which is what your bill is based on.
* In production, route different tasks to different models inside the same endpoint instead of picking one model for everything.
