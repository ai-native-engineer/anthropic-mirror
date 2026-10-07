<!-- source: https://claude.com/resources/guides/deploying-claude-across-your-organization/adoption-at-scale -->

Chapter 056 min read

# Driving Claude Cowork adoption at scale

6 min read

17 min remaining

Deploying the technology is the easy part; getting an organization to actually use it is much harder.

Month-by-month rollout phases for scaling Claude Cowork adoption

| Phase | Timeline | Target level | Actions | What you'd expect to see |
| --- | --- | --- | --- | --- |
| Evaluate | Month 1 | Champions reach Level 1 | Security review. Identify 2-3 champion teams. Install pre-built plugins. Connect 1-2 core systems. | Champions reporting back use cases. First "this saved me an hour" moments. |
| Pilot | Months 2-3 | Champions reach Levels 2-3 | Champions run real workflows. Weekly check-ins. Measure against defined criteria. Demo wins to adjacent teams. | Measurable time savings. Champions building and scheduling custom skills. Pull from other teams. |
| Scale | Months 4-6 | Department reaches Level 4 | Admin-provisioned plugin marketplace. Encode pilot learnings as org-wide skills. Onboard next wave. | Skills shared across teams. New hires ramping on encoded workflows. Declining support tickets for "how do I." |

In this section, we share a month-by-month framework for scaling Claude Cowork across your organization that maps to our adoption levels. Month 1 gets your champions to Level 1, familiarizing themselves with the solution. Months 2 and 3 get those champions to Levels 2 and 3, building and scheduling their own skills. Months 4 through 6 take what the champions built and provision it as Level 4 department plugins for everyone else. Each phase has a different audience, motion, and success signal.

## Month 1: Evaluate

Find your Claude Cowork power users, the early adopters experimenting with the tool in their day-to-day work. They're your first pilot leads, and most are already using AI for chat. Let them surface Claude Cowork use cases that matter to their function rather than prescribing from above.

Have champions leverage pre-configured plugins so they get value in the first session. The cold-start problem is real: if someone opens Claude Cowork and doesn't know what to do, they close it. If they open it, type */morning-briefing*, and get something useful in ninety seconds, they come back tomorrow. Check out our [open-source plugin library (opens in new tab)](https://github.com/anthropics/knowledge-work-plugins) covering sales, legal, finance, marketing, product, HR, and more.

Connect systems and data sources early on in the process. Our pre-built plugins are much more useful when they use real data and have organizational context. A sales plugin that reads your most critical Salesforce dashboard is categorically more useful than one that doesn't. Connected systems are also what make Level 1 possible; without them, users stay stuck at Level 0 chat.

## Months 2-3: Pilot

At this stage, encourage your champions to show the impact of Claude Cowork live with their teams. When your legal team watches a four-hour contract review happen in forty-five minutes on a real contract they recognize, they'll become champions, too.

Run with your two or three champion teams against clear evaluation criteria. Check in weekly, not to micromanage, but because pilot teams surface edge cases fast and you want to hear about them while they're fresh so you can action them before a broader rollout.

The signal that a pilot is working isn't just hours saved. It's champions starting to write their own skills. When a rep takes the call-prep workflow she's been running by hand and turns it into a `/call-prep` skill, she's crossed from Level 1 to Level 2, and that skill is now an asset the rest of the org can inherit. When she schedules it to run before every calendar event tagged "external," she's at Level 3. Track how many champion-authored skills exist at the end of the pilot; it's the leading indicator for the scale phase.

## Months 4-6: Scale

This is where the economics shift. Every skill built during the pilot is an asset. Your best rep's call prep is now everyone's call prep, and the marketing blog review skill legal built is a template comms can adapt for their own use case. Tribal knowledge gets encoded and reused rather than walking out the door when someone leaves, and over time, shared among teams.

The pattern is bottom-up discovery, top-down scale. Let teams experiment and find what works for their function, then take what works and provision it org-wide through admin-managed plugin marketplaces. The finance plugin that one team built becomes the finance plugin the whole finance org runs, with version control and the ability to push improvements to everyone at once. That's Level 4: a curated, maintained bundle of skills, subagents, and connectors that defines how a department works with Claude.

Level 4 also changes the onboarding equation. A new hire who installs the department's plugin on day one starts at Level 2, not Level 0. They get the encoded workflows before they've had time to develop bad habits, and the floor for the whole team rises.

### Zapier: Skills that travel between projects

[Zapier's (opens in new tab)](https://claude.com/customers/zapier-cowork-qa) product marketing team uses Claude Cowork to prototype new homepage messaging before involving design or engineering. The workflow is deliberately light: give Claude the existing homepage as a baseline, load a custom skill that encodes the team's voice, positioning intent, and page-structure conventions, then point Claude at the new direction and ask for a revised concept.

Claude navigates to the live page, identifies the core modules, and generates an HTML mockup aligned to the new positioning, something with enough fidelity to evaluate copy direction and page structure before anyone opens Figma. The operator stays in a review loop, giving directional edits while Claude Cowork regenerates, and keeps working on other things in parallel.

What makes this repeatable is the skill. The team's PMM context travels with the tool. The next concepting task starts from the same strategic foundation rather than a blank prompt, and anyone on the team can pick it up. It's a Level 2 asset doing Level 4 work: one well-built skill that quietly became how an entire function approaches a recurring problem.

> “I connected Claude Cowork to our homepage, a custom skill with our PMM guidelines, and our internal tools through MCP so it could pull from Slack threads, Glean searches, whatever context it needed. Now I give Claude new positioning and ask it to develop versions of our homepage with improved messaging. It looks at the page, works through its steps, and generates an HTML mockup. After 15 minutes I'm sharing it with our team to build on.”

Joe StychHead of Product Marketing, Zapier
