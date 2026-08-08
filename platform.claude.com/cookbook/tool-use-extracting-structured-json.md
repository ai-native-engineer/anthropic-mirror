<!-- source: https://platform.claude.com/cookbook/tool-use-extracting-structured-json -->

#  Extracting Structured JSON using Claude and Tool Use

In this cookbook, we'll explore various examples of using Claude and the tool use feature to extract structured JSON data from different types of input. We'll define custom tools that prompt Claude to generate well-structured JSON output for tasks such as summarization, entity extraction, sentiment analysis, and more.

If you want to get structured JSON data without using tools, take a look at our "[How to enable JSON mode(opens in new tab)](https://github.com/anthropics/anthropic-cookbook/blob/main/misc/how_to_enable_json_mode.ipynb)" cookbook.

##  Set up the environment

First, let's install the required libraries and set up the Claude API client.



%pip install anthropic requests beautifulsoup4



import json

import requests

from anthropic import Anthropic

from bs4 import BeautifulSoup

client = Anthropic()

MODEL\_NAME = "claude-haiku-4-5"

##  Example 1: Article Summarization

In this example, we'll use Claude to generate a JSON summary of an article, including fields for the author, topics, summary, coherence score, persuasion score, and a counterpoint.



tools = [

{

"name": "print\_summary",

"description": "Prints a summary of the article.",

"input\_schema": {

"type": "object",

"properties": {

"author": {"type": "string", "description": "Name of the article author"},

"topics": {

"type": "array",

"items": {"type": "string"},

"description": 'Array of topics, e.g. ["tech", "politics"]. Should be as specific as possible, and can overlap.',

},

"summary": {

"type": "string",

"description": "Summary of the article. One or two paragraphs max.",

},

"coherence": {

"type": "integer",

"description": "Coherence of the article's key points, 0-100 (inclusive)",

},

"persuasion": {

"type": "number",

"description": "Article's persuasion score, 0.0-1.0 (inclusive)",

},

},

"required": ["author", "topics", "summary", "coherence", "persuasion", "counterpoint"],

},

}

]

url = "https://www.anthropic.com/news/third-party-testing"

response = requests.get(url, timeout=30)

soup = BeautifulSoup(response.text, "html.parser")

article = " ".join([p.text for p in soup.find\_all("p")])

query = f"""

<article>

{article}

</article>

Use the `print\_summary` tool.

"""

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=[{"role": "user", "content": query}]

)

json\_summary = None

for content in response.content:

if content.type == "tool\_use" and content.name == "print\_summary":

json\_summary = content.input

break

if json\_summary:

print("JSON Summary:")

print(json.dumps(json\_summary, indent=2))

else:

print("No JSON summary found in the response.")

##  Example 2: Named Entity Recognition

In this example, we'll use Claude to perform named entity recognition on a given text and return the entities in a structured JSON format.



tools = [

{

"name": "print\_entities",

"description": "Prints extract named entities.",

"input\_schema": {

"type": "object",

"properties": {

"entities": {

"type": "array",

"items": {

"type": "object",

"properties": {

"name": {"type": "string", "description": "The extracted entity name."},

"type": {

"type": "string",

"description": "The entity type (e.g., PERSON, ORGANIZATION, LOCATION).",

},

"context": {

"type": "string",

"description": "The context in which the entity appears in the text.",

},

},

"required": ["name", "type", "context"],

},

}

},

"required": ["entities"],

},

}

]

text = "John works at Google in New York. He met with Sarah, the CEO of Acme Inc., last week in San Francisco."

query = f"""

<document>

{text}

</document>

Use the print\_entities tool.

"""

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=[{"role": "user", "content": query}]

)

json\_entities = None

for content in response.content:

if content.type == "tool\_use" and content.name == "print\_entities":

json\_entities = content.input

break

if json\_entities:

print("Extracted Entities (JSON):")

print(json\_entities)

else:

print("No entities found in the response.")



```
Extracted Entities (JSON):
{'entities': [{'name': 'John', 'type': 'PERSON', 'context': 'John works at Google in New York.'}, {'name': 'Google', 'type': 'ORGANIZATION', 'context': 'John works at Google in New York.'}, {'name': 'New York', 'type': 'LOCATION', 'context': 'John works at Google in New York.'}, {'name': 'Sarah', 'type': 'PERSON', 'context': 'He met with Sarah, the CEO of Acme Inc., last week in San Francisco.'}, {'name': 'Acme Inc.', 'type': 'ORGANIZATION', 'context': 'He met with Sarah, the CEO of Acme Inc., last week in San Francisco.'}, {'name': 'San Francisco', 'type': 'LOCATION', 'context': 'He met with Sarah, the CEO of Acme Inc., last week in San Francisco.'}]}
```

##  Example 3: Sentiment Analysis

