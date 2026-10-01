<!-- source: https://claude.com/marketplace/connectors/minutes-conversation-memory -->

More[Documentation (opens in new tab)](https://useminutes.app/for-agents)[Support (opens in new tab)](https://useminutes.app)[Privacy policy (opens in new tab)](https://useminutes.app/privacy)

Minutes is the private, owned conversation-memory layer. Record meetings, voice memos, and dictation; transcribe them on your own machine; and get structured markdown in `~/meetings/` that policy-aware local tools expose to Claude Desktop, Claude Code, Codex, Gemini CLI, Cursor, OpenCode, Pi, and MCP-compatible clients — no proprietary SDK, no API key. Restricted meetings are excluded from agent results by default; explicit access requires a trusted launch policy, a per-call request, and a durable audit record. Minutes never uploads your audio; meeting text leaves your device only when you explicitly send policy-authorized context to a connected cloud agent or summarizer. When a cloud memory tool gets acquired or subpoenaed, your recordings aren't theirs to hand over. No vendor to outlive — ten years from now, `grep` still works on your corpus.

34 tools • 11 resources • Interactive MCP App dashboard • 6 prompt templates

What you get:

• On-device transcription with sealed local whisper.cpp and optional on-device summarization (Apple Foundation Models on macOS 26+) — your audio never leaves the machine. Retained Parakeet and Apple Speech preferences resolve to Whisper until those helpers support secure byte transport.

• Re-run the AI pass on edited meetings and memos with preview-first output, backup-on-apply writes, and edit-preserving merges.

• A native chat panel that recalls policy-authorized meetings, with token streaming and read-only policy-bound search.

• Dictation that types straight at your cursor, on the same local engine.

• Live sessions that promote into diarized, summarized meetings when you stop.

• Consent provenance in every file, and sensitivity gating agents must respect.

• Diarized speaker labels, structured action items and decisions, and policy-safe search over owned markdown. Cross-meeting relationship answers are rebuilt from bounded live policy-authorized snapshots; compatibility-only derived insight and annotation reads still fail explicitly until their source provenance can be revalidated.

\*\*Before you start.\*\* Minutes runs entirely on your own machine, so it needs the Minutes engine installed locally. The extension normally downloads it for you the first time it runs. If your machine cannot reach the internet, or you are on a platform we do not publish a binary for, install it yourself: on macOS and Windows get the free desktop app from https://useminutes.app, which includes the engine and keeps it updated; on Linux install the CLI from the same page. Until the engine is present the extension still starts and lists its tools, and each tool will tell you what is missing.

## Tools

* start\_recording
* stop\_recording
* get\_status
* list\_processing\_jobs
* list\_meetings
* search\_meetings
* get\_meeting
* activity\_summary
* search\_context
* get\_moment
* get\_screen\_context
* process\_audio
* add\_note
* consistency\_report
* get\_person\_profile
* research\_topic
* start\_dictation
* stop\_dictation
* track\_commitments
* relationship\_map
* list\_voices
* confirm\_speaker
* get\_meeting\_insights
* start\_live\_transcript

Show all 34 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/8aa6ad728cfe811f74a7b65b92b44fe774b1fe17.jpg?w=128&fit=max&auto=format)

### [Atlassian MCP](https://claude.com/marketplace/connectors/atlassian)

Anthropic verifiedTrending

Search, read and update Jira, Confluence, Bitbucket, Loom and other Atlassian apps with your existing Atlassian permissions.

[Add Atlassian MCP in Claude (opens in new tab)](https://claude.ai/directory/11ba10d9-477b-4988-bd1c-90a7fa680dc1 "Add in Claude")

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/53ca8822f4c024f9b358b1e44148a1dc3c616dbe.svg?w=128&fit=max&auto=format)

### [Gmail](https://claude.com/marketplace/connectors/gmail)

Draft replies, summarize threads, & search your inbox

[Add Gmail in Claude (opens in new tab)](https://claude.ai/directory/2701e52f-b826-4aaf-8b25-11f2a97c98b0 "Add in Claude")

![](https://assets.claude.com/646945a1897f9146e5221ee6ace82001a2e52f4d.svg?w=128&fit=max&auto=format)

### [Google Calendar](https://claude.com/marketplace/connectors/google-calendar)

Manage your schedule and coordinate meetings effortlessly

[Add Google Calendar in Claude (opens in new tab)](https://claude.ai/directory/2a838eaa-f7b4-4bc2-bd47-c326f3c813c5 "Add in Claude")

![](https://assets.claude.com/e476a6c2c2f961f5f2120482f37b1daafc1506d9.jpg?w=128&fit=max&auto=format)

### [Canva](https://claude.com/marketplace/connectors/canva)

Search, create, autofill, and export Canva designs

[Add Canva in Claude (opens in new tab)](https://claude.ai/directory/eb9240f2-e1c1-43c1-828f-0fda40c22e4c "Add in Claude")

![](https://assets.claude.com/20c8443aa72ae4e4d77f923e6c33314713f965e8.svg?w=128&fit=max&auto=format)

### [Microsoft 365](https://claude.com/marketplace/connectors/microsoft-365)

Access your company's SharePoint, OneDrive, Outlook, and Teams directly in Claude

[Add Microsoft 365 in Claude (opens in new tab)](https://claude.ai/directory/ce0c9cda-5ea5-44c5-9cf2-40810dfa6582 "Add in Claude")
