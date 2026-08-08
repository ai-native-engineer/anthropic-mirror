<!-- source: https://platform.claude.com/cookbook/misc-generate-test-cases -->

#  Generate Synthetic Test Data for Your Prompt Template

Imagine you have a prompt roughly along these lines:

"""Here's some things I want you to analyze:

{{thing1}}

{{thing2}}

These things are [description of things]. Please read them carefully and [do some task]."""

Here we'd call thing1 and thing2 the "variables" -- and you want your prompt to behave well for many different possible values of thing1 and thing2.

How can you test this prompt template? Maybe you have some real-life values you can substitute in. But maybe you don't, or maybe you aren't allowed to test on the ones you do have for privacy reasons. No worries -- Claude can make them up! This cookbook demonstrates how to generate synthetic test data for your prompts using Claude & the Claude API. It includes functions for extracting variables from templates, constructing example blocks, generating test cases, and iteratively refining the results. The benefits of this are twofold:

1. Prompt Evaluation
   You can use these test cases to see how Claude will perform on realistic examples.
2. Prompt Improvement with Multishot Examples
   Giving Claude examples is perhaps the best way to improve its performance. This notebook can help you generate realistic inputs which is half the battle in getting ideal input/output pairs.



% pip install anthropic IPython



import re

import anthropic

# Enter your API key here

api\_key = ""

CLIENT = anthropic.Anthropic(api\_key=api\_key)

MODEL\_NAME = "claude-sonnet-4-6"

Let's start by defining some helper functions that we'll use throughout this notebook.



# First, we have the `extract\_variables` function,

# It takes in a prompt template and extracts the double-mustache-bracketed "variables" contained.

def extract\_variables(prompt\_template):

"""Extract variables from a prompt template."""

pattern = r"{{([^}]+)}}"

variables = re.findall(pattern, prompt\_template)

return set(variables)

# Next, we have `construct\_variables\_names`, which just joins them together connected by newlines.

def construct\_variables\_names(prompt\_template):

"""Construct a string of variable names from a prompt template."""

variables = extract\_variables(prompt\_template)

return "\n".join(variables)

# The `construct\_variables\_block` function takes in the list of variables, and constructs a "variables block"

# The variables block might look like this, if the variables were 'animal' and 'topic':

"""

<animal>

[a full, complete, value for the variable "animal"]

</animal>

<topic>

[a full, complete, value for the variable "topic"]

</topic>

"""

def construct\_variables\_block(prompt\_template):

"""Construct a variables block for the synthetic test data prompt."""

variables = extract\_variables(prompt\_template)

output = ""

for v in variables:

output += f"<{v}>\n"

output += f'[a full, complete, value for the variable "{v}". (You do not need to repeat the variable name inside the tags.)]\n'

output += f"</{v}>\n"

return output.strip()

# `construct\_examples` takes a dictionary of {variable: value} and constructs an XML-formatted example.

# E.g. if the dict is

# {'animal': 'cat', 'topic': 'movement patterns'}, then the example would be

"""

<example>

<variables>

<animal>

cat

</animal>

<topic>

movement patterns

</topic>

</variables>

</example>

"""

def construct\_example\_block(variable\_dict):

"""Construct an example block from a dictionary of variables."""

output = "<example>\n<variables>\n"

for k, v in variable\_dict.items():

output += f"<{k}>\n{v}\n</{k}>\n"

output = output.strip()

output += "\n</variables>\n</example>"

return output

##  Prompt Template for Generating the Data

The general idea of these prompt templates is to take a user-submitted prompt template with variables, and construct some values for the variables to fill the template.

There are actually two prompt templates below; one is formatted assuming that the user has already provided example variable values, and one does not assume that.

What they have in common is that both templates start by giving Claude context about the situation, and directing Claude to carefully think through the specs of each variable individually as well as the user-provided prompt template as a whole before outputting the test cases.



# Formatting Prompt Templates for Synthetic Evaluations

# This function prepares the prompt template for generating synthetic test data.

def format\_prompt\_template\_for\_synth\_evals(prompt\_template, examples=None):

"""Format a prompt template for synthetic evaluations."""

