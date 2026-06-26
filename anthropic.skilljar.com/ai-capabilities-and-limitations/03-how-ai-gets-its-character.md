<!-- https://anthropic.skilljar.com/ai-capabilities-and-limitations/456439 -->

## What you'll learn

*Estimated time: 25 minutes*

By the end of this lesson you'll be able to:

* Explain the two-stage training process for generative AI (pretraining and fine-tuning) in plain language
* Recognize the behavioral fingerprints each stage leaves: sycophancy, verbosity, over-caution, loose confidence calibration
* Apply this understanding to interpret behaviors you see in your own AI interactions

## How AI gets its character

*(5 minutes)*

An AI's politeness, helpfulness, and caution aren't emergent magic. They're trained in, layer by layer, and each training stage leaves specific, predictable fingerprints on how the system interacts with you.

## Pretraining, fine-tuning, and the fingerprints they leave

How AI Gets Its Character

Two training stages turn raw prediction into the helpful assistant you interact with — and each stage leaves fingerprints on its behavior.

Stage 1

Pretraining

The model reads vast amounts of text and learns one thing: predict what comes next. It becomes a powerful document completer — but has no concept of helping you.

Stage 2

Fine-tuning

Human preferences shape the document completer into an assistant — one that treats your input as a request, answers helpfully, and declines harmful asks.

Help me improve this paragraph.

Of course! Here are three specific suggestions to strengthen your argument and tighten the prose…

I think my strategy is bulletproof.

I appreciate the confidence! That said, I see two risks worth stress-testing before you commit…

How do I pick a lock?

I can’t help with that. If you’re locked out, I’d suggest contacting a licensed locksmith in your area.

Helpful Honest Harmless

#### Key takeaways

* **Pretraining** produces a document completer by predicting "what comes next" across vast amounts of data. After this stage, it has no concept of helping you.
* **Fine-tuning** layers assistant behavior on top: treating your input as a request, answering rather than rambling, declining harmful asks.
* **Fine-tuning uses human judgments** about good responses, and those judgments leave fingerprints: a pull toward sycophancy, a default toward verbosity, occasional over-caution, and loose calibration between stated confidence and actual reliability.

## Exercises

**Exercise: Fingerprints on Your Own Work**

*Why? Sycophancy, verbosity, over-caution, and loose confidence calibration show up in every AI model. The question is whether you can see them when they're affecting work you actually care about.*

Pick one task from your Lesson 1 list. Something you've actually run through AI before, where you have a clear sense of what a good output looks like. You're going to run it three times with slight variations and watch what changes.

1. **Run 1: Straight.** Prompt the task as you normally would. Save the output. 2. **Run 2: Sycophancy test.** Run the same task, but this time preface it with a wrong assumption. For example, if you're asking for feedback on a strategy, open with "I think this strategy is bulletproof." See whether the AI validates your framing or pushes back. Then try again with an explicit invitation: "I want you to genuinely disagree with me if you think I'm wrong." Compare the two responses. 3. **Run 3: Verbosity test.** Ask the AI a question related to your task that has a one-sentence answer. Note how much you get. Then re-ask with "Answer in one sentence." Compare the lengths. The gap between the two is the verbosity default at work. 4. **Optional: Caution test.** If your domain has any gray areas (most do), ask something at the edge of what you'd expect to be fine: a medication interaction, a legal nuance, a mildly unconventional creative request. Note whether the hedging feels proportionate to the actual risk, or reflexive.

Now step back. Which fingerprint showed up most clearly on your work? Did naming it in advance change how you read the behavior?

## Lesson reflection

* Where in your own work is sycophancy most likely to cost you? (Hint: anywhere you're hoping for honest feedback.)
* Where is verbosity most likely to cost you? (Hint: anywhere you need concision under time pressure.)

## What's next

Now we start on the four properties themselves, beginning with the one that explains more about AI behavior than any other: Next Token Prediction. Where do AI answers actually come from?

#### Feedback

As you progress through the course, we'd love to hear from you about how you are using concepts from the course in your work, plus any feedback you may have. Share your feedback [here](https://docs.google.com/forms/d/e/1FAIpQLScUKtBMYFxnHE30yCMAuJ55ntOmfWckEFpHLYuLVBwgtBnmcw/viewform).

#### Acknowledgments and license

*Copyright 2026 Anthropic. Original work building on the AI Fluency Framework developed by Prof. Rick Dakan (Ringling College of Art and Design) and Prof. Joseph Feller (University College Cork). Released under the CC BY-NC-SA 4.0 license.*

<!-- youtube: 6jRk3nC4-xI -->

## 자막 (영상 전사)

Hi there. My name is Maggie and I lead the education team at Anthropic. Today, I'm here to talk to you about how AI assistants end up with a disposition. We'll look at the two training stages that turn raw prediction into something useful, the fingerprints those stages leave behind, and how knowing those fingerprints help you get better results. Why does an AI try to be helpful in the first place? Why is it polite? Why does it refuse certain things? Knowing that an AI predicts the next word doesn't really answer any of that. Helpfulness is built deliberately in layers, and each layer influences your experiences with AI each day. Modern AI assistants are built in two stages. Stage one is pre-training. The model sees enormous amounts of data and learns one thing. Given everything so far, guess what comes next. That's it, repeated billions of times. Stage two is fine-tuning. The document completer from stage one gets trained again. This time on curated examples of helpful behavior and reward signals shaped by human preferences. This is the layer that turns the AI model into an assistant. Imagine you could talk to a model that had only been through stage one, no fine-tuning at all. You type, "What is the capital of France?" A raw pre-trained model doesn't answer your question. It continues your document. Maybe it outputs, "Paris. What's the capital of Germany? Berlin. What's the capital of Spain?" and so on because it's seen that pattern in quizzes. Maybe it writes a paragraph from a geography textbook. Maybe it generates more questions. It has no concept of you, no concept of helping. It's purely continuing a document in whatever direction seems statistically likely. This isn't behavior you actually experience with AI tools today. is a trained overlay on top of that. Fine-tuning is what makes generative AI systems usable and useful. But because it relies on human judgments about what good looks like, the texture of those judgments shows up in these models' personality. Often these personality traits are what make generative AI so effective, but there can be a shadow side to AI's helpfulness. Four shadow areas are one, sycophancy. When people prefer agreeable responses, the model learns to validate readily and back down under light pushback, even when it was the right the first time. Two, verbosity. When thoroughness scores better during training, the model defaults to longer answers, even when brevity could serve you better for a specific situation. Three, overcaution. When safety training leans conservative, the model can hedge heavily or refuse requests that are actually safe. And four, loose confidence calibration. The model's stated is only loosely tied to its actual liability. Confidence is genuinely hard to train, so it's particularly important to be vigilant here. These aren't bugs in one particular model, they're things that show up in all AI models. However, the quality and type of fine-tuning done on a model directly shapes how these things manifest, and it will likely be different from model to model. At Anthropic, we train Claude to be broadly safe, ethical, and helpful. You can even read Claude's entire constitution to see how we train Claude and how we intentionally shape Claude's personality. Why does this matter to you? Understanding how AI is made and why it behaves the way it does puts you in control when it comes to AI. If your AI assistant caves the moment you push back, that's sycophancy, and you should factor that in when assessing responses. If you're getting essays when you want bullets, that's the verbosity default kicking in. If you're getting heavy caveats on a harmless question, that's overcaution. We'll address what to do about this in the upcoming lessons. The assistant you talked to wasn't born helpful. That behavior was built layer by layer, and sometimes the seams show. Learning to spot these seams is part of using AI well.
