<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/a-multi-index-rag-pipeline -->

Lesson 38 of 67 · Building with the Claude APIA Multi-Index RAG pipeline

We've built separate implementations for semantic search (using vector embeddings) and lexical search (using BM25). Now it's time to combine them into a unified search pipeline that leverages the strengths of both approaches.

## The Multi-Index Architecture

Both our VectorIndex and BM25Index classes share nearly identical APIs - they both have `add_document()` and `search()` methods. This consistency makes it straightforward to wrap them together in a new class called Retriever.

![](https://academy.claude.com/assets/media/841de3dd2498b6abea4ec4b1c8e249bf013c75fda5306e8ebb4291126d1adebd.jpg)

The Retriever acts as a coordinator that forwards user queries to both indexes, collects their results, and merges them using a technique called reciprocal rank fusion.

## Understanding Reciprocal Rank Fusion

Merging results from different search methods isn't as simple as just concatenating lists. Each method uses different scoring systems, so we need a way to normalize and combine their rankings fairly.

![](https://academy.claude.com/assets/media/6a0de30359d580ae3cb7891111b887273e564ebedbb26b42ed70bbe1501a5dae.jpg)

Here's how reciprocal rank fusion works with an example. Let's say we search for information about "INC-2023-Q4-011" and get these results:

* VectorIndex returns: Section 2 (rank 1), Section 7 (rank 2), Section 6 (rank 3)
* BM25Index returns: Section 6 (rank 1), Section 2 (rank 2), Section 7 (rank 3)

![](https://academy.claude.com/assets/media/0e763ee4ad98f118835eae963cd07ebad356935b7b3572b60bd088caeba15ccc.jpg)

We combine these into a single table showing each text chunk's rank from both indexes, then apply the RRF formula:

```
RRF_score(d) = Σ(1 / (k + rank_i(d)))
```



Where k is a constant (often 60, but we'll use 1 for clearer results) and rank\_i(d) is the rank of document d in the i-th ranking.

![](https://academy.claude.com/assets/media/391f12a30a1f250062b7bfa66a3877163f9dc5edfc1613ac0128a2ca3cc1c54a.jpg)

For our example:

* Section 2: 1.0/(1+1) + 1.0/(1+2) = 0.833
* Section 7: 1.0/(1+2) + 1.0/(1+3) = 0.583
* Section 6: 1.0/(1+3) + 1.0/(1+1) = 0.75

![](https://academy.claude.com/assets/media/d9bd5a5627706194dba4a8e65f051923d1048f3da5f26daabc0b2ba7e81f9e28.jpg)

The final ranking becomes: Section 2 (0.833), Section 6 (0.75), Section 7 (0.583). This makes intuitive sense - Section 2 performed well in both indexes, so it rises to the top.

## Implementation Details

The Retriever class wraps multiple search indexes and provides a unified interface:

python

```
class Retriever:
    def __init__(self, *indexes: SearchIndex):
        if len(indexes) == 0:
            raise ValueError("At least one index must be provided")
        self._indexes = list(indexes)

    def add_document(self, document: Dict[str, Any]):
        for index in self._indexes:
            index.add_document(document)

    def search(self, query_text: str, k: int = 1, k_rrf: int = 60):
        # Get results from all indexes
        all_results = []
        for idx, results in enumerate(all_results):
            for rank, (doc, _) in enumerate(results):
                # Track document ranks across indexes
                # Apply RRF scoring formula
        # Return merged and sorted results
```

The key insight is that by maintaining consistent APIs across different search implementations, we can easily combine them without tight coupling.

## Testing the Hybrid Approach

Remember our earlier problem where searching for "what happened with INC-2023-Q4-011?" returned unexpected results from the vector-only approach? The cybersecurity incident (Section 10) came first, but financial analysis (Section 3) came second instead of the more relevant software engineering section.

With our hybrid retriever, we now get much better results:

* Section 10: Cybersecurity Analysis - Incident Response Report (most relevant)
* Section 2: Software Engineering - Project Phoenix Stability Enhancements (second most relevant)
* Section 5: Legal Developments (third)

This demonstrates how combining semantic and lexical search can overcome the limitations of either approach used alone.

## Extensibility

![](https://academy.claude.com/assets/media/2dc7491d64f74713e58baf91cfb83fa2e0abc2bff8a962df866955ce0d2c5d68.jpg)

The beauty of this architecture is its extensibility. Since all indexes implement the same SearchIndex protocol with `add_document()` and `search()` methods, you can easily add new search methodologies:

![](https://academy.claude.com/assets/media/b1af010519330112fe5663609bc83585f40020db179068956bae537d83fb5f13.jpg)

Want to add a keyword-based index? A graph-based search? A specialized domain index? Just implement the same interface and the Retriever will automatically incorporate it into the fusion process.

This modular approach keeps each search implementation focused and testable while providing a clean way to combine their strengths in the final system.
