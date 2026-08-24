<!-- source: https://academy.claude.com/tutorials/using-claude-cowork-for-sales-account-research -->

Loading

**Watch the full workflow in the video, then follow the steps below to set it up yourself.**

**In the video** — Brittney, an account executive, preps for a first call: who the customer is, what they’re building, their spend, the risks. A skill she built pulls it together in minutes; after the call, a second skill turns the transcript into the follow-up work.



If you haven’t set up Cowork yet, start with [Get started in three steps(opens in new tab)](https://academy.claude.com/tutorials/get-started-in-claude-cowork-in-three-steps), then [Customize Cowork(opens in new tab)](https://academy.claude.com/tutorials/customize-claude-cowork) for connectors and skills.

To dive deeper into Claude Cowork, take the full [Intro to Claude Cowork course(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-cowork).

## Step 1: Set up the account-research skill

Set up once

The skill is what turns a one-line prompt into a full account brief — it tells Claude what you’d want to know walking into a first call, which tools have it, and how to lay the brief out. The [Sales plugin(opens in new tab)](https://claude.ai/desktop/customize/plugins/new?marketplace=https%3A%2F%2Fgithub.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales) ships with an `account-research` skill already built. You install it, point it at your tools, and tell Claude to tailor it to your company.

**Install and set it up:**

1. **In Customize → Plugins**, open the [Sales plugin(opens in new tab)](https://claude.ai/desktop/customize/plugins/new?marketplace=https%3A%2F%2Fgithub.com%2Fanthropics%2Fknowledge-work-plugins&plugin=sales) and install it — it comes with the `account-research` skill, built on how a working sales team uses it.
2. **In Customize → Connectors**, connect the tools the skill draws on — your CRM, the data warehouse, call recordings, email, chat, and the web. When the skill runs, Claude reads all of them at once.
3. **In the Cowork chat bar**, pick a working folder Claude can read, edit, and save to. The brief lands there before the call and the debrief goes next to it after, so over time the folder becomes the account’s history.

With the plugin installed and your tools connected, tell Claude to tailor the skill to your company — your systems, the signals that matter, and the brief format you read fastest:

Customize the account-research skill from the Sales plugin for my company. My accounts are [the kind of customers I sell to] — ask me about my CRM and data sources, the signals that matter for my deals, and the brief format I read fastest.



AccountsOpen in Cowork

Claude walks you through what information to pull, which connected tools to look through, and how you want the brief laid out, then rewrites the skill to match. Once the skill is built, try running it on an account you already know, compare what comes back to how you’d write it on your own, and tell Claude to fix anything it missed.

## Step 2: Run the account brief before the call

Before each call

The skill is set up and your tools are connected. Now, the morning of a first call, open Cowork, type `/`, pick the `account-research` skill, and name the account:

/account-research [the account name]



AccountsOpen in Cowork

Claude reads from every connected source at once and writes one brief to your working folder — spend trajectory, the stakeholder map, what they’ve adopted, open deals, and the risk signals worth knowing before you’re in the room. You walk in with real context, so the first conversation is about strategy instead of getting oriented.

## Step 3: Run the debrief after the call

After each call

After the meeting you prepped for, come back to the same Cowork session, where your account context is still loaded. The Sales plugin’s `call-summary` skill reads the call transcript and turns it into your follow-up work.

Set it up the way you set up account research in step 1: customize it to the follow-up you actually send — your action items, an internal message for the team, a customer follow-up. Once it’s tailored, type `/` and run it:

/call-summary [the account name]



AccountsOpen in Cowork

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

**The setup is the same every time:**

1. Start a task in Cowork and describe what you’d want to know walking in — the sources, the signals, the format.
2. Ask Claude to write it as a skill; run it on something you already know and refine.
3. Connect the tools it names and pick a working folder.
4. Run it with one line before each meeting; run the debrief skill after.

Claude does the gathering. The judgment about what to do with it is yours.

## Learn more

* [**Claude Cowork 101**(opens in new tab)](https://academy.claude.com/courses/introduction-to-claude-cowork). Take the full Cowork course to dive deeper into the product.
* [**Customize Cowork**(opens in new tab)](https://academy.claude.com/tutorials/customize-claude-cowork). Learn how to set up connectors, skills, and instructions.
* [**AI Fluency: Framework and Foundations**(opens in new tab)](https://academy.claude.com/courses/ai-fluency-framework-foundations). Take the full AI fluency course to work towards effective, efficient, and ethical AI use.
* [**The 4 Ds of AI Fluency**(opens in new tab)](https://academy.claude.com/tutorials/the-4-ds-of-ai-fluency-behavioral-indicators). Learn practical skills and mental models behind building AI fluency.
* [**Use Cowork safely**(opens in new tab)](https://support.claude.com/en/articles/13364135-use-cowork-safely). Understand access, approvals, and what Claude can see.
