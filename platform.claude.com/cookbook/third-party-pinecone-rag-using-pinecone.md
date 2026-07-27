<!-- source: https://platform.claude.com/cookbook/third-party-pinecone-rag-using-pinecone -->

# Retrieval-Augmented Generation using Pinecone

This notebook demonstrates how to connect Claude with the data in your Pinecone vector database through a technique called retrieval-augmented generation (RAG). We will cover the following steps:

1. Embedding a dataset using Voyage AI's embedding model
2. Uploading the embeddings to a Pinecone index
3. Retrieving information from the vector database
4. Using Claude to answer questions with information from the database

## Setup

First, let's install the necessary libraries and set the API keys we will need to use in this notebook. We will need to get a [Claude API key](https://docs.claude.com/claude/reference/getting-started-with-the-api), a free [Pinecone API key](https://docs.pinecone.io/docs/quickstart), and a free [Voyage AI API key](https://docs.voyageai.com/install/).

python

```
%pip install anthropic datasets pinecone-client voyageai
```

python

```
# Insert your API keys here
ANTHROPIC_API_KEY = "<YOUR_ANTHROPIC_API_KEY>"
PINECONE_API_KEY = "<YOUR_PINECONE_API_KEY>"
VOYAGE_API_KEY = "<YOUR_VOYAGE_API_KEY>"
```

## Download the dataset

Now let's download the Amazon products dataset which has over 10k Amazon product descriptions and load it into a DataFrame.

python

```
import pandas as pd

# Download the JSONL file
!wget  https://www-cdn.anthropic.com/48affa556a5af1de657d426bcc1506cdf7e2f68e/amazon-products.jsonl

data = []
with open("amazon-products.jsonl") as file:
    for line in file:
        try:
            data.append(eval(line))  # noqa: S307
        except (SyntaxError, ValueError):
            # Skip malformed lines in the dataset
            pass

df = pd.DataFrame(data)
display(df.head())
len(df)
```

## Vector Database

To create our vector database, we first need a free API key from Pinecone. Once we have the key, we can initialize the database as follows:

python

```
from pinecone import Pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)
```

