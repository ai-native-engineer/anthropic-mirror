<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/text-chunking-strategies -->

Lesson 33 of 67 · Building with the Claude APIText chunking strategies

Text chunking is one of the most critical steps in building a RAG (Retrieval Augmented Generation) pipeline. How you break up your documents directly impacts the quality of your entire system. A poor chunking strategy can lead to irrelevant context being inserted into your prompts, causing your AI to give completely wrong answers.

![](https://academy.claude.com/assets/media/93d153d95565a34b8f54f369456c4867942a67313e604f11d87c7aa05bb41de0.jpg)

Consider this example: you have a document with sections on medical research and software engineering. If you chunk poorly, a user asking "How many bugs did engineers fix this year?" might get information about medical research instead of software engineering, simply because the medical section happened to contain the word "bug" in a different context.

![](https://academy.claude.com/assets/media/4e200d418f2f0e07231825504d56487aa94f8ce6ba0baee92b87726603815a2e.jpg)

This is why choosing the right chunking strategy matters so much. Let's explore three main approaches.

## Size-Based Chunking

![](https://academy.claude.com/assets/media/8258b5b1db40164bb6e4ecbce20307774f2ae37b64c3cef1efe1a0de0ff3c8f0.jpg)

Size-based chunking is the simplest approach - you divide your text into strings of equal length. If you have a 325-character document, you might split it into three chunks of roughly 108 characters each.

![](https://academy.claude.com/assets/media/3e4549a9b1cb208c34fae3610edfc3bfea3186dc7ccf6a13c23df5f098d95fbc.jpg)

This method is easy to implement and works with any type of document, but it has clear downsides:

* Words get cut off mid-sentence
* Chunks lose important context from surrounding text
* Section headers might be separated from their content

![](https://academy.claude.com/assets/media/ce9f3ba91e00a523dec9e8868bc25ced54d746bddb75f1c9504b58a5fb0584be.jpg)

To address these issues, you can add overlap between chunks. This means each chunk includes some characters from the neighboring chunks, providing better context and ensuring complete words and sentences.

![](https://academy.claude.com/assets/media/7aebd7018b93e601d2a19f227f84cf56ed2cd1b3a8cc72a32fe3a306d919f6bb.jpg)

Here's a basic implementation:

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

## Structure-Based Chunking

Structure-based chunking divides text based on the document's natural structure - headers, paragraphs, and sections. This works great when you have well-formatted documents like Markdown files.

![](https://academy.claude.com/assets/media/4fd57d1bcc54a111ec6ab2492c4211bc8442b21e92161a25a0f45c8bf9352d4f.jpg)

For a Markdown document, you can split on header markers:

python

```
def chunk_by_section(document_text):
    pattern = r"\n## "
    return re.split(pattern, document_text)
```

This approach gives you the cleanest, most meaningful chunks because each one represents a complete section. However, it only works when you have guarantees about your document structure. Many real-world documents are plain text or PDFs without clear structural markers.

## Semantic-Based Chunking

Semantic-based chunking is the most sophisticated approach. You divide text into sentences, then use natural language processing to determine how related consecutive sentences are. You build chunks from groups of related sentences.

This method is computationally expensive but produces the most relevant chunks. It requires understanding the meaning of individual sentences and is more complex to implement than the other strategies.

## Sentence-Based Chunking

A practical middle ground is chunking by sentences. You split the text into individual sentences using regular expressions, then group them into chunks with optional overlap:

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

## Choosing Your Strategy

Your choice depends entirely on your use case and document guarantees:

* **Structure-based**: Best results when you control document formatting (like internal company reports)
* **Sentence-based**: Good middle ground for most text documents
* **Size-based**: Most reliable fallback that works with any content type, including code

Size-based chunking with overlap is often the go-to choice in production because it's simple, reliable, and works with any document type. While it may not give perfect results, it consistently produces reasonable chunks that won't break your pipeline.

Remember: there's no single "best" chunking strategy. The right approach depends on your specific documents, use cases, and the trade-offs you're willing to make between implementation complexity and chunk quality.
