<!-- https://anthropic-partners.skilljar.com/partner-basecamp/465960 -->
<!-- scorm-content: https://anthropic-partners.skilljar.com/content/wp/4hdejjwplbrm/1fdmajcvhh1gs/module-02-foundation-models.html -->

# Understanding Foundation Models

Module 2 of 6

# Foundation *Models*

Walking backward through a model, from output token to input encoding. Every client question about Claude's behavior traces to one of four layers.

Partner Basecamp
~25 min
SET A - DAY 1 PREP
4 interactive widgets

What You'll Walk Away With

## Three things you can do after this module

Not just know. Do. Each objective below maps to a real client conversation.

Trace any client question about Claude's behavior to the layer that caused it, in real time, in a meeting.

Explain hallucination accurately, without handwaving: what is actually happening in the model's weights, and why adjusting temperature doesn't fix it.

Use the right vocabulary when a technical buyer pushes on performance, cost, or context: TTFT, tokens/sec, tokenizer efficiency.

The Structure

## Four layers, one question

When a client hits Enter, what happens? That question has four answers, one per layer. This module works backward because starting at the output makes each deeper layer feel like an excavation rather than a lecture.

01

Sampling

How Claude picks each next token

02

Parametric Memory

How Claude 'knows' what it seems to know

03

Attention

How connections between words are mapped

04

Tokenization

How text becomes usable model input

Layer 1 · Sampling

## How Claude picks every word

Claude doesn't retrieve answers. Every response begins as a probability distribution over every possible next token — and then a selection is made from that distribution. Temperature reshapes the curve. Top-k and Top-p trim the tail. Use the widget below to see all three in action.

What to do

Select a prompt tab to change the context. Drag **Temperature** up and down to watch the distribution flatten or sharpen. Then try the **Tail trimming** options to see how Top-k and Top-p constrain the pool. When you're ready, hit **Sample a token** to draw one at random from the surviving distribution.

What you'll see

The bars show the probability of each candidate next token. **Strikethrough tokens** have been eliminated by your tail trim and cannot be selected. The percentage next to each bar updates in real time. Sampled results appear at the bottom — run it multiple times to see variation.

