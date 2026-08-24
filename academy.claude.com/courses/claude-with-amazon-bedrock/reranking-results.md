<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/reranking-results -->

Lesson 40 of 65 · Claude with Amazon BedrockReranking results

The hybrid retrieval approach we've built works well, but there are still some rough edges. When you search for specific terms or use abbreviations, the results might not be perfectly ordered. For example, asking "What did the eng team do with INC-2023-Q4-011?" might return the cybersecurity section first, even though the software engineering section is more relevant to that specific query.

## LLM-Based Re-ranking

Re-ranking adds another post-processing step after merging results from your vector index and BM25 index. The concept is straightforward: take your search results and ask Claude to reorder them based on relevance to the user's question.

![](https://academy.claude.com/assets/media/b552a90bd170afa738c7ecd5cf20ef671d579705fa948df0c83d999e20c2adac.png)

Here's how the process works:

* Run your hybrid search (vector + BM25) as usual
* Merge the results like before
* Pass the merged results to a re-ranker function
* The re-ranker sends everything to Claude with a specific prompt
* Claude returns a reordered list of the most relevant documents

## System Prompts

The re-ranking prompt is designed to be clear and specific. You provide Claude with the user's question and all the documents that seem relevant, then ask for a simple task: return the most relevant documents in order of decreasing relevance.

A typical prompt structure looks like this:

```
You are tasked with finding the documents most relevant to a user's question.

<user_question>
What happened with INC-2023-Q4-011?
</user_question>

Here are documents that may be relevant:
<documents>
<document>Section 10...</document>
<document>Section 2...</document>
<document>Section 7...</document>
<document>Section 6...</document>
</documents>

Return the 3 most relevant docs, in order of decreasing relevance.
```



## Efficiency Considerations

Asking Claude to return full text chunks would be inefficient - you'd be waiting for Claude to copy large amounts of text. Instead, assign each text chunk a unique ID ahead of time. Then ask Claude to return just those IDs in the correct order.

This approach is much faster because Claude only needs to return a simple list like `["1p5g", "51n3", "ab83"]` instead of copying entire document sections.

## Implementation

The re-ranker function gets called automatically by your retriever after the initial hybrid search. Here's the basic structure:

python

```
def reranker_fn(docs, query_text, k):
    # Format documents with IDs
    joined_docs = "\n".join([
        f"<document><document_id>{doc['id']}</document_id>"
        f"<document_content>{doc['content']}</document_content></document>"
        for doc in docs
    ])

    # Create prompt with user question and documents
    prompt = f"""You are about to be given a set of documents...
    {query_text}
    {joined_docs}
    """

    # Get Claude's response and parse the document IDs
    result = chat(messages, stop_sequences=["```"])
    return json.loads(result["text"])["document_ids"]
```

## Results

When you test the re-ranker with queries like "What did the eng team do with INC-2023-Q4-011?", you should see more relevant results at the top. Claude understands the context and can identify that a query about the engineering team should prioritize the software engineering section over other sections that merely mention the incident.

The trade-off is clear: re-ranking increases latency because you need to wait for Claude's response, but it significantly improves search accuracy by leveraging Claude's understanding of context and relevance.
