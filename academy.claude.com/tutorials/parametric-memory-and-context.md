<!-- source: https://academy.claude.com/tutorials/parametric-memory-and-context -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# How context affects Claude's performance and cost

Everything Claude knows about the world was either baked into the model during training, or is part of the current context. Learn where Claude's answers come from, where you might be using more tokens than expected, and how to be intentional about the tradeoff between cost and quality.

20 min

![](https://academy.claude.com/assets/v1/thumbnail.light-hbwc6qac.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-gxfjrbde.png)

Many people use AI chat as an alternative to search. To do this safely, it's important to understand where LLMs get their information. **When an LLM produces incorrect information, it's usually a side-effect of missing, incorrect, or low-quality context.**

If you don't know *why* that happens, it's easy to feel that the model is attempting to deceive you by making up information. But once you understand where a model's knowledge comes from, you can more clearly anticipate where it might make a mistake. You can also see where your tokens are going, and decide when more context is worth paying for.

## Where answers come from[](#where-answers-come-from)

*It's a warm-up - just take a guess.*

Quick check

When an AI chat model answers your question, where does the answer come from?

It looks it up on the web each timeIt memorized it during trainingIt reads whatever is in the conversationSome mix, depending on the question

All three happen. The lesson goes through them in that order: knowledge from training, whatever you put into the conversation, and what the model looks up on its own.

## Parametric memory[](#parametric-memory)

**Models sometimes just... know things. That built-in knowledge is called parametric memory, because it's baked into the model's weights, or *parameters*.**

Nobody set out to build an encyclopedia, but the facts that LLMs can recite from memory emerged as a side-effect of learning to predict text.

## Where parametric memory runs out[](#where-parametric-memory-runs-out)

Parametric memory is better at some things than others. Below are sentences a model is in the process of writing by predicting the most likely next word. Click to reveal the next couple of words in each sentence, and then decide for yourself whether or not the model produced correct information.

## Adding context[](#adding-context)

**Take a look at a question Claude can't answer from training alone.**

In this widget, if we tweak our question by providing additional context, the task gets noticeably easier for the model.

If you've ever attached something to a chat with Claude, you already have some intuition here. The approach of giving the model everything it could possibly need is called **context stuffing**. Context stuffing generally works, but it comes up against some constraints.

## The context window[](#the-context-window)

**A language model's context has a maximum size. At the time of writing, current flagship Claude models can hold up to a million [tokens(opens in new tab)](https://academy.claude.com/tutorials/tokens-and-embeddings).**

That's about three copies of *Moby-Dick*. So how does anyone ever run out of room?

In the early days of AI chat, hitting the limit meant starting over. You may have reached this limit yourself at some point with a chat interface in 2024 or 2025. And yet when it happens, you *know* you've written way less than a novel or three - most of us just aren't that chatty. So where did your million tokens go? Let's explore.

## Filling the window[](#filling-the-window)

Drive a normal chat interaction and watch your context window fill. To keep this example digestible, we'll imagine a model with a much smaller context window of only 1,000 tokens.

Where did the tokens go?

The question you typed was 28 tokens. The system prompt that came before it was 345, and the search result Claude pulled in was 184. In a real product the numbers are bigger, but the proportions are similar, meaning most of what you pay for in a long conversation is context you didn't write.

## Compaction[](#compaction)

**When the context window nears its limit, the app asks Claude to summarize the whole conversation so far, and then that summary replaces the context that was there before.**

Compaction allows you to continue your conversation instead of starting a new one. Here's how it works:

1. **First, the app notices.** Instead of sending a request that might overload the context window, the app withholds your next turn and initiates compaction.
2. **Next, Claude summarizes.** The conversation so far is passed to Claude with a prompt like "attached is a conversation between a human and a model. Please produce a summary of everything that has happened so far."
3. **Finally, the conversation continues from that summary.** The summary replaces the conversation history, and then your withheld query from step 1 is passed to Claude for a response.

## Try it: compaction[](#try-it-compaction)

How well does compaction work?

Early compaction implementations were noticeably lossy - you could sometimes tell that guidance given before the summary hadn't survived it. Compaction prompts and models have both improved since, but it is still a summary, and can still occasionally result in lost details.

## Written memory[](#written-memory)

**Memory is how a hard-limited window can *feel* infinite: Claude writes a note in one conversation, and the notes are added back in at the start of the next.**

Think of memory as Claude writing things down, *Memento* style, and reading them back later: Claude wakes up fully refreshed after a nap and can look around at the memory files it previously wrote for itself. We'll call this **written memory**, so it doesn't get mixed up with parametric memory.

Compaction is how Claude can continue a single conversation beyond the context limit. **Written memory is how Claude keeps important details in context across multiple conversations.**

Read the sketch left to right. On Tuesday you state a preference and Claude visibly writes it down. Then, on Thursday, in a fresh conversation, Claude hasn't been told the preference again. But the memory note is quietly inserted into context before your first message. This process enables Claude to remember your preferences over time based on the direct feedback you share.

The memory makes it into future conversations, even in a brand new session without Tuesday's full context.

Different Claude products implement memory differently. Claude Code reads [CLAUDE.md files(opens in new tab)](https://code.claude.com/docs/en/memory) throughout a codebase, whereas [claude.ai keeps memory in its settings(opens in new tab)](https://support.claude.com/en/articles/11817273-using-claude-s-chat-search-and-memory-to-build-on-previous-context). But even if the location is different, the process is the same: Claude writes important information down, and then a later instance of Claude reads it back at the start of the next conversation.

## A week of memory[](#a-week-of-memory)

Five days with the same assistant. Notice what it writes down, and compare that to what it looks up fresh.

What's worth remembering?

Your project, your preferences, and your working relationships made the cut, but more ephemeral and granular details like the RSVP count and the catering quote did not. Claude can and should look those things up next time they come up, rather than writing them down and hoping they haven't changed.

## Prepended context[](#prepended-context)

Zooming out, a whole lot is added to the context before Claude sees your first token. The widget below shows what prepended context might be added to a conversation with Claude in a tool like [Cowork(opens in new tab)](https://claude.com/product/cowork). The exact contents vary from product to product.

Context is re-sent every turn.

Every message you send will re-submit the entire conversation so far, including the prepended context not visible in your chat window. That's why a short question late in a long conversation may cost more than the same question in a fresh one, and why starting a new chat can be the cheapest and fastest way to get an answer.

Bonus readingSystem prompts

Anthropic publishes the system prompts for its Claude apps and updates them as models change. Reading one is a great way to see how much of a product's behavior is written into the prompt rather than trained into the model.

**[Read the published system prompts →(opens in new tab)](https://platform.claude.com/docs/en/release-notes/system-prompts)**

## Agentic context[](#agentic-context)

Now that you know how important context is in augmenting Claude's capabilities, it's important to understand **agentic context**: when Claude decides to get more context before answering. You saw this happen in the earlier example about tomato plants, where Claude used a search tool rather than answering from parametric memory or the context it already had.

In the following widget, imagine you're Claude. The sidebar displays some info that was quietly inserted into context before the user's message. For each prompt, decide whether to answer from what you already know, or reach outside yourself for more context.

Claude makes this same decision on every turn, and how readily it reaches for more context depends partly on the effort setting. At higher effort, Claude is more likely to search, read, and check before answering, which usually means a better answer and a bigger context window. At lower effort, Claude is more likely to answer directly. [Learn how to choose an effort level in Cowork and Chat(opens in new tab)](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat) or [in Claude Code(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code).

## Tracing context[](#tracing-context)

Take this example reply from Claude in Cowork. Each highlighted section was influenced by some of the prepended context. Click a section and identify where you think it came from.

## What you can do now[](#what-you-can-do-now)

* You can name the difference between what's **in the weights** (parametric memory) and what's **in the window** (context).
* You know the window has a ceiling, and that you're not the only author filling it.
* You know that every turn re-sends the whole window, and you can be intentional about when to start a new session.
* You understand that compaction is a summarization technique that can make the window feel infinite, but may drop details.
* You can explain how written memory survives between sessions.
* You can look at a Claude reply and make some guesses about how the prepended context may have shaped it.

*Next: [choose an effort level in Cowork and Chat(opens in new tab)](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat) · [in Claude Code(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code)*

*Learn more: [AI Fluency(opens in new tab)](https://academy.claude.com/collections/ai-fluency) · [AI capabilities and limitations(opens in new tab)](https://academy.claude.com/courses/ai-capabilities-and-limitations)*

* [Where answers come from](#where-answers-come-from)
* [Parametric memory](#parametric-memory)
* [Where parametric memory runs out](#where-parametric-memory-runs-out)
* [Adding context](#adding-context)
* [The context window](#the-context-window)
* [Filling the window](#filling-the-window)
* [Compaction](#compaction)
* [Try it: compaction](#try-it-compaction)
* [Written memory](#written-memory)
* [A week of memory](#a-week-of-memory)
* [Prepended context](#prepended-context)
* [Agentic context](#agentic-context)
* [Tracing context](#tracing-context)
* [What you can do now](#what-you-can-do-now)
