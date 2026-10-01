<!-- source: https://claude.com/marketplace/plugins/fiftyone -->

Build high-quality datasets and computer vision models with FiftyOne, the open-source platform by Voxel51. This plugin provides 13 specialized skills that connect to the FiftyOne MCP Server, enabling you to manage datasets, run model inference, evaluate predictions, find duplicates, visualize embeddings, and develop custom plugins — all through natural language.

Core data skills let you import datasets from local directories or Hugging Face Hub (supporting COCO, YOLO, VOC, KITTI, and more), export to popular formats, run an 8-phase dataset curation pipeline covering quality checks, duplicate removal, class balance analysis, annotation audits, and train/val/test splitting. Model skills handle running Zoo models for detection, classification, and segmentation, then evaluate results with mAP, precision, recall, and confusion matrices.

Development skills help you scaffold custom FiftyOne plugins with operators and panels, build UIs with the VOODO design system, generate Jupyter notebooks, enforce FiftyOne code style conventions, and troubleshoot common issues like persistence, connections, and performance.

**How to use:** After installing, ask naturally for what you need. Try prompts like: "Import my dataset from /path/to/data into FiftyOne", "Find and remove duplicate images in my dataset", "Run object detection on my dataset using a Zoo model", "Evaluate my model predictions against ground truth", "Curate my dataset for training", "Create an embeddings visualization of my dataset", or "Scaffold a new FiftyOne plugin". The plugin requires the FiftyOne MCP Server (`fiftyone-mcp`) to be running for dataset operations.

## Other plugins

### [Frontend Design](https://claude.com/marketplace/plugins/frontend-design)

Craft production-grade frontends with distinctive design. Generates polished code that avoids generic AI aesthetics.

### [Superpowers](https://claude.com/marketplace/plugins/superpowers)

Claude learns brainstorming, subagent development with code review, debugging, TDD, and skill authoring through Superpowers.

### [Code Review](https://claude.com/marketplace/plugins/code-review)

AI code review with specialized agents and confidence-based filtering for pull requests

### [Context7](https://claude.com/marketplace/plugins/context7)

Upstash Context7 MCP server for live docs lookup. Pull version-specific docs and code examples from source repos into LLM context.

### [Code Simplifier](https://claude.com/marketplace/plugins/code-simplifier)

Code clarity agent: simplifies and refines recently modified code while preserving functionality and consistency.

### [Playwright](https://claude.com/marketplace/plugins/playwright)

Browser automation and end-to-end testing MCP server by Microsoft. Enables Claude to interact with web pages, take screenshots, fill forms, and automate testing workflows.
