<!-- source: https://claude.com/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch -->

Cowork

Connectors

Cowork

# Operate any computer app from your phone with Dispatch

In Claude Cowork, Dispatch with computer use lets Claude control your computer's mouse and keyboard from the Claude mobile app to work in apps that have no other interface Claude could reach.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Cowork
* Model

  Sonnet 4.6
* Features

  Connectors

  Cowork
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/operate-any-computer-app-from-your-phone-with-dispatch

1

## Describe the task

Dispatch connects Claude to your tools through three methods, each with different speed. Connectors give Claude direct access in seconds. The Chrome extension lets Claude read and interact with web applications. Computer use lets Claude operate your mouse and keyboard to control any desktop application on your computer.

Most Dispatch tasks run through [connectors](https://claude.com/connectors) or the Chrome extension. But some applications have no connector and no web version. A desktop accounting program, an installed inventory system, a locally-run reporting tool — these applications only exist on your computer's screen. Computer use reaches them.

Computer use is off by default. You turn it on in [Dispatch settings](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork), and Claude asks for your approval before controlling each application. Claude sees your screen, moves the cursor, clicks buttons, and types — the same way you would, but slower than a connector. Use computer use when no faster method exists.

In this example, Claude opens an accounting application on your computer, navigates to overdue invoices, and pulls the data — all from a single message on your phone.

‍

*Open my accounting app and pull the outstanding invoices report for March. List every invoice over 60 days past due with the client name, invoice number, and amount. Send me the totals by client.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Computer use does not need a connector — Claude operates the application through your computer's screen. Before sending this request, confirm two things: the desktop accounting application is open (or pinned to your taskbar/Dock), and computer use is enabled in your desktop app settings.

‍

## Required context

* No connectors are required. Claude uses computer use to operate the desktop application directly. You need to enable the computer use toggle in Dispatch settings before sending your request. Claude will ask for permission to control the accounting application the first time it interacts with that app in a session.

No items found.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

If you want Claude to send the results somewhere beyond your Dispatch conversation — for example, emailing the overdue list to your collections team — connect Gmail or Slack so Claude can deliver the information without a separate step.

No items found.

3

## What Claude creates

Claude opens the accounting application, navigates to the reports section, runs the outstanding invoices report for March, and reads the results from the screen. Here is an example of what Claude sends back to your phone.

From Claude

I opened your accounting app and pulled the outstanding invoices report for March. Here are all invoices more than 60 days past due:

**Overdue invoices — 60+ days**

* **Meridian Construction** INV-2024-0892 — $14,250.00 (78 days) INV-2024-0915 — $8,400.00 (72 days) Subtotal: **$22,650.00**
* **Lakeview Property Group** INV-2024-0901 — $31,500.00 (75 days) Subtotal: **$31,500.00**
* **Barnett & Associates** INV-2024-0878 — $5,200.00 (84 days) INV-2024-0886 — $5,200.00 (80 days) INV-2024-0934 — $3,100.00 (66 days) Subtotal: **$13,500.00** **Total outstanding (60+ days): $67,650.00 across 6 invoices from 3 clients.**

Barnett & Associates has the most overdue invoices (3), but Lakeview Property Group has the largest single balance. Want me to draft a follow-up email to any of these clients?

‍

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### **Check a web portal in Chrome**

[Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome) handles web applications, while computer use handles desktop apps. You can combine both in one conversation — desktop app for the accounting data, browser for vendor portals.

*Now open Chrome and check our vendor portal for the latest invoice status.*

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### **Review the report at your desk**

After Dispatch pulls data on your computer, you can continue the work on your laptop. Open the results Claude already gathered and review them before taking action.

*I'm at my desk now. Open the report you pulled so I can review it before sending.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### **Email the results to your team**

Claude can route output through connected tools like Gmail. Take the data from the desktop app and deliver it to the right people without copying it yourself.

*Email the overdue report to our finance team with a note about the top three items.*

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### **Computer use is opt-in and off by default**

You must enable the computer use toggle in Dispatch settings before Claude can control desktop applications. Claude also asks for your approval the first time it interacts with each app in a session.

### **Turn on keep-awake before stepping away**

Computer use tasks can take longer than connector-based tasks because Claude navigates the application visually. Keep your computer awake so Claude can finish without interruption.

### **Use connectors first, computer use when needed**

Connectors and the Chrome extension are faster than computer use. Reserve computer use for desktop applications that have no connector and no web version — it reaches apps nothing else can, but connectors handle most tasks more quickly.

‍

## Ready to try for yourself?

Get started with Dispatch: download the Claude desktop app and the Claude mobile app, open Claude Cowork, and tap Dispatch in the sidebar.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de741a2d9547fe8fce8037_Screenshot%202026-04-14%20at%2010.06.28%E2%80%AFAM.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Audit a folder of visual assets against your guidelines](/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Audit a folder of visual assets against your guidelines

Audit a folder of visual assets against your guidelines

Use case

[Use case](/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Use case

[Adapt a standard textbook page to every reading level](/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Adapt a standard textbook page to every reading level

Adapt a standard textbook page to every reading level

Use case

[Use case](/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Use case

[Handle a request while away from your keyboard](/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Handle a request while away from your keyboard

Handle a request while away from your keyboard

Use case

[Use case](/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Use case

[Kick off long-running computer tasks from the Claude mobile app](/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Kick off long-running computer tasks from the Claude mobile app

Kick off long-running computer tasks from the Claude mobile app

Use case

[Use case](/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Use case
