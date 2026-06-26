<!-- source: https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard -->

Cowork

Connectors

Cowork

# Handle a request while away from your keyboard

Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer. Claude finds the file, drafts the reply, and waits for your approval before sending.

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

  https://claude.com/resources/use-case/handle-a-request-while-away-from-your-keyboard

1

## Describe the task

Work does not pause when you step away from your computer. A teammate asks for a file. A client sends a question that requires information from a document on your computer. A deadline moves up. Dispatch lets you respond using everything on your computer, from your phone.

This works when your computer is awake and the Claude desktop app is running. The keep-awake toggle in [Dispatch settings](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) prevents your computer from sleeping when you step out. Turn it on once and your computer stays reachable whether you are in a car, at a coffee shop, on a plane with wifi, or simply across the office without your laptop.

Dispatch is also useful when your computer is nearby but your phone is more practical. In tight spaces, on a call, or when opening a laptop would be awkward, you can send a quick instruction from your phone and Claude handles the rest on your computer.

A teammate asks for a budget spreadsheet over Slack. From your phone, you tell Claude where the file is and where to send it — Claude finds it and posts it with your note.

*Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with “Q2” and “budget” in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled “Revised” has the current numbers.*

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Claude reads the file from your computer and posts it through the [Slack connector](https://claude.com/connectors/slack). No file uploads, no cloud sync — Claude reads the document in place on your machine and sends it through the connected tool.

## Required context

For this task, Claude needs access to your local files and one connector:

* Local files — to find and read the spreadsheet in your Documents/Finance folder.
* Slack — to post the file and your note to the #proj-planning channel.

‍

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690a5eb066fb294c24a6fb96_slack.svg)

Slack

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

No additional [connectors](https://claude.com/connectors) are needed for a file-and-send task. If the request involves drafting a reply or forwarding a document, connecting [Gmail](https://claude.com/connectors/gmail) lets Claude draft and send email on your behalf (with your approval before sending).

No items found.

3

## What Claude creates

Claude locates the file, prepares the message, and — if you have Slack set to [needs-approval](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) for sending — shows you the message before posting. Here is what the exchange looks like on your phone:

From Claude

I found **Q2-Budget-Revised-v3.xlsx** in Documents/Finance.

Before I post, here is the message I will send to **#proj-planning**:

*Hi Jamie — here is the Q2 budget spreadsheet you asked for. The tab labeled “Revised” has the latest numbers.*

[Attached: Q2-Budget-Revised-v3.xlsx]

Should I go ahead and post this?

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### **Draft a reply with approval before sending**

Claude can draft messages using files on your computer, then wait for your approval before sending. This keeps you in control of what goes out while Claude does the research and writing.

‍

*Draft a reply to the client email about pricing. Use the proposal in my Documents folder for the numbers, but don't send until I approve.*

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### **Pick up the thread on your laptop**

When you get back to your desk, continue in the same Dispatch conversation. Claude remembers everything it did while you were away — what it found, what it sent, and any requests that came in.

*I'm back at my desk. Show me what you sent and any other requests that came in while I was out.*

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### **Use computer use to reach a desktop app**

[Computer use](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) lets Claude operate desktop applications that have no connector and no web version. If the information you need lives in a native desktop app, Claude can open it and pull what you need.

*There's a report I need from the analytics dashboard app on my computer. Open it and screenshot the Q1 summary.*

‍

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### **Set send permissions to needs-approval**

For connectors like Slack and Gmail, set send access to needs-approval. Claude drafts the message and shows it to you before posting or emailing — so nothing goes out without your sign-off.

### **Turn on keep-awake before stepping away**

The keep-awake toggle prevents your computer from sleeping while you are out. Turn it on before you leave so Claude can respond to requests on your machine at any time.

### **Files stay local when Claude reads them**

Claude reads documents in place on your computer. When it posts a file to Slack or references data in an email, the source document stays on your machine — nothing gets uploaded to a cloud service.

### **Computer use is a separate toggle**

Computer use is off by default and must be enabled in Dispatch settings. Claude asks for your approval before controlling each new application.

## Ready to try for yourself?

Get started with Dispatch: download the Claude desktop app and the Claude mobile app, open Claude Cowork, and tap Dispatch in the sidebar

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de771df969adffff67d2ac_Screenshot%202026-04-14%20at%2010.19.17%E2%80%AFAM.png)

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

[Kick off long-running computer tasks from the Claude mobile app](/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Kick off long-running computer tasks from the Claude mobile app

Kick off long-running computer tasks from the Claude mobile app

Use case

[Use case](/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)Use case

[Operate any computer app from your phone with Dispatch](/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch)Operate any computer app from your phone with Dispatch

Operate any computer app from your phone with Dispatch

Use case

[Use case](/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch)Use case
