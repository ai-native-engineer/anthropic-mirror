<!-- source: https://claude.com/resources/use-cases/log-sales-calls-to-your-crm -->

Claude in Chrome

Professional

Browser Use

# Log sales calls to your CRM

Claude in Chrome can read your calendar, match attendees to Salesforce contacts, and draft activity logs for each call. You add notes and approve before anything gets created.

Try in Claude

[Try in Claude](https://claude.com/download)Try in Claude

* Author

  Anthropic

  Claude in Chrome
* Model

  Haiku 4.5
* Features

  Browser Use
* Share

  [Copy link](#)

  https://claude.com/resources/use-case/log-sales-calls-to-your-crm

1

## Describe the task

Claude reads your Google Calendar, finds each meeting's attendees in Salesforce, and drafts activity logs. You provide notes on what was discussed and review everything before Claude creates the records.

This works for logging a single day or catching up on a backlog. Claude handles the cross-referencing and formatting; you add the context that makes the logs useful.

Log my calls from today in Salesforce.

**Steps:**

1. Go to my Google Calendar and find today's external meetings (skip internal)
2. For each meeting, look up the attendees in Salesforce
3. Create an activity log for each call—I'll provide a quick summary of what was discussed
4. Format each log with next steps included

**Do not submit.** Show me everything for review before saving to Salesforce.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

2

## Give Claude context

Claude uses browser use to work across your calendar and CRM through your existing browser sessions. If you're logged into Google Calendar and Salesforce, Claude can read your meetings, look up contacts, and create activity records. No API configuration or IT tickets required.

## Required context

Log into Google Calendar and Salesforce in Chrome before starting. Claude navigates between them using your existing sessions.

No items found.

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

## Optional context

If you take notes during calls—in a doc, notepad, or even bullet points—have them accessible. Claude can format rough notes into structured activity descriptions.

No items found.

3

## What Claude creates

Claude shows what it found on your calendar, matches attendees to Salesforce contacts, and drafts activity logs for your review.

From Claude

**External Meetings Today**

 5 found — Here's the status:

**9:00 AM — Intro call - Acme Corp**  - Salesforce match: Sarah Chen (VP Ops)  
  - Status: Ready to log

**10:30 AM — Demo - TechStart**  - Salesforce match: Marcus Johnson  
  - Status: Ready to log

**1:00 PM — Follow-up - Blue Sky**  - Salesforce match: Rachel Torres  
  - Status: Ready to log

**2:30 PM — Pricing - Orion Systems**  - Salesforce match: James Park  
  - Status: Ready to log

**4:00 PM — Discovery - NewCo**  - Salesforce match: No match found  
  - Status: Needs input

**Ready to Log (4 calls)**

 Give me a quick summary for each and I'll format the activity log.

**1. Acme Corp — Sarah Chen**

 You: "Good discovery call. Evaluating us vs Competitor X. Pain point is reporting—current tool takes 2 hours for what should take 5 minutes. Decision by end of Q1. Next step is technical demo with ops team."

 Draft Activity Log:  
  - Subject: Discovery Call - Acme Corp  
  - Type: Call  
  - Related To: Acme Corp - New Business

**Description:**

 Discovery call with Sarah Chen (VP Operations).

**Discussion:**  - Evaluating our solution against Competitor X  
  - Primary pain point: reporting inefficiency (2 hours for reports that should take 5 minutes)  
  - Decision timeline: End of Q1

**Next Steps:**  - Schedule technical demo with operations team  
  - Send competitive comparison materials

**Needs Your Input**

**5. NewCo Discovery**

 No contact found matching the attendee email ([[email protected]](/cdn-cgi/l/email-protection)).

**Options:**  - Create a new contact record  
  - Log the activity against the Account only  
  - Skip this one

 Once you confirm and give me the remaining summaries, I'll show the complete batch for final review.

4

## Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Update opportunity stages

While logging activities, update the opportunity records based on what you learned.

For Acme Corp, move the opportunity to "Demo Scheduled" and update the close date to end of Q1. Add Competitor X to the competitors field.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Catch up on the week

Process multiple days of calls at once before a pipeline review.

I've fallen behind on logging. Can you do this for all my external meetings from the past week? I'll review everything before our Monday pipeline meeting.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

### Create missing contacts

Add new contacts when attendees don't exist in Salesforce yet. Claude can create them and link the activity in one step.

Go ahead and create a contact for Alex at NewCo. His title is Director of Partnerships—you can pull the rest from his email signature in the calendar invite. Then log the activity against that new record.

[Next](#)Next

Ask Claude

[Ask Claude](#)Ask Claude

5

## Tricks, tips, and troubleshooting

### Drag Calendar and Salesforce into the same tab group

For cross-app workflows, drag both Google Calendar and Salesforce into Claude's tab group. You'll see a tab group highlighting the tabs Claude can access. Now Claude can read calendar attendees and look up Salesforce contacts simultaneously—no tab switching. Before visiting new sites, Claude asks for permission. You can grant site-level permissions for websites you trust, allowing Claude to work without repeated approvals on those specific domains.

### Permissions before taking actions

Before clicking "send," "publish," "post," "submit," or similar action buttons, Claude asks for approval. This includes sending emails, posting to social media, submitting forms, or messaging others on your behalf.

### Save your workflow as a shortcut

Once you have an activity log format that works, save the prompt as a shortcut by clicking on the shortcut icon below a successful prompt. You can also set a schedule for when you want the workflow to run next. Alternatively, manually trigger the workflow, by typing "/" and selecting the shortcut.

## Ready to try for yourself?

Claude in Chrome is available to all paid plan users. Install the extension, log into Google Calendar and Salesforce, and ask Claude to log today's calls. It works with your existing browser sessions—no integrations to configure.

Try in Claude

[Try in Claude](/download)Try in Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/694336496e647f7737a583c8_salesforce.png)

Open artifact in new window

[Open artifact in new window](#)Open artifact in new window

## Related use cases

[Pull metrics from analytics dashboards](/resources/use-cases/pull-metrics-from-analytics-dashboards)Pull metrics from analytics dashboards

Pull metrics from analytics dashboards

Use case

[Use case](/resources/use-cases/pull-metrics-from-analytics-dashboards)Use case

[Prepare and plan from your calendar](/resources/use-cases/prepare-and-plan-from-your-calendar)Prepare and plan from your calendar

Prepare and plan from your calendar

Use case

[Use case](/resources/use-cases/prepare-and-plan-from-your-calendar)Use case

[Compare products across sites](/resources/use-cases/compare-products-across-sites)Compare products across sites

Compare products across sites

Use case

[Use case](/resources/use-cases/compare-products-across-sites)Use case

[Clean up promotional emails](/resources/use-cases/clean-up-promotional-emails)Clean up promotional emails

Clean up promotional emails

Use case

[Use case](/resources/use-cases/clean-up-promotional-emails)Use case
