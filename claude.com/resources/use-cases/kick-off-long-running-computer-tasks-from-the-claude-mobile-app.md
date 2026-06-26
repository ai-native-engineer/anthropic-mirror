<!-- source: https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app -->

[](https://claude.com/resources/use-cases-category/cowork)
Cowork
[](https://claude.com/use-cases-features/cowork)
Cowork
  * [Login](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)

[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

  * [Login](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)

[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude
[Try Claude](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2)Try Claude

  2. Kick off long-running computer tasks from the Claude mobile app

  * [Ask questions about this page](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  * [Copy as markdown](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)

# Kick off long-running computer tasks from the Claude mobile app
Check progress on a running task, give Claude Cowork the next instruction, and keep work moving — all from the Claude mobile app, without returning to your desk.
Cowork
Cowork
[Copy link](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
https://claude.com/resources/use-case/kick-off-long-running-computer-tasks-from-the-claude-mobile-app

Some tasks take time. Processing a folder of invoices, cleaning a large dataset, reorganizing hundreds of files — these jobs can run for minutes after you start them. You do not need to sit and watch.
Dispatch keeps one persistent conversation between your phone and your computer. When you send Claude a task from your desk and walk away, Claude keeps working. Later, from your phone, you can ask Claude what happened, review the results, and send the next instruction. Claude remembers every previous message and every file it touched in the conversation.
The key detail: your computer must stay awake while Claude works. Turn on the [keep-awake](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork#keep-awake) toggle in [Dispatch settings](https://support.claude.com/en/articles/13947068-assign-tasks-to-claude-from-anywhere-in-cowork) before you leave your desk.
This starts with a batch job — extracting invoice data from a folder of PDFs into a spreadsheet. After walking away, you check in from your phone and start the next step.
_Go through every PDF in ~/Documents/Invoices/March-2026 and pull out the vendor name, invoice number, date, and total amount. Put all of it into a spreadsheet called march-invoices.csv in the same folder. Let me know when you're done._
[Next](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Next
[Ask Claude](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Ask Claude
Claude needs access to the folder where the invoices are stored. Grant folder access during Dispatch setup on your computer. No [connectors](https://claude.com/connectors) are required for this use case — Claude works directly with files on your machine.
  * No connectors are required. Claude reads the PDF files and creates the CSV directly on your computer.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)
  * If you want Claude to email the finished spreadsheet or post a summary to [Slack](https://claude.com/connectors/slack), enable the [Gmail](https://claude.com/connectors/gmail) or Slack connector. Otherwise, the file stays on your computer and you can grab it when you get back.

You sent the first message from your desk and walked to a meeting. Twenty minutes later, you open the Claude app on your phone and check in.
Done. I processed 47 PDF invoices from ~/Documents/Invoices/March-2026.
Here is a summary:
  * **Total invoices processed:** 47
  * **Unique vendors:** 18
  * **Date range:** March 1 – March 28, 2026
  * **Grand total across all invoices:** $34,219.57
  * **Largest invoice:** $8,400.00 from Redwood Design Co (invoice #RDC-2026-0342) The spreadsheet is saved at ~/Documents/Invoices/March-2026/march-invoices.csv. Each row has four columns: Vendor Name, Invoice Number, Date, and Total Amount.

Three invoices had formatting I want to flag:
  * scan_031.pdf — the total was handwritten and hard to read. I recorded $215.00 but you may want to double-check.
  * consolidated_march.pdf — this file contained two separate invoices. I split them into two rows.

draft_invoice.pdf — marked as DRAFT. I included it but added a note in a fifth column.
### **Build on the data Claude already has**
Dispatch keeps a persistent conversation. Claude already processed the invoices and has every vendor, amount, and date in memory. Your next question can reference that data directly — no need to re-describe the file.
_Now compare the totals by vendor against the Q1 budget forecast and flag anything over 15%._
[Next](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Next
[Ask Claude](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Ask Claude
### **Create a summary file from the results**
Claude can create new files on your computer from the data it has already processed. Ask for a formatted report and tell Claude where to save it.
_Create a summary PDF with the top 10 vendors by spend and save it to my Finance folder._
[Next](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Next
[Ask Claude](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Ask Claude
### **Run this batch job every month**
A Dispatch prompt can become a [scheduled task](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-cowork) that runs on a recurring cadence. Set it once and Claude processes the new invoices automatically each month.
_Set this up to run on the first of every month with the new invoices folder._
[Next](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Next
[Ask Claude](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Ask Claude
### **Turn on keep-awake before starting a long task**
Batch processing can take minutes. The keep-awake toggle prevents your computer from sleeping while Claude works through the files. It does not keep the screen on — just the machine.
### **Dispatch remembers what it did**
Claude keeps full context of every file it processed and every result it produced. When you check in later, Claude can answer follow-up questions, compare data, or build on its earlier work without starting over.
### **Describe the file location clearly**
Include the full path when you know it (like ~/Documents/Invoices/March-2026). If you are not sure of the exact path, describe the folder name and location — Claude searches the folders you granted access to.
### **Scheduled tasks turn one-off jobs into routines**
Once a batch prompt works, save it as a scheduled task. Claude runs the same instructions on the cadence you set, processing new files each time without you sending the prompt again.
Get started with Dispatch: download the Claude desktop app and the Claude mobile app, open Cowork, and tap Dispatch in the sidebar.
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69de77952d4c85bc23f8b79f_Screenshot%202026-04-14%20at%2010.21.20%E2%80%AFAM.png)
[Open artifact in new window](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Open artifact in new window
[Audit a folder of visual assets against your guidelines](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Audit a folder of visual assets against your guidelines
Audit a folder of visual assets against your guidelines
[Use case](https://claude.com/resources/use-cases/audit-a-folder-of-visual-assets-against-your-guidelines)Use case
[Adapt a standard textbook page to every reading level](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Adapt a standard textbook page to every reading level
Adapt a standard textbook page to every reading level
[Use case](https://claude.com/resources/use-cases/adapt-a-standard-textbook-page-to-every-reading-level)Use case
[Handle a request while away from your keyboard](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Handle a request while away from your keyboard
Handle a request while away from your keyboard
[Use case](https://claude.com/resources/use-cases/handle-a-request-while-away-from-your-keyboard)Use case
[Operate any computer app from your phone with Dispatch](https://claude.com/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch)Operate any computer app from your phone with Dispatch
Operate any computer app from your phone with Dispatch
[Use case](https://claude.com/resources/use-cases/operate-any-computer-app-from-your-phone-with-dispatch)Use case
[Next](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Next
[Button Text](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Button Text
[Button Text](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Button Text
[Button Text](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)Button Text
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  

[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  

[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  

[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)
  
[](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app#)

[Log in](https://claude.ai/redirect/claudedotcom.v1.f7f3e0dd-a8b0-47f6-bf05-fb0f3530bdd2/login)Log in

[English (US)](https://claude.com/resources/use-cases/kick-off-long-running-computer-tasks-from-the-claude-mobile-app)
