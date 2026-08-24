<!-- source: https://academy.claude.com/courses/claude-with-google-cloud-s-vertex-ai/reranking-results -->

Lesson 41 of 66 · Claude with Google Cloud's Vertex AIReranking results

The hybrid retrieval approach we've built works well, but it still has some rough edges. When we search for "what did the eng team do with INC-2023-Q4-011?", we'd expect the Software Engineering section to rank higher since it specifically mentions the engineering team and the incident. However, the Cybersecurity section still comes first.

This is where re-ranking comes in - a post-processing technique that can significantly improve retrieval accuracy.

## How Re-ranking Works

Re-ranking adds an extra step after your hybrid search process. Instead of just returning the merged results from your vector and BM25 indexes, you pass those results through an LLM for intelligent reordering.

![](https://academy.claude.com/assets/media/b552a90bd170afa738c7ecd5cf20ef671d579705fa948df0c83d999e20c2adac.png)

The process is straightforward:

* Run your existing hybrid search (vector + BM25)
* Merge the results as before
* Send the merged results to Claude with a re-ranking prompt
* Get back a reordered list of the most relevant documents

## The Re-ranking Prompt

The prompt structure is simple but effective. You provide Claude with the user's question and all the candidate documents, then ask it to return the most relevant ones in order of decreasing relevance.

```
You are about to be given a set of documents, along with an id of each.
Your task is to select the {k} most relevant documents to answer the user's question.

Here is the user's question:
<question>
{query_text}
</question>

Here are the documents to select from:
<documents>
{joined_docs}
</documents>

Respond in the following format:
```json
\{
  "document_ids": str[] # List document ids, \{k\} elements long, sorted in order of decreasing relevance
\}
```
```



## Efficiency Considerations

A key optimization is using document IDs instead of asking Claude to return full text chunks. If you asked Claude to return the complete text of each relevant document, you'd waste time waiting for it to copy large amounts of text.

![](https://academy.claude.com/assets/media/457382fdfe7e06e2f634616f9282ae5df52f77719206e833b9b59054751206bc.png)

Instead, assign each text chunk a unique ID ahead of time, then ask Claude to return just those IDs in the preferred order. This makes the re-ranking process much faster while still giving you the reordered results you need.

## Implementation

The re-ranker function gets called automatically after your initial hybrid search completes. Here's the basic structure:

python

```
def reranker_fn(docs, query_text, k):
    joined_docs = "\n".join([
        f"""
        <document>
        <document_id>{doc["id"]}</document_id>
        <document_content>{doc["content"]}</document_content>
        </document>
        """
        for doc in docs
    ])

    # Build prompt with user question and documents
    # Send to Claude with JSON response format
    # Parse and return reordered document IDs
```

You can integrate this into your retriever by passing the re-ranker function as a parameter:

python

```
retriever = Retriever(bm25_index, vector_index, reranker_fn=reranker_fn)
```

## Results

The re-ranking approach shows clear improvements. When testing the query "what did the eng team do with INC-2023-Q4-011?", the Software Engineering section now correctly appears first, ahead of the Cybersecurity section. Claude successfully identified that the user was specifically asking about the engineering team's involvement with the incident.

## Trade-offs

Re-ranking comes with trade-offs to consider:

* **Increased latency:** You now need to wait for an additional LLM call to complete
* **Improved accuracy:** The LLM can understand context and intent better than pure similarity scores
* **Cost considerations:** Each search now requires an LLM API call

For many applications, the accuracy improvement justifies the additional latency and cost, especially when precise retrieval is critical for your use case.
