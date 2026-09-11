<!-- source: https://claude.com/connectors/unstructured-transform -->

[Skip to main content](#main-content)

Connector URL`https://mcp.transform.unstructured.io/`

More[Documentation (opens in new tab)](https://docs.unstructured.io/transform/overview)[Support (opens in new tab)](mailto:support@unstructured.io)[Privacy policy (opens in new tab)](https://unstructured.io/privacy-policy)

Unstructured Transform turns real-world documents into clean, structured, AI-ready data. Point it at a file — PDF, Word, PowerPoint, Excel, HTML, email, scanned images, and ~70 other formats — and it returns the content as Markdown, element-level JSON, HTML, or plain text that an agent can act on immediately.

Under the hood it runs a configurable pipeline: partition documents into structured elements (titles, paragraphs, tables, lists, images) with layout and page metadata; optionally enrich them with vision-language passes (image and table descriptions, table-to-HTML, named-entity recognition, generative OCR); chunk the content for retrieval; and generate embeddings for a vector store. It can also extract structured JSON from a document against a schema you provide — or draft that schema for you.

Work is submitted as an asynchronous job, and results are delivered out of band through a short-lived download link, so even large documents never overwhelm the conversation. Each request handles up to 10 files, 50 MB per file.

Common uses: feed specification PDFs into a coding task, ground answers in policy or contract documents, build a searchable Q&A corpus over enterprise files, pull structured fields from forms, invoices, or contracts against a JSON schema, or prepare large document sets for a RAG pipeline.

Requires a free Unstructured account. Learn more at docs.unstructured.io/transform.

## Tools

* check\_job\_status
* get\_job\_results
* request\_file\_upload\_url
* start\_extraction\_job
* start\_transform\_job
* suggest\_extraction\_schema\_for\_file

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://drive.google.com&size=64)

### [Google Drive](https://claude.com/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://t0.gstatic.com/faviconV2?client=SOCIAL&type=FAVICON&fallback_opts=TYPE,SIZE,URL&url=https://calendar.google.com&size=64)

### [Google Calendar](https://claude.com/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=microsoft.com&sz=96)

### [Microsoft 365](https://claude.com/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=atlassian.com&sz=96)

### [Atlassian Rovo](https://claude.com/connectors/atlassian)

Access Jira & Confluence from Claude

[Add Atlassian Rovo in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://www.notion.so/images/notion-logo-block-main.svg)

### [Notion](https://claude.com/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")

![](https://www.google.com/s2/favicons?domain=slack.com&sz=96)

### [Slack](https://claude.com/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")
