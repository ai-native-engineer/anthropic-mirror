<!-- source: https://claude.com/marketplace/connectors/pdf-tools -->

More[Documentation (opens in new tab)](https://github.com/Open-Document-Alliance/PDF-Tools/blob/master/README.md)[Support (opens in new tab)](https://github.com/Open-Document-Alliance/PDF-Tools)

PDF Tools turns Claude Desktop into a complete PDF workstation with local file operations. Claude can fetch PDFs from URLs, inspect them visually, fill forms, manage pages, add signature/date zones, apply local signatures or text, extract structured data, and return document content to the selected MCP host for analysis.

This package targets Claude Desktop and other local MCP hosts today. It does not yet include a remote Claude/Cowork connector.

\*\*Interactive PDF Viewer:\*\*

• View PDFs with page navigation, zoom, search, text selection, and fullscreen

• See form fields in a sidebar with fill status

• Use visual page management to reorder, rotate, and remove pages before saving

• Switch into Sign mode to work with signature/date zones on the PDF

\*\*Sign Mode & Local Signatures:\*\*

• Detect signature, initials, printed-name, and date zones with visible coordinates Claude can reason from

• Draw or reuse saved local signatures

• Place signatures, dates, or other text on detected or custom zones

• Inspect a region, preview it, and turn it into a typed signing zone when the automatic detector is not enough

• Keep edits local, with active-document tracking and automatic backup behavior for same-file mutations

\*\*URL-to-PDF Workflows:\*\*

• Fetch PDFs from HTTP(S) URLs to the user's local machine, including cases where Claude's WebFetch is blocked

• Open downloaded PDFs immediately in the viewer for fill, sign, page management, extraction, or analysis

• Use page-bounded reads, text search, page renders, and region renders instead of one brittle all-document operation

\*\*Forms & Reusable Profiles:\*\*

• Fill W-9s, 1099s, rental applications, waivers, and any fillable PDF

• Save personal or business details as reusable profiles

• List, load, and apply saved profiles so repeated forms take seconds instead of minutes

• Bulk fill many PDFs from CSV data and validate required fields before submission

\*\*Page Organization Tools:\*\*

• Merge multiple PDFs into one document

• Split PDFs by exact page ranges or regular intervals

• Rotate and reorder pages, or apply a full page plan in one pass

• Keep the original intact by saving organized output as a new file

\*\*Extraction, Rendering & Analysis:\*\*

• Read existing PDF text layers for summarization, question answering, and research workflows

• Read specific page ranges and search PDF text with page-numbered snippets

• Convert supported born-digital page ranges to deterministic Markdown with explicit coverage gaps

• Render full pages or bounded regions to PNG for host/model vision on scanned or image-heavy documents

• If a selected `read\_pdf\_content` extraction has no text, return a rendered image of page 1 when available

• Keep rendering and text recognition distinct: page and region renders are raster images, not OCR text

• Treat mixed text/raster documents and raster pages after page 1 as potentially unrecognized by broad text reads

• Extract structured data to CSV

• Inspect page-level details like orientation, text presence, images, and likely blank pages

• Review metadata such as page count, dimensions, form fields, and file size

\*\*Local file operations and host-aware privacy:\*\* PDF Tools reads, renders, edits, and saves files on the user's machine and does not upload them to a separate PDF service. Text, images, or metadata returned through MCP may be processed under the selected host or model provider's data terms. Claude Desktop users choose which folders PDF Tools may read from or write to.

\*\*Works with many PDF types:\*\* Forms, contracts, research papers, technical manuals, invoices, financial statements, scanned documents, municipal packets, and encrypted PDFs. The local runtime does not currently bundle OCR; optional local OCR remains planned rather than shipped.

\*\*Best for:\*\* People who need more than a viewer: operators processing forms, lawyers organizing contracts, accountants handling tax documents, researchers reviewing papers, and anyone who wants local PDF file operations with their chosen MCP host.

## Tools

* display\_pdf
* list\_pdfs
* read\_pdf\_fields
* fill\_pdf
* bulk\_fill\_from\_csv
* save\_profile
* load\_profile
* list\_profiles
* fill\_with\_profile
* extract\_to\_csv
* validate\_pdf
* read\_pdf\_content
* read\_pdf\_pages
* read\_pdf\_layout
* convert\_pdf\_to\_markdown
* verify\_table\_proposal
* render\_pdf\_page
* render\_pdf\_region
* search\_pdf\_text
* get\_pdf\_resource\_uri
* get\_pdf\_identity
* merge\_pdfs
* split\_pdf
* rotate\_pdf\_pages

Show all 43 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://raw.githubusercontent.com/grafana/ai-marketplace/12be5634a492f73c189d466c5449d09b853ad7a4/plugins/grafana-cloud-mcp/assets/logo.svg)

### [Grafana Cloud](https://claude.com/marketplace/connectors/grafana-cloud)

Anthropic verifiedNew

Query metrics, logs, and traces and manage dashboards and alerts

[Add Grafana Cloud in Claude (opens in new tab)](https://claude.ai/directory/3392c633-e335-4638-bda7-5b259808c3f7 "Add in Claude")

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/53ca8822f4c024f9b358b1e44148a1dc3c616dbe.svg?w=128&fit=max&auto=format)

### [Gmail](https://claude.com/marketplace/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://assets.claude.com/8aa6ad728cfe811f74a7b65b92b44fe774b1fe17.jpg?w=128&fit=max&auto=format)

### [Atlassian MCP](https://claude.com/marketplace/connectors/atlassian)

Search, read and update Jira, Confluence, Bitbucket, Loom and other Atlassian apps with your existing Atlassian permissions.

[Add Atlassian MCP in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")
