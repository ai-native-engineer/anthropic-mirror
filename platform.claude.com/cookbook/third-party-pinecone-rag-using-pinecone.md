<!-- source: https://platform.claude.com/cookbook/third-party-pinecone-rag-using-pinecone -->

#  Retrieval-Augmented Generation using Pinecone

This notebook demonstrates how to connect Claude with the data in your Pinecone vector database through a technique called retrieval-augmented generation (RAG). We will cover the following steps:

1. Embedding a dataset using Voyage AI's embedding model
2. Uploading the embeddings to a Pinecone index
3. Retrieving information from the vector database
4. Using Claude to answer questions with information from the database

##  Setup

First, let's install the necessary libraries and set the API keys we will need to use in this notebook. We will need to get a [Claude API key(opens in new tab)](https://docs.claude.com/claude/reference/getting-started-with-the-api), a free [Pinecone API key(opens in new tab)](https://docs.pinecone.io/docs/quickstart), and a free [Voyage AI API key(opens in new tab)](https://docs.voyageai.com/install/).

%pip install anthropic datasets pinecone-client voyageai

# Insert your API keys here

ANTHROPIC\_API\_KEY = "<YOUR\_ANTHROPIC\_API\_KEY>"

PINECONE\_API\_KEY = "<YOUR\_PINECONE\_API\_KEY>"

VOYAGE\_API\_KEY = "<YOUR\_VOYAGE\_API\_KEY>"

##  Download the dataset

Now let's download the Amazon products dataset which has over 10k Amazon product descriptions and load it into a DataFrame.

import pandas as pd

# Download the JSONL file

!wget https://www-cdn.anthropic.com/48affa556a5af1de657d426bcc1506cdf7e2f68e/amazon-products.jsonl

data = []

with open("amazon-products.jsonl") as file:

for line in file:

try:

data.append(eval(line)) # noqa: S307

except (SyntaxError, ValueError):

# Skip malformed lines in the dataset

pass

df = pd.DataFrame(data)

display(df.head())

len(df)

##  Vector Database

To create our vector database, we first need a free API key from Pinecone. Once we have the key, we can initialize the database as follows:

from pinecone import Pinecone

pc = Pinecone(api\_key=PINECONE\_API\_KEY)

