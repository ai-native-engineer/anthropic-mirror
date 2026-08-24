<!-- source: https://academy.claude.com/use-cases/prepare-and-plan-from-your-calendar -->

2. /[Use cases](https://academy.claude.com/use-cases)

[Use cases](https://academy.claude.com/use-cases)

# Prepare and plan from your calendar

Claude in Chrome reads your calendar, pulls context from email threads, flags which meetings need prep, and books rooms for the ones missing them. Run it every evening and start each day knowing what's coming.

10 minClaude in Chrome

Get Claude in ChromeCopy prompt

![](https://academy.claude.com/assets/v1/thumbnail.light-a8f13pls.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-ms6ban8i.png)

![Prepare and plan from your calendar result](https://academy.claude.com/assets/v1/prepare-and-plan-from-your-calendar-o4y1fyqa.png)

## 1. Describe the task

Claude for Chrome lets Claude interact directly with web pages—reading content, clicking, typing, and navigating sites on your behalf. For calendar prep, this means Claude can open your Google Calendar, check each meeting's attendee list, switch to Gmail to search for relevant threads with those people, and even book conference rooms.

Point Claude at your Google Calendar and tell it what to look for. It handles the cross-referencing between calendar and email, surfaces what needs your attention, and can fix the gaps.

Look at my calendar and help me get ready for tomorrow.

**For each meeting:**

* Tell me if it's internal or external (check the attendee domains)
* Find any recent email threads with those attendees about this topic
* Flag if the meeting is missing a room (for in-person) or a video link (for remote). If it is, assign one to the meeting.
* For external meetings, note anything I should review beforehand, like relevant docs attached to the meeting or related emails.

Give me a quick prep summary for the day, finding what needs my attention before I show up.

Copy prompt

## 2. Give Claude context

Claude reads your calendar and email directly in Chrome. It cross-references attendees, threads, and meeting details to build context.

### Required context

**Required:** Open Google Calendar showing tomorrow's date and Gmail in another tab. Claude navigates between them to gather context for each meeting. Make sure you're logged into both.

## 3. What Claude creates

Claude reviews each meeting and gives you a prep summary organized by what needs attention.

**Tomorrow: Wednesday, December 18**

You have **6 meetings**. Here's what I found:

**Needs Prep (External Meetings)**

| Meeting | Time | Context |
| --- | --- | --- |
| Acme Corp quarterly review | 10:00 AM | External (3 attendees from @acme.com). Found email thread from Dec 12 where they asked about API rate limits—might come up. No room booked. |
| Vendor intro - DataFlow | 2:00 PM | External (new contact). They sent a capabilities deck on Dec 15 you haven't opened. Zoom link is in the invite. |

**Missing Logistics**

| Meeting | Issue | Suggested Fix |
| --- | --- | --- |
| Acme Corp quarterly review | No room | Book Sequoia (seats 6) — available |
| Team planning sync | No room | Book Birch (seats 8) — available |
| Design review | No video link | Found Meet link in thread with Sarah—add to invite? |

**Ready to Go (No Action Needed)**

* **Standup** — 9:00 AM, has Zoom link, recurring
* **Marcus 1:1** — 11:30 AM, internal, has room (Aspen)
* **End of day sync** — 4:30 PM, internal, has Meet link

**Quick Prep Summary**

1. Review the API rate limits thread before Acme call (I can pull the key points if helpful)
2. Open the DataFlow deck before the 2pm—it's 12 slides
3. Book rooms for Acme and Team planning
4. Add Meet link to Design review

Want me to book those rooms and add the video link now?

## 4. Follow up prompts

Continue the conversation with Claude to refine, expand, or explore further.

### Fix the logistics

Claude can book rooms and add links directly to calendar events. Once you've reviewed what needs fixing, approve the changes.

Yes, book those rooms and add the Meet link. Use a room on the 6th floor if available—that's where I sit.

Copy prompt

### Get deeper prep for the external meeting

For important calls, Claude can summarize recent correspondence with those contacts. This surfaces what's been discussed and what might come up.

For the Acme meeting, can you summarize the last few email threads I've had with them? I want to know what's been discussed recently and what they might bring up.

Copy prompt

### Make this a nightly routine

Claude in Chrome can run tasks on a schedule. Set this to run every evening so you start each morning with prep done.

Can you save this as a shortcut I run every evening at 6pm? Call it "Prep tomorrow" and have it review my calendar, flag external meetings, and check for missing rooms or links.

Copy prompt

## 5. Tricks, tips, and troubleshooting

### Save and automate your workflow as a shortcut

Save the prompt as a shortcut by clicking on the shortcut icon below a successful prompt. You can also set a schedule for when you want the workflow to run next. Alternatively, manually trigger the workflow, by typing "/" and selecting the shortcut.

### Navigating to new sites

Claude asks for permission before visiting new sites. You can grant site-level permissions for websites you trust, allowing Claude to work without repeated approvals on those specific domains.

### Permissions before taking actions

Before clicking "send," "publish," "post," "submit," or similar action buttons, Claude asks for approval. This includes sending emails, posting to social media, submitting forms, or messaging others on your behalf.

## 6. Ready to try for yourself?

Install the Claude in Chrome extension and watch Claude scan tomorrow's meetings, find what you need to know, and fix what's missing—prep done before tomorrow arrives.

[Try in Claude(opens in new tab)](https://claude.com/download)

* [1. Describe the task](#1-describe-the-task)
* [2. Give Claude context](#2-give-claude-context)
* [3. What Claude creates](#3-what-claude-creates)
* [4. Follow up prompts](#4-follow-up-prompts)
* [5. Tricks, tips, and troubleshooting](#5-tricks-tips-and-troubleshooting)
* [6. Ready to try for yourself?](#6-ready-to-try-for-yourself)
