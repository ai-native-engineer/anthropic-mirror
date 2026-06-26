<!-- source: https://claude.com/resources/tutorials/using-claude-cowork-for-sales-account-research -->

# Using Claude Cowork for sales: research any account before the first call

Before a first call, Claude Cowork pulls everything you’d want to know about an account into one brief. You go into the call already knowing the account, and the recap is written for you afterward.

  Sales
* Product

  Claude Cowork
* Reading time

  Watch time

  5

  min

  4

  min
* Share

  [Copy link](#)

  https://claude.com/resources/tutorials/using-claude-cowork-for-sales-account-research

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b7301c567070bec13098a_Screenshot%202026-05-18%20at%2012.31.52%E2%80%AFPM.png)

###### Watch the full workflow in the video, then follow the steps below to set it up yourself.

**In the video** — Brittney, an account executive, preps for a first call: who the customer is, what they’re building, their spend, the risks. A skill she built pulls it together in minutes; after the call, a second skill turns the transcript into the follow-up work.

Follow along to set up

[1Set up the account-research skillSet up once](#step-1-set-up-the-account-research-skill)[2Run the account brief before the callBefore each call](#step-2-run-the-account-brief-before-the-call)[3Run the debrief after the callAfter each call](#step-3-run-the-debrief-after-the-call)

If you haven’t set up Cowork yet, start with [Get started in three steps](https://claude.com/resources/tutorials/get-started-in-claude-cowork-in-three-steps), then [Customize Cowork](https://claude.com/resources/tutorials/customize-claude-cowork) for connectors and skills.

To dive deeper into Claude Cowork, take the full [Intro to Claude Cowork course](https://anthropic.skilljar.com/introduction-to-claude-cowork).

Set up once

## Step 1: Set up the account-research skill

The skill is what turns a one-line prompt into a full account brief — it tells Claude what you’d want to know walking into a first call, which tools have it, and how to lay the brief out. The [Sales plugin](https://claude.ai/desktop/customize/plugins/new?marketplace=https%3A%2F%2Fgithub.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales) ships with an `account-research` skill already built. You install it, point it at your tools, and tell Claude to tailor it to your company.

Install and set it up:

1. 1In Customize → Plugins, open the [Sales plugin](https://claude.ai/desktop/customize/plugins/new?marketplace=https%3A%2F%2Fgithub.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales) and install it — it comes with the `account-research` skill, built on how a working sales team uses it.
2. 2In Customize → Connectors, connect the tools the skill draws on — your CRM, the data warehouse, call recordings, email, chat, and the web. When the skill runs, Claude reads all of them at once.
3. 3In the Cowork chat bar, pick a working folder Claude can read, edit, and save to. The brief lands there before the call and the debrief goes next to it after, so over time the folder becomes the account’s history.

With the plugin installed and your tools connected, tell Claude to tailor the skill to your company — your systems, the signals that matter, and the brief format you read fastest:

Customize the account-research skill from the Sales plugin for my company. My accounts are the kind of customers I sell to — ask me about my CRM and data sources, the signals that matter for my deals, and the brief format I read fastest.

Copy prompt
[Open in Cowork](claude://cowork/new?q=)

Accounts

Ask

Claude walks you through what information to pull, which connected tools to look through, and how you want the brief laid out, then rewrites the skill to match. Once the skill is built, try running it on an account you already know, compare what comes back to how you’d write it on your own, and tell Claude to fix anything it missed.

Before each call

## Step 2: Run the account brief before the call

The skill is set up and your tools are connected. Now, the morning of a first call, open Cowork, type /, pick the `account-research` skill, and name the account:

/account-research [the account name]

Copy prompt
[Open in Cowork](claude://cowork/new?q=)

Accounts

Ask

Claude reads from every connected source at once and writes one brief to your working folder — spend trajectory, the stakeholder map, what they’ve adopted, open deals, and the risk signals worth knowing before you’re in the room. You walk in with real context, so the first conversation is about strategy instead of getting oriented.

After each call

## Step 3: Run the debrief after the call

After the meeting you prepped for, come back to the same Cowork session, where your account context is still loaded. The Sales plugin’s `call-summary` skill reads the call transcript and turns it into your follow-up work.

Set it up the way you set up account research in step 1: customize it to the follow-up you actually send — your action items, an internal message for the team, a customer follow-up. Once it’s tailored, type / and run it:

/call-summary [the account name]

Copy prompt
[Open in Cowork](claude://cowork/new?q=)

Accounts

Ask

From the transcript, Claude drafts three pieces:

* **Action items** — a checklist, saved straight to your working folder
* **Team message** — key takeaways, next steps, and owners for your account channel
* **Customer follow-up** — a recap and next steps, drafted in your voice

## Make it yours

This setup fits any role that walks into a meeting needing more context than they have:

* **Customer success** before a renewal or escalation — usage history, support tickets, the account’s chat channel
* **Partnerships** before a first meeting — deal history, public news, what’s been discussed internally
* **Recruiting** before a panel — the candidate’s portfolio, prior interview notes, the role’s requirements
* **Corporate development** before a diligence call — public filings, prior internal analysis, market signals

The setup is the same every time:

1. 1Start a task in Cowork and describe what you’d want to know walking in — the sources, the signals, the format.
2. 2Ask Claude to write it as a skill; run it on something you already know and refine.
3. 3Connect the tools it names and pick a working folder.
4. 4Run it with one line before each meeting; run the debrief skill after.

Claude does the gathering. The judgment about what to do with it is yours.

## Learn more

* [Claude Cowork 101](https://anthropic.skilljar.com/introduction-to-claude-cowork). Take the full Cowork course to dive deeper into the product.
* [Customize Cowork](https://claude.com/resources/tutorials/customize-claude-cowork). Learn how to set up connectors, skills, and instructions.
* [AI Fluency: Framework and Foundations](https://anthropic.skilljar.com/ai-fluency-framework-foundations). Take the full AI fluency course to work towards effective, efficient, and ethical AI use.
* [The 4 Ds of AI Fluency](https://claude.com/resources/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators). Learn practical skills and mental models behind building AI fluency.
* [Use Cowork safely](https://support.claude.com/en/articles/13364135-use-cowork-safely). Understand access, approvals, and what Claude can see.

## Related tutorials

[Using Claude Design for presentations and slide decks](/resources/tutorials/using-claude-design-for-presentations-and-slide-decks)Using Claude Design for presentations and slide decks

Using Claude Design for presentations and slide decks

Tutorial

[Tutorial](/resources/tutorials/using-claude-design-for-presentations-and-slide-decks)Tutorial

[How to build a plugin from scratch in Claude Cowork](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)How to build a plugin from scratch in Claude Cowork

How to build a plugin from scratch in Claude Cowork

Tutorial

[Tutorial](/resources/tutorials/how-to-build-a-plugin-from-scratch-in-cowork)Tutorial

[Claude for Sales](/resources/tutorials/claude-for-sales)Claude for Sales

Claude for Sales

Tutorial

[Tutorial](/resources/tutorials/claude-for-sales)Tutorial
