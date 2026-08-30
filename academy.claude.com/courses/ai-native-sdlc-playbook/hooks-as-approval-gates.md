<!-- source: https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates -->

Lesson 11 of 14 · The AI-Native SDLC PlaybookHooks as approval gates

3. /[The AI-Native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

[The AI-Native SDLC Playbook](https://academy.claude.com/courses/ai-native-sdlc-playbook)

# Hooks as approval gates

Lesson 115 min

The build phase used hooks as guardrails, allowing or blocking actions with no human involved (**Stage 3: Build**). A hook can also ask, pausing the action until a specific person approves, which is what release gating needs.

The play sits in **Stage 5: Deploy** because the release gate is the clearest case, but hooks are not deploy-specific: they run wherever Claude acts. For example, hooks can block edits to migrations and infra without a change ticket during **Stage 3: Build**, and stop the agent editing test files during a fix task in **Stage 4: Test**.

## Getting started[](#getting-started)

* **Prerequisites**: None.
* **Infrastructure**: A written list of the approvals the change process requires.

## How to execute it[](#how-to-execute-it)

1. Engineering leadership, with change management and compliance, lists the human approval gates that must survive, such as change management sign-off, release authorization, and edits to protected paths.
2. The platform engineer expresses each gate as a hook, a script that runs before Claude acts that can allow, ask, or block.
3. Team hooks go in `.claude/settings.json` in Git, and non-negotiable hooks go in managed settings owned by the platform or IT admin, where individual engineers cannot switch them off.
4. A block should explain itself, so when a hook stops an action, the reason and the route to approval appear in Claude's output.

## What it looks like[](#what-it-looks-like)

A standalone example in the project's `.claude/settings.json`:

json

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/production-gate.sh" }
        ]
      }
    ]
  }
}
```

**And the gate itself (`.claude/hooks/production-gate.sh`):**

bash

```
#!/bin/bash
# Production deploys require a named release authorization
cmd=$(jq -r '.tool_input.command' < /dev/stdin)
if [[ "$cmd" == *"deploy"* && "$cmd" == *"production"* ]]; then
  if [ -z "$RELEASE_APPROVAL" ]; then
    echo "Production deploys need a release authorization." >&2
    exit 2   # exit 2 blocks the action; the message goes to Claude
  fi
