<!-- source: https://platform.claude.com/cookbook/extended-thinking-extended-thinking -->

#  Extended Thinking

##  Table of contents

* [Setup](#setup)
* [Basic example](#basic-example)
* [Streaming with extended thinking](#streaming-with-extended-thinking)
* [Token counting and context window management](#token-counting-and-context-window-management)
* [Understanding redacted thinking](#understanding-redacted-thinking-blocks)
* [Handling error cases](#handling-error-cases)

This notebook demonstrates how to use Claude 3.7 Sonnet's extended thinking feature with various examples and edge cases.

Extended thinking gives Claude 3.7 Sonnet enhanced reasoning capabilities for complex tasks, while also providing transparency into its step-by-step thought process before it delivers its final answer. When extended thinking is turned on, Claude creates `thinking` content blocks where it outputs its internal reasoning. Claude incorporates insights from this reasoning before crafting a final response. For more information on extended thinking, see our [documentation(opens in new tab)](https://docs.claude.com/en/docs/build-with-claude/extended-thinking).

##  Setup

First, let's install the necessary packages and set up our environment.

%pip install anthropic

import anthropic

import os

# Set your API key as an environment variable or directly

# os.environ["ANTHROPIC\_API\_KEY"] = "your-api-key-here"

# Initialize the client

client = anthropic.Anthropic()

# Helper functions

def print\_thinking\_response(response):

"""Pretty print a message response with thinking blocks."""

print("\n==== FULL RESPONSE ====")

for block in response.content:

if block.type == "thinking":

print("\n🧠 THINKING BLOCK:")

# Show truncated thinking for readability

print(block.thinking[:500] + "..." if len(block.thinking) > 500 else block.thinking)

print(f"\n[Signature available: {bool(getattr(block, 'signature', None))}]")

if hasattr(block, 'signature') and block.signature:

print(f"[Signature (first 50 chars): {block.signature[:50]}...]")

elif block.type == "redacted\_thinking":

print("\n🔒 REDACTED THINKING BLOCK:")

print(f"[Data length: {len(block.data) if hasattr(block, 'data') else 'N/A'}]")

elif block.type == "text":

print("\n✓ FINAL ANSWER:")

print(block.text)

print("\n==== END RESPONSE ====")

def count\_tokens(messages):

"""Count tokens for a given message list."""

result = client.messages.count\_tokens(

model="claude-sonnet-4-6",

messages=messages

)

return result.input\_tokens

##  Basic example

Let's start with a basic example to show extended thinking in action:

def basic\_thinking\_example():

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=4000,

thinking= {

"type": "enabled",

"budget\_tokens": 2000

},

messages=[{

"role": "user",

"content": "Solve this puzzle: Three people check into a hotel. They pay $30 to the manager. The manager finds out that the room only costs $25 so he gives $5 to the bellboy to return to the three people. The bellboy, however, decides to keep $2 and gives $1 back to each person. Now, each person paid $10 and got back $1, so they paid $9 each, totaling $27. The bellboy kept $2, which makes $29. Where is the missing $1?"

}]

)

print\_thinking\_response(response)

basic\_thinking\_example()

```
==== FULL RESPONSE ====

🧠 THINKING BLOCK:
Let's work through this problem step by step:

Initial situation:
- Three people each pay $10, for a total of $30 given to the manager.
- The room actually costs $25.
- Manager gives $5 to the bellboy to return to the customers.
- Bellboy keeps $2 and gives $1 back to each person ($3 total).

After these transactions:
- Each person has effectively paid $9 (they paid $10 and got $1 back).
- So the three people together paid $27.
- The hotel kept $25 for the room.
- The bellboy kept $2.

So the mo...

[Signature available: True]
[Signature (first 50 chars): EuYBCkQYAiJAGF6X7aWRuRByTdymAUdNOMC++3ZqSJv7jcY5Ly...]

✓ FINAL ANSWER:
# Hotel Bill Puzzle Solution

This is a classic misdirection puzzle that confuses us by mixing up two different accounting approaches.

## The actual flow of money

1. Three people each pay $10, totaling $30
2. The hotel keeps $25 for the room
3. The bellboy keeps $2
4. The guests receive $3 back ($1 each)

## The accounting error in the puzzle

The error occurs when the puzzle tries to add:
- What the guests paid ($27 total after refunds)
- What the bellboy kept ($2)

This is incorrect accounting because the $2 the bellboy kept is already included in the $27 the guests paid. The money should be tracked from a single perspective.

## Correct accounting

From the guests' perspective:
- $27 (what they ultimately paid)
- = $25 (to the hotel) + $2 (to the bellboy)

There is no missing dollar. The puzzle creates confusion by inappropriately adding money from different accounting perspectives.

==== END RESPONSE ====
```

##  Streaming with extended thinking

This example shows how to handle streaming with thinking:

def streaming\_with\_thinking():

with client.messages.stream(

model="claude-sonnet-4-6",

max\_tokens=4000,

thinking={

"type": "enabled",

"budget\_tokens": 2000

},

messages=[{

"role": "user",

"content": "Solve this puzzle: Three people check into a hotel. They pay $30 to the manager. The manager finds out that the room only costs $25 so he gives $5 to the bellboy to return to the three people. The bellboy, however, decides to keep $2 and gives $1 back to each person. Now, each person paid $10 and got back $1, so they paid $9 each, totaling $27. The bellboy kept $2, which makes $29. Where is the missing $1?"

}]

) as stream:

# Track what we're currently building

current\_block\_type = None

current\_content = ""

for event in stream:

if event.type == "content\_block\_start":

current\_block\_type = event.content\_block.type

print(f"\n--- Starting {current\_block\_type} block ---")

current\_content = ""

elif event.type == "content\_block\_delta":

if event.delta.type == "thinking\_delta":

print(event.delta.thinking, end="", flush=True) # Just print dots for thinking to avoid clutter

current\_content += event.delta.thinking

elif event.delta.type == "text\_delta":

print(event.delta.text, end="", flush=True)

current\_content += event.delta.text

elif event.type == "content\_block\_stop":

if current\_block\_type == "thinking":

# Just show a summary for thinking

print(f"\n[Completed thinking block, {len(current\_content)} characters]")

elif current\_block\_type == "redacted\_thinking":

print("\n[Redacted thinking block]")

print(f"--- Finished {current\_block\_type} block ---\n")

current\_block\_type = None

elif event.type == "message\_stop":

print("\n--- Message complete ---")

streaming\_with\_thinking()

```
--- Starting thinking block ---
This is a classic mathematical puzzle that contains a misdirection in how the calculations are presented. Let's break it down step by step:

Initial situation:
- Three people each pay $10, for a total of $30 given to the manager.
- The room actually costs $25.
- The manager gives $5 to the bellboy to return to the customers.
- The bellboy keeps $2 and returns $1 to each person (total of $3 returned).

Now, let's analyze the accounting:

What actually happened:
- The three people originally paid $30.
- They got back $3 in total ($1 each).
- So they actually paid $30 - $3 = $27 in total.
- Of this $27, $25 went to the hotel for the room.
- The remaining $2 went to the bellboy.
- $25 + $2 = $27, which matches what the guests paid. Everything balances.

The error in the puzzle is in how it frames the question. The puzzle states "each person paid $10 and got back $1, so they paid $9 each, totaling $27. The bellboy kept $2, which makes $29." This is mixing up different accounting methods.

The $27 that the guests paid in total should be divided as:
- $25 for the room
- $2 for the bellboy

When we add the bellboy's $2 to the guests' $27, we're double-counting the $2, which creates the illusion of a missing dollar. The $2 is already included in the $27, so we shouldn't add it again.

Another way to think about it: Out of the original $30, $25 went to the hotel, $3 went back to the guests, and $2 went to the bellboy. That's $25 + $3 + $2 = $30, so everything is accounted for.
[Completed thinking block, 1492 characters]
--- Finished thinking block ---

--- Starting text block ---
# The Missing $1 Puzzle Solution

This puzzle uses a misleading way of accounting that creates confusion. Let's clarify what actually happened:

## The correct accounting:
- Three people paid $30 total initially
- The room cost $25
- The bellboy kept $2
- The guests received $3 back ($1 each)

So where did all the money go?
- $25 went to the hotel
- $2 went to the bellboy
- $3 went back to the guests
- $25 + $2 + $3 = $30 ✓

## The error in the puzzle:
The puzzle incorrectly adds the $27 paid by the guests (after refunds) to the $2 kept by the bellboy. This is a mistake because the $2 kept by the bellboy is already part of the $27.

The puzzle creates the illusion of a missing dollar by mixing two different perspectives:
1. How much the guests paid ($27 total)
2. Where the original $30 went (hotel + bellboy + refunds)

There is no missing dollar - it's just an accounting trick!--- Finished text block ---

--- Message complete ---
```

##  Token counting and context window management

This example demonstrates how to track token usage with extended thinking:

def token\_counting\_example():

# Define a function to create a sample prompt

def create\_sample\_messages():

messages = [{

"role": "user",

"content": "Solve this puzzle: Three people check into a hotel. They pay $30 to the manager. The manager finds out that the room only costs $25 so he gives $5 to the bellboy to return to the three people. The bellboy, however, decides to keep $2 and gives $1 back to each person. Now, each person paid $10 and got back $1, so they paid $9 each, totaling $27. The bellboy kept $2, which makes $29. Where is the missing $1?"

}]

return messages

# Count tokens without thinking

base\_messages = create\_sample\_messages()

base\_token\_count = count\_tokens(base\_messages)

print(f"Base token count (input only): {base\_token\_count}")

# Make a request with thinking and check actual usage

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=8000,

thinking = {

"type": "enabled",

"budget\_tokens": 2000

},

messages=base\_messages

)

# Calculate and print token usage stats

thinking\_tokens = sum(

len(block.thinking.split()) \* 1.3 # Rough estimate

for block in response.content

if block.type == "thinking"

)

final\_answer\_tokens = sum(

len(block.text.split()) \* 1.3 # Rough estimate

for block in response.content

if block.type == "text"

)

print(f"\nEstimated thinking tokens used: ~{int(thinking\_tokens)}")

print(f"Estimated final answer tokens: ~{int(final\_answer\_tokens)}")

print(f"Total estimated output tokens: ~{int(thinking\_tokens + final\_answer\_tokens)}")

print(f"Input tokens + max\_tokens = {base\_token\_count + 8000}")

print(f"Available for final answer after thinking: ~{8000 - int(thinking\_tokens)}")

# Demo with escalating thinking budgets

thinking\_budgets = [1024, 2000, 4000, 8000, 16000, 32000]

context\_window = 200000

for budget in thinking\_budgets:

print(f"\nWith thinking budget of {budget} tokens:")

print(f"Input tokens: {base\_token\_count}")

print(f"Max tokens needed: {base\_token\_count + budget + 1000}") # Add 1000 for final answer

print(f"Remaining context window: {context\_window - (base\_token\_count + budget + 1000)}")

if base\_token\_count + budget + 1000 > context\_window:

print("WARNING: This would exceed the context window of 200k tokens!")

# Uncomment to run the example

token\_counting\_example()

```
Base token count (input only): 125

Estimated thinking tokens used: ~377
Estimated final answer tokens: ~237
Total estimated output tokens: ~614
Input tokens + max_tokens = 8125
Available for final answer after thinking: ~7623

With thinking budget of 1024 tokens:
Input tokens: 125
Max tokens needed: 2149
Remaining context window: 197851

With thinking budget of 2000 tokens:
Input tokens: 125
Max tokens needed: 3125
Remaining context window: 196875

With thinking budget of 4000 tokens:
Input tokens: 125
Max tokens needed: 5125
Remaining context window: 194875

With thinking budget of 8000 tokens:
Input tokens: 125
Max tokens needed: 9125
Remaining context window: 190875

With thinking budget of 16000 tokens:
Input tokens: 125
Max tokens needed: 17125
Remaining context window: 182875

With thinking budget of 32000 tokens:
Input tokens: 125
Max tokens needed: 33125
Remaining context window: 166875
```

##  Understanding redacted thinking blocks

Occasionally Claude's internal reasoning will be flagged by safety systems. When this occurs, we encrypt some or all of the `thinking` block and return it to you as a `redacted_thinking` block. These redacted thinking blocks are decrypted when passed back to the API, allowing Claude to continue its response without losing context.

This example demonstrates working with redacted thinking blocks using a special test string that triggers them:

def redacted\_thinking\_example():

# Using the special test string that triggers redacted thinking

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=4000,

thinking={

"type": "enabled",

"budget\_tokens": 2000

},

messages=[{

"role": "user",

"content": "ANTHROPIC\_MAGIC\_STRING\_TRIGGER\_REDACTED\_THINKING\_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB"

}]

)

# Identify redacted thinking blocks

redacted\_blocks = [block for block in response.content if block.type == "redacted\_thinking"]

thinking\_blocks = [block for block in response.content if block.type == "thinking"]

text\_blocks = [block for block in response.content if block.type == "text"]

print(response.content)

print(f"Response includes {len(response.content)} total blocks:")

print(f"- {len(redacted\_blocks)} redacted thinking blocks")

print(f"- {len(thinking\_blocks)} regular thinking blocks")

print(f"- {len(text\_blocks)} text blocks")

# Show data properties of redacted blocks

if redacted\_blocks:

print(f"\nRedacted thinking blocks contain encrypted data:")

for i, block in enumerate(redacted\_blocks[:3]): # Show first 3 at most

print(f"Block {i+1} data preview: {block.data[:50]}...")

# Print the final text output

if text\_blocks:

print(f"\nFinal text response:")

print(text\_blocks[0].text)

# Uncomment to run the example

redacted\_thinking\_example()

```
[TextBlock(citations=None, text=None, type='redacted_thinking', data='EvAFCoYBGAIiQL7asmglEdeKXw4EdihR2gBQ7O7+j/dGecLjsS2PMgW9av+NRwuIV2nFD4I61hUHrp5vzJF7/y+i/vvbnxaRnwMqQMizGiLSDcowtEvP9EcIT4d75iPhZ8TaiVdD22bZp3YVcc0laY8u1lEJTSesgLUywuc3QHZcg4NZ7tKjWwKgcVUSDHgb6gZUK9aP47KvNxoMCNjkIDR40zmq/QmVIjBSCnvTMSUE+jnmLZSq1TZO9T7ImALNJt8I5j1ls24CO1fibsRThJ7Ha5A0/tuEKVoqlgRc+e2tS+BQMXx572lT4Hkl4aVpcM4SQbqBjeVeR3NmCBLoOxlQ2JLiIYwMHUS/K9GDLyMQcYd1KUWgN34CZRK7k44CSkNsO8oh4uj/1qsRsZjq1l6RQ29rLKSEXvMU4XbZufJ1icvYZS1I6PIZzER6/u6it+WNYyBxJ2vaFICjDePNgIHfRA/ceTz9mfCtBiTfagyPBbs2HflXlSlW26TSdI7PKof5/EsQ+DUkjAy+9VTLX7zHYzNZtwJPL2ryYw4loSwRbc4syldA0Ncnn7hA+yJyY0QwSrxZFIm/t9X9p9s+2SL0F4wSRsimnxRiIhfJD3i+oTw8AbGklyoP0kCH2WxA7Gr3rNLJVkRTJl48AjlSL7ClaWvLWrNer13etD7n5rbwiXOn5husy8gAm5GE3/eFyty3Y+/ad+lMPKXSjL0aP67WoJrFq/teItolOVZeOOERjVFdw5jIV1EUknlAZ/pfI53pLYqwFl17M7IXMdGxEaKoGDIKcnYTwT31uUNlB5JSBWoq1SnkFsFy2zDsDTFzjml3HEXz4szZi3j5/qHWJlMMCcB1walZUisxEp0v1euvcgatY5wfYSiAP3s9wOrgYKCkuLcidlgiyQHJB1haZjO8/tZ9gzWk1n//7pTncdKgd5ZK9/ErxWFlBV/vQwjp0cB7zoVcLh1ydi/Coea6ZOuei+ICKVl4IcR2A6DD8gtEJmc='), TextBlock(citations=None, text="I notice you've sent what appears to be a prompt attempting to access internal systems or processes. I can't respond to commands of this nature.\n\nInstead, I'm happy to have a normal conversation and assist you with legitimate questions or tasks. What would you like help with today?", type='text')]
Response includes 2 total blocks:
- 1 redacted thinking blocks
- 0 regular thinking blocks
- 1 text blocks

Redacted thinking blocks contain encrypted data:
Block 1 data preview: EvAFCoYBGAIiQL7asmglEdeKXw4EdihR2gBQ7O7+j/dGecLjsS...

Final text response:
I notice you've sent what appears to be a prompt attempting to access internal systems or processes. I can't respond to commands of this nature.

Instead, I'm happy to have a normal conversation and assist you with legitimate questions or tasks. What would you like help with today?
```

##  Handling error cases

When using extended thinking, keep in mind:

1. **Minimum budget**: The minimum thinking budget is 1,024 tokens. We suggest starting at the minimum and increasing incrementally to find the optimal range.
2. **Incompatible features**: Thinking isn't compatible with temperature, top\_p, or top\_k modifications, and you cannot pre-fill responses.
3. **Pricing**: Extended thinking tokens count towards the context window and are billed as output tokens. They also count towards your rate limits.

For more details on extended thinking with tool use, see the "Extended Thinking with Tool Use" notebook.

def demonstrate\_common\_errors():

# 1. Error from setting thinking budget too small

try:

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=4000,

thinking={

"type": "enabled",

"budget\_tokens": 500 # Too small, minimum is 1024

},

messages=[{

"role": "user",

"content": "Explain quantum computing."

}]

)

except Exception as e:

print(f"\nError with too small thinking budget: {e}")

# 2. Error from using temperature with thinking

try:

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=4000,

temperature=0.7, # Not compatible with thinking

thinking={

"type": "enabled",

"budget\_tokens": 2000

},

messages=[{

"role": "user",

"content": "Write a creative story."

}]

)

except Exception as e:

print(f"\nError with temperature and thinking: {e}")

# 3. Error from exceeding context window

try:

# Create a very large prompt

long\_content = "Please analyze this text. " + "This is sample text. " \* 150000

response = client.messages.create(

model="claude-sonnet-4-6",

max\_tokens=20000, # This plus the long prompt will exceed context window

thinking={

"type": "enabled",

"budget\_tokens": 10000

},

messages=[{

"role": "user",

"content": long\_content

}]

)

except Exception as e:

print(f"\nError from exceeding context window: {e}")

# Run the common error examples

demonstrate\_common\_errors()

```
Error with too small thinking budget: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'thinking.enabled.budget_tokens: Input should be greater than or equal to 1024'}}

Error with temperature and thinking: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': '`temperature` may only be set to 1 when thinking is enabled. Please consult our documentation at https://docs.claude.com/en/docs/build-with-claude/extended-thinking#important-considerations-when-using-extended-thinking'}}

Error from exceeding context window: Error code: 400 - {'type': 'error', 'error': {'type': 'invalid_request_error', 'message': 'prompt is too long: 214315 tokens > 204798 maximum'}}
```
