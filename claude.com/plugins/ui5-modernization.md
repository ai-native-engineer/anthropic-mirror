<!-- source: https://claude.com/plugins/ui5-modernization -->

# UI5 Modernization

SAPUI5/OpenUI5 modernization toolkit with workflow and specialized fix patterns

  [SAP SE](https://github.com/UI5/plugins-coding-agents)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

A complete toolkit for modernizing SAPUI5 and OpenUI5 applications. The plugin provides a structured five-phase workflow that upgrades your UI5 app to manifest version 2.0.0 with a minimum framework version of 1.136.0 — covering test infrastructure, manifest and component configuration, module system globals, deprecated API replacements, and CSP compliance. Each phase commits separately for easy rollback, and a final report documents any issues requiring manual attention.

Includes 19 specialized fix skills that target specific UI5 linter rule categories: global namespace elimination (`/fix-js-globals`, `/fix-xml-globals`), deprecated control replacement (`/fix-deprecated-controls`), module dependency resolution (`/fix-cyclic-deps`, `/fix-pseudo-modules`), manifest and component modernization (`/fix-manifest-json`, `/fix-component-async`), CSP compliance (`/fix-csp-compliance`), bootstrap parameter updates (`/fix-bootstrap-params`), and more. Each skill uses the UI5 linter for both detection and verification.

Supports three verification modes — full autonomous (automated build/test with up to three self-remediation retries), half autonomous (build/test with user decision points), and manual (summary-only for external verification). Optionally integrates Chrome DevTools MCP for automated browser testing.

**How to use:** Run `/modernize-ui5-app` to launch the full end-to-end modernization workflow across all five phases. For targeted fixes, invoke individual skills like `/fix-deprecated-controls`, `/fix-js-globals`, `/fix-csp-compliance`, or `/modernize-test-starter`. Use `/modernize-flp-sandbox` to modernize FLP Sandbox configurations separately. Requires a UI5 project with `ui5.yaml` and a clean git working directory.
