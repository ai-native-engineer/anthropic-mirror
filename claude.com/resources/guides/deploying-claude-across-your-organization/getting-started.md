<!-- source: https://claude.com/resources/guides/deploying-claude-across-your-organization/getting-started -->

Chapter 045 min read

# Getting started with Claude Cowork

5 min read

22 min remaining

Every function has work that is high-volume, information-dense, and process-driven, and that's exactly the shape of work office agents like Claude Cowork are good at. We suggest teams start with a pilot, evaluate the results, and scale from there.

In levels terms, the goal of this phase is modest: get a handful of people from Level 0 (asking Claude questions) to Level 1 (handing Claude a real folder of work and getting a finished deliverable back). You're not building skills or plugins yet; you're finding the two or three workflows where a Level 1 win is obvious enough that the people who experience it will want to encode it.

## Choosing your first use case

Good pilot candidates fall into one or a few of these categories:

* **High volume, high repetition.** Work that happens dozens of times a week and follows a knowable pattern, like meeting prep docs or data pulls.
* **Information-dense synthesis.** Anywhere a human is spending time being the integration layer between systems, including pipeline reviews, regulatory monitoring, and quarterly financial reports.
* **Bottleneck-creating work.** Speeding up cross-functional work (i.e., legal reviews of marketing blogs or creative briefs) doesn't save one person time; it unblocks everyone downstream.
* **Expertise-dependent but process-driven.** Business reviews, specialized recruiting screens, or product briefs–in other words, the work only your best people do well today, because they've internalized a process nobody wrote down–fit the bill. This category pays back the most: encode that process in a skill and everyone on the team inherits it.

If you don't know where to start, ask Claude. Point Claude Cowork at your department's recent intake, whether that's tickets, requests, email volume, or whatever system holds the queue, and ask it to categorize the work and tell you where the time goes. This is itself a Level 1 task, and a useful one: Anthropic's Legal team did exactly this with 742 Jira tickets and the analysis reshaped how they structure intake. (Jump ahead to learn more about this use case.)

### Structure your evaluation

Before you pilot, run the security review. Claude Cowork reads local files and connects to enterprise systems; your security team will want to understand the data boundaries, the connector permission model, and the auditability options. OpenTelemetry support lets admins export usage and tool activity to Datadog, Splunk, or whatever backend you run. Get this done before users are waiting on it.

Share

Share our [Claude Cowork Enterprise Admin Guide (opens in new tab)](https://claude.com/resources/tutorials/claude-cowork-enterprise-administrator-guide) with your IT team.

Pilot with two or three champion teams rather than one. A single team gives you one data point, but a handful gives you enough to separate the pattern from the team. Pick teams with a motivated lead who's already experimenting with AI. They'll surface the real use cases faster than a top-down mandate will.

Define success before you start among relevant stakeholders. "*Hours saved per week*" is measurable. "*Transformation*" is not.

Provision plugins at the admin level. When individuals adopt AI tools without oversight you get shadow AI: dozens of private workflows nobody can see, audit, or improve. Admin-provisioned plugins mean consistency across teams, security controls from the first user, and a single place to push updates when you improve a workflow.

### Starting points by function

Each of these is a Level 1 entry point: a single, real deliverable Claude produces against your actual files and systems. They're chosen because they convert quickly into Level 2 skills once a team has run them a few times by hand.

First Claude Cowork use cases and success measures by function

| Function | First use case | What you'd measure |
| --- | --- | --- |
| Legal | NDA review and redline against your playbook | Review turnaround time; queue depth |
| Finance | Variance analysis with root-cause commentary | Time from close to narrative; analyst hours per cycle |
| Sales | Pre-call research and brief generation | Prep time per call; rep-reported confidence |
| Product | PRD drafting from customer feedback and analytics | Time to first reviewable draft |
| HR | Performance review drafting from rubric and manager notes | Cycle completion rate; manager time per review |
| Marketing | Campaign brief to asset draft against brand guidelines | Concept-to-review time; rounds of revision |

### Jamf: A custom app in 45 minutes, without the engineers

[Jamf's (opens in new tab)](https://claude.com/customers/jamf) performance review process lives in a spreadsheet most organizations would recognize: seven competency facets, branching logic by level and role, and a structure that makes perfect sense to the HR team and almost nobody else. The usual path to making something like that usable is a quarter of engineering time and a custom internal app.

Jamf built it as a Claude Cowork skill instead. The skill turns the spreadsheet into a guided, interactive experience: it asks the manager the right questions, applies the right rubric for the role, and produces the review.

It's also a clean illustration of the Level 1 to Level 2 jump. The HR team had run the review process by hand against the spreadsheet enough times to know exactly what "good" looked like. Encoding it as a skill took 45 minutes because the workflow was already proven; the skill just made it repeatable.

> “We built a skill that turns a complex performance review spreadsheet, seven competency facets, branching logic by level and role, into a guided, interactive experience in Claude Cowork. What would have required a team of engineers building a custom React app, Claude Cowork delivered in 45 minutes. And it's more adaptive than anything we would have built.”

Matt BenyoDirector of AI Initiatives, Jamf
