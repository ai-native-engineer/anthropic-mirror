<!-- source: https://academy.claude.com/tutorials/customize-claude-cowork -->

[Claude Cowork(opens in new tab)](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) runs full tasks across your files and tools. Customizing it once means every task after that starts with your systems connected and your team's process already in place. For the quickstart, see [Get started in Cowork in three steps(opens in new tab)](https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps).

## Level 1: Your context and tools

### **Connectors**

[Connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) plug Cowork into the systems where your work already is — Slack, HubSpot, Microsoft 365, Jira, your company's internal tools — giving it the context to understand a task and the ability to act on it. With a connector enabled, Claude can read your data *and* write back: update a ticket, draft a reply, post to a channel, save a file.

Enable connectors from the **Customize** panel in the left sidebar. Authorize once; Claude can then use that tool in any session.



**Permissions.** For enterprise users, your admin controls which connectors are available — including Claude in Chrome — and whether each has read-only or write authorization. You can adjust which tools are enabled for a given session from the **Customize** menu or in the chat bar. [More on connector permissions.(opens in new tab)](https://support.claude.com/en/collections/15399129-connectors)

### **Instructions**

Instructions are standing rules you write for how Claude should work — tone, formatting, which sources to check first, conventions to follow. Set them at two levels:

**1. Global instructions** apply to every Cowork session you run. *Edit them at Settings → Cowork → Global instructions (desktop app only).*

**2. Project instructions** apply only inside that Project, on top of your global ones. *Edit them in the* [*Project's*(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) *right panel under Instructions.*

**3. Organization instructions:** For enterprise users, your admin may also set Organization preferences. This is org-wide guidance that applies across Chat, Cowork, and Code alongside your own instructions.

Instructions apply to every task — they're like the background rules Claude follows regardless of what you're working on. A Skill is for one specific kind of task, loads only when relevant, and can be shared with teammates. General rules go in Instructions; a repeatable process goes in a Skill.

## Level 2: Capture your process

### **Skills**

[Skills(opens in new tab)](https://support.claude.com/en/articles/12512176-what-are-skills) are instruction files for Claude to complete specific tasks in a repeatable way. Use skills to encode your personal best practices — as well as your team's expertise — into a repeatable set of instructions.

[To use a skill(opens in new tab)](https://support.claude.com/en/articles/12512180-use-skills-in-claude), name it directly (`/skill-name`) or describe the task in plain language. Claude can recognize when a skill applies and load it.

[Creating a skill(opens in new tab)](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) can also be done with Claude in a prompt. Run through a workflow in Cowork the way you normally would. At the end of the work, ask Claude:

Package what we just did into a skill.

Open in Cowork

The built-in skill-creator captures the steps, templates, and source locations so the next run is one prompt. [Create your first skill in Cowork](claude://cowork/new?q=Walk%20me%20through%20creating%20my%20first%20Skill.%20Ask%20me%20about%20a%20task%20I%20repeat%20every%20week%2C%20then%20help%20me%20capture%20it.).

## Level 3: Bundle and share

### **Plugins**

[Plugins(opens in new tab)](https://support.claude.com/en/articles/13837440-use-plugins-in-cowork) bundle together Connectors and Skills so teammates have what they need to get started.

Loading

#### **Example plugins**

Anthropic publishes ready-made plugins for common roles, each pairing the connectors that role relies on with skills for its core workflows:

* [**Sales**(opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/sales) — HubSpot, Close, Clay, ZoomInfo, and Fireflies (plus Slack), with Skills for account research, call prep, pipeline reviews, and competitive battle cards.
* [**Product**(opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/product-management) — Atlassian (Jira and Confluence), Linear, Notion, and Slack, with Skills for feedback clustering, PRD writing, sprint updates, and competitive teardowns.
* [**Legal**(opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/legal) — Box, Egnyte, DocuSign, Slack, and Atlassian, with Skills for contract review, NDA triage, signature requests, and vendor checks.
* [**Operations**(opens in new tab)](https://github.com/anthropics/knowledge-work-plugins/tree/main/operations) — Jira, Asana, and Notion, with Skills for vendor reviews, process documentation, change requests, and capacity planning.

Browse available Plugins in the **Customize** sidebar for more options, or ask Claude to bundle your own connectors and Skills into a custom plugin to share with your team. [Browse plugins for my role in Cowork](claude://cowork/new?q=Show%20me%20the%20plugins%20available%20for%20my%20role%20and%20help%20me%20pick%20one%20to%20install.).

## Where to go from here

Most people start with connectors and Instructions, write a skill after running the same task a few times, and share it once a teammate asks how to set theirs up the same way. Plugins are how your admin distributes the org's standard set across roles.

Once you're set up, additional Cowork features can take you further:

* **Scheduled tasks** run a prompt at a set time, with access to everything you've connected — so a Skill you've written can run every weekday at 9am without you starting it. Type /schedule in any session to set one up. [More on scheduled tasks(opens in new tab)](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork).
* **Artifacts** are dashboards, trackers, and comparison views that stay in the sidebar between sessions. Open one any time and ask Claude to refresh it with current data from your connectors. [More on artifacts(opens in new tab)](https://support.claude.com/en/articles/14729249-use-live-artifacts-in-claude-cowork).

For more on working in Cowork:

* [When to use Chat vs Cowork(opens in new tab)](https://academy.claude.com/tutorials/choosing-between-claude-cowork-or-chat) — how to choose the right mode for the task you're working on.
* [Building plugins from scratch(opens in new tab)](https://academy.claude.com/tutorials/how-to-build-a-plugin-from-scratch-in-cowork) — when the marketplace doesn't have what you need.
