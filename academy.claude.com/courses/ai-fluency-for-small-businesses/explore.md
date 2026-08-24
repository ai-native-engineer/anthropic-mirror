<!-- source: https://academy.claude.com/courses/ai-fluency-for-small-businesses/explore -->

Lesson 4 of 9 · AI Fluency for Small BusinessesExplore!

**Text Your Friend Markov** — *The 100% interpretable next-token generator*

## Send a Text

Long ago, my friends and I would play this game where you'd grab your phone and craft a message to a friend using only the recommended next words. Maybe you did this too.

Here's a simulator that was "trained" on a bit of content. Have a play!

Loading

We talked about this as if it were a "Me-bot". We knew it was recommending words based on our individual usage patterns, and we could see our voices in our personalized recommendations.

At the time, we were happy to dismiss it as tech magic. I don't think we realized how simple the algorithm might be.

Keep reading if you want to build one with me :)

## "Training" Your Model

Let's train on a handful of messages. All we need to do is tally the connections between words. Let's do this one message at a time.

Loading

This finished map of connections between words is called a **frequency table**. Normalize each row and you get a probability distribution of what comes next.

The act of picking a next word based on what you have so far is called **sampling**. We use that same term for this process with modern language models like Claude.

## Do Some Sampling

Using the same matrix based on 5 texts, go ahead and have a more informed play at our game. We'll show you the probabilities.

Loading

The highlighted row is your current context. Pick a word from the available choices to continue.

## 100-year-old Tech

*"Is this real tech?" Great question, reader.*

Markov published this idea in 1906. A century later in 2010, n-gram models like this were powering next-word prediction on your phone (SwiftKey, then Apple's QuickType). Around 2015, neural networks — first RNNs, then transformers in 2017 — began to replace the table lookup approach with a learned function, and the rest is... well, it's what we're working on now.
