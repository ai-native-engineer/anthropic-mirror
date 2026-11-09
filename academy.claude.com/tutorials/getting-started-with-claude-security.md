<!-- source: https://academy.claude.com/tutorials/getting-started-with-claude-security -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Getting started with Claude Security

Getting started with Claude Security

8 minClaude Security

![](https://academy.claude.com/assets/v1/thumbnail.light-ec0g8s4j.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-niae113s.png)

![](https://academy.claude.com/assets/media/7442485a1a64b789216cc80456f7ff291b578839cef64d75787bda356a6840e9.png)

Claude Security is a capability built into [Claude.ai(opens in new tab)](http://Claude.ai), which continuously watches your codebases for security vulnerabilities, tracks each finding until it is fixed, and suggests targeted software patches for you to review, allowing you and your team to find and fix security issues that traditional methods often miss. It is a beta feature available to Claude Enterprise accounts.

Most engineering teams don’t have the reviewer-hours and skills to identify sophisticated vulnerabilities across every change, and many issues are easy to miss without a security-focused mindset. Claude Security helps close that gap: it scans your codebase, surfaces the issues that actually matter, and proposes patches that you or your team can review and apply. Claude Security is powered by our full family of models, including Claude Mythos, with no Cyber Verification Program access required.

This guide covers everything you need to set up Claude Security, create your first Project, review findings, and find tips for ongoing use.

## **Prerequisites**[](#prerequisites)

Before you can use Claude Security, the following requirements must be in place:

* **Eligible plans:** Your organization must have an active Claude Enterprise account.
* **Access to your repositories**:
  + For repositories on GitHub, your administrator must have installed the [Claude GitHub App(opens in new tab)](https://github.com/apps/claude) and granted it access to the repositories you wish to scan, and each person who adds a repository must connect their own GitHub account to Claude. This is the same Claude GitHub App used for Claude Code in the cloud.
  + For GitHub Enterprise Server, the app must be installed on your GHES instance, and that instance must already be connected to Claude Code in the cloud.
* For repositories hosted on other Git providers (e.g. GitLab, BitBucket, etc.), you need the repository’s address and an auth token.
* **Permission to create Projects:** Admins can decide what RBAC roles can create Claude Security projects.
* **User Seats:** Each person who uses Claude Security needs a seat that includes Claude Code ([which seats do(opens in new tab)](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)).
* **Claude Code in the cloud (optional):** Lets users run suggested fixes with [Claude Code in the cloud(opens in new tab)](https://code.claude.com/docs/en/claude-code-on-the-web). Without it, they copy a prompt into their own Claude Code.

## **Setup**[](#setup)

If your organization already uses Claude Code in the cloud, most of the setup is already complete. Here is what you need to confirm:

1. **Check billing.** Scans are charged at direct token cost, with no additional platform fee. If your plan has Standard and Premium seats, turn on usage credits first ([how(opens in new tab)](https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans)). On other Enterprise plans, see [How am I billed for my Enterprise plan?(opens in new tab)](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan). Costs scale with the size of your repositories and how often they change, so set spend limits that align with your expected usage. After Claude Security is enabled, you can also set a separate spend limit for the feature.
2. **Give Claude access to your GitHub repositories.** Install the [Claude GitHub App(opens in new tab)](https://github.com/apps/claude) on the repositories you want to scan (on a GitHub organization, an owner of that organization may need to approve it), and turn on the **GitHub connector** in Organization settings > Connectors. For GitHub Enterprise Server, follow the [GitHub Enterprise Server guide(opens in new tab)](https://code.claude.com/docs/en/github-enterprise-server). For repositories hosted on other Git servers, create an auth token for the repositories you plan to add.
3. Enable the **Claude Security** feature in the admin console: [http://claude.ai/admin-settings/claude-security(opens in new tab)](https://claude.ai/admin-settings/claude-security)
4. **Configure access and capabilities.** Admins can decide what RBAC roles can create projects and who can view, triage, or manage all projects by configuring the capabilities in custom roles.
5. **Enable Claude Code in the cloud (optional).** This allows users to run fixes in the cloud. It is optional otherwise.

Each person who uses Claude Security also connects their own GitHub account to Claude ([how to check(opens in new tab)](https://support.claude.com/en/articles/14661296-use-claude-security#h_8db96825dc)).

## **Creating a Project**[](#creating-a-project)

Once Claude Security is enabled, creating a Project is straightforward:

1. **Navigate to Claude Security through Claude.ai.** Go to [claude.ai(opens in new tab)](http://claude.ai) and click on the Security icon on the left sidebar, or [claude.ai/security(opens in new tab)](http://claude.ai/security).
2. **Click “New project” and give it a name.** A Project is the unit of access control and billing.
3. **Add repositories.** Connect up to eight repositories from GitHub or other Git providers. For each repository, you can optionally set a branch, a folder scope, and excluded folders.
4. **Add what the code can’t show (optional).** Tell Claude how your code is deployed, who can reach it, and which risks you’ve accepted, as notes or as documents such as architecture docs. You can edit these later.
5. **Create the Project.** Click “Create project”. Claude reads the code, writes a threat model, and runs a deep baseline scan. Depending on the size of the repositories, the baseline scan may take several minutes or hours, and you can leave the page while it runs.
6. **Review findings.** Findings appear on the Project’s Findings tab as Claude reports them with details including vulnerability type, severity, affected file and line, and a description of the issue.

Afterwards, Claude checks for new commits and continuously scans for vulnerabilities.

## **Reviewing and Acting on Findings**[](#reviewing-and-acting-on-findings)

A Project’s Findings tab lists its open findings. You have several options for each finding:

* **Review details.** Each finding includes a description of the vulnerability, the affected code locations, the evidence and reasoning behind it, and a suggested fix. You can also ask Claude about a finding in the Project’s chat.
* **Start a fix.** Click “Fix” on a finding to open Claude Code and fix that specific vulnerability.
* **Triage a finding.** Mark it as fixed, or dismiss it as a false positive, an accepted risk, a duplicate, or for another reason.
* **Track fixes.** Claude checks open findings against the code that changed and marks them fixed when the fix lands. A finding marked fixed reopens automatically if Claude later finds the issue again.
* **Export findings.** To export findings into your own tracking and notification systems, use the Claude Security API, the Claude Security connector, or webhooks.

Findings are categorized by severity to help you prioritize your remediation efforts. We recommend starting with the highest-severity items and working through the list.

## **Tips for ongoing use**[](#operationalizing-the-tool-for-ongoing-use)

These tips make ongoing use easier.

### **Set up Projects**[](#set-up-projects)

* **Group related repositories in one Project:** Create one Project per service or team so findings stay attributable and reviewers don’t have to wade through results that belong to someone else. Put repositories that work together, such as a backend and its client app, in the same Project so Claude can trace issues across them. A Project holds up to eight repositories from GitHub or other Git providers.
* **Scope large repositories:** For large repositories and monorepos, set a folder scope on each repository and exclude the folders you don’t need covered. A narrower scope increases determinism and focuses Claude’s attention. Claude can still trace logic and pull context from across the broader codebase, excluded folders included, as needed.
* **Add what the code can’t show:** Tell Claude how your code is deployed, who can reach it, and which risks you’ve accepted. Claude keeps this in each Project’s threat model and uses it to decide what to flag and how to rate it. To read and edit the threat model or add documents such as architecture docs, open the Project’s Resources tab. People with the Full role can edit them.

### **Triage and collaborate**[](#triage-and-collaborate)

* **Add a reason and a note when you triage:** When you triage a finding, pick the reason and add a triage note to create an audit trail and give future reviewers context. Claude reads the notes on dismissed findings too, and uses them for the Project. Each finding also keeps a History of who changed it and when, for audit and compliance.
* **Share Projects with teammates:** In a Project, click Share to give specific members a role:

  + **Full:** manage findings, settings, and who has access
  + **Triage:** view findings, update their status, and start fixes
  + **View:** just stay informed

  You can also share a Project with your whole org.

### **Connect your tools**[](#connect-your-tools)

* **Pull findings into your systems with the API:** Create a personal access token in Claude Security settings. Then use the Claude Security API to pull findings into your ticketing, vulnerability management, and reporting tools, and to resolve them from there, so triage and status live alongside everything else the team uses.
* **Fix and resolve in one session with the connector:** With the Claude Security connector, engineers can pull up a finding in Claude or Claude Code, fix it, and resolve it in the same session.
* **Alert your team with webhooks:** Create webhooks in Claude Security settings to push new-finding events into your own systems in real time. Wire them into tools like Slack or Jira so triage can start without anyone having to check the dashboard.

### **Manage cost and access**[](#manage-cost-and-access)

* **Track each Project’s cost:** In a Project’s settings, open Usage to see its cost for the month to date and per day.
* **Roll out to more teams with custom roles:** Admins can use [custom roles(opens in new tab)](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans) to decide which RBAC roles can create Projects and who can view, triage, or manage all Projects.

For more information and FAQ, please visit our [support center.(opens in new tab)](https://support.claude.com/en/articles/14661296-use-claude-security)

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Creating a Project](#creating-a-project)
* [Reviewing and Acting on Findings](#reviewing-and-acting-on-findings)
* [Tips for ongoing use](#operationalizing-the-tool-for-ongoing-use)
