<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/pdf-support -->

Lesson 44 of 65 · Claude with Amazon BedrockPDF support

Claude can read and analyze PDF documents just as easily as it handles images. This capability opens up powerful possibilities for document analysis, summarization, and question-answering workflows.

## Setting Up PDF Processing

To work with PDFs, you'll need to make a few key changes to the standard message structure. The process is similar to image handling, but with some important differences in the document specification.

First, read your PDF file as binary data:

python

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()
```

## Document Message Structure

The message structure for PDFs differs from images in several ways. Instead of an "image" object, you'll use a "document" object with these required fields:

python

```
add_user_message(
    messages,
    [
        {"document": {"format": "pdf", "name": "earth", "source": {"bytes": file_bytes}}},
        {"text": "Summarize this document in one sentence"},
    ],
)
```

Key points about the document structure:

* Use `"document"` instead of `"image"`
* Set `"format": "pdf"`
* Include a `"name"` field with the filename without extension
* The `"source"` contains the file bytes

When you run this code, Claude analyzes the entire PDF content and provides a comprehensive response. In this case, it successfully summarized the Earth Wikipedia article, demonstrating its ability to process multi-page documents with complex layouts, images, and structured information.

## What Claude Can Do with PDFs

Claude can handle various PDF processing tasks:

* Extract and summarize key information
* Answer specific questions about document content
* Analyze document structure and formatting
* Process multi-page documents efficiently
* Work with PDFs containing both text and images

The PDF processing capability becomes even more powerful when combined with other features like citations, which allow Claude to reference specific parts of the document in its responses. This makes it particularly useful for research, document analysis, and content extraction workflows.
