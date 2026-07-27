<!-- source: https://platform.claude.com/cookbook/misc-prompt-caching -->

# Prompt caching with the Claude API

Prompt caching lets you store and reuse context within your prompts, reducing latency by >2x and costs by up to 90% for repetitive tasks.

There are two ways to enable prompt caching:

* **Automatic caching** (recommended): Add a single `cache_control` field at the top level of your request. The system automatically manages cache breakpoints for you.
* **Explicit cache breakpoints**: Place `cache_control` on individual content blocks for fine-grained control over exactly what gets cached.

This cookbook demonstrates both approaches, starting with the simpler automatic method.

## Setup

python

```
%pip install --upgrade 'anthropic>=0.83.0' bs4 requests python-dotenv --quiet
```

```
Note: you may need to restart the kernel to use updated packages.
```

python

```
import time

import anthropic
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic()
MODEL_NAME = "claude-sonnet-4-6"

# Unique prefix to ensure we don't hit a stale cache from a previous run
TIMESTAMP = int(time.time())
```

Let's fetch the full text of *Pride and Prejudice* (~187k tokens) to use as our large context.

python

```
def fetch_article_content(url):
    response = requests.get(url, timeout=30)
    soup = BeautifulSoup(response.content, "html.parser")

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = "\n".join(chunk for chunk in chunks if chunk)

    return text

book_url = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
book_content = fetch_article_content(book_url)

print(f"Fetched {len(book_content)} characters from the book.")
print("First 500 characters:")
print(book_content[:500])
```

```
Fetched 737526 characters from the book.
First 500 characters:
The Project Gutenberg eBook of Pride and Prejudice
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.
Title:
```

We'll also define a small helper to print usage stats:

python

```
def print_usage(response, elapsed):
    """Print token usage and timing for an API response."""
    usage = response.usage
    cache_create = getattr(usage, "cache_creation_input_tokens", 0)
    cache_read = getattr(usage, "cache_read_input_tokens", 0)

    print(f"  Time:                {elapsed:.2f}s")
    print(f"  Input tokens:        {usage.input_tokens}")
    print(f"  Output tokens:       {usage.output_tokens}")
    if cache_create:
        print(f"  Cache write tokens:  {cache_create}")
    if cache_read:
        print(f"  Cache read tokens:   {cache_read}")
```

---

## Example 1: Automatic caching (single turn)

Automatic caching is the easiest way to get started. Add `cache_control={"type": "ephemeral"}` at the **top level** of your `messages.create()` call and the system handles the rest — automatically placing the cache breakpoint on the last cacheable block.

We'll compare three scenarios:

1. **No caching** — baseline
2. **First cached call** — creates the cache entry (similar timing to baseline)
3. **Second cached call** — reads from cache (the big speedup)

### Baseline: no caching

python

```
start = time.time()
baseline_response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=300,
    messages=[
        {
            "role": "user",
            "content": str(TIMESTAMP)
            + "<book>"
            + book_content
            + "</book>"
            + "\n\nWhat is the title of this book? Only output the title.",
        }
    ],
)
baseline_time = time.time() - start

print(f"Response: {baseline_response.content[0].text}")
print_usage(baseline_response, baseline_time)
```

```
Response: Pride and Prejudice
  Time:                4.89s
  Input tokens:        187364
  Output tokens:       8
```

### First call with automatic caching (cache write)

The only change is the top-level `cache_control` parameter. The first call writes to the cache, so timing is similar to the baseline.

python

```
start = time.time()
write_response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=300,
    cache_control={"type": "ephemeral"},  # <-- one-line change
    messages=[
        {
            "role": "user",
            "content": str(TIMESTAMP)
            + "<book>"
            + book_content
            + "</book>"
            + "\n\nWhat is the title of this book? Only output the title.",
        }
    ],
)
write_time = time.time() - start

print(f"Response: {write_response.content[0].text}")
print_usage(write_response, write_time)
```

```
Response: Pride and Prejudice
  Time:                4.28s
  Input tokens:        3
  Output tokens:       8
  Cache write tokens:  187361
```

### Second call with automatic caching (cache hit)

Same request again. This time the cached prefix is reused, so you should see a significant speedup.

python

