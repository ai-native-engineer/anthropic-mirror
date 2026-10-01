<!-- https://anthropic.skilljar.com/introduction-to-claude-cowork/485947 -->

## What you'll learn

*Estimated time: 11 minutes*

By the end of this lesson you'll be able to:

* Recognize the kinds of work Claude in Chrome unlocks
* Use Chrome alongside Cowork on a real piece of work

## Watch it work

The video shows how Claude can work in Chrome to read, click, and navigate
websites alongside you.

## Key takeaways

* **Claude in Chrome is the bridge for tools that don't have a connector.** For anything that lives in a browser, Claude can read and act on those pages.
* **Claude in Chrome and Cowork work together.** Claude can gather info and take actions in the browser; it then takes the results and builds the deliverable back in Cowork. One conversation, both surfaces.
* **You stay in control.** By default, Claude in Chrome asks before sensitive actions, and you can approve or deny each one.

## What this unlocks

A few examples that matter in real work:

* **Internal dashboards.** Your finance team's Tableau view, your sales ops Looker dashboard, the BI tool with the metric you check every Monday. Claude can pull the numbers, download them to your computer, and use that context for Cowork tasks.
* **Vendor portals and customer systems.** The procurement portal that doesn't have an API. The CRM that's behind your single sign-on. The customer support tool where every ticket has to be triaged. Claude can navigate the portal, pull what you need, and act on it the way you would.
* **Web apps behind a login.** Anything with a browser interface — even tools your team built — becomes scriptable. *"Open the procurement system, find every PO from our top ten suppliers in Q3, and pull the line items into a spreadsheet."*
* **Web research that ends in a deliverable.** Open ten tabs, pull what's on each, and turn it into a brief — without copy-paste.

The pattern: any time you'd find yourself thinking *"I'd love to give this context to Claude, but it lives on the web,"* Claude in Chrome is the answer.

## Use it with Cowork

A real example: your team's customer health dashboard lives behind a login and doesn't have a connector. You want a one-page summary of every account showing yellow or red, by Friday.

In Cowork, you say:

Open the customer health dashboard in Chrome, pull every account showing yellow or red, and for each one, pull the past 30 days of activity from the customer's folder in Drive and recent threads in #customer-success in Slack. Build a one-page summary I can review before my Friday call.

[Open in Cowork](claude://cowork/new?q=Open%20the%20customer%20health%20dashboard%20in%20Chrome%2C%20pull%20every%20account%20showing%20yellow%20or%20red%2C%20and%20for%20each%20one%2C%20pull%20the%20past%2030%20days%20of%20activity%20from%20the%20customer's%20folder%20in%20Drive%20and%20recent%20threads%20in%20%23customer-success%20in%20Slack.%20Build%20a%20one-page%20summary%20I%20can%20review%20before%20my%20Friday%20call.)

Claude hands the browser steps to Claude in Chrome, takes the data back, pulls the supporting context from Drive and Slack, and builds the summary in your folder. One delegation, three sources of context.

## A few watch-outs

* **You need to be signed in.** Claude can't sign in to a tool for you. If the dashboard requires authentication, you log in once in your browser; Claude works in the session you're already authenticated in.
* **Be deliberate about what you give Claude access to on the web.** Just like with connectors, Claude sees what you see — but on the open web, that includes anything you have access to. For sensitive sites, narrow what Claude can act on, and review the actions before approving them.

To find the latest setup guidance, see [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome).

## Try it now

Pick one task on your plate that lives in a browser-based tool that doesn't have a connector. Give it to Cowork and let Claude work in Chrome, the way the dashboard example above does.

## What’s next

In the next lesson, you'll see Claude show up inside the M365 apps where a lot of work actually lands — Word, Excel, PowerPoint, and Outlook.

<!-- embed: https://academy.claude.com/embed/courses/introduction-to-claude-cowork/ChromeDashboardHandoff -->

Film: an animated illustration plays on its own, showing Claude's cursor filtering and exporting data on a mock customer-health dashboard in Chrome, then handing the results off to Cowork to build a summary document.

Cowork prompt

“Pull yellow and red accounts from the customer-health dashboard for the last 30 days, then build a one-page summary with the top three at-risk accounts.”

Claude (MCP)

Customer Health — Dashboard×

app.internal/customer-health

Customer health

All statuses

Green

Yellow

Red

Last 90 days

Last 7 days

Last 30 days

Last 90 days

Export

Exported · handed to Cowork

Account

ARR

Status

Last activity

Northwind

$1.4M

Green

2 hours ago

Acme

$980K

Green

Yesterday

Globex

$640K

Yellow

5 days ago

Initech

$420K

Red

12 days ago

Hooli

$1.1M

Green

3 hours ago

Massive Dynamic

$830K

Yellow

8 days ago

Soylent

$310K

Green

Yesterday

Claude

Cowork takes it from here

at-risk-accounts-summary.docxPulling Drive context · building summary · 1 of 3 sections
<!-- youtube: IypXvHej9eY -->

[![Customer health](https://img.youtube.com/vi/IypXvHej9eY/hqdefault.jpg)](https://www.youtube.com/watch?v=IypXvHej9eY)

<details>
<summary>자막: Customer health</summary>

Claude for Chrome brings the power of Sonnet 4.5, our state of the art model for computer use directly to your browser. In this example, Claude is helping with a home renovation. It will organize your renovation budget, which is currently spread across a planning doc and several contractor email exchanges. Once prompted, Claude gets to work to collect the right context. In this case, finding all the relevant emails and receipts you’ve requested. Claude uses what it learns and actively works with your spreadsheet. Tracking down the missing numbers and updating your budget in real time. Finally, Claude makes it easy for you to share your plans with your partner by drafting an email for you. But don't worry, you're still in control of the final edits before you send that email. We took many steps to build this product with safety and security at its core. For example, you control what actions Claude can take through granular permissions. We've also implemented protection against prompt injection attacks and added restrictions around what websites Claude can use. And it always asks before taking sensitive actions like making purchases. Bring Claude to your browser today.

</details>
