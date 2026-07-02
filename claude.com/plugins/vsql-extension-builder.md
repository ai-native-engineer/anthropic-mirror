<!-- source: https://claude.com/plugins/vsql-extension-builder -->

# VillageSQL Extension Builder

Builds a VillageSQL extension for MySQL end-to-end through a 7-phase persona-driven workflow. Commonly used to port P...

  [VillageSQL](https://github.com/villagesql)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Builds production-quality VillageSQL (MySQL) extensions end-to-end through a structured 7-phase, persona-driven workflow. Five specialized personas — Product Strategist, Architect, Team Lead, CTO, and End-User — each own distinct phases with strict quality gates, ensuring every extension passes feasibility analysis, incremental implementation with parallel code review, CTO quality audit, and live user acceptance testing before delivery.

The skill dynamically discovers the current VillageSQL Extension Framework (VEF) API from live SDK headers rather than hardcoded references, ensuring compatibility across SDK updates. It supports both C++ (default) and Rust extensions, and is commonly used to port PostgreSQL extensions to MySQL using a dedicated porting guide. Each phase produces tracked artifacts — architecture docs, limitation logs, acceptance criteria, and test output — so nothing is lost between steps.

**How to use:** Install the plugin and invoke the skill to start building an extension. The workflow begins automatically at Phase 0, where you describe your extension and confirm your environment. Example prompts:

`/vsql-extension-builder Build a JSON path query extension for MySQL` — starts the full 7-phase workflow from scratch.  
`/vsql-extension-builder Port the pg_trgm trigram extension from PostgreSQL to MySQL` — activates the PostgreSQL porting guide and walks through adaptation.  
Say `resume` at any point to pick up from the last completed gate after a session interruption.

The workflow handles scaffold generation from GitHub templates, CMake build configuration, automated test execution, three parallel code-review agents (Reuse, Quality, Efficiency), a CTO critic checklist audit, and final documentation generation including README, TESTING guide, known limitations with upstream issue drafts, and a structured closing summary.