fi
exit 0
```

## Governance considerations[](#governance-considerations)

Hooks are the approval gates. The gate condition is enforced every time, for everyone. Allow and block decisions are logged with a timestamp. The gate also defines what counts as approval, whether that's an approved change ticket or the release manager's sign-off.

## Managed settings for a regulated enterprise[](#managed-settings-for-a-regulated-enterprise)

Managed settings for a regulated enterprise, deployed by the platform team via mobile device management (MDM) or the admin console. Engineers cannot edit or override any of the settings therein. See below:

json

```
{
  "permissions": {
    "deny": [
      "Read(.env*)", "Read(./secrets/**)",
      "WebFetch", "Bash(curl *)", "Bash(wget *)"
    ],
    "allow": [
      "Bash(git *)", "Bash(make build)",
      "Bash(make test)", "Bash(make lint)"
    ],
    "disableBypassPermissionsMode": "disable"
  },
  "allowManagedPermissionRulesOnly": true,
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "allowUnsandboxedCommands": false,
    "network": { "allowedDomains": ["git.internal.example.com", "registry.npmjs.org"] },
    "credentials": {
      "files": [
        { "path": "~/.ssh", "mode": "deny" },
        { "path": "~/.aws/credentials", "mode": "deny" }
      ],
      "envVars": [ { "name": "GITHUB_TOKEN", "mode": "deny" } ]
    }
  },
  "allowManagedHooksOnly": true,
  "disableSideloadFlags": true,
  "allowManagedMcpServersOnly": true,
  "strictKnownMarketplaces": [
    { "source": "github", "repo": "example-corp/approved-plugins" }
  ],
  "requiredMinimumVersion": "2.1.193"
}
```

**What the settings do, in control terms:**

* `permissions.deny` keeps secrets out of the agent's context and blocks arbitrary network egress through tools. `permissions.allow` pre-approves the safe inner loop so the deny list doesn't turn into prompt fatigue.
* `disableBypassPermissionsMode` plus `allowManagedPermissionRulesOnly` means no engineer, project file, or command-line flag can widen the rules.
* `sandbox` covers what permissions cannot. A tool-level deny on WebFetch doesn't stop a shell command reaching the network, whereas the OS-level domain allowlist blocks egress outright, so the two enforce one objective at different layers. `failIfUnavailable` and `allowUnsandboxedCommands` turn the sandbox into a precondition, meaning Claude Code refuses to start when the sandbox cannot initialize and a command that fails inside the sandbox cannot be retried outside it.
* `credentials` handles a case the deny rules miss. `permissions.deny` governs Claude's file tools, but a sandboxed shell command could still read `~/.ssh` or `~/.aws/credentials` by default. This block denies those reads and strips the listed secrets from the environment of sandboxed commands.
* `allowManagedHooksOnly` means only hooks defined in managed settings run; hooks in user, project, and local settings are blocked, including the standalone `.claude/settings.json` example above. To keep this play's approval gate enforced, define it in the managed file's own `hooks` block.
* `disableSideloadFlags` and `strictKnownMarketplaces` mean that any skill, agent, hook, or MCP server on an engineer's machine came through the organization's approved plugin marketplace and not from a home directory. The marketplace allowlist controls what can be installed, and the flags that would sideload a plugin, agent, or MCP config for a single run are rejected at startup.
* `allowManagedMcpServersOnly` makes the agent's tool surface an allowlist owned by the platform team.
* `requiredMinimumVersion` refuses to start on a version below the approved floor, so the controls are enforced by a build the organization has actually assessed.

Treat the example as a starting point to customize to your own environment. Each deny rule removes some capability, and the right balance depends on the data classification of the repo. The [settings reference(opens in new tab)](https://code.claude.com/docs/en/settings) documents all keys, including the managed-only ones.

## How to measure it[](#how-to-measure-it)

For the hooks themselves:

* **Leading indicator**: Time spent waiting on each approval gate. Every hook decision is written to the OpenTelemetry export with a timestamp and an allow or block verdict, so the wait is visible per gate.
* **Lagging indicator**: Gate violations reaching production before and after hooks, from the incident tracker.

[Previous lessonAI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop)[Next lessonCI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment)

Lesson 11 of 14 · The AI-Native SDLC PlaybookHooks as approval gates

Introduction

* [Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction)

Stage 1: Plan

* [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent)

Stage 2: Design

* [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design)

Stage 3: Build

* [Claude Code plan mode as the default starting point](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode)
* [The CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md)
* [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge)
* [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents)

Stage 4: Test

* [Give Claude a feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop)
* [Continuous evals in CI](https://academy.claude.com/courses/ai-native-sdlc-playbook/continuous-evals-in-ci)

Stage 5: Deploy

* [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop)
* [Hooks as approval gates](https://academy.claude.com/courses/ai-native-sdlc-playbook/hooks-as-approval-gates)
* [CI/CD integration and deployment](https://academy.claude.com/courses/ai-native-sdlc-playbook/ci-cd-integration-and-deployment)

Stage 6: Maintain

* [Closing the loop on metrics](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-the-loop-on-metrics)

Closing

* [Closing thoughts and resources](https://academy.claude.com/courses/ai-native-sdlc-playbook/closing-thoughts-and-resources)

* [Course complete](https://academy.claude.com/courses/ai-native-sdlc-playbook/complete)

* [Getting started](#getting-started)
* [How to execute it](#how-to-execute-it)
* [What it looks like](#what-it-looks-like)
* [Governance considerations](#governance-considerations)
* [Managed settings for a regulated enterprise](#managed-settings-for-a-regulated-enterprise)
* [How to measure it](#how-to-measure-it)