Capital of FranceBest languageFemale vocalistMeaning of lifedef fibonacci(

The capital of France is \_\_\_

Probability distribution

Paris85.0%

Lyon3.0%

a2.5%

the2.0%

one1.5%

not1.0%

well0.8%

arguably0.7%

known0.6%

located0.5%

considered0.4%

called0.3%

+ 3 more tokens

Temperature
1.00

focused
random

Default (1.0) — probabilities exactly as the model learned them.

⚠ The Anthropic API caps temperature at 1.0. This range is shown for educational purposes only.

Tail trimming

None
Top-k
Top-p

Sample a token →

Adjust the distribution, then hit "Sample a token" to draw one →

Reset



**Key insight**

Temperature, Top-k, and Top-p don't change what the model *knows* — only which possibility gets selected. When a client asks you to "make it more accurate," these parameters are not the answer. Accuracy problems live in the training data and the weights, not the sampling settings.

Layer 2 . Parametric Memory

## Where does that confidence come from?

The sampling distribution for 'best-selling female vocalist' is peaked. The model is confident. But it didn't look that up. No database query, no API call. That confidence was baked in during training. The model processed billions of documents that mentioned that artist in that context, and the weights reflect it.

Everything Claude knows lives in its parameters. About any given fact, the model is in one of three states. Click each to see the implications.

Confident and correct

▼

A fact with dense training signal. 'Who wrote Hamlet?' The weights point clearly to Shakespeare. Peaked distribution, correct answer. This is the easy case.

Confident and wrong

▼

A fact that changed after the training cutoff, or a pattern the model learned incorrectly. The model produces a peaked distribution toward a wrong answer. This is the dangerous case. The model isn't lying. It's reporting what its weights say. Temperature=0 makes this worse, not better.

Uncertain and honest

▼

A genuinely obscure question where training data was sparse. The model hedges: 'I'm not certain, but...' This is actually the best behavior. Claude is trained to recognize when its knowledge signal is weak and communicate that uncertainty rather than confabulate.

Anthropic Differentiator

## Claude knows what it doesn't know

Anthropic invests heavily in the third state: uncertain and honest. The product-level result is that Claude is trained to recognize its knowledge boundaries and to act on them. Not just acknowledge them.

When Claude is configured with web search capabilities and encounters a question past its training cutoff, it can recognize the gap and use a web search tool to return current information. Note: availability depends on your deployment setup. Most models either hallucinate an answer or give a generic 'I don't have information past my training cutoff' response. Claude does something more specific: detects the gap, uses the tool, surfaces the real answer.

**Try this in Claude right now:**  
"What won best picture at the 2026 Oscars?"  
  
Claude doesn't guess. It searches. You'll see it acknowledge the gap, trigger a search, and return the actual result.

**For clients evaluating AI platforms:** This is architecture, not marketing. Claude's self-awareness about knowledge boundaries is demonstrable in a meeting. Use it.

Layer 3 . Attention

## How context gets connected

When the model generates each word, which other words in the prompt actually matter? Before transformers, the answer was: only the last three or four. Attention changes this fundamentally.

Without Attention (Markov, n=3)

A Markov model with a window of 3 sees only the last three words. For the sentence 'Who is the best-selling female vocalist of all time?' the model generating 'time' sees only 'all' 'of' and nothing before that. The subject of the sentence is invisible. This is why Markov-generated text falls apart after a few words: the model loses the thread because it literally cannot see it.

With Attention (Transformer)

Every prior word gets a weight, a measure of how relevant it is to the current word being processed. The strongest connections are the semantically meaningful ones, regardless of distance. A word 40 tokens back can have a stronger attention signal than the word immediately before, if it carries more semantic relevance.

**Why does Claude lose track in long prompts?** Attention dilution at distance. The signal from early content gets weaker as context grows.

**Why is Claude's 200k context window meaningful?** More tokens for the attention mechanism to span. And more that can stay in view.

Layer 3 . Interactive

## Attention in action

The sentence below is processed by the attention mechanism. Click any token to see which earlier tokens it attends to most strongly. Start with 'it' and the result will explain a lot.

The
cat
sat
on
the
mat
because
it
was
tired

Layer 3 . Mechanics

## The forward pass

Every token runs through the same pipeline: Embedding and Position, then Self-Attention, then Feed-Forward layers where the parametric knowledge lives, then Output Logits. The probability distribution you saw in Layer 1. But this pipeline runs in two very different modes: Input Processing (Prefill) and Output Generation (Decode).

Input Processing (Prefill)
Output Generation (Decode)

**ALL INPUT TOKENS IN PARALLEL**

All input tokens run through every layer in parallel. The result, the model's full understanding of your prompt, is stored in the KV cache (Key-Value cache), a record of what it computed for each input token. A snapshot.

**TTFT (time-to-first-token)**

The pause before Claude starts typing. Long system prompts and large documents in context all run in prefill, which is why TTFT grows with context length.

**Product insight:** Prompt caching persists the KV cache between API calls. If your client sends the same system prompt on every request, which most applications do, prompt caching skips prefill entirely for that content. Faster TTFT, lower cost. Worth including in proposals.

Layer 4 . Tokenization

## Text becomes numbers

Before any of the above can happen, text has to become something the model can process. Not words, not characters. Tokens, discrete numerical IDs. Common English words are typically single tokens. The tabs below show what happens with other languages and specific number strings.

Select a language or number string to see how it tokenizes differently.

English
Japanese
Number: 1847
Number: 1848

ORIGINAL TEXT

Who is the best-selling female vocalist of all time?

TOKENIZED

Who
is
the
best
sell
ing
female
voc
alist
of
all
time
?

14 tokens, 51 chars, 0.27 tokens/char

How the vocabulary was built

Byte Pair Encoding (BPE) is a compression algorithm that builds a vocabulary by repeatedly finding the most common adjacent characters and combining them. This is why common English words become single tokens, but rare languages require multiple tokens for the same concept.

The tokenizer learns vocabulary bottom-up using Byte Pair Encoding. Start with individual characters. Find the most frequent adjacent pair. Merge. Repeat.

l

o

w

e

s

t

Start: every character is its own token

Click **Next** to step through each merge — and **Prev** to go back.

Prev

Step 0 of 5

Next

**Key insight:** The vocabulary is fixed after training. Non-English languages had fewer training examples, so fewer merges happened for their character sequences. That is the root cause of the multilingual cost difference.

Knowledge Check

## Two real situations

These are conversations you will have in client engagements. Reason through each before reading the answer.

Scenario 1 . Temperature

A client is building a legal document review system. They set temperature to zero expecting perfectly deterministic outputs. But they're still seeing slightly different responses to the same prompt. What's the most likely explanation, and what do you recommend?

Think it through...

Reveal answer

**Root cause:** Floating-point non-determinism in distributed inference. Temperature=0 is near-deterministic, not perfectly deterministic. Multiple GPUs calculate slightly differently and these small differences compound.  
  
**Recommendation:** Design the system to be robust to slight variation rather than relying on exact reproduction. For use cases requiring strict determinism, explore Anthropic's determinism features and discuss whether the downstream review process can tolerate minor variation.

Scenario 2 . Multilingual Cost

A client budgeted their API costs based on an English prototype. After launching in Japanese, Korean, and Arabic, costs are 2 to 3 times higher despite the same conversation length in characters. Why is this happening, and how would you advise them?

Think it through...

Reveal answer

**Root cause:** BPE tokenizer efficiency. Same semantic content, but more tokens per unit in non-English languages. Fewer merges happened for those character sequences during training vocabulary construction. The context window and billing are both token-based, not character-based.  
  
**Recommendation:** Run tokenizer analysis per target language before deployment. Re-budget based on token counts, not character counts. Anthropic's tokenizer tools can estimate this before the client commits to a multilingual rollout.

Module 2 of 6 Complete

## Sampling. Memory. Attention. Tokens. *That's the complete explanation.*

You now have the framework:  
**3 shifts** that explain why the window is open  
**3 pillars** that categorize any client problem  
**3 levers** that define the technical architecture  
  
Every session for the rest of the Basecamp builds on this foundation.

Next up: Module 3

Models & Capabilities

You'll apply this framework to the Claude model family. When to use Haiku, Sonnet, and Opus — and what breaks when you switch.

Mark module as complete

Begin
