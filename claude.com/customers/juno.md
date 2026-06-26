<!-- source: https://claude.com/customers/juno -->

Case study | Claude Platform

# Juno helps people with chronic illness find patterns in their symptoms with Claude

Try Claude

[Try Claude](https://claude.ai)Try Claude

Contact sales

[Contact sales](/contact-sales)Contact sales

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a30dd3770a64a8d0590bd78_logo_juno2-light-mode.svg)![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a30dd3ac6c210dba5fe16c6_logo_juno2-dark-mode.svg)

Industry:

Software

Company size:

Startup

Product:

Claude Code

Claude Cowork

Location:

North America

10% increase in next-day retention

after using Claude for their onboarding flow

100,000 users onboarded

after launching in October 2025

[Juno](https://junocompanion.com/) is an AI health assistant for people living with chronic illness. People talk to it by voice or text about how they're feeling each day, and it draws on the medical history and biometrics they bring in to turn those conversations into symptom patterns and doctor-ready summaries. Its voice and text agents run on Claude.

## With Claude, Juno:

* Increased next-day retention 10% across 4,000 users after using Claude's large context window to process its onboarding flow.
* Lifted first-conversation conversions 3-4% after moving from Claude Sonnet to Claude Opus.
* Built automatic symptom tracking with Claude Haiku to infer severity from how users describe their day.
* Created voice and text agents with access to roughly 50 tools, for tasks like medication tracking and calendar management.
* Onboarded more than 100,000 patients since launching in October, with the app built and maintained by a two-person team using Claude Code.

## The challenge

Claude for Healthcare

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/696415a56ed108d94045852e_heart-marginalia.avif)

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

Read more

[Read more](https://claude.com/healthcare)Read more

Claude for Healthcare

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude for Healthcare

Claude helps healthcare organizations move faster without sacrificing accuracy, safety, or compliance. Less administrative work, more time with the people you serve.

## Building for a community many tools overlook

The apps built for people with chronic illness can often be thin and fragmented, aimed at what many treat as a niche. "A lot of people treat this as a minority community, when in fact one in three adults live with a chronic condition," said Marshall Gould, co-founder and CEO of Juno.

People with chronic illness often manage several symptoms a day, many of them correlated with environmental factors. Finding what drives a flare-up means tracking everything, and most people won't keep a manual log. They also tend to be less than fully candid with the professionals meant to help them, leaving out what feels embarrassing or beside the point. The people with the most to gain from pattern detection are often the least likely to produce the data that makes it possible.

Gould and his co-founder both live with chronic conditions, and while earning a master's in genomic medicine at Oxford, Gould researched how people with chronic illness use social media. "When people think about chronic illness, they think about someone looking obviously ill," he said. "The reality is many people with a chronic condition look fine on the outside, but it's just a mask for trying to live a normal life.”

## The solution

Cowork

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525604b02eec936ac521_696fc8952f473c6520149cfa_4f58536f1c08deac7a94811f4be57881_og-claude-cowork.jpeg)

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

Read more

[Read more](/product/cowork)Read more

Cowork

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Cowork

Give Claude access to your local files and let it complete tasks autonomously. Agentic capabilities for non-technical knowledge work.

## Reading symptoms in how people talk

To pick a model, Juno's founders ran a head-to-head usability test with 100 people living with chronic illness. Each user asked a real health question, like describing a symptom and asking what to do, then scored how useful each model's answer was. Claude Opus scored highest of the models they tried. Early on, the team relied on a fine-tuned model, but found that prompting Claude, and moving to each newer release, beat what fine-tuning gave them. So they shifted to a system prompt, refining it to roughly 4,000 lines over three to four months to consistently perform well for their users.

The product runs on a mix of Claude models, each doing a different job. Claude Sonnet carries the everyday conversation, the daily check-ins where someone describes how they're feeling. Claude Opus takes the tool calls where accuracy matters most, drawing on the roughly 50 tools the voice and text agents share: a user can tell Juno they have taken their morning medications and have it update the log, ask what they have missed, or, on a low-energy day, have it reshape the calendar around the most important tasks and push the rest to later in the week.

The agents work from the health data each person chooses to share. Users upload their medical history, records, diagnoses, and medications directly into Juno, and the app pulls in data from connected devices and wearables where available. A newly-available Gmail connection lets users import the test results and referral letters buried in their inboxes, and direct integrations with health systems’ electronic records are in development.

Underneath each conversation, Claude Haiku reads the transcript and extracts symptoms and patterns, scoring them on Juno's own severity scale. Someone who mentions their head hurts and wonders whether it's the coffee gets a headache logged with the time and a likely trigger, no form required. Logging a symptom as a five out of ten, with the time and a probable cause, is the kind of structured chore patients tend to abandon. Juno reads it from the conversation instead, learning each person's baseline way of speaking and inferring how bad a day is from the words they use.

