<!-- source: https://platform.claude.com/cookbook/misc-building-moderation-filter -->

#  Building a moderation filter with Claude

This guide will show you how to use Claude to build a content moderation filter for user-generated text. The key idea is to define the moderation rules and categories directly in the prompt, allowing for easy customization and experimentation.

##  Basic Approach

The basic approach is to provide Claude with a prompt that describes the categories you want to filter for (e.g. "ALLOW" and "BLOCK"), along with detailed descriptions or examples of what kinds of content should fall into each category. Then, you insert the user-generated text to be classified as part of the prompt, and ask Claude to categorize it based on the provided guidelines.

Here's an example prompt structure:



You are a content moderation expert tasked with categorizing user-generated text based on the following guidelines:

BLOCK CATEGORY:

- [Description or examples of content that should be blocked]

ALLOW CATEGORY:

- [Description or examples of content that is allowed]

Here is the user-generated text to categorize:

<user\_text>{{USER\_TEXT}}</user\_text>

Based on the guidelines above, classify this text as either ALLOW or BLOCK. Return nothing else.

To use this, you would replace `{{USER_TEXT}}` with the actual user-generated text to be classified, and then send the prompt to Claude using the Claude API. Claude's response should be either "ALLOW" or "BLOCK", indicating how the text should be handled based on your provided guidelines.

##  Example usage

Here's some example Python code that demonstrates how to use this approach:



%pip install anthropic



from anthropic import Anthropic

client = Anthropic()

MODEL\_NAME = "claude-haiku-4-5"

def moderate\_text(user\_text, guidelines):

prompt\_template = """

You are a content moderation expert tasked with categorizing user-generated text based on the following guidelines:

{guidelines}

Here is the user-generated text to categorize:

<user\_text>{user\_text}</user\_text>

Based on the guidelines above, classify this text as either ALLOW or BLOCK. Return nothing else.

"""

# Format the prompt with the user text

prompt = prompt\_template.format(user\_text=user\_text, guidelines=guidelines)

# Send the prompt to Claude and get the response

response = (

client.messages.create(

model=MODEL\_NAME, max\_tokens=10, messages=[{"role": "user", "content": prompt}]

)

.content[0]

.text

)

return response

And here's an example of how you could use this function to moderate an array of user comments:



example\_guidelines = """BLOCK CATEGORY:

- Promoting violence, illegal activities, or hate speech

- Explicit sexual content

- Harmful misinformation or conspiracy theories

ALLOW CATEGORY:

- Most other content is allowed, as long as it is not explicitly disallowed

"""

user\_comments = [

"This movie was great, I really enjoyed it. The main actor really killed it!",

"Delete this post now or you better hide. I am coming after you and your family.",

"Stay away from the 5G cellphones!! They are using 5G to control you.",

"Thanks for the helpful information!",

]

for comment in user\_comments:

classification = moderate\_text(comment, example\_guidelines)

print(f"Comment: {comment}\nClassification: {classification}\n")



```
Comment: This movie was great, I really enjoyed it. The main actor really killed it!
Classification: ALLOW

Comment: Delete this post now or you better hide. I am coming after you and your family.
Classification: BLOCK

Comment: Stay away from the 5G cellphones!! They are using 5G to control you.
Classification: BLOCK

Comment: Thanks for the helpful information!
Classification: ALLOW
```

##  Customization

One of the key benefits of this approach is that you can easily customize the moderation rules by modifying the descriptions or examples provided in the prompt for the "BLOCK" and "ALLOW" categories. This allows you to fine-tune the filtering to suit your specific needs or preferences.

For example, if you wanted to Claude to moderate a rollercoaster enthusiast forum and ensure posts stay on topic, you could update the "ALLOW" and "BLOCK" category descriptions accordingly:



rollercoaster\_guidelines = """BLOCK CATEGORY:

- Content that is not related to rollercoasters, theme parks, or the amusement industry

- Explicit violence, hate speech, or illegal activities

- Spam, advertisements, or self-promotion

ALLOW CATEGORY:

- Discussions about rollercoaster designs, ride experiences, and park reviews

- Sharing news, rumors, or updates about new rollercoaster projects

- Respectful debates about the best rollercoasters, parks, or ride manufacturers

- Some mild profanity or crude language, as long as it is not directed at individuals

"""

post\_titles = [

"Top 10 Wildest Inversions on Steel Coasters",

"My Review of the New RMC Raptor Coaster at Cedar Point",

"Best Places to Buy Cheap Hiking Gear",

"Rumor: Is Six Flags Planning a Giga Coaster for 2025?",

"My Thoughts on the Latest Marvel Movie",

]

