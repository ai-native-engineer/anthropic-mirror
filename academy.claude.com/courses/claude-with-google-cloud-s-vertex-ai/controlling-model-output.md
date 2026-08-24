<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/controlling-model-output -->

Lesson 8 of 66 · Claude with Google Cloud's Vertex AIControlling model output

Beyond crafting better prompts, there are two powerful techniques for controlling Claude's output: prefilled assistant messages and stop sequences. These methods give you precise control over how Claude responds and when it stops generating text.

## Prefilled Assistant Messages

Message prefilling lets you provide the beginning of Claude's response, which it will then continue from that starting point. This technique is incredibly useful for steering Claude in a specific direction.

![](https://academy.claude.com/assets/media/b47e17ea1c9fa46a70afa394bf22292a79c2515207ee897ed00128d3d7d15fe6.png)

Here's how it works: instead of just sending a user message, you add an assistant message at the end of your message list. Claude sees this assistant message and thinks "I've already started responding to this question, so I should continue from where I left off."

![](https://academy.claude.com/assets/media/8a4248de3e8305a4bca8937642f8c00488361560278ea032e73166022c29162b.png)

For example, if you ask "Is tea or coffee better at breakfast?" without prefilling, Claude typically gives a balanced response mentioning both options. But if you add an assistant message saying "Coffee is better because", Claude will continue from there and build a case for coffee.

The key thing to understand is that Claude continues from exactly where your prefilled text ends. If you write "Coffee is better because", Claude won't repeat that text - it will pick up right after "because" and complete the thought.

Here's the code structure:

python

```
messages = []
add_user_message(messages, "Is tea or coffee better at breakfast?")
add_assistant_message(messages, "Coffee is better because")
answer = chat(messages)
```

You can steer Claude in any direction using this technique:

* Favor coffee: "Coffee is better because"
* Favor tea: "Tea is better because"
* Take a contrarian stance: "Neither is very good because"

## Stop Sequences

Stop sequences force Claude to end its response as soon as it generates a specific string of characters. This is perfect for controlling the length or endpoint of responses.

![](https://academy.claude.com/assets/media/10b88f1b5ccafd4b163e3d1173472b868c2b1d1b7b0f809c9484807522fdf454.png)

The concept is straightforward: you provide a list of strings, and when Claude generates any of those strings, it immediately stops and returns whatever it has generated up to that point.

For example, if you ask Claude to "Count from 1 to 10" with a stop sequence of "5", you'll get:

python

```
add_user_message(messages, "Count from 1 to 10")
answer = chat(messages, stop_sequences=["5"])
```

This returns: "1, 2, 3, 4, " - stopping right before the "5" is included in the output.

You can be more precise with your stop sequences. If you want to avoid the trailing comma and space, use `stop_sequences=[", 5"]` instead. This will give you a cleaner result: "1, 2, 3, 4".

Stop sequences are particularly useful for:

* Limiting list lengths
* Stopping at specific markers or delimiters
* Creating consistent output formats
* Preventing overly long responses

Both techniques give you fine-grained control over Claude's behavior, allowing you to create more predictable and targeted responses for your applications.