synth\_test\_data\_prompt\_template\_with\_example = """<Prompt Template>

{{PROMPT\_TEMPLATE}}

</Prompt Template>

Your job is to construct a test case for the prompt template above. This template contains "variables", which are placeholders to be filled in later. In this case, the variables are:

<variables>

{{CONSTRUCT\_VARIABLES\_NAMES}}

</variables>

Here are the example test cases provided by the user.

<examples>

{{EXAMPLES}}

</examples>

First, in <planning> tags, do the following:

1. Summarize the prompt template. What is the goal of the user who created it?

2. For each variable in <variables>, carefully consider what a paradigmatic, realistic example of that variable would look like. You'll want to note who will be responsible "in prod" for supplying values. Written by a human "end user"? Downloaded from a website? Extracted from a database? Think about things like length, format, and tone in addition to semantic content. Use the examples provided by the user to guide this exercise. The goal is to acquire a sense of the statistical distribution the examples are being drawn from. The example you write should be drawn from that same distribution, but sufficiently different from the examples that it provides additional signal. A tricky balancing act, but I have faith in you.

Once you're done, output a test case for this prompt template with a full, complete, value for each variable. The output format should consist of a tagged block for each variable, with the value inside the block, like the below:

<variables>

{{CONSTRUCT\_VARIABLES\_BLOCK}}

</variables>"""

synth\_test\_data\_prompt\_template\_without\_example = """<Prompt Template>

{{PROMPT\_TEMPLATE}}

</Prompt Template>

Your job is to construct a test case for the prompt template above. This template contains "variables", which are placeholders to be filled in later. In this case, the variables are:

<variables>

{{CONSTRUCT\_VARIABLES\_NAMES}}

</variables>

First, in <planning> tags, do the following:

1. Summarize the prompt template. What is the goal of the user who created it?

2. For each variable in <variables>, carefully consider what a paradigmatic, realistic example of that variable would look like. You'll want to note who will be responsible "in prod" for supplying values. Written by a human "end user"? Downloaded from a website? Extracted from a database? Think about things like length, format, and tone in addition to semantic content.

Then, output a test case for this prompt template with a full, complete, value for each variable. The output format should consist of a tagged block for each variable, with the value inside the block, like the below:

<variables>

{{CONSTRUCT\_VARIABLES\_BLOCK}}

</variables>"""

if examples:

examples\_block = "\n".join([construct\_example\_block(example) for example in examples])

return (

synth\_test\_data\_prompt\_template\_with\_example.replace(

"{{PROMPT\_TEMPLATE}}", prompt\_template

)

.replace("{{CONSTRUCT\_VARIABLES\_NAMES}}", construct\_variables\_names(prompt\_template))

.replace("{{CONSTRUCT\_VARIABLES\_BLOCK}}", construct\_variables\_block(prompt\_template))

.replace("{{EXAMPLES}}", examples\_block)

)

else:

return (

synth\_test\_data\_prompt\_template\_without\_example.replace(

"{{PROMPT\_TEMPLATE}}", prompt\_template

)

.replace("{{CONSTRUCT\_VARIABLES\_NAMES}}", construct\_variables\_names(prompt\_template))

.replace("{{CONSTRUCT\_VARIABLES\_BLOCK}}", construct\_variables\_block(prompt\_template))

)

Next, another quick helper function for filling in the appropriate prompt template and calling Claude.



def get\_test\_data(prompt\_template, examples, custom\_planning=None):

"""Generate test data using the Claude API."""

synth\_eval\_prompt\_ready = format\_prompt\_template\_for\_synth\_evals(prompt\_template, examples)

messages = [

{

"role": "user",

"content": synth\_eval\_prompt\_ready,

}

]

if custom\_planning:

messages.append(

{

"role": "assistant",

"content": custom\_planning,

}

)

message = (

CLIENT.messages.create(

max\_tokens=4000,

messages=messages,

model=MODEL\_NAME,

temperature=1,

)

.content[0]

.text

)

return message



# We'll use this function to sample Claude's response to the filled-in template,

# once we have our example values/test case.

def call\_claude\_with\_template(prompt\_template, variables):

"""Call Claude with a filled prompt template."""

filled\_template = prompt\_template

for var, value in variables.items():

filled\_template = filled\_template.replace(f"{{{{{var}}}}}", value)

message = (

CLIENT.messages.create(

max\_tokens=4000,

messages=[

{

"role": "user",

"content": filled\_template,

}

],

model=MODEL\_NAME,

temperature=0.7,

)

.content[0]

.text

)

return message

Now we can start to put the pieces together. To start, enter your prompt template here.



# Replace this with your prompt template!

# Use double-brackets to indicate variables

# Here's an example:

prompt\_template = """You are a customer support bot for Acme Corporation.

Here is an FAQ with Acme's relevant policies:

<documents>

{{DOCUMENTS}}

</documents>

Please respond to this customer support question using details from the policies:

<question>

{{QUESTION}}

</question>"""

variables = extract\_variables(prompt\_template)

print("\nIdentified variables:")

for var in variables:

print(f"- {var}")



```
Identified variables:
- DOCUMENTS
- QUESTION
```

Next, if you have any "golden examples" of inputs and ideal outputs, you can enter those. The code is commented out for now.



planning\_text = None

USER\_EXAMPLES = []

# if input("\nDo you want to provide an example value for your variables? (y/n): ").lower() == 'y':