```
start = time.time()
hit_response = client.messages.create(
    model=MODEL_NAME,
    max_tokens=300,
    cache_control={"type": "ephemeral"},
    messages=[
        {
            "role": "user",
            "content": str(TIMESTAMP)
            + "<book>"
            + book_content
            + "</book>"
            + "\n\nWhat is the title of this book? Only output the title.",
        }
    ],
)
hit_time = time.time() - start

print(f"Response: {hit_response.content[0].text}")
print_usage(hit_response, hit_time)

print("\n" + "=" * 50)
print("COMPARISON")
print("=" * 50)
print(f"No caching:     {baseline_time:.2f}s")
print(f"Cache write:    {write_time:.2f}s")
print(f"Cache hit:      {hit_time:.2f}s")
print(f"Speedup:        {baseline_time / hit_time:.1f}x")
```

```
Response: Pride and Prejudice
  Time:                1.48s
  Input tokens:        3
  Output tokens:       8
  Cache read tokens:   187361

==================================================
COMPARISON
==================================================
No caching:     4.89s
Cache write:    4.28s
Cache hit:      1.48s
Speedup:        3.3x
```

---

## Example 2: Automatic caching in a multi-turn conversation

Automatic caching really shines in multi-turn conversations. The cache breakpoint **automatically moves forward** as the conversation grows — you don't need to manage any markers yourself.

| Request | Cache behavior |
| --- | --- |
| Request 1 | System + User:A cached (write) |
| Request 2 | System + User:A read from cache; Asst:B + User:C written to cache |
| Request 3 | System through User:C read from cache; Asst:D + User:E written to cache |

python

```
system_message = f"{TIMESTAMP} <file_contents> {book_content} </file_contents>"

questions = [
    "What is the title of this novel?",
    "Who are Mr. and Mrs. Bennet?",
    "What is Netherfield Park?",
    "What is the main theme of this novel?",
]

conversation = []

for i, question in enumerate(questions, 1):
    print(f"\n{'=' * 50}")
    print(f"Turn {i}: {question}")
    print("=" * 50)

    conversation.append({"role": "user", "content": question})

    start = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=300,
        cache_control={"type": "ephemeral"},  # automatic caching
        system=system_message,
        messages=conversation,
    )
    elapsed = time.time() - start

    assistant_reply = response.content[0].text
    conversation.append({"role": "assistant", "content": assistant_reply})

    print(f"\nAssistant: {assistant_reply[:200]}{'...' if len(assistant_reply) > 200 else ''}")
    print()
    print_usage(response, elapsed)
```

```
==================================================
Turn 1: What is the title of this novel?
==================================================

Assistant: The title of this novel is **Pride and Prejudice**, written by **Jane Austen**.

  Time:                5.19s
  Input tokens:        3
  Output tokens:       24
  Cache write tokens:  187361

==================================================
Turn 2: Who are Mr. and Mrs. Bennet?
==================================================

Assistant: Mr. and Mrs. Bennet are a married couple who are central characters in the novel. They live at **Longbourn** and are the parents of **five daughters**: Jane, Elizabeth, Mary, Catherine (Kitty), and Ly...

  Time:                8.27s
  Input tokens:        3
  Output tokens:       272
  Cache write tokens:  38
  Cache read tokens:   187361

==================================================
Turn 3: What is Netherfield Park?
==================================================

Assistant: **Netherfield Park** is a large estate located near the village of **Longbourn** in Hertfordshire, where the Bennet family lives. It plays an important role in the novel as it is the home that is let ...

  Time:                8.74s
  Input tokens:        3
  Output tokens:       300
  Cache write tokens:  283
  Cache read tokens:   187399

==================================================
Turn 4: What is the main theme of this novel?
==================================================

Assistant: **Pride and Prejudice** explores several important themes throughout the novel. Here are the main ones:

**1. Pride and Prejudice**
- The most obvious theme is reflected in the title itself. Mr. Darcy...

  Time:                7.06s
  Input tokens:        3
  Output tokens:       300
  Cache write tokens:  315
  Cache read tokens:   187682
```

After the first turn, nearly 100% of input tokens are read from cache on every subsequent turn. The conversation code is just a plain list of messages — no special `cache_control` markers needed on individual blocks.

---

## Example 3: Explicit cache breakpoints

For more control, you can place `cache_control` directly on individual content blocks. This is useful when:

* You want to cache different sections with different TTLs
* You need to cache a system prompt independently from message content
* You want fine-grained control over what gets cached

