<!-- source: https://claude.com/resources/guides/claude-science-product-guide/when-to-use-which-claude-surface -->

Chapter 024 min read

# When to use which Claude surface

4 min read

35 min remaining

Claude works for life sciences teams in several ways. While Claude Science is the surface built for scientists, other Claude products cover the document, software, and enterprise work that surrounds your team's scientific discovery. Most organizations deploy more than one.

**Claude Science** is an application for the digital steps of research, including literature review, experiment design, data analysis, figure generation, and writeups. It runs locally next to the lab's data and compute, ships with domain capabilities across genomics, single cell, proteomics, structural biology, cheminformatics, and more, and tracks the provenance of every artifact so results can be reproduced and defended. *Covered in depth in the next chapter.*

[**Claude Chat** (opens in new tab)](https://claude.ai/) is the web and desktop chat interface, available at Claude.ai, for quick queries and drafting. A medical writer might use it to pressure-test a mechanism-of-action narrative, while a discovery scientist might use it to summarize a stack of papers ahead of a program review.

[**Claude Cowork** (opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) is a desktop application where Claude works across local files and connected systems—Benchling, Veeva, Microsoft 365, PubMed—to complete multi-step document projects. Reach for it for study- and submission-level work that spans folders and apps: reviewing every site monitoring report in a study folder, reconciling a TMF section, drafting a CSR section from a folder of TLFs.

[**Claude Code** (opens in new tab)](https://code.claude.com/docs/en/overview) is our command-line interface for software engineering teams, supporting scientific computing, biostatistics programming, and platform groups building and maintaining production pipelines and internal tools under version control. Use Claude Code when the output is software that ships to other teams; reach for Claude Science when the output is an analysis, a figure, or a result.

[**Claude for Microsoft 365** (opens in new tab)](https://marketplace.microsoft.com/en-us/product/office/wa200010725?tab=overview) puts Claude inside Word, Outlook, Excel, and PowerPoint via add-ins, and lets Claude search Outlook, Teams, SharePoint, and OneDrive via the M365 connector. A regulatory writer can redline a Module 2 summary with tracked changes and turn the gap analysis into a slide without leaving the app.

[**Claude Platform** (opens in new tab)](https://platform.claude.com/) is Anthropic's API for organizations embedding Claude into ELN, LIMS, CTMS, safety, and RWE systems. [**Claude Managed Agents** (opens in new tab)](https://platform.claude.com/docs/en/managed-agents/overview) runs any agent built on the Platform as a hosted service with long-running sessions, scoped permissions, and full execution tracing—for example, a Literature Surveillance agent monitoring PubMed and ClinicalTrials.gov for competitive readouts across a portfolio.

## Claude product matrix: when to use what

Claude product matrix

| Surface | Best for | Primary users | Where it runs | Example task |
| --- | --- | --- | --- | --- |
| Claude Science | End-to-end research analysis with full provenance—literature, pipelines, figures, writeup | Computational biologists, bioinformaticians, research scientists, PIs | Local app (macOS, Linux); dispatches to SSH, SLURM, or cloud compute | Run QC and clustering on this scRNA-seq dataset, show me the UMAP, then subset to immune cells and redo the marker analysis. |
| Claude Chat | Conversational drafting, day-to-day questions and answers in a chat interface | All staff | Browser, desktop, mobile | Summarize this document and flag any contradictory findings. |
| Claude Cowork | Cross-app study and document work that touches files and multiple systems | Medical writing, clinical operations, regulatory, medical affairs | Claude desktop app | Review the SAE narratives in this folder against the protocol and flag any that meet expedited reporting criteria. |
| Claude Code | Agentic software engineering inside a repository | Scientific computing, biostatistics programming, platform engineering | Terminal, IDE | Migrate or refactor large codebases |
| Claude for Microsoft 365 | In-place drafting, redlining, and review across the Microsoft suite | Medical writing, regulatory, clinical operations | Word, Outlook, Excel, PowerPoint (add-ins); Teams, SharePoint, OneDrive (connector) | Redline Module 2.5 against the new nonclinical data and produce a change summary for the submission team. |
| Claude Platform (API) | Embedding Claude into ELN, LIMS, CTMS, safety, or RWE systems | Scientific computing, R&D IT, clinical systems | Anthropic API, Amazon Bedrock, Google Vertex AI, Microsoft Foundry | Integrate Claude into our ELN to draft experiment summaries from structured results with source citations. |
| Claude Managed Agents | Running custom agents as hosted cloud services | Platform and scientific computing teams | Claude Platform (hosted by Anthropic) | Deploy our Literature Surveillance agent as a managed service with scoped database access and audit tracing. |