In this example, we'll use Claude to perform sentiment analysis on a given text and return the sentiment scores in a structured JSON format.



tools = [

{

"name": "print\_sentiment\_scores",

"description": "Prints the sentiment scores of a given text.",

"input\_schema": {

"type": "object",

"properties": {

"positive\_score": {

"type": "number",

"description": "The positive sentiment score, ranging from 0.0 to 1.0.",

},

"negative\_score": {

"type": "number",

"description": "The negative sentiment score, ranging from 0.0 to 1.0.",

},

"neutral\_score": {

"type": "number",

"description": "The neutral sentiment score, ranging from 0.0 to 1.0.",

},

},

"required": ["positive\_score", "negative\_score", "neutral\_score"],

},

}

]

text = "The product was okay, but the customer service was terrible. I probably won't buy from them again."

query = f"""

<text>

{text}

</text>

Use the print\_sentiment\_scores tool.

"""

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=[{"role": "user", "content": query}]

)

json\_sentiment = None

for content in response.content:

if content.type == "tool\_use" and content.name == "print\_sentiment\_scores":

json\_sentiment = content.input

break

if json\_sentiment:

print("Sentiment Analysis (JSON):")

print(json.dumps(json\_sentiment, indent=2))

else:

print("No sentiment analysis found in the response.")



```
Sentiment Analysis (JSON):
{
  "negative_score": 0.6,
  "neutral_score": 0.3,
  "positive_score": 0.1
}
```

##  Example 4: Text Classification

In this example, we'll use Claude to classify a given text into predefined categories and return the classification results in a structured JSON format.



tools = [

{

"name": "print\_classification",

"description": "Prints the classification results.",

"input\_schema": {

"type": "object",

"properties": {

"categories": {

"type": "array",

"items": {

"type": "object",

"properties": {

"name": {"type": "string", "description": "The category name."},

"score": {

"type": "number",

"description": "The classification score for the category, ranging from 0.0 to 1.0.",

},

},

"required": ["name", "score"],

},

}

},

"required": ["categories"],

},

}

]

text = "The new quantum computing breakthrough could revolutionize the tech industry."

query = f"""

<document>

{text}

</document>

Use the print\_classification tool. The categories can be Politics, Sports, Technology, Entertainment, Business.

"""

response = client.messages.create(

model=MODEL\_NAME, max\_tokens=4096, tools=tools, messages=[{"role": "user", "content": query}]

)

json\_classification = None

for content in response.content:

if content.type == "tool\_use" and content.name == "print\_classification":

json\_classification = content.input

break

if json\_classification:

print("Text Classification (JSON):")

print(json.dumps(json\_classification, indent=2))

else:

print("No text classification found in the response.")



```
Text Classification (JSON):
{
  "categories": [
    {
      "name": "Politics",
      "score": 0.1
    },
    {
      "name": "Sports",
      "score": 0.1
    },
    {
      "name": "Technology",
      "score": 0.7
    },
    {
      "name": "Entertainment",
      "score": 0.1
    },
    {
      "name": "Business",
      "score": 0.5
    }
  ]
}
```

##  Example 5: Working with unknown keys

In some cases you may not know the exact JSON object shape up front. In this example we provide an open ended `input_schema` and instruct Claude via prompting how to interact with the tool.



tools = [

{

"name": "print\_all\_characteristics",

"description": "Prints all characteristics which are provided.",

"input\_schema": {"type": "object", "additionalProperties": True},

}

]

query = """Given a description of a character, your task is to extract all the characteristics of the character and print them using the print\_all\_characteristics tool.

The print\_all\_characteristics tool takes an arbitrary number of inputs where the key is the characteristic name and the value is the characteristic value (age: 28 or eye\_color: green).

<description>

The man is tall, with a beard and a scar on his left cheek. He has a deep voice and wears a black leather jacket.

</description>

Now use the print\_all\_characteristics tool."""

response = client.messages.create(

model=MODEL\_NAME,

max\_tokens=4096,

tools=tools,

tool\_choice={"type": "tool", "name": "print\_all\_characteristics"},

messages=[{"role": "user", "content": query}],

)

tool\_output = None

for content in response.content:

if content.type == "tool\_use" and content.name == "print\_all\_characteristics":

tool\_output = content.input

break

if tool\_output:

print("Characteristics (JSON):")

print(json.dumps(json\_classification, indent=2))

else:

print("Something went wrong.")



```
Characteristics (JSON):
{
  "height": "tall",
  "facial_hair": "beard",
  "facial_features": "scar on left cheek",
  "voice": "deep voice",
  "clothing": "black leather jacket"
}
```

These examples demonstrate how you can use Claude and the tool use feature to extract structured JSON data for various natural language processing tasks. By defining custom tools with specific input schemas, you can guide Claude to generate well-structured JSON output that can be easily parsed and utilized in your applications.