for title in post\_titles:

classification = moderate\_text(title, rollercoaster\_guidelines)

print(f"Title: {title}\nClassification: {classification}\n")



```
Title: Top 10 Wildest Inversions on Steel Coasters
Classification: ALLOW

Title: My Review of the New RMC Raptor Coaster at Cedar Point
Classification: ALLOW

Title: Best Places to Buy Cheap Hiking Gear
Classification: BLOCK

Title: Rumor: Is Six Flags Planning a Giga Coaster for 2025?
Classification: ALLOW

Title: My Thoughts on the Latest Marvel Movie
Classification: BLOCK
```

##  Improving Performance with Chain of Thought (CoT)

One technique that can enhance Claude's content moderation capabilities is "chain-of-thought" (CoT) prompting. This approach encourages Claude to break down its reasoning process into a step-by-step chain of thoughts, rather than just providing the final output.

To leverage chain of thought for moderation, you can modify your prompt to explicitly instruct Claude to break down its process into clear steps inside `<thinking>` tags. Here's an example:



cot\_prompt = """You are a content moderation expert tasked with categorizing user-generated text based on the following guidelines:

BLOCK CATEGORY:

- Content that is not related to rollercoasters, theme parks, or the amusement industry

- Explicit violence, hate speech, or illegal activities

- Spam, advertisements, or self-promotion

ALLOW CATEGORY:

- Discussions about rollercoaster designs, ride experiences, and park reviews

- Sharing news, rumors, or updates about new rollercoaster projects

- Respectful debates about the best rollercoasters, parks, or ride manufacturers

- Some mild profanity or crude language, as long as it is not directed at individuals

First, inside of <thinking> tags, identify any potentially concerning aspects of the post based on the guidelines below and consider whether those aspects are serious enough to block the post or not. Finally, classify this text as either ALLOW or BLOCK inside <output> tags. Return nothing else.

Given those instructions, here is the post to categorize:

<user\_post>{user\_post}</user\_post>"""

user\_post = "Introducing my new band - Coaster Shredders. Check us out on YouTube!!"

response = (

client.messages.create(

model=MODEL\_NAME,

max\_tokens=1000,

messages=[{"role": "user", "content": cot\_prompt.format(user\_post=user\_post)}],

)

.content[0]

.text

)

print(response)



```
<thinking>
The post appears to be promoting a band rather than discussing rollercoasters, theme parks, or the amusement industry. This falls under the "spam, advertisements, or self-promotion" category, which is grounds for blocking the post.
</thinking>

<output>BLOCK</output>
```

##  Improving Performance with Examples

Another technique for improving performance is by adding a few examples to the prompt, you provide Claude with some initial training data or "few-shot learning" to better understand the desired categorization. This can be especially helpful for nuanced or ambiguous cases where the category boundaries may not be entirely clear from the text descriptions alone. Here's an example of how you could modify the prompt template to include examples:



examples\_prompt = """You are a content moderation expert tasked with categorizing user-generated text based on the following guidelines:

BLOCK CATEGORY:

- Content that is not related to rollercoasters, theme parks, or the amusement industry

- Explicit violence, hate speech, or illegal activities

- Spam, advertisements, or self-promotion

ALLOW CATEGORY:

- Discussions about rollercoaster designs, ride experiences, and park reviews

- Sharing news, rumors, or updates about new rollercoaster projects

- Respectful debates about the best rollercoasters, parks, or ride manufacturers

- Some mild profanity or crude language, as long as it is not directed at individuals

Here are some examples:

<examples>

Text: I'm selling weight loss products, check my link to buy!

Category: BLOCK

Text: I hate my local park, the operations and customer service are terrible. I wish that place would just burn down.

Category: BLOCK

Text: Did anyone ride the new RMC raptor Trek Plummet 2 yet? I've heard it's insane!

Category: ALLOW

Text: Hercs > B&Ms. That's just facts, no cap! Arrow > Intamin for classic woodies too.

Category: ALLOW

</examples>

Given those examples, here is the user-generated text to categorize:

<user\_text>{user\_text}</user\_text>

Based on the guidelines above, classify this text as either ALLOW or BLOCK. Return nothing else."""

user\_post = "Why Boomerang Coasters Ain't It (Don't @ Me)"

response = (

client.messages.create(

model=MODEL\_NAME,

max\_tokens=1000,

messages=[{"role": "user", "content": examples\_prompt.format(user\_text=user\_post)}],

)

.content[0]

.text

)

print(response)



```
ALLOW
```
