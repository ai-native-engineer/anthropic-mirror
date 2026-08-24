<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/text-chunking-strategies -->

Lesson 34 of 65 · Claude with Amazon BedrockText chunking strategies

Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

![](https://academy.claude.com/assets/media/03ad074a9e3f24d799e4ac805037f211eb396dd141c2c6ac59fb2dc9d8b2bd6d.png)

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

![](https://academy.claude.com/assets/media/0a0f4bb26fa8c6fb5cf0245c1124101e1c0bdcf835cef8d3b045d8c3e069ab5a.png)

This demonstrates why chunking strategy matters so much. The goal is to create chunks that maintain semantic coherence and provide useful context when retrieved.

![](https://academy.claude.com/assets/media/a62744c2b485f4fef2941da5905df33efe4b85939c8cc1d2871d48712c8cdabe.png)

## Three Main Chunking Strategies

![](https://academy.claude.com/assets/media/6bbe9453171bfc5925e9574162beeba6e2c3d608d06d52bd8c2458edccb71a4a.png)

There are three primary approaches to dividing text into chunks:

* **Size-based:** Divide text into strings of equal length
* **Structure-based:** Split based on document structure (headers, paragraphs, sections)
* **Semantic-based:** Group related sentences or sections using NLP techniques

## Size-Based Chunking

Size-based chunking is the most straightforward approach. You simply divide your document into chunks of roughly equal character or word count. It's easy to implement and works reliably across different document types.

![](https://academy.claude.com/assets/media/35120558617205d6a68e8fc2799d33c104296832d923f4e5d75f378ee25929cd.png)

However, this approach has clear downsides:

* Words get cut off mid-sentence
* Chunks lose important context from surrounding text
* Related content might be split across multiple chunks

![](https://academy.claude.com/assets/media/fecf35c6b77511dff3a0cecc2efdae1dc26d80de1fb3c5803062e8d43c49ca7b.png)

## Adding Overlap

To address the context problem, you can implement an overlap strategy. Each chunk includes some characters from neighboring chunks, providing additional context and ensuring important information isn't lost at chunk boundaries.

![](https://academy.claude.com/assets/media/46f5d3dc0aaa3c2e1fcbd110dfffc8730112922367b3b5001531d29b3ba0116f.png)

While this creates some duplication, the trade-off is usually worth it for the improved context each chunk receives.

## Structure-Based Chunking

When your documents have consistent formatting (like markdown with clear headers), structure-based chunking can produce excellent results. You split on structural elements like headers, creating chunks that align with the document's natural organization.

![](https://academy.claude.com/assets/media/a07a9c97f7bdcfd571945d799a189043804e96751d509e2ec9e6f2e2ad4ab836.png)

This works beautifully for well-formatted documents but requires guarantees about document structure. It won't work reliably with plain text files or inconsistently formatted documents.

## Implementation Examples

Here are three practical chunking functions you can implement:

### Character-Based Chunking

python

```
def chunk_by_char(text, chunk_size=150, chunk_overlap=20):
    chunks = []
    start_idx = 0

    while start_idx < len(text):
        end_idx = min(start_idx + chunk_size, len(text))
        chunk_text = text[start_idx:end_idx]
        chunks.append(chunk_text)

        start_idx = (
            end_idx - chunk_overlap if end_idx < len(text) else len(text)
        )

    return chunks
```

### Sentence-Based Chunking

python

```
def chunk_by_sentence(text, max_sentences_per_chunk=5, overlap_sentences=1):
    sentences = re.split(r"(?<=[.!?])\s+", text)
    chunks = []
    start_idx = 0

    while start_idx < len(sentences):
        end_idx = min(start_idx + max_sentences_per_chunk, len(sentences))
        current_chunk = sentences[start_idx:end_idx]
        chunks.append(" ".join(current_chunk))

        start_idx += max_sentences_per_chunk - overlap_sentences

        if start_idx < 0:
            start_idx = 0

    return chunks
```

### Section-Based Chunking

python

```
def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)
```

## Choosing the Right Strategy

Your choice of chunking strategy depends entirely on your specific use case:

* **Character-based:** Most reliable fallback, works with any document type
* **Sentence-based:** Good balance of context and meaning for prose
* **Section-based:** Excellent results when you have structured documents

For user-uploaded documents with no formatting guarantees, character-based chunking is often your safest bet. For well-structured internal documents, section-based chunking can provide superior results. Sentence-based chunking works well for most prose but can struggle with code or technical documents that use periods in unexpected ways.

Remember that chunking is often an iterative process. Start with a simple approach, test it with your specific documents and use cases, then refine based on the quality of results you're getting from your RAG system.
