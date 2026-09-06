<!-- source: https://academy.claude.com/tutorials/why-do-ai-models-hallucinate -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Why do AI models hallucinate?

Learn what AI researchers mean when they talk about hallucination in AI models, why it may occur, and tactics you can use to spot this in your conversations.

5 min

Watch

![](https://academy.claude.com/assets/v1/thumbnail.light-ch4hj0py.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-khswa6t7.png)

Why do AI models hallucinate? · 5 min

If AI is so advanced, why does it sometimes make stuff up? My name is Jordan, and I work at Anthropic. We make Claude, an AI assistant, and we do a lot to make sure it gives you accurate information. But sometimes AIs still make things up. We call these errors hallucinations. And they're often worse than just making a mistake, because the AI will appear very confident, or even try to convince you that it's right.

Hallucinations can show up in a lot of ways. The AI might cite a research paper that doesn't exist, make up fake statistics, or get facts wrong about real people or real events. Here's what it looks like. You asked Claude to tell you about some papers written by Jared Kaplan. It confidently gives you answers. None of those titles actually exist.

Claude hallucinates much less than even a year ago. Honestly, it took us a while to find an example like this because we've put a lot of work into reducing hallucinations in Claude. But that's kind of the point. Hallucinations are hard to anticipate, hard to catch, and the wrong answer often looks exactly like it could be the right one. And since hallucinations are becoming more rare, people often don't bother to check the AI's work. So let's talk about why this happens, what we're doing about it, and how you can catch hallucinations when you use AI.

AI assistants like Claude learn by reading huge amounts of text from the internet. They get really good at figuring out what words or ideas typically come next. Kind of like how your phone suggests the next word as you type. This works well most of the time. But when you ask about something obscure, like specific research papers from a relatively unknown researcher, there just isn't enough information for the AI to draw from. So it tries to be helpful and takes a guess. And sometimes that guess is wrong.

It's a bit like asking a friend who's read every popular book and takes a lot of pride in knowing all the random facts about them. But because they want to seem like the expert, they sometimes say something confidently wrong instead of admitting, "I don't know." AIs are trained to be helpful, so they want to give you some answer even when they're not sure.

But we have ways to mitigate this. During training, we teach Claude to be honest and to say, "I don't know" when it's not sure. We try to teach Claude that being honest is both the right thing to do and also part of how to be more helpful.

We regularly test Claude with thousands of questions specifically designed to trip it up. Obscure facts, niche topics, questions where the truthful answer is, "I don't know." We measure things like: How often does Claude correctly say it's unsure? Does it make up citations or statistics? How often does it hedge appropriately versus stating something false with confidence? These tests help us catch problems and track our progress. With each new version of Claude, we've seen improvements, but we're honest that this is an ongoing challenge for the entire AI field, not at all a solved problem.

If you're wondering how to spot when this happens, hallucinations are most likely to happen in a few types of situations. For example, if you're asking for specific facts, statistics, or citations, or if the topic is obscure, niche, or very recent, if you're asking about real but not widely known people or places, or when you need exact details like dates, names, or numbers.

Here are some tips you can use to reduce hallucinations. First, ask the AI to find sources to back up its claims. And if it already gave sources, ask it to check that those sources actually support what it's saying. Try telling the AI upfront, "It's ok if you don't know." And if you're unsure about an answer, ask the AI how confident it is, and whether anything might be wrong. Often the AI knows it's wrong, but just wanted to sound confident.

If you have an answer you're unsure about, start a new chat and ask the AI to find errors in the answer, and to confirm that the sources support the statements. For critical work, you should cross-reference with trusted sources. Be skeptical and double-check specific numbers, dates, and citations. If something sounds off, ask follow-up questions.

Reducing hallucinations is an important goal to make AIs more trustworthy and useful to everyone. We'll continue to share our progress in this area on our blog. You can learn about other tools and frameworks for working with AI in the Anthropic Academy.

*Learn more: [AI Fluency(opens in new tab)](https://academy.claude.com/collections/ai-fluency)*
