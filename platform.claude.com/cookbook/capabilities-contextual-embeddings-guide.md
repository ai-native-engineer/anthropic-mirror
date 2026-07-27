<!-- source: https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide -->

# Enhancing RAG with Contextual Retrieval

> Note: For more background information on Contextual Retrieval, including additional performance evaluations on various datasets, we recommend reading our accompanying [blog post](https://www.anthropic.com/news/contextual-retrieval).

Retrieval Augmented Generation (RAG) enables Claude to leverage your internal knowledge bases, codebases, or any other corpus of documents when providing a response. Enterprises are increasingly building RAG applications to improve workflows in customer support, Q&A over internal company documents, financial & legal analysis, code generation, and much more.

In a [separate guide](https://github.com/anthropics/anthropic-cookbook/blob/main/capabilities/retrieval_augmented_generation/guide.ipynb), we walked through setting up a basic retrieval system, demonstrated how to evaluate its performance, and then outlined a few techniques to improve performance. In this guide, we present a technique for improving retrieval performance: Contextual Embeddings.

In traditional RAG, documents are typically split into smaller chunks for efficient retrieval. While this approach works well for many applications, it can lead to problems when individual chunks lack sufficient context. Contextual Embeddings solve this problem by adding relevant context to each chunk before embedding. This method improves the quality of each embedded chunk, allowing for more accurate retrieval and thus better overall performance. Averaged across all data sources we tested, Contextual Embeddings reduced the top-20-chunk retrieval failure rate by 35%.

The same chunk-specific context can also be used with BM25 search to further improve retrieval performance. We introduce this technique in the "Contextual BM25" section.

In this guide, we'll demonstrate how to build and optimize a Contextual Retrieval system using a dataset of 9 codebases as our knowledge base. We'll walk through:

1. Setting up a basic retrieval pipeline to establish a baseline for performance.
2. Contextual Embeddings: what it is, why it works, and how prompt caching makes it practical for production use cases.
3. Implementing Contextual Embeddings and demonstrating performance improvements.
4. Contextual BM25: improving performance with *contextual* BM25 hybrid search.
5. Improving performance with reranking,

### Evaluation Metrics & Dataset:

We use a pre-chunked dataset of 9 codebases - all of which have been chunked according to a basic character splitting mechanism. Our evaluation dataset contains 248 queries - each of which contains a 'golden chunk.' We'll use a metric called Pass@k to evaluate performance. Pass@k checks whether or not the 'golden document' was present in the first k documents retrieved for each query. Contextual Embeddings in this case helped us to improve Pass@10 performance from ~87% --> ~95%.

You can find the code files and their chunks in `data/codebase_chunks.json` and the evaluation dataset in `data/evaluation_set.jsonl`

#### Additional Notes:

Prompt caching is helpful in managing costs when using this retrieval method. This feature is currently available on Anthropic's first-party API, and is coming soon to our third-party partner environments in AWS Bedrock and GCP Vertex. We know that many of our customers leverage AWS Knowledge Bases and GCP Vertex AI APIs when building RAG solutions, and this method can be used on either platform with a bit of customization. Consider reaching out to Anthropic or your AWS/GCP account team for guidance on this!

To make it easier to use this method on Bedrock, the AWS team has provided us with code that you can use to implement a Lambda function that adds context to each document. If you deploy this Lambda function, you can select it as a custom chunking option when configuring a [Bedrock Knowledge Base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html). You can find this code in `contextual-rag-lambda-function`. The main lambda function code is in `lambda_function.py`.

## Table of Contents

1. Setup
2. Basic RAG
3. Contextual Embeddings
4. Contextual BM25
5. Reranking

## Setup

Before starting this guide, ensure you have:

**Technical Skills:**

* Intermediate Python programming
* Basic understanding of RAG (Retrieval Augmented Generation)
* Familiarity with vector databases and embeddings
* Basic command-line proficiency

**System Requirements:**

* Python 3.8+
* Docker installed and running (optional, for BM25 search)
* 4GB+ available RAM
* ~5-10 GB disk space for vector databases

**API Access:**

* [Anthropic API key](https://console.anthropic.com/) (free tier sufficient)
* [Voyage AI API key](https://www.voyageai.com/)
* [Cohere API key](https://cohere.com/)

**Time & Cost:**

* Expected completion time: 30-45 minutes
* API costs: ~$5-10 to run through the full dataset

### Libraries

We'll need a few libraries, including:

1. `anthropic` - to interact with Claude
2. `voyageai` - to generate high quality embeddings
3. `cohere` - for reranking
4. `elasticsearch` for performant BM25 search
5. `pandas`, `numpy`, `matplotlib`, and `scikit-learn` for data manipulation and visualization

### Environment Variables

Ensure the following environment variables are set:

```
- VOYAGE_API_KEY
- ANTHROPIC_API_KEY
- COHERE_API_KEY
```

python

```
%%capture
!pip install --upgrade anthropic voyageai cohere elasticsearch pandas numpy
```

We define our model names up front to make it easier to change models as new models are released

python

```
MODEL_NAME = "claude-haiku-4-5"
```

We'll start by initializing the Anthropic client that we'll use for generating contextual descriptions.

python

```
import os

import anthropic

client = anthropic.Anthropic(
    # This is the default and can be omitted
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)
```

## Initialize a Vector DB Class

We'll create a VectorDB class to handle embedding storage and similarity search. This class serves three key functions in our RAG pipeline:

1. **Embedding Generation**: Converts text chunks into vector representations using Voyage AI's embedding model
2. **Storage & Caching**: Saves embeddings to disk to avoid re-computing them (which saves time and API costs)
3. **Similarity Search**: Retrieves the most relevant chunks for a given query using cosine similarity

For this guide, we're using a simple in-memory vector database with pickle serialization. This makes the code easy to understand and requires no external dependencies. The class automatically saves embeddings to disk after generation, so you only pay the embedding cost once.

For production use, consider hosted vector database solutions.

The VectorDB class below follows the same interface patterns you'd use with production solutions, making it easy to swap out later. Key features include batch processing (128 chunks at a time), progress tracking with tqdm, and query caching to speed up repeated searches during evaluation.

python

```
import json
import pickle
from typing import Any

import numpy as np
import voyageai
from tqdm import tqdm

class VectorDB:
    def __init__(self, name: str, api_key=None):
        if api_key is None:
            api_key = os.getenv("VOYAGE_API_KEY")
        self.client = voyageai.Client(api_key=api_key)
        self.name = name
        self.embeddings = []
        self.metadata = []
        self.query_cache = {}
        self.db_path = f"./data/{name}/vector_db.pkl"

    def load_data(self, dataset: list[dict[str, Any]]):
        if self.embeddings and self.metadata:
            print("Vector database is already loaded. Skipping data loading.")
            return
        if os.path.exists(self.db_path):
            print("Loading vector database from disk.")
            self.load_db()
            return

        texts_to_embed = []
        metadata = []
        total_chunks = sum(len(doc["chunks"]) for doc in dataset)

        with tqdm(total=total_chunks, desc="Processing chunks") as pbar:
            for doc in dataset:
                for chunk in doc["chunks"]:
                    texts_to_embed.append(chunk["content"])
                    metadata.append(
                        {
                            "doc_id": doc["doc_id"],
                            "original_uuid": doc["original_uuid"],
                            "chunk_id": chunk["chunk_id"],
                            "original_index": chunk["original_index"],
                            "content": chunk["content"],
                        }
                    )
                    pbar.update(1)

        self._embed_and_store(texts_to_embed, metadata)
        self.save_db()

        print(f"Vector database loaded and saved. Total chunks processed: {len(texts_to_embed)}")

    def _embed_and_store(self, texts: list[str], data: list[dict[str, Any]]):
        batch_size = 128
        with tqdm(total=len(texts), desc="Embedding chunks") as pbar:
            result = []
            for i in range(0, len(texts), batch_size):
                batch = texts[i : i + batch_size]
                batch_result = self.client.embed(batch, model="voyage-2").embeddings
                result.extend(batch_result)
                pbar.update(len(batch))

        self.embeddings = result
        self.metadata = data

    def search(self, query: str, k: int = 20) -> list[dict[str, Any]]:
        if query in self.query_cache:
            query_embedding = self.query_cache[query]
        else:
            query_embedding = self.client.embed([query], model="voyage-2").embeddings[0]
            self.query_cache[query] = query_embedding

        if not self.embeddings:
            raise ValueError("No data loaded in the vector database.")

        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[::-1][:k]

        top_results = []
        for idx in top_indices:
            result = {
                "metadata": self.metadata[idx],
                "similarity": float(similarities[idx]),
            }
            top_results.append(result)

        return top_results

    def save_db(self):
        data = {
            "embeddings": self.embeddings,
            "metadata": self.metadata,
            "query_cache": json.dumps(self.query_cache),
        }
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "wb") as file:
            pickle.dump(data, file)

    def load_db(self):
        if not os.path.exists(self.db_path):
            raise ValueError(
                "Vector database file not found. Use load_data to create a new database."
            )
        with open(self.db_path, "rb") as file:
            data = pickle.load(file)
        self.embeddings = data["embeddings"]
        self.metadata = data["metadata"]
        self.query_cache = json.loads(data["query_cache"])
```

Now we can use this class to load our dataset

python

```
# Load your transformed dataset
with open("data/codebase_chunks.json") as f:
    transformed_dataset = json.load(f)

# Initialize the VectorDB
base_db = VectorDB("base_db")

# Load and process the data
base_db.load_data(transformed_dataset)
```

```
Processing chunks: 100%|██████████| 737/737 [00:00<00:00, 985400.72it/s]
Embedding chunks: 100%|██████████| 737/737 [00:42<00:00, 17.28it/s]
Vector database loaded and saved. Total chunks processed: 737
```

## Basic RAG

To get started, we'll set up a basic RAG pipeline using a bare bones approach. This is sometimes called 'Naive RAG' by many in the industry. A basic RAG pipeline includes the following 3 steps:

1. Chunk documents by heading - containing only the content from each subheading
2. Embed each document
3. Use Cosine similarity to retrieve documents in order to answer query

python

```
import json
from collections.abc import Callable
from typing import Any

from tqdm import tqdm

def load_jsonl(file_path: str) -> list[dict[str, Any]]:
    """Load JSONL file and return a list of dictionaries."""
    with open(file_path) as file:
        return [json.loads(line) for line in file]

def evaluate_retrieval(
    queries: list[dict[str, Any]], retrieval_function: Callable, db, k: int = 20
) -> dict[str, float]:
    total_score = 0
    total_queries = len(queries)

    for query_item in tqdm(queries, desc="Evaluating retrieval"):
        query = query_item["query"]
        golden_chunk_uuids = query_item["golden_chunk_uuids"]

        # Find all golden chunk contents
        golden_contents = []
        for doc_uuid, chunk_index in golden_chunk_uuids:
            golden_doc = next(
                (doc for doc in query_item["golden_documents"] if doc["uuid"] == doc_uuid), None
            )
            if not golden_doc:
                print(f"Warning: Golden document not found for UUID {doc_uuid}")
                continue

            golden_chunk = next(
                (chunk for chunk in golden_doc["chunks"] if chunk["index"] == chunk_index), None
            )
            if not golden_chunk:
                print(
                    f"Warning: Golden chunk not found for index {chunk_index} in document {doc_uuid}"
                )
                continue

            golden_contents.append(golden_chunk["content"].strip())

        if not golden_contents:
            print(f"Warning: No golden contents found for query: {query}")
            continue

        retrieved_docs = retrieval_function(query, db, k=k)

        # Count how many golden chunks are in the top k retrieved documents
        chunks_found = 0
        for golden_content in golden_contents:
            for doc in retrieved_docs[:k]:
                retrieved_content = (
                    doc["metadata"]
                    .get("original_content", doc["metadata"].get("content", ""))
                    .strip()
                )
                if retrieved_content == golden_content:
                    chunks_found += 1
                    break

        query_score = chunks_found / len(golden_contents)
        total_score += query_score

    average_score = total_score / total_queries
    pass_at_n = average_score * 100
    return {"pass_at_n": pass_at_n, "average_score": average_score, "total_queries": total_queries}

def retrieve_base(query: str, db, k: int = 20) -> list[dict[str, Any]]:
    """
    Retrieve relevant documents using either VectorDB or ContextualVectorDB.

    :param query: The query string
    :param db: The VectorDB or ContextualVectorDB instance
    :param k: Number of top results to retrieve
    :return: List of retrieved documents
    """
    return db.search(query, k=k)

def evaluate_db(db, original_jsonl_path: str, k):
    # Load the original JSONL data for queries and ground truth
    original_data = load_jsonl(original_jsonl_path)

    # Evaluate retrieval
    results = evaluate_retrieval(original_data, retrieve_base, db, k)
    return results

def evaluate_and_display(db, jsonl_path: str, k_values: list[int] = None, db_name: str = ""):
    """
    Evaluate retrieval performance across multiple k values and display formatted results.

    Args:
        db: Vector database instance (VectorDB or ContextualVectorDB)
        jsonl_path: Path to evaluation dataset
        k_values: List of k values to evaluate (default: [5, 10, 20])
        db_name: Optional name for the database being evaluated

    Returns:
        Dict mapping k values to their results
    """
    if k_values is None:
        k_values = [5, 10, 20]
    results = {}

    print(f"{'=' * 60}")
    if db_name:
        print(f"Evaluation Results: {db_name}")
    else:
        print("Evaluation Results")
    print(f"{'=' * 60}\n")

    for k in k_values:
        print(f"Evaluating Pass@{k}...")
        results[k] = evaluate_db(db, jsonl_path, k)
        print()  # Add spacing between evaluations

    # Print summary table
    print(f"{'=' * 60}")
    print(f"{'Metric':<15} {'Pass Rate':<15} {'Score':<15}")
    print(f"{'-' * 60}")
    for k in k_values:
        pass_rate = f"{results[k]['pass_at_n']:.2f}%"
        score = f"{results[k]['average_score']:.4f}"
        print(f"{'Pass@' + str(k):<15} {pass_rate:<15} {score:<15}")
    print(f"{'=' * 60}\n")

    return results
```

Now let's establish our baseline performance by evaluating the basic RAG system. We'll test at k=5, 10, and 20 to see how many of the golden chunks appear in the top retrieved results. This gives us a benchmark to measure improvement against.

python

```
results = evaluate_and_display(
    base_db, "data/evaluation_set.jsonl", k_values=[5, 10, 20], db_name="Baseline RAG"
)
```

```
============================================================
Evaluation Results: Contextual Embeddings
============================================================

Evaluating Pass@5...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 65.26it/s]

Evaluating Pass@10...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 64.87it/s]

Evaluating Pass@20...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 64.72it/s]

============================================================
Metric          Pass Rate       Score
------------------------------------------------------------
Pass@5          80.92%          0.8092
Pass@10         87.15%          0.8715
Pass@20         90.06%          0.9006
============================================================
```

These results show our baseline RAG performance. The system successfully retrieves the correct chunk 81% of the time in the top 5 results, improving to 87% in the top 10, and 90% in the top 20.

## Contextual Embeddings

With basic RAG, individual chunks often lack sufficient context when embedded in isolation. Contextual Embeddings solve this by using Claude to generate a brief description that "situates" each chunk within its source document. We then embed the chunk together with this context, creating richer vector representations.

For each chunk in our codebase dataset, we pass both the chunk and its full source file to Claude. Claude generates a concise explanation of what the chunk contains and where it fits in the overall file. This context gets prepended to the chunk before embedding.

### Cost and Latency Considerations

**When does this cost occur?** The contextualization happens once at ingestion time, not during every query. Unlike techniques like HyDE (hypothetical document embeddings) that add latency to each search, contextual embeddings are a one-time cost when building your vector database. Prompt caching makes this practical. Since we process all chunks from the same document sequentially, we can leverage prompt caching for significant savings.

1. First chunk: We write the full document to cache (pay a small premium)
2. Subsequent chunks: Read the document from cache (90% discount on those tokens)
3. Cache lasts 5 minutes, plenty of time to process all chunks in a document

**Cost example**: For 800-token chunks in 8k-token documents with 100 tokens of generated context, the total cost is $1.02 per million document tokens. You'll see the cache savings in the logs when you run the code below.

**Note:** Some embedding models have fixed input token limits. If you see worse performance with contextual embeddings, your contextualized chunks may be getting truncated—consider using an embedding model with a larger context window.

---

Let's see an example of how contextual embeddings work by generating context for a single chunk. We'll use Claude to create a situating context, and you'll also see the prompt caching metrics in action.

python

```
DOCUMENT_CONTEXT_PROMPT = """
<document>
{doc_content}
</document>
"""

CHUNK_CONTEXT_PROMPT = """
Here is the chunk we want to situate within the whole document
<chunk>
{chunk_content}
</chunk>

Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
Answer only with the succinct context and nothing else.
"""

def situate_context(doc: str, chunk: str) -> str:
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=1024,
        temperature=0.0,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                        "cache_control": {
                            "type": "ephemeral"
                        },  # we will make use of prompt caching for the full documents
                    },
                    {
                        "type": "text",
                        "text": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                    },
                ],
            }
        ],
    )
    return response

jsonl_data = load_jsonl("data/evaluation_set.jsonl")
# Example usage
doc_content = jsonl_data[0]["golden_documents"][0]["content"]
chunk_content = jsonl_data[0]["golden_chunks"][0]["content"]

response = situate_context(doc_content, chunk_content)
print(f"Situated context: {response.content[0].text}")
print("-" * 10)
# Print cache performance metrics
print(f"Input tokens: {response.usage.input_tokens}")
print(f"Output tokens: {response.usage.output_tokens}")
print(f"Cache creation input tokens: {response.usage.cache_creation_input_tokens}")
print(f"Cache read input tokens: {response.usage.cache_read_input_tokens}")
```

```
Situated context: This chunk contains the module documentation and initial struct definition for a differential fuzzing executor. It introduces the `DiffExecutor` struct that wraps two executors (primary and secondary) to run them sequentially with the same input, comparing their behavior for differential testing. The chunk establishes the core data structure and imports needed for the differential fuzzing implementation.
----------
Input tokens: 3412
Output tokens: 76
Cache creation input tokens: 0
Cache read input tokens: 0
```

### Building the Contextual Vector Database

Now that we've seen how to generate contextual descriptions for individual chunks, let's scale this up to process our entire dataset. The `ContextualVectorDB` class below extends our basic `VectorDB` with automatic contextualization during ingestion.

**Key features:**

* **Parallel processing**: Uses ThreadPoolExecutor to contextualize multiple chunks simultaneously (configurable thread count)
* **Automatic prompt caching**: Processes chunks document-by-document to maximize cache hits
* **Token tracking**: Monitors cache performance and calculates actual cost savings
* **Persistent storage**: Saves both embeddings and contextualized metadata to disk

When you run this, pay attention to the token usage statistics—you'll see that 70-80% of input tokens are read from cache, demonstrating the dramatic cost savings from prompt caching. On our 737-chunk dataset, this reduces what would be a ~15ingestionjobdownto 15 ingestion job down to ~15ingestionjobdownto 3.

python

```
import json
import os
import pickle
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any

import anthropic
import numpy as np
import voyageai
from tqdm import tqdm

class ContextualVectorDB:
    def __init__(self, name: str, voyage_api_key=None, anthropic_api_key=None):
        if voyage_api_key is None:
            voyage_api_key = os.getenv("VOYAGE_API_KEY")
        if anthropic_api_key is None:
            anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

        self.voyage_client = voyageai.Client(api_key=voyage_api_key)
        self.anthropic_client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.name = name
        self.embeddings = []
        self.metadata = []
        self.query_cache = {}
        self.db_path = f"./data/{name}/contextual_vector_db.pkl"

        self.token_counts = {"input": 0, "output": 0, "cache_read": 0, "cache_creation": 0}
        self.token_lock = threading.Lock()

    def situate_context(self, doc: str, chunk: str) -> tuple[str, Any]:
        DOCUMENT_CONTEXT_PROMPT = """
        <document>
        {doc_content}
        </document>
        """

        CHUNK_CONTEXT_PROMPT = """
        Here is the chunk we want to situate within the whole document
        <chunk>
        {chunk_content}
        </chunk>

        Please give a short succinct context to situate this chunk within the overall document for the purposes of improving search retrieval of the chunk.
        Answer only with the succinct context and nothing else.
        """

        response = self.anthropic_client.messages.create(
            model=MODEL_NAME,
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": DOCUMENT_CONTEXT_PROMPT.format(doc_content=doc),
                            "cache_control": {
                                "type": "ephemeral"
                            },  # we will make use of prompt caching for the full documents
                        },
                        {
                            "type": "text",
                            "text": CHUNK_CONTEXT_PROMPT.format(chunk_content=chunk),
                        },
                    ],
                },
            ],
            extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
        )
        return response.content[0].text, response.usage

    def load_data(self, dataset: list[dict[str, Any]], parallel_threads: int = 1):
        if self.embeddings and self.metadata:
            print("Vector database is already loaded. Skipping data loading.")
            return
        if os.path.exists(self.db_path):
            print("Loading vector database from disk.")
            self.load_db()
            return

        texts_to_embed = []
        metadata = []
        total_chunks = sum(len(doc["chunks"]) for doc in dataset)

        def process_chunk(doc, chunk):
            # for each chunk, produce the context
            contextualized_text, usage = self.situate_context(doc["content"], chunk["content"])
            with self.token_lock:
                self.token_counts["input"] += usage.input_tokens
                self.token_counts["output"] += usage.output_tokens
                self.token_counts["cache_read"] += usage.cache_read_input_tokens
                self.token_counts["cache_creation"] += usage.cache_creation_input_tokens

            return {
                # append the context to the original text chunk
                "text_to_embed": f"{contextualized_text}\n\n{chunk['content']}",
                "metadata": {
                    "doc_id": doc["doc_id"],
                    "original_uuid": doc["original_uuid"],
                    "chunk_id": chunk["chunk_id"],
                    "original_index": chunk["original_index"],
                    "original_content": chunk["content"],
                    "contextualized_content": contextualized_text,
                },
            }

        print(f"Processing {total_chunks} chunks with {parallel_threads} threads")
        with ThreadPoolExecutor(max_workers=parallel_threads) as executor:
            futures = []
            for doc in dataset:
                for chunk in doc["chunks"]:
                    futures.append(executor.submit(process_chunk, doc, chunk))

            for future in tqdm(as_completed(futures), total=total_chunks, desc="Processing chunks"):
                result = future.result()
                texts_to_embed.append(result["text_to_embed"])
                metadata.append(result["metadata"])

        self._embed_and_store(texts_to_embed, metadata)
        self.save_db()

        # logging token usage
        print(
            f"Contextual Vector database loaded and saved. Total chunks processed: {len(texts_to_embed)}"
        )
        print(f"Total input tokens without caching: {self.token_counts['input']}")
        print(f"Total output tokens: {self.token_counts['output']}")
        print(f"Total input tokens written to cache: {self.token_counts['cache_creation']}")
        print(f"Total input tokens read from cache: {self.token_counts['cache_read']}")

        total_tokens = (
            self.token_counts["input"]
            + self.token_counts["cache_read"]
            + self.token_counts["cache_creation"]
        )
        savings_percentage = (
            (self.token_counts["cache_read"] / total_tokens) * 100 if total_tokens > 0 else 0
        )
        print(
            f"Total input token savings from prompt caching: {savings_percentage:.2f}% of all input tokens used were read from cache."
        )
        print("Tokens read from cache come at a 90 percent discount!")

    # we use voyage AI here for embeddings. Read more here: https://docs.voyageai.com/docs/embeddings
    def _embed_and_store(self, texts: list[str], data: list[dict[str, Any]]):
        batch_size = 128
        result = [
            self.voyage_client.embed(texts[i : i + batch_size], model="voyage-2").embeddings
            for i in range(0, len(texts), batch_size)
        ]
        self.embeddings = [embedding for batch in result for embedding in batch]
        self.metadata = data

    def search(self, query: str, k: int = 20) -> list[dict[str, Any]]:
        if query in self.query_cache:
            query_embedding = self.query_cache[query]
        else:
            query_embedding = self.voyage_client.embed([query], model="voyage-2").embeddings[0]
            self.query_cache[query] = query_embedding

        if not self.embeddings:
            raise ValueError("No data loaded in the vector database.")

        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[::-1][:k]

        top_results = []
        for idx in top_indices:
            result = {
                "metadata": self.metadata[idx],
                "similarity": float(similarities[idx]),
            }
            top_results.append(result)
        return top_results

    def save_db(self):
        data = {
            "embeddings": self.embeddings,
            "metadata": self.metadata,
            "query_cache": json.dumps(self.query_cache),
        }
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "wb") as file:
            pickle.dump(data, file)

    def load_db(self):
        if not os.path.exists(self.db_path):
            raise ValueError(
                "Vector database file not found. Use load_data to create a new database."
            )
        with open(self.db_path, "rb") as file:
            data = pickle.load(file)
        self.embeddings = data["embeddings"]
        self.metadata = data["metadata"]
        self.query_cache = json.loads(data["query_cache"])
```

python

```
# Load the transformed dataset
with open("data/codebase_chunks.json") as f:
    transformed_dataset = json.load(f)

# Initialize the ContextualVectorDB
contextual_db = ContextualVectorDB("my_contextual_db")

# Load and process the data
# note: consider increasing the number of parallel threads to run this faster, or reducing the number of parallel threads if concerned about hitting your API rate limit
contextual_db.load_data(transformed_dataset, parallel_threads=5)
```

```
Processing 737 chunks with 5 threads

Processing chunks: 100%|██████████| 737/737 [05:32<00:00,  2.22it/s]

Contextual Vector database loaded and saved. Total chunks processed: 737
Total input tokens without caching: 1223730
Total output tokens: 58161
Total input tokens written to cache: 176079
Total input tokens read from cache: 2267069
Total input token savings from prompt caching: 61.83% of all input tokens used were read from cache.
Tokens read from cache come at a 90 percent discount!
```

These numbers reveal the power of prompt caching for contextual embeddings:

* We processed **737 chunks** across 9 codebase files
* **61.83% of input tokens** were read from cache (2.27M tokens at 90% discount)
* Without caching, this would cost **~$9.20** in input tokens
* With caching, the actual cost drops to **~$2.85** (69% savings)

The cache hit rate depends on how many chunks each document contains. Files with more chunks benefit more from caching since we write the full document to cache once, then read it repeatedly for each chunk in that file. This is why processing documents sequentially (rather than randomly shuffling chunks) is crucial for maximizing cache efficiency.

Now let's evaluate how much this contextualization improves our retrieval performance compared to the baseline.

python

```
results = evaluate_and_display(
    contextual_db,
    "data/evaluation_set.jsonl",
    k_values=[5, 10, 20],
    db_name="Contextual Embeddings",
)
```

```
============================================================
Evaluation Results: Contextual Embeddings
============================================================

Evaluating Pass@5...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 64.58it/s]

Evaluating Pass@10...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 64.37it/s]

Evaluating Pass@20...

Evaluating retrieval: 100%|██████████| 248/248 [00:03<00:00, 64.14it/s]

============================================================
Metric          Pass Rate       Score
------------------------------------------------------------
Pass@5          88.12%          0.8812
Pass@10         92.34%          0.9234
Pass@20         94.29%          0.9429
============================================================
```

By adding context to each chunk before embedding, we've reduced retrieval failures by **~30-40%** across all k values. This means fewer irrelevant results in your top retrieved chunks, leading to better answers when you pass these chunks to Claude for final response generation.

The improvement is most pronounced at Pass@5, where precision matters most—suggesting that contextualized chunks aren't just retrieved more often, but rank higher when relevant.

## Contextual BM25: Hybrid Search

Contextual embeddings alone improved our Pass@10 from 87% to 92%. We can push performance even higher by combining semantic search with keyword-based search using **Contextual BM25**—a hybrid approach that reduces retrieval failure rates further.

### Why Hybrid Search?

Semantic search excels at understanding meaning and context, but can miss exact keyword matches. BM25 (a probabilistic keyword ranking algorithm) excels at finding specific terms, but lacks semantic understanding. By combining both, we get the best of both worlds:

* **Semantic search**: Captures conceptual similarity and paraphrases
* **BM25**: Catches exact terminology, function names, and specific phrases
* **Reciprocal Rank Fusion**: Intelligently merges results from both sources

### What is BM25?

BM25 is a probabilistic ranking function that improves upon TF-IDF by accounting for document length and term saturation. It's widely used in production search engines (including Elasticsearch) for its effectiveness at ranking keyword relevance. For technical details, see [this blog post](https://www.elastic.co/blog/practical-bm25-part-2-the-bm25-algorithm-and-its-variables).

Instead of only searching the raw chunk content, we search both the chunk *and* the contextual description we generated earlier. This means BM25 can match keywords in either the original text or the explanatory context.

### Setup: Running Elasticsearch

Before running the code below, you'll need Elasticsearch running locally. The easiest way is with Docker:

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  elasticsearch:9.2.0
```

## Troubleshooting:

* Verify it's running: docker ps | grep elasticsearch
* If port 9200 is in use: docker stop elasticsearch && docker rm elasticsearch
* Check logs if issues occur: docker logs elasticsearch

## How the Hybrid Search Works

The retrieve\_advanced function below implements a three-step process:

1. Retrieve candidates: Get top 150 results from both semantic search and BM25
2. Score fusion: Combine rankings using weighted Reciprocal Rank Fusion
   * Default: 80% weight to semantic search, 20% to BM25
   * These weights are tunable—experiment to optimize for your use case
3. Return top-k: Select the highest-scoring results after fusion

The weighting system lets you balance between semantic understanding and keyword precision based on your data characteristics.

python

```
import json
import os
from typing import Any

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from tqdm import tqdm

class ElasticsearchBM25:
    def __init__(self, index_name: str = "contextual_bm25_index"):
        self.es_client = Elasticsearch("http://localhost:9200")
        self.index_name = index_name
        self.create_index()

    def create_index(self):
        index_settings = {
            "settings": {
                "analysis": {"analyzer": {"default": {"type": "english"}}},
                "similarity": {"default": {"type": "BM25"}},
                "index.queries.cache.enabled": False,
            },
            "mappings": {
                "properties": {
                    "content": {"type": "text", "analyzer": "english"},
                    "contextualized_content": {"type": "text", "analyzer": "english"},
                    "doc_id": {"type": "keyword", "index": False},
                    "chunk_id": {"type": "keyword", "index": False},
                    "original_index": {"type": "integer", "index": False},
                }
            },
        }

        # Change this line - remove 'body=' parameter
        if not self.es_client.indices.exists(index=self.index_name):
            self.es_client.indices.create(
                index=self.index_name,
                settings=index_settings["settings"],
                mappings=index_settings["mappings"],
            )
            print(f"Created index: {self.index_name}")

    def index_documents(self, documents: list[dict[str, Any]]):
        actions = [
            {
                "_index": self.index_name,
                "_source": {
                    "content": doc["original_content"],
                    "contextualized_content": doc["contextualized_content"],
                    "doc_id": doc["doc_id"],
                    "chunk_id": doc["chunk_id"],
                    "original_index": doc["original_index"],
                },
            }
            for doc in documents
        ]
        success, _ = bulk(self.es_client, actions)
        self.es_client.indices.refresh(index=self.index_name)
        return success

    def search(self, query: str, k: int = 20) -> list[dict[str, Any]]:
        self.es_client.indices.refresh(index=self.index_name)

        # Change this - remove 'body=' and pass query directly
        response = self.es_client.search(
            index=self.index_name,
            query={
                "multi_match": {
                    "query": query,
                    "fields": ["content", "contextualized_content"],
                }
            },
            size=k,
        )

        return [
            {
                "doc_id": hit["_source"]["doc_id"],
                "original_index": hit["_source"]["original_index"],
                "content": hit["_source"]["content"],
                "contextualized_content": hit["_source"]["contextualized_content"],
                "score": hit["_score"],
            }
            for hit in response["hits"]["hits"]
        ]

def create_elasticsearch_bm25_index(db: ContextualVectorDB):
    es_bm25 = ElasticsearchBM25()
    es_bm25.index_documents(db.metadata)
    return es_bm25

def retrieve_advanced(
    query: str,
    db: ContextualVectorDB,
    es_bm25: ElasticsearchBM25,
    k: int,
    semantic_weight: float = 0.8,
    bm25_weight: float = 0.2,
):
    num_chunks_to_recall = 150

    # Semantic search
    semantic_results = db.search(query, k=num_chunks_to_recall)
    ranked_chunk_ids = [
        (result["metadata"]["doc_id"], result["metadata"]["original_index"])
        for result in semantic_results
    ]

    # BM25 search using Elasticsearch
    bm25_results = es_bm25.search(query, k=num_chunks_to_recall)
    ranked_bm25_chunk_ids = [
        (result["doc_id"], result["original_index"]) for result in bm25_results
    ]

    # Combine results
    chunk_ids = list(set(ranked_chunk_ids + ranked_bm25_chunk_ids))
    chunk_id_to_score = {}

    # Initial scoring with weights
    for chunk_id in chunk_ids:
        score = 0
        if chunk_id in ranked_chunk_ids:
            index = ranked_chunk_ids.index(chunk_id)
            score += semantic_weight * (1 / (index + 1))  # Weighted 1/n scoring for semantic
        if chunk_id in ranked_bm25_chunk_ids:
            index = ranked_bm25_chunk_ids.index(chunk_id)
            score += bm25_weight * (1 / (index + 1))  # Weighted 1/n scoring for BM25
        chunk_id_to_score[chunk_id] = score

    # Sort chunk IDs by their scores in descending order
    sorted_chunk_ids = sorted(
        chunk_id_to_score.keys(), key=lambda x: (chunk_id_to_score[x], x[0], x[1]), reverse=True
    )

    # Assign new scores based on the sorted order
    for index, chunk_id in enumerate(sorted_chunk_ids):
        chunk_id_to_score[chunk_id] = 1 / (index + 1)

    # Prepare the final results
    final_results = []
    semantic_count = 0
    bm25_count = 0
    for chunk_id in sorted_chunk_ids[:k]:
        chunk_metadata = next(
            chunk
            for chunk in db.metadata
            if chunk["doc_id"] == chunk_id[0] and chunk["original_index"] == chunk_id[1]
        )
        is_from_semantic = chunk_id in ranked_chunk_ids
        is_from_bm25 = chunk_id in ranked_bm25_chunk_ids
        final_results.append(
            {
                "chunk": chunk_metadata,
                "score": chunk_id_to_score[chunk_id],
                "from_semantic": is_from_semantic,
                "from_bm25": is_from_bm25,
            }
        )

        if is_from_semantic and not is_from_bm25:
            semantic_count += 1
        elif is_from_bm25 and not is_from_semantic:
            bm25_count += 1
        else:  # it's in both
            semantic_count += 0.5
            bm25_count += 0.5

    return final_results, semantic_count, bm25_count

def evaluate_db_advanced(
    db: ContextualVectorDB,
    original_jsonl_path: str,
    k_values: list[int] = None,
    db_name: str = "Hybrid Search",
):
    """
    Evaluate hybrid search (semantic + BM25) at multiple k values with formatted results.

    Args:
        db: ContextualVectorDB instance
        original_jsonl_path: Path to evaluation dataset
        k_values: List of k values to evaluate (default: [5, 10, 20])
        db_name: Name for the evaluation display

    Returns:
        Dict mapping k values to their results and source breakdowns
    """
    if k_values is None:
        k_values = [5, 10, 20]
    original_data = load_jsonl(original_jsonl_path)
    es_bm25 = create_elasticsearch_bm25_index(db)
    results = {}

    print(f"{'=' * 70}")
    print(f"Evaluation Results: {db_name}")
    print(f"{'=' * 70}\n")

    try:
        # Warm-up queries
        warm_up_queries = original_data[:10]
        for query_item in warm_up_queries:
            _ = retrieve_advanced(query_item["query"], db, es_bm25, k_values[0])

        for k in k_values:
            print(f"Evaluating Pass@{k}...")

            total_score = 0
            total_semantic_count = 0
            total_bm25_count = 0
            total_results = 0

            for query_item in tqdm(original_data, desc=f"Pass@{k}"):
                query = query_item["query"]
                golden_chunk_uuids = query_item["golden_chunk_uuids"]

                golden_contents = []
                for doc_uuid, chunk_index in golden_chunk_uuids:
                    golden_doc = next(
                        (doc for doc in query_item["golden_documents"] if doc["uuid"] == doc_uuid),
                        None,
                    )
                    if golden_doc:
                        golden_chunk = next(
                            (
                                chunk
                                for chunk in golden_doc["chunks"]
                                if chunk["index"] == chunk_index
                            ),
                            None,
                        )
                        if golden_chunk:
                            golden_contents.append(golden_chunk["content"].strip())

                if not golden_contents:
                    continue

                retrieved_docs, semantic_count, bm25_count = retrieve_advanced(
                    query, db, es_bm25, k
                )

                chunks_found = 0
                for golden_content in golden_contents:
                    for doc in retrieved_docs[:k]:
                        retrieved_content = doc["chunk"]["original_content"].strip()
                        if retrieved_content == golden_content:
                            chunks_found += 1
                            break

                query_score = chunks_found / len(golden_contents)
                total_score += query_score

                total_semantic_count += semantic_count
                total_bm25_count += bm25_count
                total_results += len(retrieved_docs)

            total_queries = len(original_data)
            average_score = total_score / total_queries
            pass_at_n = average_score * 100

            semantic_percentage = (
                (total_semantic_count / total_results) * 100 if total_results > 0 else 0
            )
            bm25_percentage = (total_bm25_count / total_results) * 100 if total_results > 0 else 0

            results[k] = {
                "pass_at_n": pass_at_n,
                "average_score": average_score,
                "total_queries": total_queries,
                "semantic_percentage": semantic_percentage,
                "bm25_percentage": bm25_percentage,
            }

            print(f"Pass@{k}: {pass_at_n:.2f}%")
            print(f"Semantic: {semantic_percentage:.1f}% | BM25: {bm25_percentage:.1f}%\n")

        # Print summary table
        print(f"{'=' * 70}")
        print(f"{'Metric':<12} {'Pass Rate':<12} {'Score':<12} {'Semantic':<12} {'BM25':<12}")
        print(f"{'-' * 70}")
        for k in k_values:
            r = results[k]
            print(
                f"{'Pass@' + str(k):<12} {r['pass_at_n']:>10.2f}% {r['average_score']:>10.4f} "
                f"{r['semantic_percentage']:>10.1f}% {r['bm25_percentage']:>10.1f}%"
            )
        print(f"{'=' * 70}\n")

        return results

    finally:
        # Delete the Elasticsearch index
        if es_bm25.es_client.indices.exists(index=es_bm25.index_name):
            es_bm25.es_client.indices.delete(index=es_bm25.index_name)
            print(f"Deleted Elasticsearch index: {es_bm25.index_name}")
```

python

```
results = evaluate_db_advanced(
    contextual_db,
    "data/evaluation_set.jsonl",
    k_values=[5, 10, 20],
    db_name="Contextual BM25 Hybrid Search",
)
```

```
Created index: contextual_bm25_index
======================================================================
Evaluation Results: Contextual BM25 Hybrid Search
======================================================================

Evaluating Pass@5...

Pass@5: 100%|██████████| 248/248 [00:05<00:00, 41.79it/s]

Pass@5: 88.86%
Semantic: 54.6% | BM25: 45.4%

Evaluating Pass@10...

Pass@10: 100%|██████████| 248/248 [00:05<00:00, 42.20it/s]

Pass@10: 92.31%
Semantic: 57.6% | BM25: 42.4%

Evaluating Pass@20...

Pass@20: 100%|██████████| 248/248 [00:05<00:00, 42.15it/s]

Pass@20: 95.23%
Semantic: 60.8% | BM25: 39.2%

======================================================================
Metric       Pass Rate    Score        Semantic     BM25
----------------------------------------------------------------------
Pass@5            88.86%     0.8886       54.6%       45.4%
Pass@10           92.31%     0.9231       57.6%       42.4%
Pass@20           95.23%     0.9523       60.8%       39.2%
======================================================================

Deleted Elasticsearch index: contextual_bm25_index
```

## Reranking

We've achieved strong results with hybrid search (93.21% Pass@10), but there's one more technique that can squeeze out additional performance: **reranking**.

### What is Reranking?

Reranking is a two-stage retrieval approach:

1. **Stage 1 - Broad Retrieval**: Cast a wide net by retrieving more candidates than you need (e.g., retrieve 100 chunks)
2. **Stage 2 - Precise Selection**: Use a specialized reranking model to score these candidates and select only the top-k most relevant ones

**Why does this work?** Initial retrieval methods (embeddings, BM25) are optimized for speed across millions of documents. Reranking models are slower but more accurate—they can afford to do deeper analysis on a smaller candidate set. This creates a speed/accuracy trade-off that works well in practice.

### Our Reranking Approach

For this example, we'll use a simpler reranking pipeline that builds on contextual embeddings alone (not the full hybrid search). Here's the process:

1. **Over-retrieve**: Get 10x more results than needed (e.g., retrieve 100 chunks when we need 10)
2. **Rerank with Cohere**: Use Cohere's `rerank-english-v3.0` model to score all candidates
3. **Select top-k**: Return only the highest-scoring results

The reranking model has access to both the original chunk content and the contextual descriptions we generated, giving it rich information to make precise relevance judgments.

### Expected Performance

Adding reranking delivers a modest but meaningful improvement:

* **Without reranking**: 92.34% Pass@10 (contextual embeddings alone)
* **With reranking**: ~95% Pass@10 (additional 2-3% gain)

This might seem small, but in production systems, reducing failures from 7.66% to ~5% can significantly improve user experience. The trade-off is query latency—reranking adds ~100-200ms per query depending on candidate set size.

python

```
import json
from collections.abc import Callable
from typing import Any

import cohere
from tqdm import tqdm

def evaluate_db_rerank(
    db, original_jsonl_path: str, k_values: list[int] = None, db_name: str = "Reranking"
):
    """
    Evaluate reranking performance at multiple k values with formatted results.

    Args:
        db: ContextualVectorDB instance
        original_jsonl_path: Path to evaluation dataset
        k_values: List of k values to evaluate (default: [5, 10, 20])
        db_name: Name for the evaluation display

    Returns:
        Dict mapping k values to their results
    """
    if k_values is None:
        k_values = [5, 10, 20]
    original_data = load_jsonl(original_jsonl_path)
    co = cohere.Client(os.getenv("COHERE_API_KEY"))
    results = {}

    print(f"{'=' * 60}")
    print(f"Evaluation Results: {db_name}")
    print(f"{'=' * 60}\n")

    for k in k_values:
        print(f"Evaluating Pass@{k} with reranking...")

        total_score = 0
        total_queries = len(original_data)

        for query_item in tqdm(original_data, desc=f"Pass@{k}"):
            query = query_item["query"]
            golden_chunk_uuids = query_item["golden_chunk_uuids"]

            # Find golden contents
            golden_contents = []
            for doc_uuid, chunk_index in golden_chunk_uuids:
                golden_doc = next(
                    (doc for doc in query_item["golden_documents"] if doc["uuid"] == doc_uuid), None
                )
                if golden_doc:
                    golden_chunk = next(
                        (chunk for chunk in golden_doc["chunks"] if chunk["index"] == chunk_index),
                        None,
                    )
                    if golden_chunk:
                        golden_contents.append(golden_chunk["content"].strip())

            if not golden_contents:
                continue

            # Retrieve and rerank
            semantic_results = db.search(query, k=k * 10)

            # Prepare documents for reranking
            documents = [
                f"{res['metadata']['original_content']}\n\nContext: {res['metadata']['contextualized_content']}"
                for res in semantic_results
            ]

            # Rerank
            rerank_response = co.rerank(
                model="rerank-english-v3.0", query=query, documents=documents, top_n=k
            )
            time.sleep(0.1)  # Rate limiting

            # Get final results
            retrieved_docs = []
            for r in rerank_response.results:
                original_result = semantic_results[r.index]
                retrieved_docs.append(
                    {"chunk": original_result["metadata"], "score": r.relevance_score}
                )

            # Check if golden chunks are in results
            chunks_found = 0
            for golden_content in golden_contents:
                for doc in retrieved_docs[:k]:
                    retrieved_content = doc["chunk"]["original_content"].strip()
                    if retrieved_content == golden_content:
                        chunks_found += 1
                        break

            query_score = chunks_found / len(golden_contents)
            total_score += query_score

        average_score = total_score / total_queries
        pass_at_n = average_score * 100

        results[k] = {
            "pass_at_n": pass_at_n,
            "average_score": average_score,
            "total_queries": total_queries,
        }

        print(f"Pass@{k}: {pass_at_n:.2f}%")
        print(f"Average Score: {average_score:.4f}\n")

    # Print summary table
    print(f"{'=' * 60}")
    print(f"{'Metric':<15} {'Pass Rate':<15} {'Score':<15}")
    print(f"{'-' * 60}")
    for k in k_values:
        pass_rate = f"{results[k]['pass_at_n']:.2f}%"
        score = f"{results[k]['average_score']:.4f}"
        print(f"{'Pass@' + str(k):<15} {pass_rate:<15} {score:<15}")
    print(f"{'=' * 60}\n")

    return results
```

python

```
results = evaluate_db_rerank(
    contextual_db,
    "data/evaluation_set.jsonl",
    k_values=[5, 10, 20],
    db_name="Contextual Embeddings + Reranking",
)
```

```
============================================================
Evaluation Results: Contextual Embeddings + Reranking
============================================================

Evaluating Pass@5 with reranking...

Pass@5: 100%|██████████| 248/248 [01:40<00:00,  2.47it/s]

Pass@5: 92.15%
Average Score: 0.9215

Evaluating Pass@10 with reranking...

Pass@10: 100%|██████████| 248/248 [02:29<00:00,  1.66it/s]

Pass@10: 95.26%
Average Score: 0.9526

Evaluating Pass@20 with reranking...

Pass@20: 100%|██████████| 248/248 [03:03<00:00,  1.35it/s]
Pass@20: 97.45%
Average Score: 0.9745

============================================================
Metric          Pass Rate       Score
------------------------------------------------------------
Pass@5          92.15%          0.9215
Pass@10         95.26%          0.9526
Pass@20         97.45%          0.9745
============================================================
```

Reranking delivers our strongest results, nearly eliminating retrieval failures. Let's look at how each technique built upon the previous one to achieve this improvement.

Starting from our baseline RAG system at 87% Pass@10, we've climbed to over 95% by systematically applying advanced retrieval techniques. Each method addresses a different weakness: contextual embeddings solve the "isolated chunk" problem, hybrid search catches keyword-specific queries that embeddings miss, and reranking applies more sophisticated relevance scoring to refine the final selection.

| Approach | Pass@5 | Pass@10 | Pass@20 |
| --- | --- | --- | --- |
| **Baseline RAG** | 80.92% | 87.15% | 90.06% |
| **+ Contextual Embeddings** | 88.12% | 92.34% | 94.29% |
| **+ Hybrid Search (BM25)** | 86.43% | 93.21% | 94.99% |
| **+ Reranking** | 92.15% | 95.26% | 97.45% |

**Key Takeaways:**

1. **Contextual embeddings provided the largest single improvement** (+5-7 percentage points), validating that adding document-level context to chunks significantly improves retrieval quality. This technique alone gets you 90% of the way to optimal performance.
2. **Reranking achieves the highest absolute performance**, reaching 95.26% Pass@10—meaning the correct chunk appears in the top 10 results for 95% of queries. This represents a **47% reduction in retrieval failures** compared to baseline RAG (from 12.85% failure rate down to 4.74%).
3. **Trade-offs matter**: Each technique adds complexity and cost:

   * Contextual embeddings: One-time ingestion cost (~$3 for this dataset with prompt caching)
   * Hybrid search: Requires Elasticsearch infrastructure and maintenance
   * Reranking: Adds 100-200ms query latency and per-query API costs (~$0.002 per query)
4. **Choose your approach** based on your requirements:

   * **High-volume, cost-sensitive**: Contextual embeddings alone (92% Pass@10, no per-query costs)
   * **Maximum accuracy, latency-tolerant**: Full reranking pipeline (95% Pass@10, best precision)
   * **Balanced production system**: Hybrid search for strong performance without per-query costs (93% Pass@10)

For most production RAG systems, **contextual embeddings provide the best performance-to-cost ratio**, delivering 92% Pass@10 with only one-time ingestion costs. Hybrid search and reranking are available when you need that extra 2-3 percentage points of precision and can afford the additional infrastructure or query costs.

### Next Steps and Key Takeaways

1. We demonstrated how to use Contextual Embeddings to improve retrieval performance, then delivered additional improvements with Contextual BM25 and reranking.
2. This example used codebases, but these methods also apply to other data types such as internal company knowledge bases, financial & legal content, educational content, and much more.
3. If you are an AWS user, you can get started with the Lambda function in `contextual-rag-lambda-function`, and if you're a GCP user you can spin up your own Cloud Run instance and follow a similar pattern!
