<!-- source: https://academy.claude.com/use-cases/my-voice -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Write in my voice

A profile of how you write, saved as a skill.

10 minClaude Cowork

Try in CoworkCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-jpnl9xn4.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-cdz8tber.png)

## Set up[](#set-up)

### Try a plugin[](#try-a-plugin)

The Productivity plugin ships with `/memory-management` so Cowork can save what it learns about how you work; you'll build your own `/my-voice` on top. If your admin manages plugins and it's not available yet, skip this; nothing below requires it.

ProductivityManage tasks, plan your day, and build up memory of important context about your work. Syncs with your calendar, email, and chat to keep everything organized and on track.

[Add](https://claude.ai/desktop/customize/plugins/new?marketplace=github.com%2Fanthropics%2Fknowledge-work-plugins&plugin=productivity)

`/memory-management`Two-tier memory system that makes Claude a true workplace collaborator.

[Run](claude://cowork/new?q=%2Fmemory-management)

`/update`Sync tasks and refresh memory from your current activity.

[Run](claude://cowork/new?q=%2Fupdate)

Show all 4 skills

### Connect your tools[](#connect-your-tools)

Claude Cowork is more powerful when it works directly with your systems. You control permissions and access. [Learn about tool access(opens in new tab)](https://support.claude.com/en/articles/13730515-manage-claude-s-tool-access).

Navigate to **Customize → Connectors** in Cowork to set up.

![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)

Gmail

[Connect](https://claude.ai/desktop/directory/gmail-gmailmcp)

![](images/b6bf6491858dcff4.svg)

Slack

[Connect](https://claude.ai/desktop/directory/slack)

![](images/3cb5db332ced9f49.svg)

Microsoft 365

[Connect](https://claude.ai/desktop/directory/microsoft-365)

![](images/ea7c24639ab8053c.svg)

Notion

[Connect](https://claude.ai/desktop/directory/notion)

![](images/a3bfc5814bd6a3e2.svg)

Google DriveOptional

[Connect](https://claude.ai/desktop/directory/google-drive-drivemcp)

Browse all connectors[Open in Cowork](https://claude.ai/desktop/customize/connectors)

**Want to try this task before setting anything up?** Add your files to a working folder, point Cowork at the folder, and start with the prompt.

### Set your working folder[](#set-your-working-folder)

This one runs almost entirely through connectors, so the working folder is optional. If you'd rather not connect mail, export a folder of writing samples (sent emails, docs you're proud of) and point Cowork at that instead. Either way, [create a Cowork project(opens in new tab)](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork) so the voice profile and your later corrections stay attached.

Personal / Writing-Samples

my-voice-profile.mdApr 26, 20264 KB

all-hands-update-feb.docxFeb 12, 202622 KB

In Cowork’s chat bar:Personal / Writing-Samples

## The prompt[](#the-prompt)

### Copy this into Claude Cowork[](#copy-this-into-claude-cowork)

Read my sent messages and tell me about my tone and writing style.

Personal / Writing-SamplesOpen in Cowork

### Why this works[](#why-this-works)

Prompt

**Start simple.** A short, open ask gets you a first read on your voice fast. You can sharpen it from there.

Source

**Your real writing is the corpus.** Reading what you actually sent, not a curated best-of, means the profile catches your real habits.

### Get a better draft[](#get-a-better-draft)

Practice

**Add an example to match.** Drop an example you like into the folder and Cowork matches your structure and voice.

Practice

**Ask it to flag uncertainty.** Add "flag anything you're not confident about" so you know where to look first when you review the draft.

## Make Cowork work for you[](#make-cowork-work-for-you)

The first profile is a snapshot; your voice keeps moving. Every time you edit a draft Cowork wrote and think "I wouldn't say it like that," feed the correction back. Tell Cowork to add the rule to `/my-voice`, or just say "remember that" in the moment and Cowork writes it into the skill's memory. Over a few weeks the profile tightens until the drafts barely need editing.

Update **/my-voice** with what I just changed in that draft: I never open with "Hope you're well," I use "folks" not "team," I lead with the ask before the context, and I sign off with just my first initial on internal mail. Save those as rules in the skill and add this edited draft to the examples so future drafts match it.

PersonalOpen in Cowork

**Save tweaks as you go.** Any time you rewrite a Cowork draft, end with "add that to /my-voice." The skill accumulates your corrections as rules and your edited drafts as reference examples, so the gap closes every time you use it.

## Make it repeatable[](#make-it-repeatable)

### Refresh the profile monthly[](#refresh-the-profile-monthly)

Your writing shifts as your role does. Type `/schedule` in the prompt, or open **Scheduled** in the Cowork sidebar, and Cowork re-reads the last 90 days each month and merges what's new into the skill without losing the rules you've added by hand.

**/schedule** Every Sunday at 6pm, re-read my sent mail and Slack from the last 90 days, update the /my-voice profile with anything new, and keep every rule I've added manually intact.

PersonalOpen in Cowork

Scheduled taskActive

Refresh /my-voice

Re-reads the last 90 days of sent mail and Slack and merges anything new into `/my-voice`, preserving your hand-added rules.

Every **Sunday at 6:00pm**[Open in Cowork](https://claude.ai/desktop/scheduled-task)

## Share with your teammates[](#share-with-your-teammates)

`/my-voice` is personal by design, but the pattern is worth spreading. Share the base skill (without your profile) so teammates can build their own in one prompt, or share your version with an EA or comms partner who drafts on your behalf.

Share the skill

In Cowork, open **Skills** → `/my-voice` → **Share** and pick your teammates (or your whole workspace, if your admin allows). They get the skill scaffold so they can build their own profile without repeating Steps 1-3.

## Going forward[](#going-forward)

### Now in your Cowork

Your processes

Personal plugin

Your tools

![](images/f37dc3507c90f690.svg)'%3e%3cpath%20d='M11.9091%2034H16.3636V23.6969L10%2019.1515V32.1818C10%2033.1879%2010.8559%2034%2011.9091%2034Z'%20fill='%234285F4'/%3e%3cpath%20d='M31.6364%2034H36.0909C37.1473%2034%2038%2033.1848%2038%2032.1818V19.1515L31.6364%2023.6969'%20fill='%2334A853'/%3e%3cpath%20d='M31.6364%2015.8182V23.6969L38%2019.1515V16.7272C38%2014.4788%2035.305%2013.1969%2033.4182%2014.5454'%20fill='%23FBBC04'/%3e%3cpath%20d='M16.3636%2023.697V15.8182L24%2021.2727L31.6364%2015.8182V23.697L24%2029.1515'%20fill='%23EA4335'/%3e%3cpath%20d='M10%2016.7272V19.1515L16.3636%2023.6969V15.8182L14.5818%2014.5454C12.6918%2013.1969%2010%2014.4788%2010%2016.7272Z'%20fill='%23C5221F'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_4766_38693'%3e%3crect%20width='28'%20height='20'%20fill='white'%20transform='translate(10%2014)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e)Gmail![](images/b6bf6491858dcff4.svg)Slack![](images/a3bfc5814bd6a3e2.svg)Google Drive

Your workspace

Writing-Samples

Every draft Cowork writes for you now loads `/my-voice` first, so it matches how you actually write — you spend your review on the content, not on making it sound like you.

[Next: Thread to decision doc](https://academy.claude.com/use-cases/thread-to-decision)

* [Set up](#set-up)
* [The prompt](#the-prompt)
* [Make Cowork work for you](#make-cowork-work-for-you)
* [Make it repeatable](#make-it-repeatable)
* [Share with your teammates](#share-with-your-teammates)
* [Going forward](#going-forward)