Next, we set up our index specification, which allows us to define the cloud provider and region where we want to deploy our index. You can find a list of all available providers and regions [here](https://www.pinecone.io/docs/data-types/metadata/).

python

```
from pinecone import ServerlessSpec

spec = ServerlessSpec(cloud="aws", region="us-west-2")
```

Then, we initialize the index. We will be using Voyage's "voyage-2" model for creating the embeddings, so we set the dimension to 1024.

python

```
import time

index_name = "amazon-products"
existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

# check if index already exists (it shouldn't if this is first time)
if index_name not in existing_indexes:
    # if does not exist, create index
    pc.create_index(
        index_name,
        dimension=1024,  # dimensionality of voyage-2 embeddings
        metric="dotproduct",
        spec=spec,
    )
    # wait for index to be initialized
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

# connect to index
index = pc.Index(index_name)
time.sleep(1)
# view index stats
index.describe_index_stats()
```

We should see that the new Pinecone index has a total\_vector\_count of 0, as we haven't added any vectors yet.

## Embeddings

To get started with Voyage's embeddings, go [here](https://www.voyageai.com) to get an API key.

Now let's set up our Voyage client and demonstrate how to create an embedding using the `embed` method. To learn more about using Voyage embeddings with Claude, see [this notebook](https://github.com/anthropics/anthropic-cookbook/blob/main/third_party/VoyageAI/how_to_create_embeddings.md).

python

```
import voyageai

vo = voyageai.Client(api_key=VOYAGE_API_KEY)

texts = ["Sample text 1", "Sample text 2"]

result = vo.embed(texts, model="voyage-2", input_type="document")
print(result.embeddings[0])
print(result.embeddings[1])
```

## Uploading data to the Pinecone index

With our embedding model set up, we can now take our product descriptions, embed them, and upload the embeddings to the Pinecone index.

python

```
from time import sleep

from tqdm.auto import tqdm

descriptions = df["text"].tolist()
batch_size = 100  # how many embeddings we create and insert at once

for i in tqdm(range(0, len(descriptions), batch_size)):
    # find end of batch
    i_end = min(len(descriptions), i + batch_size)
    descriptions_batch = descriptions[i:i_end]
    # create embeddings (try-except added to avoid RateLimitError. Voyage currently allows 300/requests per minute.)
    done = False
    while not done:
        try:
            res = vo.embed(descriptions_batch, model="voyage-2", input_type="document")
            done = True
        except Exception:
            sleep(5)

    embeds = [record for record in res.embeddings]
    # create unique IDs for each text
    ids_batch = [f"description_{idx}" for idx in range(i, i_end)]

    # Create metadata dictionaries for each text
    metadata_batch = [{"description": description} for description in descriptions_batch]

    to_upsert = list(zip(ids_batch, embeds, metadata_batch, strict=False))

    # upsert to Pinecone
    index.upsert(vectors=to_upsert)
```

## Making queries

With our index populated, we can start making queries to get results. We can take a natural language question, embed it, and query it against the index to return semantically similar product descriptions.

python

```
USER_QUESTION = (
    "I want to get my daughter more interested in science. What kind of gifts should I get her?"
)

question_embed = vo.embed([USER_QUESTION], model="voyage-2", input_type="query")
results = index.query(vector=question_embed.embeddings, top_k=5, include_metadata=True)
results
```

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

## Optimizing search

These results are good, but we can optimize them even further. Using Claude, we can take the user's question and generate search keywords from it. This allows us to perform a wide, diverse search over the index to get more relevant product descriptions.

python

```
import anthropic

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

def get_completion(prompt):
    completion = client.completions.create(
        model="claude-2.1",
        prompt=prompt,
        max_tokens_to_sample=1024,
    )
    return completion.completion
```

python

```
def create_keyword_prompt(question):
    return f"""\n\nHuman: Given a question, generate a list of 5 very diverse search keywords that can be used to search for products on Amazon.

The question is: {question}

Output your keywords as a JSON that has one property "keywords" that is a list of strings. Only output valid JSON.\n\nAssistant:{{"""
```

With our Anthropic client setup and our prompt created, we can now begin to generate keywords from the question. We will output the keywords in a JSON object so we can easily parse them from Claude's output.

python

```
keyword_json = "{" + get_completion(create_keyword_prompt(USER_QUESTION))
print(keyword_json)
```

python

```
import json

# Extract the keywords from the JSON
data = json.loads(keyword_json)
keywords_list = data["keywords"]
print(keywords_list)
```

Now with our keywords in a list, let's embed each one, query it against the index, and return the top 3 most relevant product descriptions.

python

```
results_list = []
for keyword in keywords_list:
    # get the embeddings for the keywords
    query_embed = vo.embed([keyword], model="voyage-2", input_type="query")
    # search for the embeddings in the Pinecone index
    search_results = index.query(vector=query_embed.embeddings, top_k=3, include_metadata=True)
    # append the search results to the list
    for search_result in search_results.matches:
        results_list.append(search_result["metadata"]["description"])
print(len(results_list))
```

## Answering with Claude

Now that we have a list of product descriptions, let's format them into a search template Claude has been trained with and pass the formatted descriptions into another prompt.

python

```
# Formatting search results
def format_results(extracted: list[str]) -> str:
    result = "\n".join(
        [
            f'<item index="{i + 1}">\n<page_content>\n{r}\n</page_content>\n</item>'
            for i, r in enumerate(extracted)
        ]
    )

    return f"\n<search_results>\n{result}\n</search_results>"

def create_answer_prompt(results_list, question):
    return f"""\n\nHuman: {format_results(results_list)} Using the search results provided within the <search_results></search_results> tags, please answer the following question <question>{question}</question>. Do not reference the search results in your answer.\n\nAssistant:"""
```

Finally, let's ask the original user's question and get our answer from Claude.

python

```
answer = get_completion(create_answer_prompt(results_list, USER_QUESTION))
print(answer)
```

```
To get your daughter more interested in science, I would recommend getting her an age-appropriate science kit or set that allows for hands-on exploration and experimentation. For example, for a younger child you could try a beginner chemistry set, magnet set, or crystal growing kit. For an older child, look for kits that tackle more advanced scientific principles like physics, engineering, robotics, etc. The key is choosing something that sparks her natural curiosity and lets her actively investigate concepts through activities, observations, and discovery. Supplement the kits with science books, museum visits, documentaries, and conversations about science she encounters in everyday life. Making science fun and engaging is crucial for building her interest.
```
