<!-- source: https://support.claude.com/en/articles/16059458-inference-hooks-overview -->

Inference hooks lets your compliance team inspect and enforce policy on every prompt, tool call response, and uploaded file text before it reaches Claude.

Inference hooks are available in beta to Enterprise plans and cover Claude, Claude Code, Cowork, and all other Claude Enterprise products. They can be turned on and managed by Owners and Primary Owners.

When you turn on inference hooks, Claude sends every prompt to a server you host before it starts generating a response. Your server checks the prompt against your policy, then answers **allow** or **deny**. Claude only continues once it has that answer.

Because this check happens inside Claude’s infrastructure rather than on someone's device, it doesn't rely on anything installed on employees' devices. One setup covers your whole organization: Claude, Claude Code, Cowork, and more, including tool calls made through skills, plugins, and connected tools.

Common uses include data loss prevention, real-time transcript archival, and enforcing your own organization’s policies.

## Technical documentation

For the full technical documentation, including configuring and monitoring the hook, implementing an endpoint, verifying request signatures, and the API reference, see **[Inference hooks](https://platform.claude.com/docs/en/manage-claude/inference-hooks)**.

* [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
* [Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)
* [Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)
* [Claude Cowork architecture overview](https://support.claude.com/en/articles/14479288-claude-cowork-architecture-overview)
* [Enable US-only inference for your organization](https://support.claude.com/en/articles/15422948-enable-us-only-inference-for-your-organization)
