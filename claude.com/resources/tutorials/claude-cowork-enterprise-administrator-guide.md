<!-- source: https://claude.com/resources/tutorials/claude-cowork-enterprise-administrator-guide -->

# Claude Cowork Enterprise Admin Guide

Claude Cowork brings Claude’s agentic capabilities to the Claude Desktop app, enabling multi-step knowledge work beyond coding

  Professional
* Product

  Claude Cowork
* Reading time

  Watch time

  5

  min

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/claude-cowork-enterprise-administrator-guide

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Introduction

### What Is Claude Cowork?

Claude Cowork brings Claude’s agentic capabilities to the Claude Desktop app, enabling multi-step knowledge work beyond coding. Rather than responding to individual prompts sequentially, Claude can tackle complex, multi-step tasks and execute them on a user’s behalf. Users delegate work and return to polished deliverables like formatted documents, organized files, synthesized research, and more.

Claude Cowork sits alongside [claude.ai](http://claude.ai), the API, and Claude Code in the Claude product lineup. What distinguishes it for enterprise is the combination of local file access, connectors to the tools your teams already use (e.g. Slack, Google Workspace, M365), a plugin ecosystem with repeatable workflows that organizations can curate and govern, and scheduled tasks that run on a cadence. It requires the Claude Desktop app on macOS or Windows and is available on all Claude paid plans.

### Requirements

* **Claude Desktop app:** Claude Cowork requires the desktop app for macOS or Windows and is not currently available on web or mobile.
* **Claude subscription:** Claude Cowork is available to paid Claude plans (Pro, Max, Team, and Enterprise), with some features still in research preview. Learn more [here](https://claude.com/pricing#team-&-enterprise).
* **Active internet connection:** Required throughout the session.
* **Connectors:** Claude Cowork is most powerful when you connect it to your favorite apps, services, and data sources via connectors.

## Phase 1: Technical Setup

You’re building the delegation infrastructure:  identity controls gate who can delegate work to Claude, connectors give Claude the tools to do that work, and observability lets you see what’s happening. Complete these steps to deploy Claude Cowork to your organization.

### Planning & Prerequisites

*Complete these before touching any admin console. Security review can run in parallel with the other steps.*

#### Assemble your rollout team

Identify who you need before you start. Later steps stall if these people aren't looped in early.

* Primary Owner (one per org; confirm who holds it)
* DNS admin and IdP admin (already done if on Claude Enterprise)
* Connector owners — one per data source (M365, Slack, Google Workspace)
* MDM admin, if deploying centrally
* Internal champions — identify 2–3 per department as part of your pilot group. These are the people who will drive peer adoption in Phase 2.

#### Plan desktop app installation

* Claude Cowork requires the Claude Desktop app. Decide whether you’ll push via MDM or have users self-install, and plan comms so users know to install it before launch day. See the Claude Desktop collection for installation resources. See [Installing Claude Desktop](https://support.claude.com/en/articles/10065433-installing-claude-desktop).

#### Choose your org architecture

* Decide between a single org with role-based access controls (RBAC) and groups, parent-child, or multiple parents based on how many identity providers you have and how much data isolation you need. This decision shapes every step below and is challenging to change later.

#### Confirm endpoint and network prerequisites

* Claude Cowork runs locally on each user's machine, with code execution sandboxed in a kernel-isolated environment. As a result, it has different infrastructure requirements than claude.ai. For an overview of how Claude Cowork differs from claude.ai, see [Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork#h_bd829a921b).

Verify your fleet and network can support it — endpoint and network issues are the most common cause of deployment problems. Ensure that required domains are allowlisted, minimum OS versions are met, and any proxy or firewall rules permit Claude Cowork traffic.

#### Plan billing and seats

* Confirm that your [seat allocation](https://support.claude.com/en/articles/13799932) covers everyone you intend to provision via SCIM. Even on consumption-based billing, seat count gates provisioning — if SCIM tries to provision more users than you have seats, provisioning silently fails with no error.

#### Start your security review

* Assemble your review packet from the [Anthropic Trust Center](https://trust.anthropic.com) and the [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135) article. This can run in parallel with the rest of Phase 1. Note that the Compliance API and Audit Logs do not cover Claude Cowork yet.

### Identity & Access

*SSO before RBAC. Do not enforce either until both are fully configured.*

#### Set up identity and SSO

Identity is the foundation everything else depends on. RBAC, connectors, and deployment all reference the groups you create here.

* For existing Claude Enterprise orgs, confirm your SSO and SCIM configuration and set up IdP groups for role-based access controls . For new orgs, complete the [full identity setup](https://support.claude.com/en/collections/17270717-identity-management-sso-jit-scim).
* Create IdP groups before configuring RBAC — RBAC references groups, not individual users. Nested IdP groups are not supported; only direct members sync.
* SSO controls who can log in; RBAC (next step) controls which Claude product surfaces they can access — including Claude Cowork.
* Only enforce SSO after both groups/mappings and RBAC roles are fully configured and tested. Enforcing early locks out everyone who isn’t yet provisioned, and there’s no self-service recovery.

#### Configure Role-based access controls

* Enable Claude Cowork at the org level, then create [custom roles](https://support.claude.com/en/articles/13930452) with the Claude Cowork entitlement and assign them to groups. See [RBAC setup](https://support.claude.com/en/articles/13930458) for configuration steps.
* Roles are additive — a user in multiple groups gets the union of permissions. [Spend limits](https://support.claude.com/en/articles/13799932) use the opposite rule: the most restrictive limit across a user’s groups wins.
* Migrate to enforcement last. There is no in-product undo — migrating before roles are configured drops every user to zero permissions.

### Connectors & Hardening

*Configure after RBAC is in place so access controls are set before connectors go live.*

#### Set up connectors

* Connectors let Claude Cowork reach into the tools your teams already use — Slack, Google Workspace, M365, and more — so Claude can read, search, and act on real work data.

* Connectors use a two-gate model: an admin enables the connector org-wide, then each user individually OAuths to link their account. There is no per-group connector control — enabling a connector makes it available to everyone in the org. Configure connectors in the admin console under your organization's connector settings.
* Prioritize enabling the connectors that map to where your users already do their work. Users who can connect to their everyday tools from day one generate fewer support requests and onboard faster.

#### Set Up Plugins

* Plugins are how you curate the Claude Cowork experience for your organization. A seeded marketplace gives users high-value workflows from day one instead of starting from scratch.
* Seed your private plugin marketplace if applicable. Configure distribution policies and pre-approve plugins before launch. See [Manage Claude Cowork plugins for your organization](https://support.claude.com/en/articles/13837433).

#### Configure security controls

* Harden your deployment by configuring network egress allowlists, mount controls, and desktop extension allowlists. These security controls are configured in the admin console under your organization's Claude Cowork settings.

### Deployment & Launch

*Deploy Claude Cowork after identity, access, and connectors are all confirmed working.*

**Deploy the desktop app**

* Push the installer via your MDM tool or allow users to self-install. Use the MSIX installer on Windows (not .exe). See [Deploy for macOS](https://support.claude.com/en/articles/12611117), [Deploy for Windows](https://support.claude.com/en/articles/12622703), and [Enterprise configuration](https://support.claude.com/en/articles/12622667) for managed settings.
* After deployment, verify: the VM image downloads, the app launches, and the user authenticates via SSO.

#### Wire observability

* Set up your OTEL endpoint to export Claude Cowork session data to your SIEM or observability platform. OTEL provides real-time, event-level telemetry for Claude Cowork sessions. Test in a sandbox first if you’re running parent-child. See [Claude Cowork monitoring & observability](https://claude.com/docs/cowork/monitoring).

#### Pre-launch checklist

Before opening Claude Cowork to your pilot group, confirm:

* One user has completed a real task end-to-end
* OTEL dashboards are live and receiving data
* Plugin marketplace is seeded with at least the Anthropic plugins relevant to your pilot teams (if applicable)
* Support channel is live and escalation paths are documented

## Phase 2: Change Management & Launch

Claude Cowork introduces a fundamentally different way of working with Claude. In Chat, users collaborate — prompting back and forth to work toward an answer together. In Claude Cowork, users delegate — they describe a task, provide context and tools, define what good looks like, and come back to finished work.

An ideal Claude Cowork task produces a deliverable: a document, a financial model, a research memo, a formatted report. A successful task means the user got the output they expected, in the form they needed. This is the shift your enablement program needs to drive: from chatting to creating.

**Companion guide:** Each phase below gives you the framework — what to think about and why it matters. For the operational detail of how to scale Claude Cowork workflow across your team, see [Scaling workflows with Claude Cowork at your organization](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization).

### Claude Cowork Analytics

Before defining success metrics, know where your data lives. Claude Cowork usage data is available through two channels: the admin dashboard in claude.ai and the Analytics API. Together, they give you visibility into how your organization is adopting and using Claude Cowork — from high-level active user trends down to which skills and connectors see the most use.

#### Admin Dashboard

The admin dashboard (claude.ai org analytics) now includes Claude Cowork alongside Chat and Claude Code. Below is an overview of what you’ll be able to see for Claude Cowork.

* **Active users:** The time-series chart gains a Claude Cowork filter, so you can track daily, weekly, and monthly active users alongside your other Claude products.
* **Claude Cowork overview card:** Shows total sessions and actions across the org for any date range, providing a quick read on overall engagement.
* **Data latency:** Dashboard data refreshes on a T+1 schedule (yesterday's data is available today).

See [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420) for more details.

#### Analytics API

The Analytics API (Enterprise plan only) provides programmatic access to Claude Cowork usage data, aggregated per day. Claude Cowork adds the following metrics:

* **Per-user daily activity:** Distinct sessions started, tool actions completed, dispatch turns (autonomous background work — Claude Cowork-exclusive), messages sent, skill invocations (total and distinct), and connector invocations (total and distinct).
* **Org-wide summaries:** Claude Cowork DAU, WAU, and MAU counts alongside existing Chat and Claude Code figures, so you can compare adoption across products.
* **Skill and connector rankings:** Each entry now shows how many Claude Cowork sessions invoked it, so you can see which tools your Claude Cowork users actually reach for.

For the full endpoint specification, query parameters, and response schemas, see the [Analytics API reference guide](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans). For setup instructions, see [Access engagement and adoption data with the Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api).

### Define Success Metrics

The metrics that prove your rollout is working answer three questions — and the answers should improve week over week.

* **Are people using it?**: You're looking for the gap between "has access" and "has delegated a task."
* **How deeply?:** You're looking for whether users are actually completing work or just chatting.

**Is it paying off?:** You’re looking beyond “time saved,” and whether Cowork is being used for work that matters

| 1. Are people using it? | 2. How deeply? | 3. Is it paying off? |
| --- | --- | --- |
| Activation rate (logged in / licensed) | Sessions per active user | Hours re-allocated per week (self-reported) |
| Weekly actives by cohort | Advanced-feature uptake (connectors, skills, plugins) | Named wins per cohort |
| Return rate (week-2 retention) | Champion-to-user touchpoints | Workflows now running on Claude |
| Days from training to first real task | Help-session participation | Cost-to-value comparison |

Value is the hardest column to fill because the easiest metric to reach for — time saved — misses the biggest source of impact: work that wasn’t happening before. Anchor value measurement on three questions:

* What new work is getting done that wasn’t feasible before?
* What business outcome is tied to the new work?
* Where time is being reclaimed, what’s it going toward?

Run period user surveys anchored to specific workflows.

If any column is underperforming, look left first. Low value almost always traces back to an engagement or adoption problem upstream.

### Identify & Enable Champions

Champions are enthusiastic adopters who can help drive peer adoption across their teams.  Identify internal champions in each department as part of your pilot group and equip them early so they can support their teams from day one. Look for people already experimenting with AI tools or who volunteered for the pilot.

* Select 2–3 champions per department or team
* Give champions early access so they build fluency before launch.
* Equip champions with key talking points on the differences between Claude Cowork and Chat, who to contact for help, and how to report issues.
* Create a dedicated communication channel for champions to share wins, tips, and common questions,
* Recognize and reward champion contributions

### **Launch Communication**s

Stage your communications so users know what’s coming, why it matters, and where to go for help. Claude Cowork is accessed from the Claude desktop app and works with your files, tools, and browser — it's a different experience from claude.ai and your messaging should set that expectation.

Every message should reinforce the delegation model: Claude Cowork produces deliverables, not just answers. Users describe a task, provide context and tools, define what good looks like, and come back to finished work.

#### Pre-launch (2 weeks before)

* Send a message from leadership explaining what Claude Cowork is, why the org is adopting it, and what users can expect. Emphasize that Claude Cowork is for delegating real work — not just chat.
* Share the training schedule and point users to self-service resources. Let them know who their department champion is.

#### Launch day

* Send the onboarding guide with install instructions (or confirm the app is already pushed via MDM).
* Announce the support channel and office hours schedule.
* Have champions available in their departments to help with first-time setup and answer questions.

#### Post-launch (week 1)

* Share early usage tips and quick wins. Highlight specific tasks users have successfully delegated — emphasize the deliverable they received, not just that they used Cowork.
* Surface early success stories from champions or pilot users.
* Send a reminder about training resources and the support channel.

#### Ongoing

* Share regular tips and feature spotlights (e.g., new plugins, scheduled task patterns, Chrome workflows).
* Announce when new connectors are approved and live. Many connectors require a two-gate authentication system (admin + user). Share directions to authenticate if the connector requires individual OAuth setup.
* Publish monthly usage updates to leadership using the metrics defined above.
* Run quarterly reviews to assess adoption progress and recalibrate targets.

## Phase 3: Enablement & Training

Without enablement, users may treat Claude Cowork as indistinguishable from Chat. Your enablement program needs to build the muscle for delegation — describing a task, providing context and tools, and coming back to finished work.

### Structured Training Programs

* **All-Staff 101 sessions:** 30–60 minute workshops where every attendee completes a real delegation-style task before the session ends. The task should produce a deliverable — not just a chat response. Cover the interface and file access in the context of completing that task, not as standalone steps.
* **Department-level enablement:** Customized sessions with exec sponsors, focused on workflows relevant to each team. Each session should center on a real task from the team’s actual work — not a demo walkthrough. Equip teams with ready-to-customize workflow templates and the skills and plugins relevant to their function.
* **Office hours:** Weekly or biweekly drop-in sessions where users bring real work and get hands-on help from champions.
* **LMS integration:** Package training into trackable courses to monitor completion rates across departments and identify teams that need additional support.

### Self-Service Resources

#### For end users

* [Introduction to Claude Cowork](https://anthropic.skilljar.com/introduction-to-claude-cowork) — self-paced end-user course covering getting started, agents, and plugins.
* [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190) — Set up Claude Cowork, select folders, and complete your first task.
* [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135) — Safety model, guardrails, and responsible use guidance for Claude Cowork.
* [Use plugins in Claude Cowork](https://support.claude.com/en/articles/13837440) — Plugin ecosystem, marketplace, and how to install and use plugins.

#### For admins

* [Use Claude Cowork on team and enterprise plans](https://support.claude.com/en/articles/13455879) — Enterprise-specific setup, licensing, and admin controls for Claude Cowork.
* [Manage plugins for your organization](https://support.claude.com/en/articles/13837433) — Marketplace setup, distribution policies, and plugin governance for admins.

#### General AI literacy

* [Anthropic Academy](https://anthropic.skilljar.com) — interactive courses on AI fundamentals and prompt engineering.
* [AI Fluency Course](https://www.anthropic.com/learn/claude-for-you) — broader AI literacy for users new to working with AI.
* [Prompt Engineering Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering) — techniques for getting better results from Claude.
* [Help Center](https://support.claude.com) — comprehensive documentation and FAQs.

### Claude Cowork Features to Cover

These are the key capabilities users should understand.

* [**File access**](https://support.claude.com/en/articles/14128542): Select which folders Claude Cowork can read from and write to. Finished work is delivered directly back to those folders.
* [**Connectors**](https://support.claude.com/en/articles/11176164): Connect your apps and services so Claude can retrieve data and take actions within them.
* [**Skills**](https://support.claude.com/en/articles/12512180): Instruction sets that Claude loads dynamically to improve performance on specialized tasks.
* [**Plugins & marketplace**](https://support.claude.com/en/articles/13837440): Plugin bundles that package skills, connectors, and sub-agents together. Available through your organization's private marketplace.
* [**Scheduled tasks**](https://support.claude.com/en/articles/13854387): Tasks that run on-demand or automatically on a cadence of your choosing.
* [**Projects**](https://support.claude.com/en/articles/14116274): Group related tasks into workspaces with their own files, context, and memory.
* [**Claude in Chrome**](https://support.claude.com/en/articles/12012173): Use Claude’s capabilities directly in your browser.
* [**Dispatch**](https://support.claude.com/en/articles/13947068): One continuous conversation with Claude, reachable from phone or desktop. Assign tasks from anywhere — Claude determines the right workspace, does the work, and messages you the outcome. The desktop app must be running for Dispatch to execute tasks.

### Internal Support Channels

* Create a dedicated communications channel for Claude Cowork questions, tips, and troubleshooting. Champions should be active here daily during the first month.
* Run weekly office hours with champions where users can bring real tasks and get live help.
* Integrate with your IT helpdesk so Claude Cowork issues route to the right team — separate from general claude.ai support if possible. Ensure admins go live with clear escalation paths so users know exactly where to go if something breaks or to request access or more usage.
* Stand up monthly user groups for knowledge sharing — teams that have built useful skills or plugins present to the broader org.

## Phase 4: Scaling Adoption

Your pilot validated the approach. Scaling means replicating it — expanding to new teams, demonstrating business impact, and putting governance in place that grows with usage.

### Expanding Across Teams

* Prioritize teams whose work regularly produces deliverables — reports, analyses, decks, formatted documents — and who already work in tools with available connectors in claude.ai.
* For each new team: identify 2–3 high-value delegation workflows, appoint a local champion, and deliver tailored onboarding using the department-level enablement sessions from Phase 3.
* Expanding means adding RBAC groups progressively and enabling additional connectors per team’s needs.

### Measuring Impact

In Phase 2, you defined metrics across three columns: are people using it?, how deeply?, and is it paying off? At this stage, shift emphasis to the third section. Focus on outcomes that matter to leadership:

* Pair quantitative data with qualitative examples such as short case studies from team leads illustrating real impact.
* Establish a regular reporting cadence (e.g., quarterly business reviews) to keep stakeholders informed.

### Governance

As usage grows, your governance needs grow with it. Start with the org-level controls you configured in Phase 1, then refine as you observe what teams build. Today, some governance happens in-product and some requires manual processes outside of Claude Cowork. Plan for both

#### What you can govern in-product today

* **Connector access:** Org-wide on/off. When you enable a new connector, it’s available to everyone — plan your rollout communications accordingly.
* **Spend controls:** Group-based spend limits with most-restrictive precedence. An org-level cap overrides individual seat limits.
* **Plugin marketplace:** Curate which plugins appear in your organization's marketplace. Configure distribution policies, pre-approve plugins, and use group-level overrides to control availability per team. Works with SCIM groups.
* **RBAC:** Control who can access Claude Cowork, Claude Code, and other product surfaces via custom roles assigned to groups.

#### What requires manual governance today

* **Skill review and approval:** There is no in-product workflow for submitting, reviewing, and approving skills. If you want governance over skill creation, you’ll need to build a process outside of Claude Cowork — for example, a request form, a review committee, and a shared directory of approved skills.
* **Per-group connector access:** Connectors are currently org-wide (on/off). If you need different teams to have access to different connectors, this requires multiple orgs or a manual policy layer.
* **Peer-to-peer and peer-to-org sharing controls:** Sharing is currently an org-level toggle (on/off), not per-group.

#### Ongoing governance practices

* Maintain an allowlist of approved connectors, routing new requests through your standard change management process.
* Run quarterly curation reviews to archive stale skills and promote high-value workflows to official plugins. Champions can drive this process.
* Review data policies and audit cadences at each stage of rollout as the user base expands.

### Capability Governance

#### Go live with the full platform

Claude Cowork’s value comes from capabilities working together — file access, connectors, skills, and code execution combine to produce finished work. As you scale, evaluate these additional capabilities as governance decisions, not just feature toggles:

* **Memory:** Enables Claude Cowork to retain context across sessions. Evaluate what level of persistent context fits your data policies.
* **Network egress (web search):** Controls what Claude Cowork can reach when researching or verifying information. Your network and data policies should drive this.
* **Office agents (Claude across apps):** Lets Claude work across applications. Consider whether your teams’ workflows cross application boundaries.
* **Dispatch:** Task assignment from phone or desktop. A different interaction model worth evaluating separately for your organization’s work patterns.

### Building a Lasting Program

Scaling Claude Cowork isn’t a launch, it’s an ongoing program. The organizations that see compounding value are the ones that treat adoption as a discipline: continuously surfacing new use cases, curating the best workflows into reusable skills, and connecting what teams learn back into the enablement program.

For the full operational playbook — program ownership models, champion councils, quarterly review cadences, and long-term sustaining frameworks — see [Scaling workflows with Claude Cowork at your organization](https://claude.com/resources/tutorials/scaling-workflows-with-claude-cowork-at-your-organization).

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
