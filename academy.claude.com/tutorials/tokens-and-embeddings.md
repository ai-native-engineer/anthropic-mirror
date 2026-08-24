<!-- source: https://academy.claude.com/tutorials/tokens-and-embeddings -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Tokens: why some inputs cost more than others

Claude usage is measured in tokens. Whether you're monitoring a usage bill or wondering when a rate limit will kick in, tokens are the unit of measurement. Learn what a token is, predict how many a piece of text will use, and see how tokens encode meaning.

15 min

![](https://academy.claude.com/assets/v1/thumbnail.light-o6cqv60g.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-dzby7rgv.png)

You may remember a time when most LLMs couldn't tell you how many r's are in "strawberry." But why does that happen? The answer explains a surprising amount about what language models are good at, what they find hard, and how they use math to produce text. It also explains how your usage is calculated, which impacts how quickly you'll hit a rate limit or what your API bill might look like.

Let's start with some role reversal.

*This is a warm-up question, so just take your best guess.*

Quick check

If you type "Hello Claude" and hit send, what do you imagine arrives at the model?

The word "Hello" and the word "Claude"A list of letters: H, e, l, l, o, , C, l, a, u, d, eA list of numbersA tiny picture of each word

## Three ways to represent text

Think about this three-character string: `"Hi!"`. Now think about three different ways we could pass that information to a language model.

1. **The exact way you see it.** A *string*: `"Hi!"`.
2. **As a list of characters.** `['H', 'i', '!']`. The brackets `[` `]` mean *list*; this particular list has three items in it.
3. **As one number per character.** Every character could correspond to a standard number: `'H'` is `72`, `'i'` is `105`, `'!'` is `33`.

```
string:      "Hi!"
characters:  [ 'H', 'i', '!' ]
numbers:     [ 72,  105, 33  ]
```

While all three approaches have their uses in code, language models do a fourth, more strategic thing. What arrives is still a list of numbers, but not one number per character from a fixed table: it's one number per **chunk** of text, from a vocabulary the model learned.

A chunk of text with its numerical ID is called a *token*.

## Tokens

The widget below includes several pieces of text that you can **tokenize**. Click through the examples, tokenize each one, and see for yourself: how is a token different from a word?

The splits and ID numbers in these examples come from an illustrative tokenizer, not Claude's. Claude's tokenizer might break words up differently and use different IDs, but the patterns are roughly the same.

## Over or under?

Now that you know what tokens look like, see if you can predict how many tokens will be produced by tokenizing the following strings.

## Why subwords?

You might be wondering: why not just one token per character, or one per word?

The set of unique token IDs a tokenizer can produce is called its **vocabulary**. Deciding the just-right token size and vocabulary size is still a matter of some exploration and research, but most public tokenizers aim for a Goldilocks zone. Take a look at the sentence *"The tokenizer rocks."* chopped up three different ways by three different tokenizers.

With **tiny tokens** (one per character) the sentence costs 20 tokens. That's going to be slow and expensive to process!

```
[T] [h] [e] [ ] [t] [o] [k] [e] [n] [i] [z] [e] [r] [ ] [r] [o] [c] [k] [s] [.]
```

With **large tokens** (one per word) the sentence only costs 4 tokens, but the model is going to have to learn a *huge* vocabulary to know niche words like "tokenizer":

```
[The] [ tokenizer???] [ rocks] [.]
```

With a **middle ground** (one token per word or subword) the sentence costs 5 tokens, without the vocabulary having to include as many specialized words:

```
[The] [ token] [izer] [ rocks] [.]
```

A tokenizer's vocabulary is *baked into the model*, and cannot be changed after it is trained. Any specific model is said to be "locked to a tokenizer" because it only ever learned what `token 4062` means, not what `"quick"` means.

Bonus readingByte-pair encoding

Vocabularies like this are usually *grown* rather than hand-picked. The most common process is an algorithm called **byte-pair encoding** (BPE). It starts with the smallest possible token (individual bytes) so that every possible character (and every emoji fragment) is already covered. Then it scans an enormous pile of text for the pair of adjacent pieces that appears most often, glues that pair into a new single piece, and adds it to the vocabulary. It repeats this until the vocabulary reaches the researcher's target size. Common words emerge early on and end up as single tokens; rarer words seldom do.

Want to dive deeper into BPE? Ask Claude to build you a visualization:

I'm learning how tokenizers work, and I understand that text becomes tokens with numerical IDs. Teach me byte-pair encoding by building an interactive visualization. First, show me how the merge table is built: start from a few sentences and let me step through the merges one at a time, so I can watch common words become single tokens. Then, once I understand that, show me how the finished merge table is applied to new text, including how the tokenizer handles a word it has never seen.

Open in Claude

## Decoding output

So now you know that the text you send to a model becomes a list of token IDs before it's processed. A model's **output** is *also* a list of token IDs. Try decoding this reply.

## From tokens to meaning

Tokenization gives every chunk of text a number, but tokens with similar IDs like `9906` and `9907` aren't *related* - they're just neighbors in a list. A model needs a way to know that *cat* and *kitten* are close in meaning, even if their IDs are far apart in the vocabulary. Models do this by assigning each token a *multi-dimensional score*.

Let's start with a 2D scoring system.

## Embeddings

An LLM embedding works the same way as the scoring you just did. Each word (or really, each token) becomes a point, and similar words (tokens) land near each other. Real embeddings are more complicated in two ways:

1. **An LLM embedding has thousands of dimensions**, not just two. You can imagine we could also include an axis for "dangerous" that might help us separate our tiger from our kitten.
2. **The meaning captured in a single dimension isn't labeled**, and may actually mean something there isn't even a great human word for. Cuteness is in there *somewhere*, but there's no axis explicitly named "cuteness" - the model invents or discovers the dimensions during training, and the process of decoding what they mean is one focus of **interpretability** research.

**Examine "cat" in 2, 3, and thousands of dimensions**

```
2 dimensions       "cat" = [ 8.0,  3.5 ]                                cute, big
3 dimensions       "cat" = [ 8.0,  3.5,  1.0 ]                          cute, big, dangerous
4,096 dimensions   "cat" = [ 0.031, -0.184, 0.772, …, -0.094 ]          (no labels)

The exact number of dimensions varies by model. 4,096 is a common size in open-weight models.
```

Want to explore embeddings further? Ask Claude to build you a visualization:

I'm learning about embeddings. I understand that a token becomes a point in a space with many dimensions, that similar tokens land near each other, and that the dimensions aren't labeled with human words. Help me build intuition by making an interactive visualization: place a couple of dozen everyday words in a small embedding space, let me pick any word and see its nearest neighbours, and let me add a word of my own to see where it lands and why.

Open in Claude

## Recap

So now you know that the text you send to an LLM becomes a series of tokens, and tokens become embeddings.

```
text:        "Hi"
token:       [ 13347 ]
embedding:   [ 0.12, -0.48, 0.91, …, 0.07 ]
```

Congratulations! This is a huge step towards understanding how a language model works.

You may already be intuiting that the information captured in embeddings (how cute and big and *everything* things are) plays a huge part in how a language model makes sense of its inputs and picks the right outputs. If so, your intuition is correct!

If these four statements feel true, you've got what this lesson set out to teach.

* You can explain why a 100-character URL costs more tokens than a 100-character sentence.
* You can predict roughly how many tokens a chunk of text will be.
* You know why a model is locked to its tokenizer, and why rarer words are chopped into pieces.
* You can explain what an embedding is and why it matters using the words "score," "dimension," and "nearby."

*Next: [How context affects Claude's performance and cost(opens in new tab)](https://academy.claude.com/tutorials/parametric-memory-and-context) · [Choosing the right Claude model(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-claude-model) · [choose an effort level in Cowork and Chat(opens in new tab)](https://academy.claude.com/tutorials/how-to-select-the-right-effort-setting-for-claude-cowork-and-chat) · [in Claude Code(opens in new tab)](https://academy.claude.com/tutorials/choosing-the-right-effort-level-in-claude-code)*

*Learn more: [AI Fluency(opens in new tab)](https://academy.claude.com/collections/ai-fluency) · [AI capabilities and limitations(opens in new tab)](https://academy.claude.com/courses/ai-capabilities-and-limitations)*

* [Three ways to represent text](#three-ways-to-represent-text)
* [Tokens](#tokens)
* [Over or under?](#over-or-under)
* [Why subwords?](#why-subwords)
* [Decoding output](#decoding-output)
* [From tokens to meaning](#from-tokens-to-meaning)
* [Embeddings](#embeddings)
* [Recap](#recap)
