<!-- source: https://claude.com/resources/tutorials/getting-started-with-claude-security -->

# Getting started with Claude Security

  Professional
* Product

  Claude Security
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/getting-started-with-claude-security

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f3737a458dc4569ed9083d_Screenshot%202026-04-30%20at%208.21.23%E2%80%AFAM.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f38cd5490be2a82d14d5f4_Screenshot%202026-04-30%20at%2010.09.33%E2%80%AFAM.png)

Claude Security is a capability built into Claude.ai, which scans your codebases for security vulnerabilities and suggests targeted software patches for you to review, allowing you and your team to find and fix security issues that traditional methods often miss (See our [announcement](https://claude.com/product/claude-security) for more). It is a beta feature available to Claude Enterprise accounts.

Most engineering teams don’t have the reviewer-hours and skills to identify sophisticated vulnerabilities across every change, and many issues are easy to miss without a security-focused mindset. Claude Security helps close that gap: it scans your codebase, surfaces the issues that actually matter, and proposes patches that you or your team can review and apply.  
  
This guide covers everything you need to set up Claude Security, run your first scan, review findings, and operationalize the tool for ongoing use.

## **Prerequisites**

Before you can use Claude Security, the following requirements must be in place:

* **Eligible plans:** Your organization must have an active Claude Enterprise account.
* **Claude Code on the Web**: [Claude Code on the Web](https://code.claude.com/docs/en/claude-code-on-the-web) must be enabled for your organization. Users access it at claude.ai/code.
* **Extra Usage**: Extra usage needs to be enabled in order for consumption billing to work.
* **GitHub App Installed:** Your administrator must have installed the Anthropic GitHub App and granted it access to the repositories you wish to scan. This is the same GitHub App used for Claude Code on the Web.
* **User Seats:** Each user who will run scans needs a premium seat on your organization’s Claude.ai account.

> **Note:** Claude Security currently supports repositories hosted on GitHub.com.

## **Setup**

If your organization already uses Claude Code on the Web, most of the setup is already complete. Here is what you need to confirm:

1. **Verify Extra Usage is enabled.** Ensure Extra Usage is enabled in Organization Billing settings. Claude Security uses consumption billing. Costs scale with the size and number of scans you run, so set spend limits that align with your expected usage. After Claude Security is enabled, you can also set a separate spend limit for the feature.
2. **Verify GitHub App access.** Ensure the Anthropic GitHub App has been installed on your GitHub organization and has been granted access to the repositories you want to scan. Your Claude Code admin can confirm this in your GitHub organization’s settings under Installed GitHub Apps.
3. **Confirm user seats.** Each user who will run scans should have an active **premium** seat on your Claude.ai organization.  Standard seats do not include Claude Code on the Web.  Verify this in your Claude.ai admin console.
4. Enable the **Claude Security** feature in the admin console: [http://claude.ai/admin-settings/claude-security](https://claude.ai/admin-settings/claude-security)

Once these steps are complete, the Security Scan feature will appear in your Claude Code on the Web interface.

## **Running a Scan**

Once Claude Security is enabled, running a scan is straightforward:

1. **Navigate to Claude Security through Claude.ai.** Go to [claude.ai](http://claude.ai) and click on the Security icon on the left sidebar, or [claude.ai/security](http://claude.ai/security).
2. **Open Security.** You will see the Security entry point in your sidebar. Click on it to launch the scanning interface.
3. **Select a repository.** Choose the GitHub repository you want to scan from the list of available repos. You can optionally scope the scan to a specific directory or branch within the repo. For larger repositories, we highly recommend picking a directory to increase the success rate of the scan.
4. **Start the scan.** Click to begin the scan. Claude will analyze the codebase for vulnerabilities. Depending on the size of the repository, the scan may take several minutes or hours.
5. **Review findings.** Once the scan completes, findings are displayed with details including vulnerability type, severity, affected file and line, and a description of the issue. You can also view your scan history at claude.ai/security.

## **Reviewing and Acting on Findings**

After a scan completes, you have several options for each finding:

* **Review details.** Each finding includes a description of the vulnerability, the affected code location, and a suggested fix.
* **Export finding.** A Project, Scan, or a Finding can be exported to a CSV or a Markdown file.
* **Open a remediation session.** Click the remediation button on a finding to open a Claude Code on the Web session focused on fixing that specific vulnerability. Claude will analyze the vulnerability in context and generate a potential patch.
* **Dismiss a finding.** If a finding is a false positive or not applicable to your context, you can dismiss it with a reason. Dismissed findings will not reappear in future scans.

Findings are categorized by severity to help you prioritize your remediation efforts. We recommend starting with the highest-severity items and working through the list.

## **Operationalizing the tool for ongoing use**

To make ongoing use easier, you can:

* **Run multiple scans at the same time and have multiple working Projects.** Use separate Projects to scope work meaningfully — one per repository, per service, or per team — so that findings stay attributable and reviewers aren’t wading through results that belong to someone else. Parallel scans are useful when you want to triage several repos at once or compare a hardened branch against main without waiting for one to finish before starting the next.
* ‍**Users can configure scan effort.** On the first scan, or after material changes, they can choose between "Regular" and "Extended" — use Extended for a deeper review.**‍**
* **Schedule scans on a decided cadence.** A weekly cadence works well for many teams — frequent enough to catch issues introduced by recent changes, infrequent enough that reviewers actually work through the backlog between runs. Tie the cadence to something you already do: a Monday triage meeting, a sprint boundary, or a pre-release checkpoint. Scheduled scans matter most when paired with a named owner; otherwise findings accumulate and the backlog becomes the thing people avoid rather than the thing they act on.**‍**
* **Export CSVs and findings to desired tracking and audit systems, or share it with your team members.** Export findings into that system so triage, assignment, and status live alongside everything else the team is using. For audit and compliance purposes, keep the CSV exports themselves: they’re the paper trail that shows what was scanned, when, and how the team responded.**‍**
* **You can also configure webhook endpoints per Project** to push scan-completion and new-finding events into your own systems in real time, and connect tools like Slack and Jira to notify your team automatically when a scan completes or a new finding lands — so triage can start without anyone having to check the dashboard. Users can also set email notifications through the “Notifications” section under “General” in personal settings. **‍**
* **When triaging findings, set dismissal reasons to create an audit trail and clarity for future reviewers.**
* **Scope large repositories.** For large repositories or monorepos, we recommend scoping scans to individual modules or subdirectories rather than running against the full repo. Narrower scope increases determinism and focuses the agent's attention, while still allowing it to trace logic and pull context from across the broader codebase as needed.**‍**
* **RBAC and access management can be controlled by the admins.** Admins can set custom roles through Claude Enterprise RBAC to enforce who can run a scan.

> For more information and FAQ, please visit our [support center.](https://support.claude.com/en/articles/14661296-use-claude-security)

## Related tutorials

[Tasks to try with @Claude in your workspace](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tasks to try with @Claude in your workspace

Tasks to try with @Claude in your workspace

Tutorial

[Tutorial](/resources/tutorials/tasks-to-try-with-claude-tag-in-your-workspace)Tutorial

[Best practices for using @Claude](/resources/tutorials/best-practices-using-claude-tag)Best practices for using @Claude

Best practices for using @Claude

Tutorial

[Tutorial](/resources/tutorials/best-practices-using-claude-tag)Tutorial

[Using Claude Cowork for legal: answer fast questions on past decisions](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Using Claude Cowork for legal: answer fast questions on past decisions

Using Claude Cowork for legal: answer fast questions on past decisions

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-legal-question-briefing)Tutorial

[Using Claude Cowork for marketing ops: run a weekly review that preps itself](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Using Claude Cowork for marketing ops: run a weekly review that preps itself

Using Claude Cowork for marketing ops: run a weekly review that preps itself

Tutorial

[Tutorial](/resources/tutorials/using-claude-cowork-for-marketing-ops-review)Tutorial