Next, we set up our index specification, which allows us to define the cloud provider and region where we want to deploy our index. You can find a list of all available providers and regions [here(opens in new tab)](https://www.pinecone.io/docs/data-types/metadata/).

from pinecone import ServerlessSpec

spec = ServerlessSpec(cloud="aws", region="us-west-2")

Then, we initialize the index. We will be using Voyage's "voyage-2" model for creating the embeddings, so we set the dimension to 1024.

import time

index\_name = "amazon-products"

existing\_indexes = [index\_info["name"] for index\_info in pc.list\_indexes()]

# check if index already exists (it shouldn't if this is first time)

if index\_name not in existing\_indexes:

# if does not exist, create index

pc.create\_index(

index\_name,

dimension=1024, # dimensionality of voyage-2 embeddings

metric="dotproduct",

spec=spec,

)

# wait for index to be initialized

while not pc.describe\_index(index\_name).status["ready"]:

time.sleep(1)

# connect to index

index = pc.Index(index\_name)

time.sleep(1)

# view index stats

index.describe\_index\_stats()

We should see that the new Pinecone index has a total\_vector\_count of 0, as we haven't added any vectors yet.

##  Embeddings

To get started with Voyage's embeddings, go [here(opens in new tab)](https://www.voyageai.com) to get an API key.

Now let's set up our Voyage client and demonstrate how to create an embedding using the `embed` method. To learn more about using Voyage embeddings with Claude, see [this notebook(opens in new tab)](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md).

import voyageai

vo = voyageai.Client(api\_key=VOYAGE\_API\_KEY)

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-2", input\_type="document")

print(result.embeddings[0])

print(result.embeddings[1])

##  Uploading data to the Pinecone index

With our embedding model set up, we can now take our product descriptions, embed them, and upload the embeddings to the Pinecone index.

from time import sleep

from tqdm.auto import tqdm

descriptions = df["text"].tolist()

batch\_size = 100 # how many embeddings we create and insert at once

for i in tqdm(range(0, len(descriptions), batch\_size)):

# find end of batch

i\_end = min(len(descriptions), i + batch\_size)

descriptions\_batch = descriptions[i:i\_end]

# create embeddings (try-except added to avoid RateLimitError. Voyage currently allows 300/requests per minute.)

done = False

while not done:

try:

res = vo.embed(descriptions\_batch, model="voyage-2", input\_type="document")

done = True

except Exception:

sleep(5)

embeds = [record for record in res.embeddings]

# create unique IDs for each text

ids\_batch = [f"description\_{idx}" for idx in range(i, i\_end)]

# Create metadata dictionaries for each text

metadata\_batch = [{"description": description} for description in descriptions\_batch]

to\_upsert = list(zip(ids\_batch, embeds, metadata\_batch, strict=False))

# upsert to Pinecone

index.upsert(vectors=to\_upsert)

##  Making queries

With our index populated, we can start making queries to get results. We can take a natural language question, embed it, and query it against the index to return semantically similar product descriptions.

USER\_QUESTION = (

"I want to get my daughter more interested in science. What kind of gifts should I get her?"

)

question\_embed = vo.embed([USER\_QUESTION], model="voyage-2", input\_type="query")

results = index.query(vector=question\_embed.embeddings, top\_k=5, include\_metadata=True)

results

```
{'matches': [{'id': 'description_1771',
              'metadata': {'description': 'Product Name: Scientific Explorer '
                                          'My First Science Kids Science '
                                          'Experiment Kit\n'
                                          '\n'
                                          'About Product: Experiments to spark '
                                          'creativity and curiosity | Grow '
                                          'watery crystals, create a rainbow '
                                          'in a plate, explore the science of '
                                          'color and more | Represents STEM '
                                          '(Science, Technology, Engineering, '
                                          'Math) principles – open ended toys '
                                          'to construct, engineer, explorer '
                                          'and experiment | Includes cross '
                                          'linked polyacrylamide, 3 color '
                                          'tablets, 3 mixing cups, 3 test '
                                          'tubes, caps and stand, pipette, '
                                          'mixing tray, magnifier and '
                                          'instructions | Recommended for '
                                          'children 4 years of age and older '
                                          'with adult supervision\n'
                                          '\n'
                                          'Categories: Toys & Games | Learning '
                                          '& Education | Science Kits & Toys'},
              'score': 0.772703767,
              'values': []},
             {'id': 'description_3133',
              'metadata': {'description': 'Product Name: Super Science Magnet '
                                          'Kit.\n'
                                          '\n'
                                          'About Product: \n'
                                          '\n'
                                          'Categories: Toys & Games | Learning '
                                          '& Education | Science Kits & Toys'},
              'score': 0.765997052,
              'values': []},
             {'id': 'description_1792',
              'metadata': {'description': 'Product Name: BRIGHT Atom Model - '
                                          'Student\n'
                                          '\n'
                                          'About Product: \n'
                                          '\n'
                                          'Categories: Toys & Games | Learning '
                                          '& Education | Science Kits & Toys'},
              'score': 0.765654,
              'values': []},
             {'id': 'description_1787',
              'metadata': {'description': 'Product Name: Thames & Kosmos '
                                          'Biology Genetics and DNA\n'
                                          '\n'
                                          'About Product: Learn the basics of '
                                          'genetics and DNA. | Assemble a '
                                          'model to see the elegant '
                                          'double-stranded Helical structure '
                                          "of DNA. | A parents' Choice Gold "
                                          'award winner | 20 experiments in '
                                          'the 48 page full color experiment '
                                          'manual and learning guide\n'
                                          '\n'
                                          'Categories: Toys & Games | Learning '
                                          '& Education | Science Kits & Toys'},
              'score': 0.765174091,
              'values': []},
             {'id': 'description_120',
              'metadata': {'description': 'Product Name: Educational Insights '
                                          "Nancy B's Science Club Binoculars "
                                          'and Wildlife Activity Journal\n'
                                          '\n'
                                          'About Product: From bird search and '
                                          'ecosystem challenges to creative '
                                          'writing and drawing exercises, this '
                                          'set is perfect for the nature lover '
                                          'in your life! | Includes 4x '
                                          'magnification binoculars and '
                                          '22-page activity journal packed '
                                          'with scientific activities! | '
                                          'Binoculars are lightweight, yet '
                                          'durable. | Supports STEM learning, '
                                          'providing hands-on experience with '
                                          'a key scientific tool. | Great '
                                          'introductory tool for young '
                                          'naturalists on-the-go! | Part of '
                                          "the Nancy B's Science Club line, "
                                          'designed to encourage scientific '
                                          'confidence. | Winner of the '
                                          "Parents' Choice Recommended Award. "
                                          '| Scientific experience designed '
                                          'specifically for kids ages 8-11.\n'
                                          '\n'
                                          'Categories: Electronics | Camera & '
                                          'Photo | Binoculars & Scopes | '
                                          'Binoculars'},
              'score': 0.765075564,
              'values': []}],
 'namespace': '',
 'usage': {'read_units': 6}}
```

##  Optimizing search

These results are good, but we can optimize them even further. Using Claude, we can take the user's question and generate search keywords from it. This allows us to perform a wide, diverse search over the index to get more relevant product descriptions.

import anthropic

client = anthropic.Anthropic(api\_key=ANTHROPIC\_API\_KEY)

def get\_completion(prompt):

completion = client.completions.create(

model="claude-2.1",

prompt=prompt,

max\_tokens\_to\_sample=1024,

)

return completion.completion

def create\_keyword\_prompt(question):

return f"""\n\nHuman: Given a question, generate a list of 5 very diverse search keywords that can be used to search for products on Amazon.

The question is: {question}

Output your keywords as a JSON that has one property "keywords" that is a list of strings. Only output valid JSON.\n\nAssistant:{{"""

With our Anthropic client setup and our prompt created, we can now begin to generate keywords from the question. We will output the keywords in a JSON object so we can easily parse them from Claude's output.

keyword\_json = "{" + get\_completion(create\_keyword\_prompt(USER\_QUESTION))

print(keyword\_json)

import json

# Extract the keywords from the JSON

data = json.loads(keyword\_json)

keywords\_list = data["keywords"]

print(keywords\_list)

Now with our keywords in a list, let's embed each one, query it against the index, and return the top 3 most relevant product descriptions.

results\_list = []

for keyword in keywords\_list:

# get the embeddings for the keywords

query\_embed = vo.embed([keyword], model="voyage-2", input\_type="query")

# search for the embeddings in the Pinecone index

search\_results = index.query(vector=query\_embed.embeddings, top\_k=3, include\_metadata=True)

# append the search results to the list

for search\_result in search\_results.matches:

results\_list.append(search\_result["metadata"]["description"])

print(len(results\_list))

##  Answering with Claude

Now that we have a list of product descriptions, let's format them into a search template Claude has been trained with and pass the formatted descriptions into another prompt.

# Formatting search results

def format\_results(extracted: list[str]) -> str:

result = "\n".join(

[

f'<item index="{i + 1}">\n<page\_content>\n{r}\n</page\_content>\n</item>'

for i, r in enumerate(extracted)

]

)

return f"\n<search\_results>\n{result}\n</search\_results>"

def create\_answer\_prompt(results\_list, question):

return f"""\n\nHuman: {format\_results(results\_list)} Using the search results provided within the <search\_results></search\_results> tags, please answer the following question <question>{question}</question>. Do not reference the search results in your answer.\n\nAssistant:"""

Finally, let's ask the original user's question and get our answer from Claude.

answer = get\_completion(create\_answer\_prompt(results\_list, USER\_QUESTION))

print(answer)

```
To get your daughter more interested in science, I would recommend getting her an age-appropriate science kit or set that allows for hands-on exploration and experimentation. For example, for a younger child you could try a beginner chemistry set, magnet set, or crystal growing kit. For an older child, look for kits that tackle more advanced scientific principles like physics, engineering, robotics, etc. The key is choosing something that sparks her natural curiosity and lets her actively investigate concepts through activities, observations, and discovery. Supplement the kits with science books, museum visits, documentaries, and conversations about science she encounters in everyday life. Making science fun and engaging is crucial for building her interest.
```
