<!-- source: https://claude.com/connectors/llamaparse -->

[Skip to main content](#main-content)

Connector URL`https://mcp.llamaindex.ai/mcp`

More[Documentation (opens in new tab)](https://developers.llamaindex.ai/llamaparse/)[Support (opens in new tab)](mailto:support@llamaindex.ai)[Privacy policy (opens in new tab)](https://www.llamaindex.ai/legal/privacy-notice)

Connect Claude to LlamaParse to read, search, and pull structured data from your documents. LlamaParse helps you achieve the Pareto frontier in cost and accuracy, enabling you to read documents at 4x lower token costs and up to 5x higher accuracy.

LlamaParse is especially helpful when dealing with documents that include:

- Complex page layouts with multiple columns or nested sections that need dedicated layout parsing, not just text extraction

- Embedded visuals like charts, images, and tables that require structured visual parsing to extract accurate numbers

- Low-quality scans or handwriting that need specialized document processing beyond what general-purpose models provide

LlamaParse provides multiple SOTA capabilities for document understanding, including the ability to:

- Parse entire documents into structured markdown, JSON, or HTML, ready for downstream agentic reasoning

- Extract defined schemas of information from long documents to pull out only what's relevant

- Index documents and search across them with filesystem-style tools: locate relevant files, grep for pattern matches, read a file in full, or run hybrid retrieval

- Classify documents into known types

- Split document pages into individual pre-defined sections

We also offer LiteParse, our open-source parser, which works well for text-heavy PDFs with straightforward single-column layouts and no tables, charts, or scanned pages to interpret.

Requires a LlamaParse account.

## Tools

* addFilesToDirectory
* classifyFile
* createDirectory
* createIndex
* estimateFileComplexity
* extractFile
* findFilesInIndex
* generateExtractionConfig
* getIndexStatus
* getUploadUrl
* getUserProjects
* grepFileFromIndex
* listDirectories
* listDirectory
* listIndexes
* parseFile
* parseWithLiteParse
* readFileFromIndex
* retrieveFromIndex
* splitFile
* syncIndex
* uploadFileByUrl

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

![](https://www.notion.so/images/notion-logo-block-main.svg)

### [Notion](https://claude.com/connectors/notion)

Connect your Notion workspace to search, update, and power workflows across tools

[Add Notion in Claude (opens in new tab)](https://claude.ai/directory/69f3a300-cc60-48c4-b237-dfac56530dbf "Add in Claude")

![](https://www.google.com/s2/favicons?domain=atlassian.com&sz=96)

### [Atlassian Rovo](https://claude.com/connectors/atlassian)

Access Jira & Confluence from Claude

[Add Atlassian Rovo in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=slack.com&sz=96)

### [Slack](https://claude.com/connectors/slack)

Send messages, create canvases, and fetch Slack data

[Add Slack in Claude (opens in new tab)](https://claude.ai/directory/597f662f-36de-437e-836e-5a81013cbfbe "Add in Claude")
