<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/bm25-lexical-search -->

Lesson 39 of 66 · Claude with Google Cloud's Vertex AIBM25 lexical search

When building a RAG pipeline, you'll quickly discover that semantic search alone doesn't always return the best results. Sometimes you need exact term matches that semantic search might miss. The solution is to combine semantic search with lexical search using a technique called BM25.

## The Problem with Semantic Search Alone

Let's say you're searching for a specific incident ID like "INC-2023-Q4-011" in a document. While this exact term appears multiple times in relevant sections, semantic search might return unrelated sections that are semantically similar but don't actually contain the specific term you're looking for.

![](https://academy.claude.com/assets/media/ae16f186b3678b86bceb950af1750e6b11be3e1202d94ae3d02dbbf4ce9c0363.png)

This happens because semantic search focuses on meaning rather than exact matches. When you need precise term matching, you need a different approach.

## Hybrid Search Strategy

The solution is to run two searches in parallel and merge the results:

![](https://academy.claude.com/assets/media/02a7c7cadb95e5dd57b37ba6071ab25a60fb4c01524a9bd25d92a133699ecf79.png)

* **Semantic Search** - Uses embeddings and vector databases for meaning-based matching
* **Lexical Search** - Uses classic text search for exact term matching
* **Merge Results** - Combines both result sets for better coverage

## How BM25 Works

BM25 (Best Match 25) is a popular algorithm for lexical search in RAG pipelines. Here's how it processes a search query:

![](https://academy.claude.com/assets/media/e24396bf85a106a14d16e827ef1a9cc156f970c36bf4fe4eb6c071b4f5873d8c.png)

The algorithm follows these key steps:

1. **Tokenize the query** - Break the user's question into individual terms
2. **Count term frequency** - See how often each term appears across all documents
3. **Weight terms by rarity** - Terms used less frequently get higher importance scores
4. **Find best matches** - Return chunks that contain more instances of the higher-weighted terms

The key insight is that rare terms like "INC-2023-Q4-011" are much more important for search than common words like "a" or "the".

## Implementing BM25 Search

Here's how to set up a BM25 search system:

python

```
# Create a BM25 store
store = BM25Index()

# Add documents to the store
for chunk in chunks:
    store.add_document({"content": chunk})

# Search the store
results = store.search("What happened with INC-2023-Q4-011?", 3)
```

The BM25 implementation provides the same API as your semantic search system - both have `add_document()` and `search()` methods, making them easy to use together.

## Better Search Results

When you run the same query through BM25 that failed with semantic search alone, you get much better results. Instead of returning irrelevant sections, BM25 prioritizes the sections that actually contain your specific search terms.

The algorithm correctly identifies that "INC-2023-Q4-011" is a rare, important term and ranks documents containing it much higher than documents with only common words from the query.

## Next Steps

Now that you have both semantic and lexical search systems working independently, the next step is merging their results. This hybrid approach gives you the best of both worlds - the contextual understanding of semantic search combined with the precision of exact term matching from lexical search.

![](https://academy.claude.com/assets/media/d08ed8f624060d523dead1ab28ff3dab4f31c13971dd19740d9bdcc80ddacc9d.png)

Both search systems use similar APIs, making it straightforward to query both in parallel and combine their results into a single, more comprehensive result set.