# example = {}

# for var in variables:

# example[var] = input(f"Enter an example value for {var}: ")

# USER\_EXAMPLES.append(example)

Next, we can get the test case generation prompt template filled out with this information, and get a test case!



result = get\_test\_data(prompt\_template, USER\_EXAMPLES, planning\_text)

Now, let's take a look at both the test case and the planning that Claude used to generate it.



planning\_match = re.search(r"<planning>(.\*?)</planning>", result, re.DOTALL)

if planning\_match and not planning\_text:

planning\_text = "<planning>\n" + planning\_match.group(1).strip() + "\n</planning>"

extracted\_variables = {}

for var in variables:

var\_match = re.search(f"<{var}>(.\*?)</{var}>", result[result.index("<variables>") :], re.DOTALL)

if var\_match:

extracted\_variables[var] = var\_match.group(1).strip()

USER\_EXAMPLES.append(extracted\_variables)

print("~~~~~~~~~~~\nGenerated test case:\n~~~~~~~~~~~")

for var, value in extracted\_variables.items():

print(f"{var}:\n{value}\n")

print("~~~~~~~~~~~\nPlanning:\n~~~~~~~~~~~")

print(planning\_text)



```
~~~~~~~~~~~
Generated test case:
~~~~~~~~~~~
DOCUMENTS:
Return Policy
- Items may be returned within 30 days of purchase with original receipt
- Items must be unused and in original packaging
- Shipping costs are non-refundable
- Gift cards are non-returnable

Shipping Information
- Standard shipping (5-7 business days): Free on orders over $50
- Express shipping (2-3 business days): $12.99
- Overnight shipping (next business day): $24.99
- We ship to continental US only
- Alaska and Hawaii orders incur additional $15 fee

Payment Methods
- We accept Visa, Mastercard, American Express, and PayPal
- Payment is processed at time of order
- Gift cards cannot be used for partial payment

QUESTION:
Hi, I ordered a sweater last week but it doesn't fit right. Can I return it? And will I get refunded for the shipping I paid? Thanks!

~~~~~~~~~~~
Planning:
~~~~~~~~~~~
<planning>
1. Prompt Template Summary:
This template creates a customer service chatbot for Acme Corporation that answers customer questions based on official company policies/FAQ documents. The goal is to ensure consistent, policy-compliant responses to customer inquiries.

2. Variable Analysis:

DOCUMENTS:
- Would likely be maintained by Acme's policy/legal team
- Stored in a knowledge base or content management system
- Formatted as structured FAQ entries or policy statements
- Professional, formal tone
- Multiple paragraphs covering different topics
- Clear headers and categories
- Length: Several paragraphs (300-500 words)

QUESTION:
- Written by end users/customers
- Informal, conversational tone
- Usually 1-2 sentences
- Often includes context about their specific situation
- May contain typos or casual language
- Length: 20-50 words
</planning>
```

From here, there are a few ways we can go. We could generate more test cases, or we could edit Claude's planning logic. Let's edit Claude's planning logic a little bit. Maybe we know that ACME's documentation uses numbered lines. Some other realistic changes could be:

* Have Claude tell itself to make the documents longer and more detailed.
* Have Claude tell itself to make the customer support query more or less formal.



planning\_text = planning\_text.replace(

"each with a question and answer format",

"each with a question and answer format and associated number.",

)

# You might have slightly different planning text and therefore need to rewrite the replace.

Let's reset our examples, but use this planning text as a prefill. (This saves a little bit of sampling time.)



USER\_EXAMPLES = []

result = get\_test\_data(prompt\_template, USER\_EXAMPLES, planning\_text)

Now let's see the new results.



# Copied and pasted from a cell above.

planning\_match = re.search(r"<planning>(.\*?)</planning>", result, re.DOTALL)

if planning\_match and not planning\_text:

planning\_text = "<planning>\n" + planning\_match.group(1).strip() + "\n</planning>"

extracted\_variables = {}

for var in variables:

var\_match = re.search(f"<{var}>(.\*?)</{var}>", result[result.index("<variables>") :], re.DOTALL)

if var\_match:

extracted\_variables[var] = var\_match.group(1).strip()

USER\_EXAMPLES.append(extracted\_variables)

print("~~~~~~~~~~~\nGenerated test case:\n~~~~~~~~~~~")

for var, value in extracted\_variables.items():

print(f"{var}:\n{value}\n")

print("~~~~~~~~~~~\nPlanning:\n~~~~~~~~~~~")

print(planning\_text)



