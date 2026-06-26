<!-- source: https://claude.com/docs/third-party/claude-desktop/legal -->

##  Legal agreements

###  License

Your use of the Claude Desktop application, including in Claude Desktop on third-party (3P) mode, is subject to Anthropic’s [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms).

###  Commercial agreements

Claude Desktop on 3P routes model inference through the provider you configure (Google Cloud’s Vertex AI, Amazon Bedrock, Microsoft Foundry, a compatible gateway, or the Anthropic API directly). Inference usage is billed by, and subject to your agreement with, that provider. When you configure the Anthropic API as your provider, inference billing and data terms fall under your Anthropic agreement. Your existing commercial agreement with Anthropic continues to apply to your use of the Claude Desktop application, unless we’ve mutually agreed otherwise.

##  Compliance

When using Vertex AI or Bedrock, conversation content is sent only to your configured inference endpoint and stored on the local device; the compliance posture of your deployment is determined by your inference provider and the device environment you control. During the Microsoft Foundry preview, Claude models run on Anthropic’s infrastructure and customers are subject to Anthropic’s data use terms. See the [Overview](/docs/third-party/claude-desktop/overview) for the architecture and the provider-specific data path.
For Anthropic’s certifications and compliance reports, see the [Anthropic Trust Center](https://trust.anthropic.com).
For HIPAA, see [HIPAA](/docs/third-party/claude-desktop/overview#hipaa) on the Overview page. When using Vertex AI or Bedrock, Anthropic does not interact with PHI; the BAA relationship is between you and your cloud service provider, and any remote MCP servers you connect should be reviewed for HIPAA compliance.

##  Usage policy

Use of Claude models, including via Claude Desktop on 3P, is subject to the [Anthropic Usage Policy](https://www.anthropic.com/legal/aup).

##  Privacy and telemetry

The Claude Desktop application sends operational telemetry (crash reports and product analytics) to Anthropic by default. This telemetry contains no prompt or response content and can be fully disabled via managed configuration. See [Telemetry and egress](/docs/third-party/claude-desktop/telemetry) for what each category contains and how to disable it.
Anthropic’s [Privacy Policy](https://www.anthropic.com/legal/privacy) describes how Anthropic handles data it receives.

##  Security and trust

Security architecture, threat-model, and data-flow documentation for Claude Desktop and Claude Desktop on 3P is available on the [Anthropic Trust Center](https://trust.anthropic.com).

###  Security vulnerability reporting

Anthropic manages our security program through HackerOne. [Use this form to report vulnerabilities](https://hackerone.com/4f1f16ba-10d3-4d09-9ecc-c721aad90f24/embedded_submissions/new).

---

© Anthropic PBC. All rights reserved. Use is subject to applicable Anthropic Terms of Service.

[User identity and local data](/docs/third-party/claude-desktop/data-storage)[Changelog](/docs/cowork/changelog)
