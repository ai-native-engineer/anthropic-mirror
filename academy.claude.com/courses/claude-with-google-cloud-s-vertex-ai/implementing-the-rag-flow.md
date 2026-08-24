<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/implementing-the-rag-flow -->

Lesson 38 of 66 · Claude with Google Cloud's Vertex AIImplementing the RAG flow

Now that we understand the RAG flow conceptually, let's implement it step by step using a practical example. We'll work through all five stages of the RAG process, from chunking text to finding relevant documents for user queries.

## Setting Up the Vector Database

For this implementation, we'll use a custom VectorIndex class that provides the basic functionality we need for storing and searching embeddings. The class handles vector storage, distance calculations (using cosine similarity), and document retrieval.

## The Five-Step RAG Implementation

Let's walk through each step of the RAG process:

### Step 1: Chunk the Text by Section

First, we need to break our source document into manageable chunks. We'll use the same section-based chunking approach from earlier:

python

```
chunks = chunk_by_section(text)
```

This splits our report.md file into logical sections that we can process individually.

### Step 2: Generate Embeddings for Each Chunk

Next, we convert each text chunk into a numerical embedding that captures its semantic meaning:

python

```
embeddings = generate_embedding(chunks)
```

These embeddings allow us to perform mathematical comparisons between different pieces of text.

### Step 3: Store Embeddings in the Vector Database

Now we create our vector store and populate it with our embeddings and their associated text:

python

```
store = VectorIndex()

for embedding, chunk in zip(embeddings, chunks):
    store.add_vector(embedding, {"content": chunk})
```

Notice that we store both the embedding and the original text content. This is crucial because when we retrieve similar embeddings later, we need access to the actual text, not just the numerical vectors. The embedding alone isn't useful to us as developers - we need the human-readable content it represents.

### Step 4: Generate an Embedding for the User Query

When a user asks a question, we need to convert their query into the same embedding space as our stored documents:

python

```
user_embedding = generate_embedding("What did the software engineering dept do last year?")
```

### Step 5: Search for Relevant Documents

Finally, we search our vector store to find the most relevant chunks:

python

```
results = store.search(user_embedding, 2)

for doc, distance in results:
    print(distance, "\n", doc["content"][0:200], "\n")
```

This returns the two most similar chunks along with their cosine distance scores.

![](https://academy.claude.com/assets/media/4bee5dc249e2e187e3cbbc328b8ac07f5239ef6a39c502a991c151de3b061470.png)

The diagram above illustrates how the vector database processes a user query. When we ask a question, it gets converted to an embedding vector, and the database finds the stored vectors that are "closest" to it in the high-dimensional space.

## Understanding the Results

When we run this example with the query about the software engineering department, we get back two relevant sections:

* Section 2: Software Engineering - Project Phoenix Stability Enhancements (distance: 0.71)
* Methodology section (distance: 0.72)

The lower the distance score, the more similar the content is to our query. Both results are relevant to our question about what the software engineering department accomplished.

## Why Store Content with Embeddings

You might wonder why we store the original text alongside each embedding. The reason is practical: embeddings are just arrays of numbers that have no direct meaning to humans. When our search returns the most similar embeddings, we need the actual text content to understand what was found and to use it in generating responses.

Some implementations store just an ID that points back to the original text, but for simplicity, we're storing the content directly with each vector.

## What's Next

This implementation covers the core RAG workflow, but there are still improvements we can make. In real-world applications, you might encounter scenarios where this basic approach doesn't work as expected, and we'll explore those refinements in upcoming sections.