You can also combine both approaches: use explicit breakpoints for your system prompt while automatic caching handles the conversation.

Below, we place `cache_control` directly on the book content block and manually move the breakpoint forward on each turn.

python

```
class ConversationWithExplicitCaching:
    """Multi-turn conversation that manually places cache_control on the last user message."""

    def __init__(self):
        self.turns = []

    def add_user(self, content):
        self.turns.append({"role": "user", "content": [{"type": "text", "text": content}]})

    def add_assistant(self, content):
        self.turns.append({"role": "assistant", "content": [{"type": "text", "text": content}]})

    def get_messages(self):
        """Return messages with cache_control on the last user message."""
        result = []
        last_user_idx = max(i for i, t in enumerate(self.turns) if t["role"] == "user")

        for i, turn in enumerate(self.turns):
            if i == last_user_idx:
                result.append(
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": turn["content"][0]["text"],
                                "cache_control": {"type": "ephemeral"},
                            }
                        ],
                    }
                )
            else:
                result.append(turn)

        return result

conv = ConversationWithExplicitCaching()

for i, question in enumerate(questions, 1):
    print(f"\n{'=' * 50}")
    print(f"Turn {i}: {question}")
    print("=" * 50)

    conv.add_user(question)

    start = time.time()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=300,
        system=[
            {
                "type": "text",
                "text": system_message,
                "cache_control": {"type": "ephemeral"},  # explicit breakpoint on system
            },
        ],
        messages=conv.get_messages(),
    )
    elapsed = time.time() - start

    assistant_reply = response.content[0].text
    conv.add_assistant(assistant_reply)

    print(f"\nAssistant: {assistant_reply[:200]}{'...' if len(assistant_reply) > 200 else ''}")
    print()
    print_usage(response, elapsed)
```

```
==================================================
Turn 1: What is the title of this novel?
==================================================

Assistant: The title of this novel is **Pride and Prejudice**, written by **Jane Austen**.

  Time:                4.53s
  Input tokens:        3
  Output tokens:       24
  Cache read tokens:   187361

==================================================
Turn 2: Who are Mr. and Mrs. Bennet?
==================================================

Assistant: Mr. and Mrs. Bennet are a married couple who are central characters in the novel. They live at **Longbourn** and are the parents of **five daughters**: Jane, Elizabeth (Lizzy), Mary, Catherine (Kitty)...

  Time:                7.57s
  Input tokens:        3
  Output tokens:       283
  Cache read tokens:   187399

==================================================
Turn 3: What is Netherfield Park?
==================================================

Assistant: **Netherfield Park** is a large estate located near the village of **Longbourn** in Hertfordshire, where the Bennet family lives. It plays an important role in the novel as it is the residence that se...

  Time:                6.85s
  Input tokens:        3
  Output tokens:       300
  Cache write tokens:  294
  Cache read tokens:   187399

==================================================
Turn 4: What is the main theme of this novel?
==================================================

Assistant: **Pride and Prejudice** explores several interconnected themes throughout the novel. Here are the main ones:

**1. Pride and Prejudice**
The most central theme is reflected in the title itself. Both M...

  Time:                7.00s
  Input tokens:        3
  Output tokens:       300
  Cache write tokens:  315
  Cache read tokens:   187693
```

---

## Choosing an approach

|  | Automatic caching | Explicit breakpoints |
| --- | --- | --- |
| **Ease of use** | One-line change | Must place and move `cache_control` markers |
| **Multi-turn** | Breakpoint moves forward automatically | You manage breakpoint placement |
| **Fine-grained control** | No | Up to 4 independent breakpoints |
| **Mixed TTLs** | Single TTL for auto breakpoint | Different TTLs per breakpoint |
| **Combinable** | Yes — automatic + explicit together | Yes |

**Start with automatic caching.** It covers the majority of use cases with minimal effort. Switch to explicit breakpoints only when you need fine-grained control.

### Key details

* **Minimum cacheable length:** 1,024 tokens for Sonnet; 4,096 tokens for Opus and Haiku 4.5
* **Cache TTL:** 5 minutes by default (refreshed on each hit). A 1-hour TTL is available at 2x base input price.
* **Pricing:** Cache writes cost 1.25x base input price. Cache reads cost 0.1x base input price.
* **Breakpoint limit:** Up to 4 explicit breakpoints per request. Automatic caching uses one slot.

For full details, see the [prompt caching documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching).
