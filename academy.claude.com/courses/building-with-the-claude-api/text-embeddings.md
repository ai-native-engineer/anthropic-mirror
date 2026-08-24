<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/text-embeddings -->

Lesson 34 of 67 · Building with the Claude APIText embeddings

After breaking a document into chunks, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is essentially a search problem - you need to look through all your text chunks and identify the ones that relate to what the user is asking about.

![](https://academy.claude.com/assets/media/974fa9d12a1524d19e048317f4f35b378a1902c079fe4d3af09c7c0e836c3c65.jpg)

## Semantic Search

The most common approach for finding relevant chunks is semantic search. Unlike keyword-based search that looks for exact word matches, semantic search uses text embeddings to understand the meaning and context of both the user's question and each text chunk.

![](https://academy.claude.com/assets/media/3325be08d94ce03a851f4c322d35ff96cfa8204b7059106d9afc0e4868d3ec21.jpg)

## Text Embeddings

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

![](https://academy.claude.com/assets/media/daed6b6448ba1ee01ebfc2c569d5402d42fae6a27e7cab17820de9983390343a.jpg)

Here's how the process works:

* You feed text into an embedding model
* The model outputs a long list of numbers (the embedding)
* Each number ranges from -1 to +1
* These numbers represent different qualities or features of the input text

## Understanding the Numbers

Each number in an embedding is essentially a "score" for some quality of the input text. However, here's the important caveat: we don't know precisely what each number represents.

![](https://academy.claude.com/assets/media/1ba79edd89af76870de1a2e598fdba5bf1999248ad3a51598d9d7b9eb0a1464d.jpg)

While it's helpful to imagine that one number might represent "how happy the text is" or "how much the text talks about oceans," these are just conceptual examples. The actual meaning of each dimension is learned by the model during training and isn't directly interpretable by humans.

## VoyageAI for Embeddings

Since Anthropic doesn't currently provide embedding generation, the recommended provider is VoyageAI. You'll need to:

* Sign up for a separate VoyageAI account
* Get an API key (free to get started)
* Add the key to your environment variables

![](https://academy.claude.com/assets/media/ce8910552c50c71fe19d0c7826855c3af57a2d9b9d5c01014fff66ecdf9582d4.jpg)

In your `.env` file, add:

bash

```
VOYAGE_API_KEY="your_key_here"
```

## Implementation

First, install the VoyageAI library:

bash

```
%pip install voyageai
```

Then set up the client and create a function to generate embeddings:

python

```
from dotenv import load_dotenv
import voyageai

load_dotenv()
client = voyageai.Client()

def generate_embedding(text, model="voyage-3-large", input_type="query"):
    result = client.embed([text], model=model, input_type=input_type)
    return result.embeddings[0]
```

![](https://academy.claude.com/assets/media/458bbee724a04696d648d5b0db1b8bbcf5ce7f07369ab9e01ab50a1a9bb9a7cf.jpg)

When you run this function on a text chunk, you'll get back a list of floating-point numbers representing the embedding. The process is quick and straightforward - the real challenge is understanding how to use these embeddings effectively in your RAG pipeline for finding the most relevant content.

![](https://academy.claude.com/assets/media/6cdd71446c9d39fbdfd455c4b73f032d4b70a713a03f9dcfb0d5c4ce2c2ac52d.jpg)

The next step is learning how to compare embeddings to determine which chunks are most similar to a user's question, which forms the core of the semantic search process.
