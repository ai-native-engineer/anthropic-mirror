<!-- source: https://claude.com/resources/guides/claude-for-the-legal-industry/how-anthropics-legal-team-uses-claude -->

Chapter 034 min read

# How Anthropic's Legal team uses Claude

4 min read

18 min remaining

Anthropic's own legal team has built four Claude-powered workflows into daily practice. Each one targets work that follows a standard shape and gets reviewed by a lawyer before anything moves downstream.

## Marketing review

The Marketing Material Self-Review Tool lets go-to-market employees check their own content before sending it to Legal for final review. Marketers paste their draft into [a Claude Project (opens in new tab)](https://www.youtube.com/watch?v=tJP6SKfo49c), and Claude analyzes it using a skill that captures the legal team's historical guidance and review framework. The tool flags issues like publicity rights concerns, overstated claims, and statistical accuracy problems, and labels each as low, medium, or high risk. It also suggests fixes before the marketer submits a formal review ticket.

<!-- yt-inline:tJP6SKfo49c -->
[![How Anthropic uses Claude in Legal](https://img.youtube.com/vi/tJP6SKfo49c/hqdefault.jpg)](https://www.youtube.com/watch?v=tJP6SKfo49c)

<details>
<summary>자막: How Anthropic uses Claude in Legal (3:40)</summary>

[00:00]
This is
a legal lamp. That's what we call it.
And I was working on a project
to learn more about how Claude Code works.
And so I was trying to
think of a fun project that would sort of
make my desk come to life more.
And now I can type a message
and ask this lamp to blink in Morse code.
It says it's thinking it's going to do
four quick blinks and two quick blinks,
which is H. I.
Abracadabra.
It's kind of magical. I'm not an engineer.
I'm non-technical.
I don't know how to code.
But with Claude Code,
you don't have to know how to code.
And you can just kind of talk to it
in plain language. And.
No lawyer
likes doing the same repetitive exercise
over and over and over again.
The work can be dull.
You can make mistakes before Claude.
I had a ton of busywork.
Things I would put off
to the end of the day, because I just knew
it'd take a lot of time,
but not using the best parts of my brain.
So we put our heads together and realized
we might be able to use Claude to help

[00:01]
get our best work done and build
workflows.
It used to be that the marketing team
would reach out to me, maybe a day before
a launch and say, hey, we've got this
really exciting launch happening tomorrow.
We're so sorry.
The blog post just came together.
We need you to quickly read this and flag
anything that might be problematic.
So, I asked,
Claude wants to just build me a workflow.
Here's what I care about.
And to my surprise, Claude
just ran with it and set it up.
If I were a marketer and I needed to get
one of my blog posts reviewed,
I would open up this link
to the Marketing Materials Software
review tool,
which is pinned in my channel.
I would cut and paste.
So let me copy their blog post.
I'm going to go back to the review tool.
I'm going to paste all that content
and then I'm going to click
the Analyze Content button.
And this is going to send Claude off
on its journey reviewing my material.
There we have it.
Review results.
Claude is identified
five issues to address.
So it wants to make
sure I focus on accuracy.

[00:02]
It wants to review the security claims,
wants to make sure we have publicity
rights on third
party content,
as well as partnership considerations.
And it gave me props.
It said what looks good
clear the feature descriptions.
Comprehensive integration
details, specific use cases.
Here are the items that require
legal tickets.
Review.
I'm going to click on Generate
Slack message for legal team.
And Claude has now summarized the issues
here.
I'm going to click on Copy the Clipboard
and I'm going to click
go to Legal Tickets to file on my ticket.
To tee it up for legal review,
it identifies the most important issues.
It helps me prioritize.
Sort of has like a low, medium, high risk
level signal.
That's based on a framework
that I gave it.
So it's kind of acting as my eyes
and ears to that first pass.
As we build these types of automations
and in new workflows, I'm always trying
to ensure that a human remains in the loop
from the legal team.
We know that AI systems
can still hallucinate.
I'm still making sure
I'm reviewing the work.

[00:03]
But this is really helping us move
with more speed and sort
of preemptively flagging things
within the legal department.
We're using Claude
in so many different ways.
So we're using it to do redlining
exercises and commercial, matters.
We're using Claude to help us,
with our conflict of interest
policy and reviewing outside business
activity requests.
When people reach out to me and ask,
how do I get started?
I tell them to think of their most routine
work.
Just open up Claude and give it a shot.
You really don't know what it's capable of
doing until you give it a shot.

</details>


When content does get submitted for formal review, it is triaged to the right lawyer with the pre-flagged issues attached. Turnaround time dropped from two to three days down to 24 hours after the tool went live. Lawyers still read every blog post; the self-review layer just clears the obvious issues so review time can go to the calls that require judgment.

## Outside business activity review

The Outside Business Activity Request Form expedites conflict-of-interest review for Anthropic employees who want to consult or join a nonprofit board. Employment lawyers were previously spending significant time on routine COI form reviews; this workflow takes the routine cases off their plate.

Employees fill out a form with their department, manager, and a description of the proposed activity. Claude analyzes the submission against the COI policy framework and sends a recommendation to lawyers via Slack for approval. Where reviewers used to follow up with employees over multiple rounds to surface details, Claude reads the form, asks for more information if needed, and proposes an outcome. The recommendation lands in the legal team's queue with the analysis already completed.

## Privacy impact assessments

Writing PIAs from scratch was tedious, even when assessments followed similar patterns. Anthropic's legal team now uses MCP servers to connect Claude to a Google Drive folder of prior PIAs, paired with a Skill that captures the firm's format and the issues to look for in each new assessment.

A lawyer can ask Claude to read the prior assessments, apply the standard concerns from the Skill, and draft a new PIA from that context. The lawyer then reviews and finalizes the document. End-to-end, this new workflow reduces time spent on each PIA from roughly two hours to thirty minutes.

## Contract redlining

Comparing contract versions and recommending fallback language is time-consuming work. Claude now compares document versions in Google Docs and Microsoft 365, highlights the changes, and recommends language from the firm's commercial playbook. The team configured Claude to work inside Google Docs and comment with suggested edits in real time, so a reviewer can ask directly in the document whether a piece of language meets the firm's standard, and get an immediate answer.

The team also writes skills to streamline review of specific document types like NDAs and third-party vendor agreements. This workflow has reduced redlining from hours to minutes per agreement.
