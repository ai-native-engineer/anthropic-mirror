<!-- source: https://academy.claude.com/use-cases/handle-a-request-while-away-from-your-keyboard -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Handle a request while away from your keyboard

Use Dispatch in Claude Cowork to respond to requests from the Claude mobile app using everything on your computer. Claude finds the file, drafts the reply, and waits for your approval before sending.

15 minClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-lyytfhz3.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-jx0gutex.png)

## 1. Describe the task

Work does not pause when you step away from your computer. A teammate asks for a file. A client sends a question that requires information from a document on your computer. A deadline moves up. Dispatch lets you respond using everything on your computer, from your phone.

This works when your computer is awake and the Claude desktop app is running. The keep-awake toggle in [Dispatch settings(opens in new tab)](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) prevents your computer from sleeping when you step out. Turn it on once and your computer stays reachable whether you are in a car, at a coffee shop, on a plane with wifi, or simply across the office without your laptop.

Dispatch is also useful when your computer is nearby but your phone is more practical. In tight spaces, on a call, or when opening a laptop would be awkward, you can send a quick instruction from your phone and Claude handles the rest on your computer.

A teammate asks for a budget spreadsheet over Slack. From your phone, you tell Claude where the file is and where to send it — Claude finds it and posts it with your note.

Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with “Q2” and “budget” in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled “Revised” has the current numbers.

Open in Cowork

## 2. Give Claude context

Claude reads the file from your computer and posts it through the [Slack connector(opens in new tab)](https://claude.com/connectors/slack). No file uploads, no cloud sync — Claude reads the document in place on your machine and sends it through the connected tool.

### Required context

For this task, Claude needs access to your local files and one connector:

* Local files — to find and read the spreadsheet in your Documents/Finance folder.
* Slack — to post the file and your note to the #proj-planning channel.

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

## 3. What Claude creates

Claude locates the file, prepares the message, and — if you have Slack set to [needs-approval(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) for sending — shows you the message before posting. Here is what the exchange looks like on your phone:

I found **Q2-Budget-Revised-v3.xlsx** in Documents/Finance.

Before I post, here is the message I will send to **#proj-planning**:

*Hi Jamie — here is the Q2 budget spreadsheet you asked for. The tab labeled “Revised” has the latest numbers.*

[Attached: Q2-Budget-Revised-v3.xlsx]

Should I go ahead and post this?

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Draft a reply with approval before sending

Claude can draft messages using files on your computer, then wait for your approval before sending. This keeps you in control of what goes out while Claude does the research and writing.

Draft a reply to the client email about pricing. Use the proposal in my Documents folder for the numbers, but don't send until I approve.

Open in Cowork

### Pick up the thread on your laptop

When you get back to your desk, continue in the same Dispatch conversation. Claude remembers everything it did while you were away — what it found, what it sent, and any requests that came in.

I'm back at my desk. Show me what you sent and any other requests that came in while I was out.

Open in Cowork

### Use computer use to reach a desktop app

[Computer use(opens in new tab)](https://support.claude.com/en/articles/14128542-let-claude-use-your-computer-in-cowork) lets Claude operate desktop applications that have no connector and no web version. If the information you need lives in a native desktop app, Claude can open it and pull what you need.

There's a report I need from the analytics dashboard app on my computer. Open it and screenshot the Q1 summary.

Open in Cowork

## 5. Tricks, tips, and troubleshooting

### Set send permissions to needs-approval

For connectors like Slack and Gmail, set send access to needs-approval. Claude drafts the message and shows it to you before posting or emailing — so nothing goes out without your sign-off.

### Turn on keep-awake before stepping away

The keep-awake toggle prevents your computer from sleeping while you are out. Turn it on before you leave so Claude can respond to requests on your machine at any time.

### Files stay local when Claude reads them

Claude reads documents in place on your computer. When it posts a file to Slack or references data in an email, the source document stays on your machine — nothing gets uploaded to a cloud service.

### Computer use is a separate toggle

Computer use is off by default and must be enabled in Dispatch settings. Claude asks for your approval before controlling each new application.

## 6. Ready to try for yourself?

Get started with Dispatch: download the Claude desktop app and the Claude mobile app, open Claude Cowork, and tap Dispatch in the sidebar

Jamie just asked me on Slack for the latest Q2 budget spreadsheet. Find it in my Documents/Finance folder on my computer — the file with “Q2” and “budget” in the name. Post it to Jamie in the #proj-planning Slack channel. Add a note that the tab labeled “Revised” has the current numbers.

Try in Cowork

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
