<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/text-embeddings -->

Lesson 36 of 66 · Claude with Google Cloud's Vertex AIText embeddings

After extracting text chunks from a document, the next step in a RAG pipeline is finding which chunks are most relevant to a user's question. This is essentially a search problem - you need to look through all your chunks and identify the ones that relate to what the user is asking about.

![](https://academy.claude.com/assets/media/5bdbb520520b8a663e1eee52844c40be0df9427e8abeacf52a2e33fa6f0e0a0b.png)

## Semantic Search

The most common approach for finding relevant chunks is semantic search. Unlike traditional keyword-based search, semantic search uses text embeddings to understand the actual meaning of both the user's question and each text chunk. This allows the system to find conceptually related content even when the exact words don't match.

![](https://academy.claude.com/assets/media/952c238e944430644b7ce72e79e11fe8f66e8f20be31104a4297a303da10e432.png)

## What Are Text Embeddings?

A text embedding is a numerical representation of the meaning contained in some text. Think of it as converting words and sentences into a format that computers can work with mathematically.

![](https://academy.claude.com/assets/media/5126d0bcc653475f702151e4cff43edeb4a70c94315da05688a4ec5072fc7ab5.png)

Here's how the process works:

* You feed text into an embedding model
* The model outputs a long list of numbers (the embedding)
* Each number ranges from -1 to +1
* These numbers represent different qualities or features of the input text

## Understanding the Numbers

Each number in an embedding is essentially a "score" for some quality of the input text. However, here's the important caveat: we don't actually know what each specific number represents.

![](https://academy.claude.com/assets/media/bcff1d5482df41d7d7196a0dcbdc6f27892114a53102a3aca0fc0537fb8f742a.png)

While it's helpful to imagine that one number might represent "how happy the text is" and another might represent "how much the text talks about oceans," these are just conceptual examples. The embedding model learns these features during training, but they're not explicitly labeled or interpretable to us.

Despite this opacity, embeddings are incredibly powerful because they capture semantic meaning in a way that allows for mathematical comparison between different pieces of text.

## Embeddings on Vertex AI

Claude can't generate embeddings directly. Instead, you need to use a specialized embedding model. On Vertex AI, the model we'll use is called `text-embedding-005`.

![](https://academy.claude.com/assets/media/c353c4d3d6190d0a1c8f12954515f17cd2ef95ae7a0758346164bcf957b4b249.png)

## Implementation

To work with embeddings on Vertex AI, you'll need to install the Google GenAI SDK:

bash

```
pip install google-genai
```

Here's the basic setup for generating embeddings:

python

```
from google import genai

client = genai.Client(
    project="YOUR_PROJECT_ID",
    location="global",
    vertexai=True
)

def generate_embedding(text):
    response = client.models.embed_content(
        model="text-embedding-005",
        contents=text
    )

    if not response.embeddings:
        return []

    return [e.values for e in response.embeddings]
```

When you run this function with a text chunk, you'll get back a list of floating-point numbers representing the semantic meaning of that text. These embeddings form the foundation for implementing semantic search in your RAG system.

The next step is understanding how to use these embeddings to actually find the most relevant chunks for a user's question, which involves comparing embeddings mathematically to determine similarity.