The tone is a deliberate choice, too. Because Juno stays non-judgmental, people tell it the things they might hold back from a live conversation, surfacing patterns a clinical intake might miss. The same closeness creates a risk, though. A model that agrees with whatever a user says can also be highly retentive and quietly harmful. "It creates a cascade that's almost limitless," Gould explained.

Juno's prompts draw on motivational theory, guiding people toward their own realizations rather than naming what's wrong. The prompts also rely on Gould's Oxford research showing that people with chronic illness engage roughly eight times more with encouragement and small wins than with negative content. "Our aim isn't to be the nicest chatbot in the world," he said. "It's to create something more actionable, to make people healthier." Juno's semantic analysis shows the pattern: mood often dips over the first few sessions, when Juno isn't simply telling people what they want to hear, then climbs over time.

## Building and testing the app as a team of two

The founders lean on Claude Code and Claude Cowork to move fast. "Being a team of two, you have to be extremely efficient," Gould said. Cowork can take a task like building a pitch deck most of the way to done on its own, and for heavier work the team kicks off large batches of agents, sometimes around 100 at once, to work a complex build in parallel. The front end started in Claude Design, where the team wrote a design.md spec covering fonts, structure, and colors that Claude follows when generating new screens. "We like to give Claude some free rein to experiment with what would be good UX and UI," Gould said, "and then, using our own taste, we make it better." In practice that means letting Claude draft ten layouts before they pick one and refine it by hand.

Mobile testing is the hardest part for a two-person team, with a long list of devices and screen sizes to cover. Juno connects Claude Code through the Model Context Protocol (MCP) to mobile simulators that run in the cloud around the clock. When a bug appears, Claude Code reproduces it across devices, applies a fix, runs CI/CD checks with a Claude Code review, and confirms the fix before it ships.

"We want to take the average time to diagnosis from 7.6 years down to just a couple of months, if not days."

Marshall Gould

Co-founder and CEO, Juno

Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/698f525504b02eec936ac51b_68c469d41149ace562bfd24d_og-claude-product-claude-code.jpeg)

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

Claude Code

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

[Next](#)Next

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

[Next](#)Next

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

Claude Code

Anthropic's agentic coding tool. Claude Code understands your codebase, edits files, runs commands, and helps you ship faster.

## The outcome

## Higher usability, and users who stay

Since launching in October, Juno has grown to more than 100,000 users, and the founders run five to ten user calls a day to shape what comes next. Half of its users manage more than three conditions at once.

On the first conversation, moving from Claude Sonnet to Claude Opus lifted conversion by 3 to 4%, as new users reached a moment of value sooner. That same move helped retention: once Opus could take in Juno's full onboarding, about 50 slides of personal history, through its large context window in one pass, next-day retention rose by 10%. "The more that you do, the less useful the app becomes," Gould said. A generalist app can only stretch so far, which is why Juno is moving toward generative UI that reshapes itself per condition: a period-tracking section for endometriosis, live blood pressure tied to energy for POTS.

The larger goal is diagnosis. "The one thing every person with a chronic illness has in common is that they were once undiagnosed," Gould said. By Juno's own figures, getting that diagnosis in the U.S. is often slow and expensive, on the order of $30,000 per patient. For rare conditions, the path is longest: studies have found it takes an average of 7.6 years in the U.S. to reach a correct diagnosis, through visits to as many as eight physicians and two to three misdiagnoses along the way. By structuring a long medical history, lab results, and daily conversation into something a doctor can read in a page, Juno wants to compress that. "We want to take the average time to diagnosis from 7.6 years down to just a couple of months," Gould said, "if not days."

"Our aim isn't to be the nicest chatbot in the world. It's to create something more actionable."

Marshall Gould

Co-founder and CEO, Juno

## Related stories

[How Vercel built an ecosystem on the open skills standard](/customers/vercel-qa)How Vercel built an ecosystem on the open skills standard

How Vercel built an ecosystem on the open skills standard

Customer story

[Customer story](/customers/vercel-qa)Customer story

[Box builds document creation into its AI agent with Claude](/customers/box)Box builds document creation into its AI agent with Claude

Box builds document creation into its AI agent with Claude

Customer story

[Customer story](/customers/box)Customer story

[A conversation with Cursor on building coding agents for professional developers](/customers/cursor-qa)A conversation with Cursor on building coding agents for professional developers

A conversation with Cursor on building coding agents for professional developers

Customer story

[Customer story](/customers/cursor-qa)Customer story

[Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code](/customers/delightai-qa)Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Inside Delight.ai’s AI/ML team: Building internal tools with Claude Code

Customer story

[Customer story](/customers/delightai-qa)Customer story
