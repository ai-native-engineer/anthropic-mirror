---
title: "Behind the prompt: Prompting tips for Claude.ai"
channel: anthropic-ai
url: https://www.youtube.com/watch?v=OfUn6HjwXhI
youtube_id: OfUn6HjwXhI
published: 2023-08-25
duration: "3:36"
---

# Behind the prompt: Prompting tips for Claude.ai

[![Behind the prompt: Prompting tips for Claude.ai](https://img.youtube.com/vi/OfUn6HjwXhI/hqdefault.jpg)](https://www.youtube.com/watch?v=OfUn6HjwXhI)

<details>
<summary>자막: Behind the prompt: Prompting tips for Claude.ai (3:36)</summary>

[00:00]
[Music]
foreign
I'm Alex, I'm a prompt
engineer at Anthropic. I help people get
the most out of Claude with safety at
the top of mind. I first got into
prompt engineering back in last
August. Anthropic released their paper,
"Red Teaming Language Models to Reduce
Harms" and immediately I read it and it
was hooked.
I was inspired to see that a company was
taking a safety first approach to
researching language models, and I
thought it was really interesting how
you could see the ways that models would
output to different and diverse ranges
of prompts.
You may be familiar with red teaming
attacks as prompt exploits or the more
Infamous name "jailbreaks". I decided to
start writing jailbreaks after reading
the paper and becoming inspired by the
opportunities that still existed to red
team these models. Jailbreaks are
specific prompts that are written to
circumvent the filters that have been
applied on top of language models. Prompt
engineering is the practice of

[00:01]
optimizing your prompt in order to get
the best response from the language
model. At anthropic we like to take an
empirical test driven approach to prompt
engineering. Whenever we write a new
prompt we run it against a series of
benchmarks in order to scientifically
measure its performance. With Claude
we've discovered a set of best practices
that'll allow you to get the most out of
the model.
So, let's get into it here are my five
tips for getting the best performance
from Claude.
First, describe your task. Claude responds
well to clear direct and specific
instructions.
Let's say you wanted Claude to remove
personal identifiable information from a
piece of text.
Explaining the quad exactly what that
means helps Claude recognize what pieces
of text to remove.
For example email addresses and phone
numbers. Second, mark different parts of
your prompt with XML tags XML tags look
like this.
Claude has been fine-tuned to pay

[00:02]
special attention to their structure.
In our example we use XML tags to
indicate the beginning and end of text
that claw needs to de-identify.
Third, give examples. The more examples,
the better.
Including a wide range of examples helps
Claude learn how to do the task.
Back to our PII prompt,
we provide cod with examples of how to
de-identify text within XML tags.
Fourth, make use of the long context.
Claude can read up to a hundred-thousand
tokens. That's roughly 70 000 words or
the length of the entire Great Gatsby.
And finally, the last tip is to let
Claude think.
Researchers have discovered that giving
language models some time to think
through their response before producing
their final answer leads to better
performance.
With Claude, we like to use thinking tags
so that it can jot down its ideas before
answering a complex question.
Here in this example you can see Claude

[00:03]
starts to reason within thinking tags
and then outputs its final answer.
Alright, so those are my top tips for
getting the most out of Claude and a
little bit about me and my own prompting
Journey. To stay up to date on the latest
prompting best practices, make sure to go
check out our developer docs site. And if
you haven't got access to the Claude API
yet, you can still practice your prompt
engineering right now at claude.ai
[Music]

</details>
