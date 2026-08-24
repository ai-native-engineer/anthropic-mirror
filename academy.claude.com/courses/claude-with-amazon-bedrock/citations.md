<!-- source: https://academy.claude.com/courses/claude-with-amazon-bedrock/citations -->

Lesson 45 of 65 · Claude with Amazon BedrockCitations

When working with PDFs in Claude, one of the biggest challenges is trust. Users often have to take it on faith that the AI is correctly interpreting the document contents. Claude's citations feature directly addresses this problem by showing exactly where information comes from in your source documents.

## Enabling Citations

To enable citations in your PDF processing, you need to add a single parameter to your document configuration:

python

```
with open("./earth.pdf", "rb") as f:
    file_bytes = f.read()

messages = []

add_user_message(
    messages,
    [
        {
            "document": {
                "format": "pdf",
                "name": "earth",
                "source": {"bytes": file_bytes},
                "citations": {"enabled": True}
            }
        },
        {"text": "How were Earth's atmosphere and oceans formed?"},
    ]
)

response = chat(messages)
```

The key addition is `"citations": {"enabled": True}` in the document dictionary. This tells Claude to track where it finds information and include citation data in its response.

## Understanding Citation Responses

When citations are enabled, Claude's response structure changes significantly. Instead of just returning text, you get multiple parts:

* **Text parts** - The regular response content you're familiar with
* **Citations content parts** - New structured data that maps statements back to source locations

The citations content includes detailed information about where Claude found supporting evidence for each statement, including the specific document, page numbers, and even the exact text that influenced its response.

## Why Citations Matter

Citations provide several key benefits for PDF-based applications:

* **Verification** - Users can check Claude's work by going back to the source
* **Confidence** - Knowing where information comes from builds trust in AI responses
* **Transparency** - The AI's reasoning process becomes visible and auditable
* **Accuracy** - Citations encourage more careful information extraction

This feature is particularly valuable in professional, academic, or research contexts where accuracy and source attribution are critical. Instead of treating Claude as a black box, citations turn it into a transparent research assistant that shows its work.