```
~~~~~~~~~~~
Generated test case:
~~~~~~~~~~~
DOCUMENTS:
Return Policy
- Items may be returned within 30 days of purchase with original receipt
- Items must be unused and in original packaging
- Shipping costs are non-refundable
- Store credit will be issued for items returned without receipt

Shipping Information
- Standard shipping (5-7 business days): $5.99
- Express shipping (2-3 business days): $12.99
- Free standard shipping on orders over $50
- We currently ship only within the continental United States
- Alaska and Hawaii orders subject to additional fees

Payment Methods
- We accept Visa, Mastercard, American Express, and PayPal
- Gift cards cannot be used for online purchases
- Payment is processed at time of order
- All prices are in USD

QUESTION:
Hi, I ordered a sweater last week but it doesn't fit right. Can I return it? I still have the tags on it but I threw away the receipt. Thanks!

~~~~~~~~~~~
Planning:
~~~~~~~~~~~
<planning>
1. Prompt Template Summary:
This template creates a customer service chatbot for Acme Corporation that answers customer questions based on official company policies/FAQ documents. The goal is to ensure consistent, policy-compliant responses to customer inquiries.

2. Variable Analysis:

DOCUMENTS:
- Would likely be maintained by Acme's policy/legal team
- Stored in a knowledge base or content management system
- Formatted as structured FAQ entries or policy statements
- Professional, formal tone
- Multiple paragraphs covering different topics
- Clear headers and categories
- Length: Several paragraphs (300-500 words)

QUESTION:
- Written by end users/customers
- Informal, conversational tone
- Usually 1-2 sentences
- Often includes context about their specific situation
- May contain typos or casual language
- Length: 20-50 words
</planning>
```

Great, it did the numbered Q and A!

Let's make another example. This one will use the example we already have, so hopefully it will be interestingly different.



result = get\_test\_data(prompt\_template, USER\_EXAMPLES, planning\_text)



# Copied and pasted from a cell above.

planning\_match = re.search(r"<planning>(.\*?)</planning>", result, re.DOTALL)

if planning\_match and not planning\_text:

planning\_text = "<planning>\n" + planning\_match.group(1).strip() + "\n</planning>"

extracted\_variables = {}

for var in variables:

var\_match = re.search(f"<{var}>(.\*?)</{var}>", result[result.index("<variables>") :], re.DOTALL)

if var\_match:

extracted\_variables[var] = var\_match.group(1).strip()

USER\_EXAMPLES.append(extracted\_variables)

print("~~~~~~~~~~~\nGenerated test case:\n~~~~~~~~~~~")

for var, value in extracted\_variables.items():

print(f"{var}:\n{value}\n")

print("~~~~~~~~~~~\nPlanning:\n~~~~~~~~~~~")

print(planning\_text)



```
~~~~~~~~~~~
Generated test case:
~~~~~~~~~~~
DOCUMENTS:
Product Warranty
- All electronics come with a 1-year limited manufacturer warranty
- Warranty covers defects in materials and workmanship
- Warranty does not cover accidental damage or misuse
- Extended warranty available for purchase within 30 days

Price Match Policy
- We match prices from authorized retailers
- Item must be identical model/color/specification
- Must be in stock at competitor's store
- Online retailers excluded from price matching
- Price match requests must be made at time of purchase

Order Cancellation
- Orders can be cancelled within 2 hours of placement
- Once order is shipped, cancellation not possible
- Cancelled orders refunded to original payment method
- Processing time for refunds: 3-5 business days
- Contact customer service for cancellation requests

QUESTION:
Hello, I bought a laptop from your store 3 weeks ago and it keeps shutting down randomly. It's still under warranty, right? What do I need to do to get it fixed? Thanks in advance!

~~~~~~~~~~~
Planning:
~~~~~~~~~~~
<planning>
1. Prompt Template Summary:
This template creates a customer service chatbot for Acme Corporation that answers customer questions based on official company policies/FAQ documents. The goal is to ensure consistent, policy-compliant responses to customer inquiries.

2. Variable Analysis:

DOCUMENTS:
- Would likely be maintained by Acme's policy/legal team
- Stored in a knowledge base or content management system
- Formatted as structured FAQ entries or policy statements
- Professional, formal tone
- Multiple paragraphs covering different topics
- Clear headers and categories
- Length: Several paragraphs (300-500 words)

QUESTION:
- Written by end users/customers
- Informal, conversational tone
- Usually 1-2 sentences
- Often includes context about their specific situation
- May contain typos or casual language
- Length: 20-50 words
</planning>
```

Still about ACME corporation, but the question is different and so is the knowledge base.

From here, the world is your oyster -- you can generate more test cases by running the code in a loop, edit the planning more, evaluate Claude on these test cases, and put the test cases you make along with golden answers into your prompt as multishot examples.

To get golden answers, you can either write them yourself from scratch, or have Claude write an answer and then edit it to taste. With the advent of prompt caching, there's never been a better time to add tons of examples to your prompt to improve performance.
