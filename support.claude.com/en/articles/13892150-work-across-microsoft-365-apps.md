<!-- source: https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps -->

# Work across Microsoft 365 apps

May 7, 2026

Claude can now work across Microsoft 365 apps to coordinate between the Excel, PowerPoint, Word, and Outlook add-ins. Instead of switching between apps and providing context each time, Claude can read from one app and make changes in another. For example, you can ask Claude to analyze data in an Excel workbook, then create a presentation in PowerPoint using those results, without copying and pasting between apps.

## Requirements

* A paid Claude plan (Pro, Max, Team, or Enterprise)
* The Claude for Excel add-in installed from the Microsoft Marketplace
* The Claude for PowerPoint add-in installed from the Microsoft Marketplace
* The Claude for Word add-in installed from the Microsoft Marketplace
* The Claude for Outlook add-in installed from the Microsoft Marketplace

## Let Claude work across apps

### 1. Install the add-ins

Get the add-ins from the Microsoft Marketplace:

* **[Claude for Microsoft 365 (Excel, PowerPoint, and Word)](https://marketplace.microsoft.com/en-us/product/office/WA200010725?tab=Overview)**
* **[Claude for Outlook](https://marketplace.microsoft.com/en-us/product/office/WA200010724?tab=Overview)**

Open each app and activate the add-in at least once before using the cross-app features.

### 2. Toggle the setting on

**Note:** If you're a member of a Team or Enterprise plan, an organization owner needs to go to **[Organization settings > Office agents](https://claude.ai/admin-settings/office-agents)** and toggle the **Let Claude work across apps** setting on before you can enable this capability individually.

Go to **Settings** in each of the add-ins and toggle **Let Claude work across files** on:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152216540/23e9f22eca1109ec09f2c6138191/2ef697a8-3a60-4193-bbd7-639ed91b20e9?expires=1782459900&signature=180f99852d8d36c8283799c0ea2ca634fdd1f26e3af7c317485543b5c0071d15&req=diEiFMt%2Fm4RbWfMW1HO4ze%2BVVHbxVQdWQEr1GSm7Lk11bOdf55IMLjfAE9yl%0ABT%2FTUAgFgqHiDJ79FTI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152216540/23e9f22eca1109ec09f2c6138191/2ef697a8-3a60-4193-bbd7-639ed91b20e9?expires=1782459900&signature=180f99852d8d36c8283799c0ea2ca634fdd1f26e3af7c317485543b5c0071d15&req=diEiFMt%2Fm4RbWfMW1HO4ze%2BVVHbxVQdWQEr1GSm7Lk11bOdf55IMLjfAE9yl%0ABT%2FTUAgFgqHiDJ79FTI%3D%0A)

**Note:** This setting is default on for Pro and Max plans and default off for Team and Enterprise plans.

You'll see connected file indicators when Excel, PowerPoint, Word, or Outlook files are linked to your session:

[![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152215013/db0cfd2aa4034975480d82218aad/8f11dc16-2173-4b34-a05a-e31a53b58cc2?expires=1782459900&signature=97fe30eda27673583712eeba2a22b3d4c646f74b6061051370ced1146d752e3a&req=diEiFMt%2FmIFeWvMW1HO4zZtV3m%2By3ttoGgi4PNaz7vUeg2UnPAPUDrbAhjXi%0AILZbdAmhSeyB4%2BLb7B4%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2152215013/db0cfd2aa4034975480d82218aad/8f11dc16-2173-4b34-a05a-e31a53b58cc2?expires=1782459900&signature=97fe30eda27673583712eeba2a22b3d4c646f74b6061051370ced1146d752e3a&req=diEiFMt%2FmIFeWvMW1HO4zZtV3m%2By3ttoGgi4PNaz7vUeg2UnPAPUDrbAhjXi%0AILZbdAmhSeyB4%2BLb7B4%3D%0A)

##

## How it works

When you describe a task that involves multiple files or apps, Claude coordinates behind the scenes:

* Claude uses the Excel, PowerPoint, Word, and Outlook add-ins to read from and write to open files.
* Context transfers between apps automatically, so you don't need to copy and paste information manually.
* You stay in one place while Claude does the switching.

## What you can do

### Read and write across open files

Claude can read data from an open Excel workbook, PowerPoint presentation, Word document, or Outlook email, and make changes to them directly. For example:

* Pull numbers from an Excel model into a PowerPoint slide or a Word memo.
* Update a chart in PowerPoint with the latest figures from Excel.
* Read content from a presentation and use it to populate a spreadsheet.
* Summarize a Word document into PowerPoint slides.
* Draft a Word memo using data from an Excel workbook.
* Open your Outlook emails and full thread history, including attachments.

### Pass context between apps

When Claude works across multiple files in Excel, PowerPoint, Word, and Outlook, it carries relevant context forward. If you've been building a financial model in Excel and ask Claude to create a summary deck or draft an investment memo, Claude already understands the model's structure and key outputs, so you don't need to re-explain.

## Skills work across apps too

Skills you've enabled in your Claude settings apply when Claude is working in Excel, PowerPoint, Word, or Outlook during a cross-app task. If you have a Skill that enforces your team's modeling conventions in Excel and another that matches your slide template in PowerPoint, Claude uses each one in the right app as it moves through the workflow.

For more on how Skills work, see **[Use Skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).**

## Data handling

Inputs and outputs are automatically deleted from Anthropic's backend within 30 days of receipt or generation, except in cases outlined in **[How long do you store my organization's data?](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** The Claude for Excel, Claude for PowerPoint, Claude for Word, and Claude for Outlook add-ins do not inherit custom data retention settings your organization may have set, and activity is not currently included in Enterprise audit logs, the Compliance API, or data exports.

### For admins who want to manage access

Team and Enterprise organization owners can control whether team members can access this capability:

1. Go to **[Organization settings > Office agents](https://claude.ai/admin-settings/office-agents)**
2. Toggle **Let Claude work across apps** on or off.

Admins can also manage member access to the Claude for Excel, PowerPoint, Word, and Outlook add-ins through the **[Microsoft 365 Admin Center](https://admin.microsoft.com)**.

## Current limitations

* Claude can only read from and write to files that are currently open in Excel, PowerPoint, Word, or Outlook.
* Claude cannot create, open, close, or switch files directly from the add-ins—the files and add-ins must be open with the feature turned on.
* Chat history for cross-app sessions is not saved between sessions.

## Troubleshooting

### Claude doesn't see my open file

Make sure the add-in is activated in the app (**Tools > Add-ins** on Mac or **Home > Add-ins** on Windows) and that working across apps is turned on in Claude Desktop settings.

### Changes aren't appearing in the other app

Claude works on open files in sequence. Wait for Claude to finish its current action, then check the target file. You may need to ask Claude to refresh or re-read the file.

[Use Claude for PowerPoint](https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint)[Use Claude for Microsoft 365 with third-party platforms](https://support.claude.com/en/articles/13945233-use-claude-for-microsoft-365-with-third-party-platforms)[Use Claude for Word](https://support.claude.com/en/articles/14465370-use-claude-for-word)[Use Claude for Outlook](https://support.claude.com/en/articles/14855664-use-claude-for-outlook)[Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
