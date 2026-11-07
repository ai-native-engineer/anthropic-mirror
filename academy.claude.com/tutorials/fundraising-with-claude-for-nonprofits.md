<!-- source: https://academy.claude.com/tutorials/fundraising-with-claude-for-nonprofits -->

2. /[Tutorials](https://academy.claude.com/tutorials)

[Tutorials](https://academy.claude.com/tutorials)

# Find funders and report on grants with Claude for Nonprofits

Create a map of where your records are kept and a voice guide, then follow a nonprofit as it finds funders and drafts a grant report. In each step you ask Claude for research or a first draft based on your organization's documents, then review it before you use it.

10 minClaude Cowork

[Open Cowork](https://claude.ai/new?surface=cowork)

![](https://academy.claude.com/assets/v1/thumbnail.light-b9l86rdi.png)![](https://academy.claude.com/assets/v1/thumbnail.dark-kmg77r4y.png)

The last few months of the year are a busy time for fundraising. You may have grant deadlines coming up, with your year-end appeal close behind. At many nonprofits, the person running the programs is also the one raising the money and writing every letter, proposal, and report. Claude can handle the first pass of that work:

* Finding funders that give to your cause
* Checking their eligibility requirements
* Pulling figures from past proposals into a new draft
* Choosing a story for your appeal
* Comparing your outcomes and spending with your award letter

You describe the task and share your organization's documents. Claude prepares a draft, cites its sources, and tells you what's missing. Then you review the draft before you use it.

Getting the plugin

The skills in the Claude for Nonprofits plugin help you do that and more. They're installed automatically on most nonprofit plans. If you don't see the plugin, ask your admin, who can [add it for your organization(opens in new tab)](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization). If you're not on a nonprofit plan, [check eligibility and sign up(opens in new tab)](https://claude.com/solutions/nonprofits).

The tutorial below covers what to set up first, then breaks down two of the fundraising skills: finding funders who fit, and showing funders what their grant made possible. The example follows Kofi Mensah, the development director at Maple Hollow After-School Project, a fictional nonprofit with a reading program. All people, data, documents, and figures are fictional.

## Set up once[](#set-up-once)

Start by having Claude create a map of where your records are kept and a voice guide for your organization's writing style. Every other skill in the plugin uses both.

Where Claude finds your documents

* **Connected tools:** When you connect a tool, like your shared drive, Claude can open the documents you keep there. Claude's data access mirrors yours, so it can only see what you already have access to. [Learn more about connectors(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).
* **Memory:** Memory allows Claude to use what it has saved in earlier chats to inform future ones. Turn on memory in Settings so Claude can save a data map and voice guide and use them in later chats. Memory works in tasks that run in the cloud. [Check where your tasks run(opens in new tab)](https://support.claude.com/en/articles/15811196-what-to-expect-with-claude-cowork-in-the-cloud). [Learn more about memory(opens in new tab)](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).
* **Files you attach:** If you can't reach your data through a connector, download the files and attach them to your message.

If you don't see a tool, or can't turn on memory or run tasks in the cloud, ask your admin.

### 1. A map of where your data lives[](#1-a-map-of-where-your-data-lives)

Your records are probably kept in several places: donor and gift records in a donor database, grant files on a shared drive, budgets somewhere else. Claude creates a map that lists each kind of record and where you keep it, so Claude knows where to look for future tasks.

In this setup, Kofi asks Claude to map where Maple Hollow keeps its records, using the `/where-things-live` skill.

Here is what the skill is built to do:

* Claude asks you where you keep each kind of record.
* Claude saves the name of the tool or place where each record is kept, without saving any details from your records.
* Claude shows you the whole map in the chat, then confirms it's saved to memory.
* From then on, the other skills check the map before they ask you where a record is kept.

Now Kofi has a map of where Maple Hollow keeps each kind of record.

**Before you act:**

* Review the entire map when Claude shows it to you, and correct any location that's wrong.
* If you aren't sure where a record is kept, say so. Claude offers to look in your connected tools. You can come back and update the map once you find it.
* [Connect the tools on your map(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities) wherever a connector is available. The map tells Claude where a record is kept, and the connector lets Claude open it.

**What you need:**

* Memory turned on, and a task that runs in the cloud. The skill also runs without memory, but the map isn't saved for later chats.
* No documents required
* A general sense of where your team keeps each kind of record

**Try it:**

I want to stop explaining where our records are in every chat. Can you ask me about each kind of record and put my answers in a map? Show me the map before you save it.

Open in Cowork

### 2. A voice guide[](#2-a-voice-guide)

Your organization has a unique voice: its writing style and tone, what it calls the people it serves, and how it asks for support. A voice guide codifies that voice in writing so every draft sounds like your organization, whoever writes it.

In this setup, Kofi asks Claude to make a voice guide for Maple Hollow from three of its past letters, using the `/org-voice-guide` skill.

Here is what the skill is built to do:

* Claude looks for an existing voice guide first. If there isn't one, Claude builds a guide from your organization's existing materials and asks you questions to fill in the rest.
* Claude marks which guidelines are its own suggestions.
* Claude writes a short sample in your organization's voice and saves the guide once you confirm the sample sounds right.
* Claude offers to share the finished guide with your team and add it to your map, so the other skills can use your organization's voice for future drafts.

Now Kofi has a short voice guide for Maple Hollow that Claude can use in later drafts.

**Before you act:**

* Read the sample out loud. If part of it doesn't sound like your organization, tell Claude which part and give it feedback before you approve the guide.
* Check that your examples cover each audience you write to, such as donors, funders, and the people you serve. That's how Claude learns your organization's voice for each one.

**What you need:**

* Your organization's voice or style guide, if it has one
* Three to five examples of your organization's materials, like newsletters, website pages, grant applications, or donor letters. Claude can find them in your connected tools, or you can attach them to your message.

**Try it:**

Can you learn how we write, so your drafts sound like us? Use [the materials you chose]. Show me the guide and a sample so I can check it sounds right.

Open in Cowork

## Find funders who fit[](#find-funders-who-fit)

One of the most time-consuming parts of applying for grants is figuring out which funders to approach. You're looking for funders that give to your cause, in your area, to organizations your size. You also have to keep track of who already funds you.

In this section, Kofi asks Claude to find funders for one of Maple Hollow's programs, using the `/funder-and-grant-research` skill.

Here is what the skill is built to do:

* Claude reviews your documents before it asks you any questions.
* Claude finds foundations, companies, agencies, and individual donors that give to causes like yours.
* Claude finds open grants you can apply for, and cites each funder's website for its eligibility requirements and deadline.
* Claude tells you when it can't confirm a deadline or a grant amount.

Now Kofi has a short list of prospective funders for Maple Hollow's reading program, with the strongest fit first.

**Before you act:**

* Follow the source link for each funder and make sure Claude's summary matches the funder's website. Remove any funder that doesn't match.
* Confirm each deadline on the funder's website before you plan around it, because deadlines and priorities change.
* Review any details Claude couldn't confirm, and ask the funder about any that aren't on its website.

**What you need:**

* A description of the program you're raising money for
* The types of funders or funding opportunities you're looking for
* Your list of current funders

**Try it:**

Can you find funders that fit [program name], and skip anyone who already funds us? I want a short list so I can decide who to approach first.

Open in Cowork

## Show funders what their grant made possible[](#show-funders-what-their-grant-made-possible)

You've put a funder's grant to work in your programs. Now it's time to show the funder the results: how your outcomes and spending compare with the goals and budget in your award letter.

Maple Hollow has a report due to the Maple County Community Foundation, which funds its reading program. In this section, Kofi asks Claude to draft that report, using the `/grant-reporting` skill.

Here is what the skill is built to do:

* Claude reports your outcomes against each goal in your award letter and your spending against each budget line.
* Claude takes each figure from your documents, cites the source, and shows its work for any figure it calculated.
* If the report needs a figure or an explanation that isn't in your documents, Claude adds a placeholder in brackets.
* Claude asks you for what your documents can't explain, like why a result came in under the goal.

Now Kofi has a draft report that follows the Foundation's form, with a source for every figure. Next, Kofi will add the missing figure and the explanations, then submit the report.

**Before you act:**

* Make sure the figures in the draft match your program and financial records.
* Wherever the draft has a placeholder, add the missing figure or write the explanation yourself.
* If a result fell short or a budget line ran over, talk to your program officer before you submit the report.

**What you need:**

* The funder's report form or template
* Your award letter or grant agreement
* Your outcomes for the reporting period
* Your spending by budget line

**Try it:**

We owe [funder] a report on our grant. Can you draft it using their form, show the source of every figure, and leave a placeholder where a number is missing? I'll write the reason for any line where we spent more than we planned.

Open in Cowork

## Work with Claude on other fundraising tasks[](#work-with-claude-on-other-fundraising-tasks)

The fundraising skills also cover these tasks. To start one, describe the task and share your documents.

* **Check your fit for a grant** (`/funder-and-grant-research`). Before you put time into an application, it helps to know whether your organization meets the funder's requirements. Share the request for proposals and documents that describe your organization, and Claude rates each requirement "Met", "Not met", or "Can't tell yet". For each requirement rated "Can't tell yet", share what's missing and ask Claude to check again.
* **Write a letter of inquiry or a proposal** (`/grant-proposal-writing`). Share the funder's application guidelines, one or two past proposals, and your latest outcomes report, and Claude bases the draft on them. Make sure every figure matches the source Claude cites, because Claude can make mistakes.
* **Prepare for a funder call, then follow up** (`/donor-and-funder-relations`). Tell Claude who the call is with and what you want from it, and Claude prepares a brief from your records and public sources. Ask Claude to tell you what it couldn't find, and track down those details before the call. After the call, share your notes, and Claude writes them up and drafts the thank-you note.
* **Thank your donors** (`/donor-and-funder-relations`). Share this year's gift records, and Claude writes each thank-you letter with the amount, date, and purpose of the donor's gift, then lists the letters that need a closer look. Read those first.
* **Draft your year-end appeal** (`/donor-and-funder-relations`). Share your gift records and one story from your program that the person in it agreed to share, and Claude bases the appeal on them. Read the appeal for any figure or story you didn't give Claude. If Claude can't cite a source for it, cut it.

## Keep the review habit[](#keep-the-review-habit)

Claude can take a draft up to the point of sending. Before you send it, ask these three questions:

* **Is each claim sourced?** Every figure and claim should have a source you can check.
* **Is each gap marked?** Look for a bracketed placeholder wherever a figure, name, or date is missing.
* **Is any fact stated that you didn't provide?** If so, ask Claude for the source.

Then decide whether to use the draft, revise it, or start over.

You can review a board update, a job posting, or any other draft the same way.

## Learn more[](#learn-more)

* [Teach Claude your way of working using skills(opens in new tab)](https://academy.claude.com/tutorials/teach-claude-your-way-of-working-using-skills)
* [Use connectors to extend Claude's capabilities(opens in new tab)](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
* [Use Claude's chat search and memory to build on previous context(opens in new tab)](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
* [Nonprofit solutions page(opens in new tab)](https://claude.com/solutions/nonprofits): plans and pricing for nonprofits.

* [Set up once](#set-up-once)
* [Find funders who fit](#find-funders-who-fit)
* [Show funders what their grant made possible](#show-funders-what-their-grant-made-possible)
* [Work with Claude on other fundraising tasks](#work-with-claude-on-other-fundraising-tasks)
* [Keep the review habit](#keep-the-review-habit)
* [Learn more](#learn-more)
