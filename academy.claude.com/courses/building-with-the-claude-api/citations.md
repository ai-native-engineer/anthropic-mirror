<!-- source: https://academy.claude.com/courses/building-with-the-claude-api/citations -->

Lesson 42 of 67 · Building with the Claude APICitations

When Claude answers questions based on documents you provide, users might assume it's just drawing from its training data. But what if Claude could show exactly where it found specific information? That's where citations come in - a powerful feature that lets Claude reference specific parts of your source documents and show users exactly where each piece of information comes from.

## Why Citations Matter

Imagine asking Claude about how Earth's atmosphere formed and getting a detailed answer. Without citations, users have no way to verify the information or understand that Claude is actually referencing a specific document you provided. Citations solve this transparency problem by creating a clear trail from Claude's response back to your source material.

![](https://academy.claude.com/assets/media/acd587075d92213562edeea50e9dccc8a5ed4c4c8474f5e669bec3dc54e9702f.jpg)

## Enabling Citations

To enable citations, you need to modify your document message structure. Add two new fields to your document block:

python

```
{
    "type": "document",
    "source": {
        "type": "base64",
        "media_type": "application/pdf",
        "data": file_bytes,
    },
    "title": "earth.pdf",
    "citations": { "enabled": True }
}
```

The `title` field gives your document a readable name, while `citations: {"enabled": True}` tells Claude to track where it finds information.

## Understanding Citation Structure

When citations are enabled, Claude's response becomes more complex. Instead of simple text, you get structured data that includes citation information for each claim.

![](https://academy.claude.com/assets/media/8c3469eb501a1d2cdb2b07d59d3b83ed42c47b3636f0c413942887a57a502a9c.jpg)

Each citation contains several key pieces of information:

* **cited\_text** - The exact text from your document that supports Claude's statement
* **document\_index** - Which document Claude is referencing (useful when you provide multiple documents)
* **document\_title** - The title you assigned to the document
* **start\_page\_number** - Where the cited text begins
* **end\_page\_number** - Where the cited text ends

![](https://academy.claude.com/assets/media/2b7dd19d40b53383e053c90045559770e559173fb4550acdcd0f8bd388eb60f8.jpg)

## Building User Interfaces with Citations

The real power of citations comes from building user interfaces that make this information accessible. You can create interactive elements where users can hover over citation markers to see exactly where information came from.

![](https://academy.claude.com/assets/media/cf4ccf4c29402413b993b325a33c33bb63cafab2e27be3148430f9e37eee9613.jpg)

This creates a transparent experience where users can:

* See that Claude's answers are grounded in actual source material
* Verify the information by checking the original document
* Understand the context around each cited piece of information

## Citations with Plain Text

Citations aren't limited to PDF documents. You can also use them with plain text sources. When working with text, modify your document structure like this:

python

```
{
    "type": "document",
    "source": {
        "type": "text",
        "media_type": "text/plain",
        "data": article_text,
    },
    "title": "earth_article",
    "citations": { "enabled": True }
}
```

With plain text sources, instead of page numbers, you'll get character positions that pinpoint exactly where in the text Claude found each piece of information.

## When to Use Citations

Citations are particularly valuable when:

* Users need to verify information for accuracy
* You're working with authoritative documents that users should be able to reference
* Transparency about information sources is critical for your application
* Users might want to explore the broader context around specific facts

By implementing citations, you transform Claude from a "black box" that provides answers into a transparent research assistant that shows its work. This builds user trust and enables them to dive deeper into your source materials when needed.
